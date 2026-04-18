import pygame

class Track:
    """赛道类，定义赛道边界和检测"""

    def __init__(self, screen_width, screen_height):
        """
        初始化赛道

        Args:
            screen_width: 屏幕宽度
            screen_height: 屏幕高度
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

        # 矩形赛道配置（外矩形减去内矩形）
        margin = 100
        track_width = 100

        self.outer_rect = pygame.Rect(
            margin, margin,
            screen_width - 2 * margin,
            screen_height - 2 * margin
        )

        self.inner_rect = pygame.Rect(
            margin + track_width, margin + track_width,
            screen_width - 2 * margin - 2 * track_width,
            screen_height - 2 * margin - 2 * track_width
        )

        # 赛道边界数据（用于碰撞检测）
        self.boundaries = {
            'outer': {
                'left': margin,
                'right': screen_width - margin,
                'top': margin,
                'bottom': screen_height - margin
            },
            'inner': {
                'left': margin + track_width,
                'right': screen_width - margin - track_width,
                'top': margin + track_width,
                'bottom': screen_height - margin - track_width
            }
        }

        # 起点位置和方向
        self.start_pos = {
            'x': margin + track_width // 2,
            'y': screen_height // 2,
            'angle': 0  # 指向右侧
        }

        # 终点线位置
        self.finish_line = {
            'start': (margin + track_width // 2, margin + track_width // 2),
            'end': (margin + track_width // 2, screen_height - margin - track_width // 2)
        }

        # 检查点（用于检测完成圈数）
        self.checkpoints = [
            {'x': screen_width - margin - track_width // 2, 'y': screen_height // 2, 'passed': False}
        ]

        # 计时相关
        self.lap_time = 0.0
        self.best_time = None
        self.finished = False

    def is_on_track(self, x, y):
        """
        检测位置是否在赛道内

        Args:
            x: X 坐标
            y: Y 坐标

        Returns:
            bool: 如果在赛道内返回 True
        """
        # 在外矩形内
        if not self.outer_rect.collidepoint(x, y):
            return False
        # 不在内矩形内
        if self.inner_rect.collidepoint(x, y):
            return False
        return True

    def get_start_position(self):
        """
        返回起点坐标和角度

        Returns:
            dict: 包含 x, y, angle 的字典
        """
        return self.start_pos

    def update(self, dt, car):
        """
        更新赛道状态（检查点、计时等）

        Args:
            dt: 时间增量
            car: Car 对象
        """
        if self.finished:
            return

        # 更新计时
        self.lap_time += dt

        # 检查检查点
        for checkpoint in self.checkpoints:
            if not checkpoint['passed']:
                dx = car.x - checkpoint['x']
                dy = car.y - checkpoint['y']
                if abs(dx) < 50 and abs(dy) < 50:
                    checkpoint['passed'] = True

        # 检查是否完成一圈（回到起点且所有检查点已通过）
        all_checkpoints_passed = all(cp['passed'] for cp in self.checkpoints)
        dx = car.x - self.start_pos['x']
        dy = car.y - self.start_pos['y']

        if all_checkpoints_passed and abs(dx) < 80 and abs(dy) < 80 and self.lap_time > 2.0:
            self.finished = True
            if self.best_time is None or self.lap_time < self.best_time:
                self.best_time = self.lap_time

    def reset(self):
        """重置赛道状态"""
        self.lap_time = 0.0
        self.finished = False
        for checkpoint in self.checkpoints:
            checkpoint['passed'] = False

    def draw(self, surface):
        """
        绘制赛道

        Args:
            surface: Pygame 表面对象
        """
        # 绘制背景
        surface.fill((30, 30, 30))

        # 绘制赛道表面
        pygame.draw.rect(surface, (70, 70, 70), self.outer_rect)
        pygame.draw.rect(surface, (30, 30, 30), self.inner_rect)

        # 绘制边界线
        pygame.draw.rect(surface, (255, 255, 255), self.outer_rect, 3)
        pygame.draw.rect(surface, (255, 255, 255), self.inner_rect, 3)

        # 绘制起点线
        start_x = self.start_pos['x']
        pygame.draw.line(surface, (0, 255, 0),
                        (start_x, self.outer_rect.top),
                        (start_x, self.outer_rect.bottom), 5)

        # 绘制终点线
        pygame.draw.line(surface, (255, 255, 0),
                        (start_x, self.outer_rect.top),
                        (start_x, self.outer_rect.top + 30), 5)
        pygame.draw.line(surface, (255, 255, 0),
                        (start_x, self.outer_rect.bottom - 30),
                        (start_x, self.outer_rect.bottom), 5)

        # 绘制检查点标记
        for checkpoint in self.checkpoints:
            color = (0, 255, 255) if checkpoint['passed'] else (150, 150, 150)
            pygame.draw.circle(surface, color, (int(checkpoint['x']), int(checkpoint['y'])), 10)
