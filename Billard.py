import pygame

import draw

import color

import bowl

import tisch

import random

import spieler

def queue(k_x):
    draw.set_pen_color(color.DARK_RED)
    (mouse_x, mouse_y) = draw.mouse_position()
    draw._thick_line(k_x.x, k_x.y, k_x.x - (((mouse_x - k_x.x) / ((((mouse_y - k_x.y)**2) + ((mouse_x - k_x.x)**2)) **
            (1/2))) * 0.15) , k_x.y - (((mouse_y - k_x.y) / ((((mouse_y - k_x.y)**2) + ((mouse_x - k_x.x)**2))**(1/2)))
                                       * 0.15 * (10/6)), 0.003)


def kollision_check(k1,k2):
    dx = k2.x - k1.x
    dy = (k2.y - k1.y) * 6/10
    dist = (dx ** 2 + dy ** 2) ** 0.5
    #Enthacken
    if dist < (k1.r + k2.r):
        if k1.x >= k2.x:
            k1.x = k1.x + (k1.r - dist/2) * 2
        if k1.y >= k2.y:
            k1.y = k1.y + (k1.r - dist/2) * 2
        if k1.x < k2.x:
            k1.x = k1.x - (k1.r - dist/2) * 2
        if k1.y < k2.y:
            k1.y = k1.y - (k1.r - dist/2) * 2
                
    #Überprüfe Kollision
    if dist <= (k1.r + k2.r):
        return True
    else:
        return False
    
def strike_check(kugel,x,y,r):
    dist = ((x - kugel.x)**2 + (y - kugel.y)**2 )**0.5
    if dist <= r:
        return True
    else:
        return False

def replace_bowl(kugel,koe,striked):
        if draw.mouse_pressed():
            x,y = draw.mouse_position()
            if y > 0.25 + 0.02 * 10/6 and y < 0.75 - 0.02 * 10/6 :
                kugel.set_x(0.3)
                kugel.set_y(y)
                kugel.set_v_x(0)
                kugel.set_v_y(0)
                koe.append(kugel)
                striked.remove(kugel)
        return koe,striked

def main():
    pygame.init()

    #screen = pygame.display.set_mode((1200, 1200))

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 100)

    pygame.display.set_caption("Billard")

    draw.set_canvas_size(1000, 600)

    running = True

    c_bande = 0.02
    c_bande_2 = c_bande * 1000 / 600
    
    #setzt Löcher
    holes = [(0.2,0.25),(0.2,0.75),(0.5,0.25),(0.5,0.75),(0.8,0.25),(0.8,0.75)]
    
    #Initialisiert die Kugeln
    liste = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(liste)

    x = 0
    j = 0
    liste_neu = []
    while x != 7:
        if liste[j] < 9:
            liste_neu.append(liste[j])
            j = j + 1
            x = x + 1
        else:
            j = j + 1

    x = 0
    j = 0
    while x != 7:
        if liste[j] >= 9:
            liste_neu.append(liste[j])
            j = j + 1
            x = x + 1
        else:
            j = j + 1

    for i in liste_neu:
        liste.remove(i)


    c = (((8 * ((((((3**(1/2)) / 2) * c_bande)**2) + ((0.5 * c_bande_2)**2))**(1/2)))**2) - ((4 * c_bande_2)**2))**(1/2)

    startwert_1 = 0.65
    startwert_2 = 0.5


    k_0 = bowl.kugel(0.35, 0.5, 0, 0, c_bande * 0.5, 0)
    k_1 = bowl.kugel(startwert_1, startwert_2, 0, 0, c_bande * 0.5, liste_neu[0])
    k_2 = bowl.kugel(startwert_1 + (c / 8), startwert_2 + (c_bande_2 / 2), 0, 0, c_bande * 0.5, liste_neu[1])
    k_3 = bowl.kugel(startwert_1 + (c / 8), startwert_2 - (c_bande_2 / 2), 0, 0, c_bande * 0.5, liste_neu[7])
    k_4 = bowl.kugel(startwert_1 + (c / 4), startwert_2 + c_bande_2, 0, 0, c_bande * 0.5, liste_neu[8])
    k_5 = bowl.kugel(startwert_1 + (c / 4), startwert_2, 0, 0, c_bande * 0.5, 8)
    k_6 = bowl.kugel(startwert_1 + (c / 4), startwert_2 - c_bande_2, 0, 0, c_bande * 0.5, liste_neu[2])
    k_7 = bowl.kugel(startwert_1 + (3*c / 8), startwert_2 + (1.5 * c_bande_2), 0, 0, c_bande * 0.5, liste_neu[3])
    k_8 = bowl.kugel(startwert_1 + (3*c / 8), startwert_2 + (0.5 * c_bande_2), 0, 0, c_bande * 0.5, liste_neu[9])
    k_9 = bowl.kugel(startwert_1 + (3*c / 8), startwert_2 - (0.5 * c_bande_2), 0, 0, c_bande * 0.5, liste_neu[4])
    k_10 = bowl.kugel(startwert_1 + (3*c / 8), startwert_2 - 1.5 * c_bande_2, 0, 0, c_bande * 0.5, liste_neu[10])
    k_11 = bowl.kugel(startwert_1 + (c / 2), startwert_2 + (2 * c_bande_2), 0, 0, c_bande * 0.5, liste_neu[11])
    k_12 = bowl.kugel(startwert_1 + (c / 2), startwert_2 + c_bande_2, 0, 0, c_bande * 0.5, liste_neu[12])
    k_13 = bowl.kugel(startwert_1 + (c / 2), startwert_2, 0, 0, c_bande * 0.5, liste_neu[5])
    k_14 = bowl.kugel(startwert_1 + (c / 2), startwert_2 - c_bande_2, 0, 0, c_bande * 0.5, liste_neu[13])
    k_15 = bowl.kugel(startwert_1 + (c / 2), startwert_2 - (2 * c_bande_2), 0, 0, c_bande * 0.5, liste_neu[6])

    hole_in = []
    k = [k_0, k_1, k_2, k_3, k_4, k_5, k_6, k_7, k_8, k_9, k_10, k_11, k_12, k_13, k_14, k_15]
    
    #Spieler konfigurieren
    player = []
    player.append(spieler.spieler(0))
    player.append(spieler.spieler(1))
    round_counter = 0
    no_ply = 0
    end = False
    while running:
 #       clock.tick(1000000)
        tisch.tisch()

        kugel_geschw_test = 0
        for i in k:
            if i.v_x or i.v_y != 0:
                kugel_geschw_test += 1

        if kugel_geschw_test == 0:
            queue(k_0,)
            k_0.move()

        #eingelochte Kugeln
        for ply in player:
            ply.draw_holeins()
                
                
        if (k_0 in hole_in) and (kugel_geschw_test == 0):
            check = True
            while(check):
                tisch.tisch()
                draw.set_pen_color(color.WHITE)
                draw._thick_line(0.35, 0.25, 0.35, 0.75, 0.001)
                for kugel in k:
                    kugel.draw_kugel()
                draw.show(1)
                if draw.mouse_pressed():
                    (press_x, press_y) = draw.mouse_position()
                    if 0.25 <= press_y <= 0.75:
                        ueberlagerungstest = 0
                        for i in k:
                            dx = i.x - 0.35
                            dy = (i.y - press_y) * 6 / 10
                            dist = ((dx ** 2) + (dy ** 2)) ** 0.5
                            if dist <= (2 * i.r):
                                ueberlagerungstest = ueberlagerungstest + 1
                        if ueberlagerungstest == 0:
                            hole_in.remove(k_0)
                            k_0 = bowl.kugel(0.35, press_y, 0, 0, c_bande * 0.5, 0)
                            k.append(k_0)
                            check = False
                            
        else:
            if draw.mouse_pressed() and k_0.v_x == k_0.v_y == 0:

                (press_x, press_y) = draw.mouse_position()
                k_0.v_x = (press_x - k_0.x) / 25
                k_0.v_y = (press_y - k_0.y) / 25
                round_counter += 1
          
        #Text Spieleranzeige
        if kugel_geschw_test == 0:
            if not (round_counter % 2 == no_ply):
                hole_in = []
            no_ply = round_counter % 2
            draw.set_pen_color(color.BLACK)
            draw.set_font_size(16)
            draw.set_pen_radius(5)
            draw.text(0.2,0.85,"Spieler "+str(no_ply+1)+" ist an der Reihe")
        
            # Bewegungen durchführen und zeichnen
        for kugel_1 in k:
            kugel_1.move()
            # Zeichnen
            kugel_1.draw_kugel()
            # Kollision
            k_tmp = k.copy()
            k_tmp.remove(kugel_1)
            for kugel_2 in k_tmp:
                if kollision_check(kugel_1, kugel_2):
                    kugel_1.kollision(kugel_2) 
            #Abfrage ob Kugel eingelocht
            for hole in holes :
                if strike_check(kugel_1,hole[0],hole[1],c_bande*0.75):
                    k.remove(kugel_1)
                    hole_in.append(kugel_1)
                    
                        
                    #weist die kugel_art den Spielern durch
                    if player[0].kugel_art == None and player[1].kugel_art == None :
                        if kugel_1.number == 8 :
                            end = True
                            ply = player.copy()
                            ply.remove(ply[no_ply])
                            winner = ply[0]
                        if not kugel_1.number == 0:
                            round_counter += 1    
                        player[no_ply].strike(kugel_1)
                        if no_ply == 0 and player[no_ply].kugel_art == 'voll' :
                            player[1].kugel_art = 'halb'
                        if i == 0 and player[no_ply].kugel_art == 'halb' :
                            player[1].kugel_art = 'voll'
                        if no_ply == 1 and player[no_ply].kugel_art == 'voll' :
                            player[0].kugel_art = 'halb'
                        if no_ply == 1 and player[no_ply].kugel_art == 'halb' :
                            player[0].kugel_art = 'voll'
                    #Schaut welche Kugel eingelocht wurde
                    #bestimmt das Resultat für die Spieler
                    else :
                        #Falls Schwarze Kugel versenkt wurde
                        if kugel_1.number == 8 and not (len(player[no_ply].hole_in) == 7):
                            end = True
                            ply = player.copy()
                            ply.remove(player[no_ply])
                            winner = ply[0]
                        elif kugel_1.number == 8 and len(player[no_ply].hole_in) == 7:
                            end = True
                            winner = player[no_ply]
                        #Falls eine Kugel versenkt wurde die nicht weiß oder Schwarz ist  
                        if not ((kugel_1.number > 8 and player[no_ply].kugel_art == 'halb') or (kugel_1.number < 8 and kugel_1.number > 0 and player[no_ply].kugel_art == 'voll'))                   :
                            if no_ply == 0 and not kugel_1.number == 0 :
                                player[1].strike(kugel_1)
                            if no_ply == 1 and not kugel_1.number == 0 :
                                player[0].strike(kugel_1)
                        else:
                            player[no_ply].strike(kugel_1)
                            round_counter += 1
        
        draw.show(1)
        draw.clear()
        #Bricht die while schleife ab, falls ein Spieler gewonnen hat
        if end :
            break
    #Gibt den gewinner an    
    draw.set_pen_color(color.BLACK) 
    draw.set_font_size(20)
    draw.text(0.5,0.5,"Spieler "+ str(winner.num + 1) + " hat gewonnen")
    draw.show()
                    
        

main()

