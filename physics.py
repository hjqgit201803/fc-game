import math
from car import DriftState

class Physics:
    """物理引擎类，处理物理计算和碰撞检测"""

    def __init__(self):
        """初始化物理引擎"""
        self.track_boundaries = None

    def set_track_boundaries(self, boundaries):
        """
        设置赛道边界

        Args:
            boundaries: 赛道边界字典，包含 outer 和 inner 矩形
        """
        self.track_boundaries = boundaries

    def apply_friction(self, car):
        """
        应用摩擦力

        Args:
            car: Car 对象
        """
        # 基础摩擦在 Car.update 中处理
        pass

    def check_collision(self, car):
        """
        检测车辆与赛道边界碰撞

        Args:
            car: Car 对象

        Returns:
            bool: 如果碰撞返回 True
        """
        if self.track_boundaries is None:
            return False

        bounds = self.track_boundaries
        x, y = car.x, car.y

        # 检查是否在外边界之外
        if (x < bounds['outer']['left'] or x > bounds['outer']['right'] or
            y < bounds['outer']['top'] or y > bounds['outer']['bottom']):
            return True

        # 检查是否在内边界之内（碰撞内部障碍）
        if (x > bounds['inner']['left'] and x < bounds['inner']['right'] and
            y > bounds['inner']['top'] and y < bounds['inner']['bottom']):
            return True

        return False

    def handle_collision(self, car):
        """
        处理碰撞响应

        Args:
            car: Car 对象
        """
        # 简单的碰撞处理：反弹并减速
        car.speed = -car.speed * 0.3
        car.x -= car.velocity_x * 0.1
        car.y -= car.velocity_y * 0.1

        # 结束漂移状态
        if car.drift_state == DriftState.DRIFTING:
            car.end_drift()

    def calculate_drift_physics(self, car):
        """
        漂移时的特殊物理计算

        Args:
            car: Car 对象
        """
        # 漂移物理在 Car 类中处理
        pass

    def update_position(self, car, dt):
        """
        根据速度更新位置

        Args:
            car: Car 对象
            dt: 时间增量（秒）
        """
        # 位置更新在 Car.update 中处理
        pass
