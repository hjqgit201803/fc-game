@echo off
chcp 65001 >nul
echo ============================================
echo QQ Speed Clone - 游戏启动器
echo ============================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python！
    echo 请先安装 Python 3.8 或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python 已安装
echo.

REM 检查 Pygame 是否安装
python -c "import pygame" >nul 2>&1
if errorlevel 1 (
    echo [提示] Pygame 未安装，正在安装...
    pip install pygame==2.5.0
    if errorlevel 1 (
        echo [错误] Pygame 安装失败！
        pause
        exit /b 1
    )
)

echo [OK] Pygame 已安装
echo.
echo ============================================
echo 正在启动 QQ Speed Clone...
echo ============================================
echo.
echo 游戏操作:
echo   ↑/W    - 加速
echo   ↓/S    - 刹车
echo   ←→/AD  - 转向
echo   Shift  - 漂移（转向时按住）
echo   SPACE  - 开始游戏
echo   R      - 重玩
echo   Q      - 退出
echo.
echo ============================================
echo.

python main.py

if errorlevel 1 (
    echo.
    echo [错误] 游戏运行出错！
    pause
)
