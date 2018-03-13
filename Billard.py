import pygame

import draw

import color

import bowl

import tisch

def kollision_check(k1,k2):
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
    #Init Kugeln
    k = []
    k.append(bowl.kugel(0.7, 0.5, 0, 0, c_bande * 0.5,color.WHITE,0))
    
    k.append(bowl.kugel(0.35,0.5,0,0,c_bande * 0.5,color.YELLOW,1))
    
    k.append(bowl.kugel(0.34,0.5,0,0,c_bande * 0.5,color.BLUE,9))

    while running:
        clock.tick(1000)

        draw.clear()

        tisch.tisch()
        
        
        #Bewegungn zeichnen
        if draw.mouse_pressed() :
            x,y = draw.mouse_position()
            k[0].move_to(x,y)

        for kugel_1 in k:
            #Zeichnen
            kugel_1.move()
            kugel_1.draw_kugel()
            #Kollision
            k_tmp = k.copy()
            k_tmp.remove(kugel_1) 
            for kugel_2 in k_tmp:
                if kollision_check(kugel_1,kugel_2):
                    kugel_1.kollision(kugel_2)
        
        
        
        
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
