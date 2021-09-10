# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo1.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     

    display_sizex = 500
    display_sizey = 500
    spaceship_radius = 30
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((display_sizex,display_sizey))
     
    # define a variable to control the main loop
    running = True
     
    x= 100
    y= 100
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                y=y-10
                print("w is pressed")
            if pressed[pygame.K_s]:
                y=y+10
                print("s is pressed")
            if pressed[pygame.K_a]:
                x=x-10
                print("a is pressed")
            if pressed[pygame.K_d]:
                x=x+10
                print("d is pressed")
        

            # check if y or x is larger than display size or smaller than 0, if so set to max screen size or 0
        if ((x+spaceship_radius)>display_sizex):
            x = display_sizex-spaceship_radius
        if ((y+spaceship_radius)>display_sizey):
            y = display_sizey-spaceship_radius
        if ((x-spaceship_radius)<0):  
            x = 0+spaceship_radius
        if ((y-spaceship_radius)<0):
            y = 0+spaceship_radius

    



        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0,255,0), (x,y), spaceship_radius)


        # should be after all visual updates in loop. redraws screen
        pygame.display.flip()    
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()