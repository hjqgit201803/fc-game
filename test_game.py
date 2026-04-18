#!/usr/bin/env python3
"""
QQ Speed Clone - 游戏测试脚本
验证所有模块是否可以正确加载
"""

import sys
import os

print("=" * 50)
print("QQ Speed Clone - 代码验证测试")
print("=" * 50)

# 检查 Python 版本
print(f"\n✓ Python 版本: {sys.version}")
print(f"✓ Python 路径: {sys.executable}")

# 检查所有必需的文件
required_files = [
    "main.py",
    "game.py",
    "car.py",
    "physics.py",
    "track.py",
    "ui.py",
    "particles.py",
    "requirements.txt"
]

print("\n" + "=" * 50)
print("文件检查")
print("=" * 50)
for file in required_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"✓ {file:20s} ({size:,} bytes)")
    else:
        print(f"✗ {file:20s} (缺失!)")

# 尝试导入 Pygame
print("\n" + "=" * 50)
print("模块导入测试")
print("=" * 50)
try:
    import pygame
    print(f"✓ Pygame 已安装 (版本 {pygame.version.ver})")
except ImportError as e:
    print(f"✗ Pygame 未安装: {e}")
    print("\n请运行: pip install pygame")
    sys.exit(1)

# 测试导入所有游戏模块
print("\n" + "=" * 50)
print("游戏模块导入测试")
print("=" * 50)

modules = [
    ("car", "Car 类"),
    ("physics", "Physics 类"),
    ("track", "Track 类"),
    ("ui", "UI 类"),
    ("particles", "粒子系统"),
    ("game", "Game 类")
]

all_ok = True
for module_name, description in modules:
    try:
        __import__(module_name)
        print(f"✓ {description:20s} ({module_name}.py)")
    except Exception as e:
        print(f"✗ {description:20s} ({module_name}.py) - 错误: {e}")
        all_ok = False

# 测试枚举和类
print("\n" + "=" * 50)
print("类和枚举测试")
print("=" * 50)

try:
    from car import Car, DriftState
    from physics import Physics
    from track import Track
    from ui import UI
    from particles import ParticleSystem
    from game import Game, GameState

    print(f"✓ Car 类")
    print(f"✓ DriftState 枚举: {list(DriftState)}")
    print(f"✓ Physics 类")
    print(f"✓ Track 类")
    print(f"✓ UI 类")
    print(f"✓ ParticleSystem 类")
    print(f"✓ Game 类")
    print(f"✓ GameState 枚举: {list(GameState)}")
except Exception as e:
    print(f"✗ 导入错误: {e}")
    all_ok = False

# 游戏功能测试（不启动图形界面）
print("\n" + "=" * 50)
print("游戏组件初始化测试")
print("=" * 50)

try:
    # 不调用 pygame.init() 以避免创建窗口
    track = Track(1200, 800)
    print(f"✓ Track 初始化成功")
    print(f"  - 起点位置: ({track.start_pos['x']}, {track.start_pos['y']})")
    print(f"  - 检查点数量: {len(track.checkpoints)}")
    print(f"  - 赛道边界: {track.boundaries}")

    car = Car(100, 400, 0)
    print(f"✓ Car 初始化成功")
    print(f"  - 初始位置: ({car.x}, {car.y})")
    print(f"  - 初始角度: {car.angle}°")
    print(f"  - 最大速度: {car.max_speed}")

    physics = Physics()
    physics.set_track_boundaries(track.boundaries)
    print(f"✓ Physics 初始化成功")
    print(f"  - 边界已设置")

    ui = UI(1200, 800)
    print(f"✓ UI 初始化成功")

    particles = ParticleSystem()
    print(f"✓ ParticleSystem 初始化成功")

except Exception as e:
    print(f"✗ 初始化错误: {e}")
    import traceback
    traceback.print_exc()
    all_ok = False

# 最终结果
print("\n" + "=" * 50)
if all_ok:
    print("✓✓✓ 所有测试通过！游戏已准备就绪！")
    print("=" * 50)
    print("\n要启动游戏，请运行: python main.py")
    print("\n游戏操作:")
    print("  ↑/W    - 加速")
    print("  ↓/S    - 刹车")
    print("  ←→/AD  - 转向")
    print("  Shift  - 漂移（转向时按住）")
    print("  SPACE  - 开始游戏")
    print("  R      - 重玩")
    print("  Q      - 退出")
else:
    print("✗✗✗ 测试失败！请检查错误信息")
    print("=" * 50)

print("=" * 50)
