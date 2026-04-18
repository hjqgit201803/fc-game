import pygame
import random
import math

class Particle:
    """粒子类，用于视觉效果"""

    def __init__(self, x, y, color, lifetime, size, velocity=(0, 0)):
        """
        初始化粒子

        Args:
            x, y: 位置
            color: 颜色
            lifetime: 生命周期（秒）
            size: 大小
            velocity: 速度向量
        """
        self.x = x
        self.y = y
        self.color = color
        self.max_lifetime = lifetime
        self.lifetime = lifetime
        self.size = size
        self.velocity = velocity

    def update(self, dt):
        """
        更新粒子状态

        Args:
            dt: 时间增量（秒）

        Returns:
            bool: 如果粒子存活返回 True
        """
        self.lifetime -= dt
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt
        return self.lifetime > 0

    def draw(self, surface):
        """
        绘制粒子

        Args:
            surface: Pygame 表面对象
        """
        alpha = int(255 * (self.lifetime / self.max_lifetime))

        # 创建临时表面用于 alpha 混合
        temp_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(temp_surface, (*self.color[:3], alpha), (self.size, self.size), self.size)

        # 直接 blit 到目标表面
        surface.blit(temp_surface, (int(self.x - self.size), int(self.y - self.size)))

class ParticleSystem:
    """粒子系统管理器"""

    def __init__(self):
        """初始化粒子系统"""
        self.particles = []

    def emit(self, x, y, color, count=1, lifetime=0.5, size=3, velocity_range=(-20, 20)):
        """
        发射粒子

        Args:
            x, y: 发射位置
            color: 粒子颜色
            count: 粒子数量
            lifetime: 生命周期（秒）
            size: 粒子大小
            velocity_range: 速度范围
        """
        for _ in range(count):
            vx = random.uniform(*velocity_range)
            vy = random.uniform(*velocity_range)
            self.particles.append(Particle(x, y, color, lifetime, size, (vx, vy)))

    def update(self, dt):
        """
        更新所有粒子

        Args:
            dt: 时间增量（秒）
        """
        self.particles = [p for p in self.particles if p.update(dt)]

    def draw(self, surface):
        """
        绘制所有粒子

        Args:
            surface: Pygame 表面对象
        """
        for particle in self.particles:
            particle.draw(surface)

    def clear(self):
        """清空所有粒子"""
        self.particles = []
