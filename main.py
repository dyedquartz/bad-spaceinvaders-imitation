import pygame

def main():

    #Init screen
    pygame.init()
    pygame.display.set_caption("TEST")
    screen_width = 1080
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    #pygame.display.toggle_fullscreen()

    #Characters and Images
    smiley = pygame.image.load("smiley.png").convert()
    smileyrect = createLargerImageRects(smiley, 5)

    clock = pygame.time.Clock()

    #Game Variables
    speed = 2
    running = True

    #Main Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ##INPUT
        #Character Input
        if (pygame.key.get_pressed()[pygame.K_RIGHT]):
            smileyrect = smileyrect.move([speed,0])
        if (pygame.key.get_pressed()[pygame.K_LEFT]):
            smileyrect = smileyrect.move([-speed,0])
        if (pygame.key.get_pressed()[pygame.K_UP]):
            smileyrect = smileyrect.move([0, -speed])
        if (pygame.key.get_pressed()[pygame.K_DOWN]):
            smileyrect = smileyrect.move([0, speed])

        #Utility Input
        if (pygame.key.get_pressed()[pygame.K_F11]):
            pygame.display.toggle_fullscreen()
        if (pygame.key.get_pressed()[pygame.K_q]):
            running = False

        #blits background and character
        screen.fill((0,0,0))
        screen.blit(smiley, smileyrect)

        #Updates Screen
        pygame.display.update(smileyrect)

        #yeet, 60fps
        clock.tick(60)

#Literally just increases a rectangle's size by x amount
def createLargerImageRects(image, size):
    rectangle = image.get_rect()
    return pygame.Rect(rectangle.left - size, rectangle.top - size, rectangle.width + size*2, rectangle.height + size*2)

#Only runs if it's the file executed
if __name__=="__main__":
    main()
