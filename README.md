# QQ Speed Clone - Python Racing Game

基于 Python/Pygame 的 2D 俯视视角赛车游戏，模仿 QQ 飞车的核心玩法。

## 特性

- 2D 俯视视角赛车体验
- 经典漂移机制（漂移 + 喷射加速）
- 计时挑战模式
- 碰撞检测系统
- 粒子特效

## 安装

```bash
pip install -r requirements.txt
```

## 运行

```bash
python main.py
```

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

```
fc-game/
├── main.py      # 游戏入口
├── game.py      # 游戏循环和状态管理
├── car.py       # 赛车类
├── physics.py   # 物理引擎
├── track.py     # 赛道类
├── ui.py        # UI 元素
├── particles.py # 粒子系统
└── requirements.txt
```

## 开发

这是一个学习项目，展示了如何使用 Pygame 构建一个完整的游戏循环。
