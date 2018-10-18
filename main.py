import pygame

def main():
    pygame.init()

    pygame.display.set_caption("TEST")

    screen_width = 480
    screen_height = 360
    screen = pygame.display.set_mode((screen_width,screen_height))

    image = pygame.image.load("smiley.png")

    running = True

    clock = pygame.time.Clock()

    xpos=50
    ypos=50

    step_x=10
    step_y=10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y

        xpos += step_x
        ypos += step_y

        screen.blit(image, (xpos,ypos))
        pygame.display.flip()

        clock.tick(10)



if __name__=="__main__":
    main()
