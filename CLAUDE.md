# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python/Pygame racing game (QQ Speed Clone) - a 2D top-down racing game with drift mechanics inspired by QQ Speed. The game is located in the `fc-game/` directory.

## Commands

### Run the game
```bash
cd fc-game && python main.py
```

### Run validation tests
```bash
cd fc-game && python test_game.py
```

### Install dependencies
```bash
pip install -r fc-game/requirements.txt
```

### Run individual test checks
No unit test framework is configured. Use `test_game.py` for module loading and initialization validation.

## Architecture

The game follows a modular OOP design with clear separation of concerns:

### Core Game Loop (`game.py`)
- **Game class**: Manages the main game loop, state transitions, and component initialization
- **GameState enum**: MENU → PLAYING → FINISHED state machine
- Fixed 60 FPS with delta time (`dt`) passed to all update methods for frame-rate independent physics

### Key Modules

| Module | Responsibility |
|--------|---------------|
| `car.py` | Vehicle physics, input handling, drift state machine (DriftState enum: NONE/DRIFTING/NITRO) |
| `physics.py` | Collision detection with track boundaries (outer/inner rectangles) |
| `track.py` | Track definition, checkpoints, lap timing, finish detection |
| `ui.py` | HUD rendering (drift bar, speed, timer), menu/results screens |
| `particles.py` | Visual effects system for drift smoke and nitro flames |

### Game Flow
1. Menu state (press SPACE to start)
2. Playing state - main racing loop with:
   - Input handling (continuous key state via `keys_pressed` set)
   - Physics update (collision detection, position update)
   - Track update (checkpoint detection, lap timing)
   - Particle emission based on drift state
3. Finished state - shows results, R to restart

### Drift System (Core Mechanic)
- Trigger: Hold Shift while turning + speed > 50
- While drifting: Car turns purple, nitro_level accumulates (0-100), drift_angle_offset creates slide effect
- Release Shift: If nitro_level > 20, enters NITRO state (red car, 1.3x speed boost, orange particles)
- Nitro duration: 0.5 seconds

### Coordinate System
- Screen: 1200x800
- Track: Rectangular oval (outer rect minus inner rect), margins of 100px
- Angles: Degrees, 0° = facing right

### Input Mapping
| Action | Keys |
|--------|------|
| Accelerate | ↑, W |
| Brake/Reverse | ↓, S |
| Steer | ←→, AD |
| Drift | Shift (hold while turning) |
| Start Game | SPACE (menu only) |
| Restart | R (finished only) |
| Quit | Q |

## Development Notes

- All modules can be imported directly without pygame.init() for testing (see `test_game.py`)
- Audio system interfaces are stubbed (`sound_enabled = False`, empty `play_sound()` method)
- Chinese comments throughout codebase - UI text is in English
- Batch files (`启动游戏.bat`, `测试代码.bat`) provided for Windows users
