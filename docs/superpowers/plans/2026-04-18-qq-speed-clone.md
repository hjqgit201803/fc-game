# QQ 飞车风格游戏实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个基于 Python/Pygame 的 2D 俯视视角赛车游戏，包含漂移机制、赛道碰撞检测和完整游戏流程。

**Architecture:** 模块化设计，分离关注点：Car 类处理车辆行为，Physics 类处理物理计算，Track 类定义赛道，Game 类管理游戏循环和状态，UI 类负责渲染。使用 Pygame 进行渲染和输入处理。

**Tech Stack:** Python 3.8+, Pygame 2.5.0

---

## Task 1: 项目初始化

**Files:**
- Create: `requirements.txt`
- Create: `main.py`

- [ ] **Step 1: 创建 requirements.txt**

```txt
pygame==2.5.0
```

- [ ] **Step 2: 创建基础 main.py 入口文件**

```python
import pygame
import sys

def main():
    """游戏入口点"""
    pygame.init()
    print("QQ Speed Clone - Initializing...")

    # 基础窗口设置（临时，后续由 Game 类接管）
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("QQ Speed Clone")

    # 临时测试窗口
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((50, 50, 50))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: 测试基础窗口启动**

Run: `python main.py`
Expected: 打开一个灰色窗口，标题为 "QQ Speed Clone"，按 ESC 或关闭窗口退出

- [ ] **Step 4: 安装依赖并验证**

Run: `pip install -r requirements.txt`
Expected: Pygame 2.5.0 安装成功

- [ ] **Step 5: 提交初始化代码**

```bash
git add requirements.txt main.py
git commit -m "feat: initialize project with pygame setup"
```

---

## Task 2: 创建游戏状态枚举和 Game 类骨架

**Files:**
- Create: `game.py`

- [ ] **Step 1: 创建 game.py 基础结构**

```python
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
```

- [ ] **Step 2: 更新 main.py 使用 Game 类**

```python
from game import Game

def main():
    """游戏入口点"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: 测试游戏状态切换**

Run: `python main.py`
Expected:
- 启动显示菜单画面
- 按 SPACE 进入游戏画面
- 目前游戏画面为空白灰色

- [ ] **Step 4: 提交游戏框架**

```bash
git add main.py game.py
git commit -m "feat: add game state management and menu system"
```

---

## Task 3: 创建 Car 类基础结构

**Files:**
- Create: `car.py`

- [ ] **Step 1: 创建 car.py 漂移状态枚举和 Car 类骨架**

```python
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
```

- [ ] **Step 2: 在 Game 类中集成 Car 并处理键盘输入**

在 `game.py` 中添加：

```python
from car import Car

class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.car = Car(100, 400, 0)  # 赛车初始位置
        self.keys_pressed = set()

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
```

- [ ] **Step 3: 在 Game.update 中更新 Car**

在 `game.py` 的 `update` 方法中：

```python
def update(self, dt):
    """更新游戏状态"""
    if self.state == GameState.PLAYING:
        self.car.update(dt)
    # ... 其他状态处理 ...
```

- [ ] **Step 4: 添加绘制赛车的代码**

在 `game.py` 中添加 `_draw_car` 方法并在 `_draw_game` 中调用：

```python
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

    # 绘制漂移粒子效果（简单版本）
    if self.car.drift_state == DriftState.DRIFTING:
        for i in range(3):
            offset_x = -math.cos(math.radians(self.car.angle)) * (20 + i * 10)
            offset_y = -math.sin(math.radians(self.car.angle)) * (20 + i * 10)
            pygame.draw.circle(self.screen, (100, 100, 100),
                             (int(self.car.x + offset_x), int(self.car.y + offset_y)), 3)

def _draw_game(self):
    """绘制游戏画面"""
    self.screen.fill((50, 50, 50))
    self._draw_car()
```

在文件顶部添加导入：
```python
import math
```

- [ ] **Step 5: 测试赛车控制**

Run: `python main.py`
Expected:
- 启动游戏按 SPACE 进入游戏
- 方向键或 WASD 控制赛车移动
- 赛车有颜色变化（正常蓝、漂移紫、喷射红）

- [ ] **Step 6: 提交 Car 类实现**

```bash
git add car.py game.py
git commit -m "feat: implement Car class with movement and drift states"
```

---

## Task 4: 创建 Physics 类处理碰撞检测

**Files:**
- Create: `physics.py`

- [ ] **Step 1: 创建 physics.py**

```python
import math

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
```

- [ ] **Step 2: 在 Game 类中集成 Physics**

在 `game.py` 中添加：

```python
from physics import Physics

class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.physics = Physics()

    def update(self, dt):
        """更新游戏状态"""
        if self.state == GameState.PLAYING:
            self.car.update(dt)
            # 碰撞检测将在 Track 类添加后集成
```

- [ ] **Step 3: 测试 Physics 类加载**

Run: `python main.py`
Expected: 游戏正常运行，Physics 类已初始化

- [ ] **Step 4: 提交 Physics 类**

```bash
git add physics.py game.py
git commit -m "feat: add Physics class for collision detection"
```

---

## Task 5: 创建 Track 类和赛道绘制

**Files:**
- Create: `track.py`

- [ ] **Step 1: 创建 track.py**

```python
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
```

- [ ] **Step 2: 在 Game 类中集成 Track**

在 `game.py` 中修改：

```python
from track import Track

class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.track = Track(1200, 800)
        self.car = Car(
            self.track.start_pos['x'],
            self.track.start_pos['y'],
            self.track.start_pos['angle']
        )
        self.physics.set_track_boundaries(self.track.boundaries)

    def update(self, dt):
        """更新游戏状态"""
        if self.state == GameState.PLAYING:
            self.car.update(dt)
            self.track.update(dt, self.car)

            # 碰撞检测
            if self.physics.check_collision(self.car):
                self.physics.handle_collision(self.car)

            # 检查是否完成比赛
            if self.track.finished:
                self.state = GameState.FINISHED

    def _draw_game(self):
        """绘制游戏画面"""
        self.track.draw(self.screen)
        self._draw_car()
```

- [ ] **Step 3: 测试赛道和碰撞**

Run: `python main.py`
Expected:
- 显示赛道（灰色可行驶区域，白色边界）
- 绿色起点线
- 赛车碰撞边界时反弹减速
- 完成一圈后显示成绩画面

- [ ] **Step 4: 提交 Track 类**

```bash
git add track.py game.py
git commit -m "feat: add Track class with collision detection and lap timing"
```

---

## Task 6: 创建 UI 类绘制 HUD

**Files:**
- Create: `ui.py`

- [ ] **Step 1: 创建 ui.py**

```python
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
```

- [ ] **Step 2: 在 Game 类中集成 UI**

在 `game.py` 中修改：

```python
from ui import UI

class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.ui = UI(1200, 800)

    def _draw_menu(self):
        """绘制菜单画面"""
        self.ui.draw_menu(self.screen)

    def _draw_game(self):
        """绘制游戏画面"""
        self.track.draw(self.screen)
        self._draw_car()
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
```

- [ ] **Step 3: 测试完整 UI**

Run: `python main.py`
Expected:
- 菜单画面显示标题和操作说明
- 游戏中显示 HUD（漂移条、速度、计时）
- 完成比赛后显示成绩

- [ ] **Step 4: 提交 UI 实现**

```bash
git add ui.py game.py
git commit -m "feat: add UI class with HUD and menu system"
```

---

## Task 7: 添加视觉效果（粒子系统和尾焰）

**Files:**
- Create: `particles.py`
- Modify: `game.py`

- [ ] **Step 1: 创建粒子系统**

```python
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
        color = (*self.color[:3], alpha)

        # 创建带 alpha 的表面
        particle_surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(particle_surf, color, (self.size, self.size), self.size)

        surface.blit(particle_surf, (int(self.x - self.size), int(self.y - self.size)))

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
```

- [ ] **Step 2: 在 Game 类中集成粒子系统**

在 `game.py` 中添加：

```python
from particles import ParticleSystem
from car import DriftState

class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.particle_system = ParticleSystem()

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

    def _draw_game(self):
        """绘制游戏画面"""
        self.track.draw(self.screen)
        self._draw_car()
        self.particle_system.draw(self.screen)
        self.ui.draw_hud(self.screen, self.car, self.track)
```

- [ ] **Step 3: 测试粒子效果**

Run: `python main.py`
Expected:
- 漂移时车尾有灰色粒子痕迹
- 喷射时车尾有橙红色尾焰

- [ ] **Step 4: 提交粒子系统**

```bash
git add particles.py game.py
git commit -m "feat: add particle system for drift and nitro effects"
```

---

## Task 8: 最终测试和清理

**Files:**
- Modify: 各文件微调

- [ ] **Step 1: 完整游戏流程测试**

Run: `python main.py`

测试检查清单：
- [ ] 菜单画面正常显示
- [ ] 按 SPACE 进入游戏
- [ ] 方向键控制赛车转向
- [ ] 加速/减速正常
- [ ] 漂移机制正常（Shift + 转向）
- [ ] 漂移后喷射触发
- [ ] 碰撞边界时反弹
- [ ] 完成一圈后显示成绩
- [ ] 按 R 重玩有效
- [ ] 按 Q 退出有效

- [ ] **Step 2: 添加音频支持（可选，预留接口）**

在 `game.py` 中添加预留的音频方法：

```python
class Game:
    def __init__(self):
        # ... 现有代码 ...
        self.sound_enabled = False
        # 音频系统预留
        # self.sounds = {}
        # self._load_sounds()

    def _load_sounds(self):
        """加载音效（预留）"""
        pass

    def play_sound(self, name):
        """播放音效（预留）"""
        pass
```

- [ ] **Step 3: 创建 README.md**

```markdown
# QQ Speed Clone - Python Racing Game

基于 Python/Pygame 的 2D 俯视视角赛车游戏，模仿 QQ 飞车的核心玩法。

## 特性

- 2D 俯视视角赛车体验
- 经典漂移机制（漂移 + 喷射加速）
- 计时挑战模式
- 碰撞检测系统
- 粒子特效

## 安装

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## 运行

\`\`\`bash
python main.py
\`\`\`

## 操作方式

| 按键 | 功能 |
|------|------|
| ↑ / W | 加速 |
| ↓ / S | 刹车/倒车 |
| ←→ / AD | 转向 |
| Shift | 漂移（转向时按住） |
| SPACE | 开始游戏 |
| R | 重玩 |
| Q | 退出 |

## 游戏机制

### 漂移系统

1. 按住 Shift 并转向触发漂移
2. 漂移时蓄力（观察漂移条）
3. 松开 Shift 触发喷射加速
4. 蓄力越多，喷射越强

### 赛道

- 绿色线为起点
- 黄色线为终点
- 蓝色点为检查点
- 必须通过所有检查点才能完成一圈

## 技术栈

- Python 3.8+
- Pygame 2.5.0

## 项目结构

\`\`\`
fc-game/
├── main.py      # 游戏入口
├── game.py      # 游戏循环和状态管理
├── car.py       # 赛车类
├── physics.py   # 物理引擎
├── track.py     # 赛道类
├── ui.py        # UI 元素
├── particles.py # 粒子系统
└── requirements.txt
\`\`\`

## 开发

这是一个学习项目，展示了如何使用 Pygame 构建一个完整的游戏循环。
\```

- [ ] **Step 4: 最终提交**

```bash
git add README.md game.py
git commit -m "docs: add README and final polish"
```

- [ ] **Step 5: 验证所有文件完整性**

Run: `git status`

确认所有文件已提交。

---

## 实施完成检查清单

- [ ] 项目结构完整
- [ ] 所有模块按设计实现
- [ ] 游戏流程正常工作
- [ ] 漂移机制符合设计
- [ ] 碰撞检测正常
- [ ] UI 显示正确
- [ ] 粒子效果正常
- [ ] 代码无语法错误
- [ ] 所有更改已提交

---

## 下一步扩展建议

完成基础版本后，可以考虑以下扩展：

1. **多赛道** - 创建不同的赛道布局
2. **多赛车** - 添加可选择的赛车，不同性能参数
3. **AI 对手** - 添加电脑对手
4. **音效** - 添加引擎声、漂移音效
5. **成就系统** - 追踪最佳成绩和成就
6. **赛道编辑器** - 允许玩家创建自定义赛道
