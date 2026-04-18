import pygame
from car import DriftState

class UI:
    """UI 类，负责绘制 HUD 和界面元素"""

    def __init__(self, screen_width, screen_height):
        """
        初始化 UI

        Args:
            screen_width: 屏幕宽度
            screen_height: 屏幕高度
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 28)

    def draw_hud(self, surface, car, track):
        """
        绘制抬头显示

        Args:
            surface: Pygame 表面对象
            car: Car 对象
            track: Track 对象
        """
        # 半透明背景
        overlay = pygame.Surface((200, 120))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (10, 10))

        # 绘制漂移条
        self._draw_drift_bar(surface, car, 20, 20)

        # 绘制速度
        self._draw_speed(surface, car, 20, 60)

        # 绘制计时
        self._draw_timer(surface, track, 20, 95)

    def _draw_drift_bar(self, surface, car, x, y):
        """
        绘制漂移蓄力条

        Args:
            surface: Pygame 表面对象
            car: Car 对象
            x, y: 位置
        """
        bar_width = 160
        bar_height = 20

        # 背景
        pygame.draw.rect(surface, (50, 50, 50), (x, y, bar_width, bar_height), border_radius=5)

        # 填充（根据蓄力值改变颜色）
        if car.nitro_level < 25:
            color = (50, 150, 255)  # 蓝色
        elif car.nitro_level < 50:
            color = (50, 255, 150)  # 绿色
        elif car.nitro_level < 75:
            color = (255, 255, 50)  # 黄色
        else:
            color = (255, 50, 50)   # 红色

        fill_width = int(bar_width * car.nitro_level / 100)
        if fill_width > 0:
            pygame.draw.rect(surface, color, (x, y, fill_width, bar_height), border_radius=5)

        # 边框
        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height), 2, border_radius=5)

        # 标签
        label = self.font_small.render("DRIFT", True, (200, 200, 200))
        surface.blit(label, (x + bar_width // 2 - label.get_width() // 2, y - 2))

    def _draw_speed(self, surface, car, x, y):
        """
        显示当前速度

        Args:
            surface: Pygame 表面对象
            car: Car 对象
            x, y: 位置
        """
        speed_kmh = int(abs(car.speed) * 0.5)  # 转换为 km/h 显示
        text = self.font_medium.render(f"{speed_kmh:3d} km/h", True, (255, 255, 255))
        surface.blit(text, (x, y))

    def _draw_timer(self, surface, track, x, y):
        """
        显示当前用时

        Args:
            surface: Pygame 表面对象
            track: Track 对象
            x, y: 位置
        """
        minutes = int(track.lap_time // 60)
        seconds = int(track.lap_time % 60)
        milliseconds = int((track.lap_time % 1) * 1000)

        time_str = f"TIME: {minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        text = self.font_small.render(time_str, True, (255, 255, 255))
        surface.blit(text, (x, y))

    def draw_menu(self, surface):
        """
        绘制菜单画面

        Args:
            surface: Pygame 表面对象
        """
        surface.fill((20, 20, 30))

        # 标题
        title = self.font_large.render("QQ SPEED CLONE", True, (255, 255, 255))
        surface.blit(title, (self.screen_width // 2 - title.get_width() // 2, 250))

        # 提示
        prompt = self.font_medium.render("Press SPACE to Start", True, (200, 200, 200))
        surface.blit(prompt, (self.screen_width // 2 - prompt.get_width() // 2, 380))

        # 操作说明
        controls = [
            "Controls:",
            "↑/W - Accelerate",
            "↓/S - Brake",
            "←→/AD - Steer",
            "Shift - Drift"
        ]

        y = 480
        for line in controls:
            text = self.font_small.render(line, True, (150, 150, 150))
            surface.blit(text, (self.screen_width // 2 - text.get_width() // 2, y))
            y += 30

    def draw_results(self, surface, track):
        """
        绘制成绩画面

        Args:
            surface: Pygame 表面对象
            track: Track 对象
        """
        surface.fill((20, 20, 30))

        # 标题
        title = self.font_large.render("RACE FINISHED!", True, (255, 255, 255))
        surface.blit(title, (self.screen_width // 2 - title.get_width() // 2, 200))

        # 本次成绩
        minutes = int(track.lap_time // 60)
        seconds = int(track.lap_time % 60)
        milliseconds = int((track.lap_time % 1) * 1000)
        time_str = f"Time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        time_text = self.font_medium.render(time_str, True, (100, 255, 100))
        surface.blit(time_text, (self.screen_width // 2 - time_text.get_width() // 2, 300))

        # 最佳成绩
        if track.best_time:
            best_minutes = int(track.best_time // 60)
            best_seconds = int(track.best_time % 60)
            best_milliseconds = int((track.best_time % 1) * 1000)
            best_str = f"Best: {best_minutes:02d}:{best_seconds:02d}.{best_milliseconds:03d}"
            best_text = self.font_medium.render(best_str, True, (255, 255, 100))
            surface.blit(best_text, (self.screen_width // 2 - best_text.get_width() // 2, 350))

        # 提示
        prompt = self.font_medium.render("R - Restart | Q - Quit", True, (200, 200, 200))
        surface.blit(prompt, (self.screen_width // 2 - prompt.get_width() // 2, 450))
