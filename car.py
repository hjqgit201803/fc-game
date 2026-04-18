import math
from enum import Enum

class DriftState(Enum):
    """漂移状态枚举"""
    NONE = "none"
    DRIFTING = "drifting"
    NITRO = "nitro"

class Car:
    """赛车类，封装赛车的所有行为和状态"""

    def __init__(self, x, y, angle=0):
        """
        初始化赛车

        Args:
            x: 初始 X 坐标
            y: 初始 Y 坐标
            angle: 初始朝向角度（度），0 指向右侧
        """
        # 位置和朝向
        self.x = x
        self.y = y
        self.angle = angle  # 角度，0-360

        # 速度相关
        self.speed = 0.0
        self.velocity_x = 0.0
        self.velocity_y = 0.0

        # 物理参数
        self.max_speed = 300.0  # 像素/秒
        self.acceleration = 200.0  # 加速度
        self.brake_force = 300.0  # 刹车力
        self.friction = 0.98  # 摩擦系数（每帧衰减）
        self.turn_speed = 180.0  # 转向速度（度/秒）

        # 漂移相关
        self.drift_state = DriftState.NONE
        self.nitro_level = 0.0  # 0-100
        self.nitro_timer = 0.0  # 喷射剩余时间
        self.nitro_duration = 0.5  # 喷射持续时间（秒）
        self.drift_angle_offset = 0.0  # 漂移时的角度偏移

        # 输入状态
        self.throttling = False
        self.braking = False
        self.turning_left = False
        self.turning_right = False
        self.drifting = False

    def handle_input(self, event):
        """
        处理输入事件

        Args:
            event: Pygame 事件对象
        """
        if event.type == "keydown":  # 伪事件类型，实际在 Game 类中处理
            pass

    def accelerate(self):
        """开始加速"""
        self.throttling = True

    def release_accelerate(self):
        """停止加速"""
        self.throttling = False

    def brake(self):
        """开始刹车"""
        self.braking = True

    def release_brake(self):
        """停止刹车"""
        self.braking = False

    def turn_left(self):
        """开始左转"""
        self.turning_left = True

    def release_turn_left(self):
        """停止左转"""
        self.turning_left = False

    def turn_right(self):
        """开始右转"""
        self.turning_right = True

    def release_turn_right(self):
        """停止右转"""
        self.turning_right = False

    def start_drift(self):
        """开始漂移"""
        if (self.turning_left or self.turning_right) and self.speed > 50:
            if self.drift_state == DriftState.NONE:
                self.drift_state = DriftState.DRIFTING
                self.drifting = True

    def end_drift(self):
        """结束漂移并触发喷射"""
        if self.drift_state == DriftState.DRIFTING:
            self.drifting = False
            if self.nitro_level > 20:  # 蓄力足够才触发喷射
                self.drift_state = DriftState.NITRO
                self.nitro_timer = self.nitro_duration
            else:
                self.drift_state = DriftState.NONE
            self.drift_angle_offset = 0.0

    def update(self, dt):
        """
        每帧更新赛车状态

        Args:
            dt: 时间增量（秒）
        """
        # 处理转向
        if self.turning_left:
            self.angle -= self.turn_speed * dt
        if self.turning_right:
            self.angle += self.turn_speed * dt

        # 规范化角度到 0-360
        self.angle %= 360

        # 处理加速和刹车
        if self.throttling:
            self.speed += self.acceleration * dt
        if self.braking:
            if self.speed > 0:
                self.speed -= self.brake_force * dt
            else:
                self.speed -= self.acceleration * dt * 0.5  # 倒车

        # 应用摩擦力
        self.speed *= self.friction

        # 限制最大速度
        if self.drift_state == DriftState.NITRO:
            max_spd = self.max_speed * 1.3
        else:
            max_spd = self.max_speed
        self.speed = max(min(self.speed, max_spd), -self.max_speed * 0.3)

        # 计算速度向量
        rad = math.radians(self.angle + self.drift_angle_offset)
        self.velocity_x = math.cos(rad) * self.speed
        self.velocity_y = math.sin(rad) * self.speed

        # 更新位置
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # 处理漂移逻辑
        self._update_drift(dt)

    def _update_drift(self, dt):
        """更新漂移状态"""
        if self.drift_state == DriftState.DRIFTING:
            # 漂移时蓄力
            self.nitro_level = min(100, self.nitro_level + 60 * dt)

            # 漂移角度偏移
            if self.turning_left:
                self.drift_angle_offset = min(30, self.drift_angle_offset + 120 * dt)
            elif self.turning_right:
                self.drift_angle_offset = max(-30, self.drift_angle_offset - 120 * dt)
            else:
                # 回正
                if self.drift_angle_offset > 0:
                    self.drift_angle_offset = max(0, self.drift_angle_offset - 60 * dt)
                else:
                    self.drift_angle_offset = min(0, self.drift_angle_offset + 60 * dt)

        elif self.drift_state == DriftState.NITRO:
            # 喷射计时
            self.nitro_timer -= dt
            if self.nitro_timer <= 0:
                self.drift_state = DriftState.NONE
                self.nitro_level = 0
        else:
            # 自然衰减漂移蓄力
            self.nitro_level = max(0, self.nitro_level - 30 * dt)

    def get_color(self):
        """根据状态返回赛车颜色"""
        if self.drift_state == DriftState.NITRO:
            return (255, 50, 50)  # 红色 - 喷射
        elif self.drift_state == DriftState.DRIFTING:
            return (150, 50, 200)  # 紫色 - 漂移
        else:
            return (50, 150, 255)  # 蓝色 - 正常
