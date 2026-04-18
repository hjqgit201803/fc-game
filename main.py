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
