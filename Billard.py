import pygame

import draw

import color

import bowl

import tisch

def kollisions_check(k1,k2):
    dx = k2.x - k1.x
    dy = k2.y - k1.y
    dist = (dx ** 2 + dy ** 2) ** 0.5
    if dist <= (k1.r + k2.r) :
        return True
    else : 
        return False


def main():
    pygame.init()

    width = 700
    highth = 500


    #screen = pygame.display.set_mode((1200, 1200))

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 100)

    clock = pygame.time.Clock()

    pygame.display.set_caption("Billard")

    draw.set_canvas_size(1000, 600)

    running = True

    c_bande = 0.02
    c_bande_2 = c_bande * 1000 / 600

    # Halb = 1 , Voll = 0
    k_white = bowl.kugel(0.7, 0.5, 0, 0, c_bande * 0.5,color.WHITE,0)
    
    k_black = bowl.kugel(0.35,0.5,0,0,c_bande * 0.5,color.YELLOW,1)

    while running:
        clock.tick(1000)

        draw.clear()

        tisch.tisch()
        
        
        #Bewegungn zeichnen
        if draw.mouse_pressed() :
            x,y = draw.mouse_position()
            k_white.move_to(x,y)

        k_white.draw_kugel()
        k_black.draw_kugel()

        k_white.move()
        k_black.move()
         
        #Kollision
        if kollisions_check(k_white,k_black):
            k_white.kollision(k_black)
        
        
        
        
        
        
        draw.show(1)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

    pygame.display.flip()

main()

def test():

    running = True

    while running:

        draw.set_canvas_size(800, 800)

        #draw.show(10000)

        draw.clear()

        #draw.set_pen_radius(1)

        draw.set_pen_color(color.RED)

        draw.filled_rectangle(0, 0, 1, 1)

        pygame.display.flip()

        draw.show(10000)

#test()
