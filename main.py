import pygame

def main():
    pygame.init()

    pygame.display.set_caption("TEST")

    screen_width = 480
    screen_height = 360
    screen = pygame.display.set_mode((screen_width,screen_height))

    smiley = pygame.image.load("smiley.png").convert()
    smileyrect = createLargerImageRects(smiley, 5)

    running = True

    clock = pygame.time.Clock()

    speed = 5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (pygame.key.get_pressed(pygame.K_RIGHT)):
            smileyrect = smileyrect.move([speed,0])
        if (pygame.key.get_pressed(pygame.K_LEFT)):
            smileyrect = smileyrect.move([-speed,0])
        if (pygame.key.get_pressed(pygame.K_UP)):
            smileyrect = smileyrect.move([0, -speed])
        if (pygame.key.get_pressed(pygame.K_DOWN)):
            smileyrect = smileyrect.move([0, speed])

        print(smileyrect.top)
        screen.fill((0,0,0))
        screen.blit(smiley, smileyrect)
        pygame.display.update(smileyrect)

        clock.tick(60)

def createLargerImageRects(image, size):
    rectangle = image.get_rect()
    return pygame.Rect(rectangle.left - size, rectangle.top - size, rectangle.width + size*2, rectangle.height + size*2)


if __name__=="__main__":
    main()
