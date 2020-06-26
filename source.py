from sys import exit
import pygame
import classes

def main():
    FPS = 60
    WIDTH = 800
    MENU_WIDTH = 200
    HEIGHT = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    cellSize = 15
    textOffsetX = 40
    textOffsetY = 20
    pressed = False
    spawn = False
    despawn = False
    randomSpawn = False

    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame.Surface((MENU_WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font("C:\WINDOWS\Fonts\ARIAL.TTF", 16)
    spawnText = font.render("Random spawn", 1, BLACK)
    clearText = font.render("Clear", 1, BLACK)
    startText = font.render("Start/Stop", 1, BLACK)
    infoText = font.render("Info: you can paint", 1, BLACK)
    spaceText = font.render("Hold space for start", 1, BLACK)

    grid = classes.Grid(WIDTH - MENU_WIDTH, HEIGHT, cellSize)

    while True:
        sc.fill(BLACK)
        menu.fill(WHITE)
        pygame.draw.rect(menu, BLACK, (10, 10, MENU_WIDTH - 20, 40), 1)
        pygame.draw.rect(menu, BLACK, (10, 60, MENU_WIDTH - 20, 40), 1)
        pygame.draw.rect(menu, BLACK, (10, 110, MENU_WIDTH - 20, 40), 1)
        menu.blit(spawnText, (textOffsetX, textOffsetY))
        menu.blit(clearText, (textOffsetX, textOffsetY + 50))
        menu.blit(startText, (textOffsetX, textOffsetY + 100))
        menu.blit(infoText, (10, HEIGHT - 50))
        menu.blit(spaceText, (10, HEIGHT - 30))
        sc.blit(menu, (WIDTH - MENU_WIDTH, 0))

        pygame.display.set_caption("FPS: " + str(clock.get_fps() // 1))

        grid.draw(sc)
                


        for i in pygame.event.get():

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    pressed = True

            if i.type == pygame.KEYUP:
                if i.key == pygame.K_SPACE:
                    pressed = False

            if i.type == pygame.MOUSEBUTTONDOWN:

                if i.button == 1:
                    if i.pos[0] <= WIDTH - MENU_WIDTH:
                        pos = i.pos
                        spawn = True
                    else:
                        if i.pos[0] > WIDTH - MENU_WIDTH + 10 and i.pos[0] < WIDTH - 10:
                            if i.pos[1] > 10 and i.pos[1] < 50:
                                grid.clear()
                                grid.randomInit()
                            if i.pos[1] > 60 and i.pos[1] < 110:
                                grid.clear()
                            if i.pos[1] > 120 and i.pos[1] < 170:
                                if pressed == True:
                                    pressed = False
                                else:
                                    pressed = True

                if i.button == 3:
                    if i.pos[0] <= WIDTH - MENU_WIDTH:
                        pos = i.pos
                        despawn = True
                    else:
                        pass

            if i.type == pygame.MOUSEBUTTONUP:

                if i.button == 1:
                    if i.pos[0] <= WIDTH - MENU_WIDTH:
                        spawn = False
                    else:
                        pass

                if i.button == 3:
                    if i.pos[0] <= WIDTH - MENU_WIDTH:
                        despawn = False
                    else:
                        pass

            if i.type == pygame.QUIT:
                exit()
        
        if spawn:
            grid.createClick(pos)
            if pygame.mouse.get_pos()[0] <= WIDTH - MENU_WIDTH:
                pos = pygame.mouse.get_pos()
        
        if despawn:
            grid.deleteClick(pos)
            if pygame.mouse.get_pos()[0] <= WIDTH - MENU_WIDTH:
                pos = pygame.mouse.get_pos()

        if pressed:
            pygame.time.wait(75)
            grid.change()

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    main()