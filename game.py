import pygame
import sys
from enum import Enum

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
                if event.key == pygame.K_q and self.state != GameState.MENU:
                    self.running = False
                elif event.key == pygame.K_SPACE and self.state == GameState.MENU:
                    self.state = GameState.PLAYING
                elif event.key == pygame.K_r and self.state == GameState.FINISHED:
                    self.reset_game()

    def update(self, dt):
        """更新游戏状态"""
        if self.state == GameState.PLAYING:
            pass  # 后续添加更新逻辑
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

    def _draw_menu(self):
        """绘制菜单画面"""
        self.screen.fill((30, 30, 40))
        font = pygame.font.Font(None, 64)
        title = font.render("QQ SPEED CLONE", True, (255, 255, 255))
        self.screen.blit(title, (1200//2 - title.get_width()//2, 300))

        font_small = pygame.font.Font(None, 32)
        prompt = font_small.render("Press SPACE to Start", True, (200, 200, 200))
        self.screen.blit(prompt, (1200//2 - prompt.get_width()//2, 400))

    def _draw_game(self):
        """绘制游戏画面"""
        self.screen.fill((50, 50, 50))

    def _draw_results(self):
        """绘制成绩画面"""
        self.screen.fill((30, 30, 40))
        font = pygame.font.Font(None, 48)
        text = font.render("Race Finished!", True, (255, 255, 255))
        self.screen.blit(text, (1200//2 - text.get_width()//2, 350))

        font_small = pygame.font.Font(None, 32)
        prompt = font_small.render("Press R to Restart | Q to Quit", True, (200, 200, 200))
        self.screen.blit(prompt, (1200//2 - prompt.get_width()//2, 420))

    def reset_game(self):
        """重置游戏状态"""
        self.state = GameState.PLAYING
