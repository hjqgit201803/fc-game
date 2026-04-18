@echo off
chcp 65001 >nul
echo ============================================
echo QQ Speed Clone - 代码测试
echo ============================================
echo.

REM 测试代码语法
echo [1/4] 检查 Python 语法...
python -m py_compile main.py >nul 2>&1
if errorlevel 1 (
    echo [错误] main.py 语法错误！
    goto :error
)
echo [OK] main.py

python -m py_compile game.py >nul 2>&1
if errorlevel 1 (
    echo [错误] game.py 语法错误！
    goto :error
)
echo [OK] game.py

python -m py_compile car.py >nul 2>&1
if errorlevel 1 (
    echo [错误] car.py 语法错误！
    goto :error
)
echo [OK] car.py

python -m py_compile physics.py >nul 2>&1
if errorlevel 1 (
    echo [错误] physics.py 语法错误！
    goto :error
)
echo [OK] physics.py

python -m py_compile track.py >nul 2>&1
if errorlevel 1 (
    echo [错误] track.py 语法错误！
    goto :error
)
echo [OK] track.py

python -m py_compile ui.py >nul 2>&1
if errorlevel 1 (
    echo [错误] ui.py 语法错误！
    goto :error
)
echo [OK] ui.py

python -m py_compile particles.py >nul 2>&1
if errorlevel 1 (
    echo [错误] particles.py 语法错误！
    goto :error
)
echo [OK] particles.py

echo.
echo [2/4] 测试模块导入...
python -c "from car import Car, DriftState; from physics import Physics; from track import Track; from ui import UI; from particles import ParticleSystem; from game import Game, GameState" >nul 2>&1
if errorlevel 1 (
    echo [错误] 模块导入失败！
    goto :error
)
echo [OK] 所有模块导入成功

echo.
echo [3/4] 测试 Pygame...
python -c "import pygame; print('  Pygame 版本:', pygame.version.ver)" 2>&1
if errorlevel 1 (
    echo [错误] Pygame 未安装！
    echo 请运行: pip install pygame
    goto :error
)

echo.
echo [4/4] 游戏文件清单...
for %%f in (main.py game.py car.py physics.py track.py ui.py particles.py) do (
    if exist %%f (
        echo   [OK] %%f
    ) else (
        echo   [MISSING] %%f
        goto :error
    )
)

echo.
echo ============================================
echo ✓✓✓ 所有测试通过！游戏已准备就绪！
echo ============================================
echo.
echo 请双击 "启动游戏.bat" 来运行游戏
echo 或者在命令行运行: python main.py
echo.
pause
goto :end

:error
echo.
echo ============================================
echo ✗✗✗ 测试失败！请检查错误信息
echo ============================================
pause
exit /b 1

:end
