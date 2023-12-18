import pygame

screenWidth = 1268
screenHeight = 746

screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()

def WirteScreen(screen, size, num, line):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', size)
    title = font.render(line, True, (255, 255, 255))
    start_button = font.render(str(num), True, (255, 255, 255))
    screen.blit(title, (screenWidth / 2 - title.get_width() / 2, screenHeight / 2 - title.get_height() / 2))
    screen.blit(start_button,
                (screenWidth / 2 - start_button.get_width() / 2, screenHeight / 2 + start_button.get_height() / 2))
    pygame.display.update()

def Aready():
    aready = 10
    speed = 1
    line = 'Look straight at the screen'
    while aready + 1:
        WirteScreen(screen, 80, aready, line)
        pygame.display.update()
        clock.tick(speed)
        aready -= 1
    pygame.quit()
