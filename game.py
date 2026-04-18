import pygame
import sys
import math
from enum import Enum
from car import Car, DriftState
from physics import Physics
from track import Track
from ui import UI
from particles import ParticleSystem

class GameState(Enum):
    """游戏状态枚举"""
    MENU = "menu"
    PLAYING = "playing"
    FINISHED = "finished"

class Game:
    """游戏主类，管理游戏循环和状态"""

    def __init__(self):
        """初始化游戏"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("QQ Speed Clone")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        self.fps = 60
        self.track = Track(1200, 800)
        self.car = Car(
            self.track.start_pos['x'],
            self.track.start_pos['y'],
            self.track.start_pos['angle']
        )
        self.keys_pressed = set()
        self.physics = Physics()
        self.physics.set_track_boundaries(self.track.boundaries)
        self.ui = UI(1200, 800)
        self.particle_system = ParticleSystem()

    def run(self):
        """主游戏循环"""
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0  # 转换为秒
            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """处理输入事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)
                if event.key == pygame.K_q and self.state != GameState.MENU:
                    self.running = False
                elif event.key == pygame.K_SPACE and self.state == GameState.MENU:
                    self.state = GameState.PLAYING
                elif event.key == pygame.K_r and self.state == GameState.FINISHED:
                    self.reset_game()
                # 漂移键处理
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    self.car.start_drift()

            elif event.type == pygame.KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)
                # 漂移键释放
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    self.car.end_drift()

        # 持续按键处理
        self._handle_continuous_input()

    def _handle_continuous_input(self):
        """处理持续按键状态"""
        if self.state == GameState.PLAYING:
            # 加速
            if pygame.K_UP in self.keys_pressed or pygame.K_w in self.keys_pressed:
                self.car.accelerate()
            else:
                self.car.release_accelerate()

            # 刹车
            if pygame.K_DOWN in self.keys_pressed or pygame.K_s in self.keys_pressed:
                self.car.brake()
            else:
                self.car.release_brake()

            # 左转
            if pygame.K_LEFT in self.keys_pressed or pygame.K_a in self.keys_pressed:
                self.car.turn_left()
            else:
                self.car.release_turn_left()

            # 右转
            if pygame.K_RIGHT in self.keys_pressed or pygame.K_d in self.keys_pressed:
                self.car.turn_right()
            else:
                self.car.release_turn_right()

    def update(self, dt):
        """更新游戏状态"""
        if self.state == GameState.PLAYING:
            self.car.update(dt)
            self.track.update(dt, self.car)

            # 碰撞检测
            if self.physics.check_collision(self.car):
                self.physics.handle_collision(self.car)

            # 漂移粒子效果
            if self.car.drift_state == DriftState.DRIFTING:
                # 计算车尾位置
                rad = math.radians(self.car.angle + 180)
                tail_x = self.car.x + math.cos(rad) * 20
                tail_y = self.car.y + math.sin(rad) * 20
                self.particle_system.emit(tail_x, tail_y, (150, 150, 150), count=2, lifetime=0.3)

            # 喷射尾焰效果
            elif self.car.drift_state == DriftState.NITRO:
                rad = math.radians(self.car.angle + 180)
                tail_x = self.car.x + math.cos(rad) * 25
                tail_y = self.car.y + math.sin(rad) * 25
                self.particle_system.emit(tail_x, tail_y, (255, 150, 50), count=3, lifetime=0.2, size=5)

            # 更新粒子
            self.particle_system.update(dt)

            # 检查是否完成比赛
            if self.track.finished:
                self.state = GameState.FINISHED
        elif self.state == GameState.MENU:
            pass
        elif self.state == GameState.FINISHED:
            pass

    def draw(self):
        """渲染游戏画面"""
        if self.state == GameState.MENU:
            self._draw_menu()
        elif self.state == GameState.PLAYING:
            self._draw_game()
        elif self.state == GameState.FINISHED:
            self._draw_results()

        pygame.display.flip()

    def _draw_car(self):
        """绘制赛车"""
        car_width = 40
        car_height = 20

        # 创建赛车表面
        car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
        color = self.car.get_color()
        pygame.draw.rect(car_surface, color, (0, 0, car_width, car_height), border_radius=5)

        # 旋转赛车
        rotated_car = pygame.transform.rotate(car_surface, -self.car.angle)
        rect = rotated_car.get_rect(center=(self.car.x, self.car.y))

        self.screen.blit(rotated_car, rect)

    def _draw_menu(self):
        """绘制菜单画面"""
        self.ui.draw_menu(self.screen)

    def _draw_game(self):
        """绘制游戏画面"""
        self.track.draw(self.screen)
        self._draw_car()
        self.particle_system.draw(self.screen)
        self.ui.draw_hud(self.screen, self.car, self.track)

    def _draw_results(self):
        """绘制成绩画面"""
        self.ui.draw_results(self.screen, self.track)

    def reset_game(self):
        """重置游戏状态"""
        self.track.reset()
        self.car.x = self.track.start_pos['x']
        self.car.y = self.track.start_pos['y']
        self.car.angle = self.track.start_pos['angle']
        self.car.speed = 0
        self.car.drift_state = DriftState.NONE
        self.car.nitro_level = 0
        self.state = GameState.PLAYING
