
import draw
import color

#Konstruiert einen Spieltisch
c_bande = 0.02
c_bande_2 = c_bande * 1000 / 600

def tisch():
    
    draw.set_pen_radius(1)

    draw.set_pen_color(color.DARK_GREEN)

    draw.filled_rectangle(0.2 - c_bande, 0.25 - c_bande_2, 0.6 + (2 * c_bande), 0.5 + (2 * c_bande_2))

    draw.set_pen_color(color.GREEN)

    draw.filled_rectangle(0.2, 0.25, 0.6, 0.5)

    # Goldene Ecken

    draw.set_pen_color(color.GOLD)

    draw.filled_rectangle(0.2 - c_bande, 0.25 - c_bande_2, c_bande, c_bande_2)

    draw.filled_rectangle(0.2 - c_bande, 0.75, c_bande, c_bande_2)

    draw.filled_rectangle(0.5 - (c_bande / 2), 0.25 - c_bande_2, c_bande, c_bande_2)

    draw.filled_rectangle(0.5 - (c_bande / 2), 0.75, c_bande, c_bande_2)

    draw.filled_rectangle(0.8, 0.25 - c_bande_2, c_bande, c_bande_2)

    draw.filled_rectangle(0.8, 0.75, c_bande, c_bande_2)

    # Löcher

    draw.set_pen_color(color.BLACK)

    draw.filled_circle(0.2, 0.25, c_bande * 0.75)

    draw.filled_circle(0.2, 0.75, c_bande * 0.75)

    draw.filled_circle(0.5, 0.25, c_bande * 0.75)

    draw.filled_circle(0.5, 0.75, c_bande * 0.75)

    draw.filled_circle(0.8, 0.25, c_bande * 0.75)

    draw.filled_circle(0.8, 0.75, c_bande * 0.75)

    # Rauten Markierung

    draw.set_pen_color(color.WHITE)

    draw.filled_raute(0.2 - (c_bande/2), 0.375, c_bande/2)

    draw.filled_raute(0.2 - (c_bande/2), 0.5, c_bande/2)

    draw.filled_raute(0.2 - (c_bande/2), 0.625, c_bande/2)

    draw.filled_raute(0.8 + (c_bande/2), 0.375, c_bande/2)

    draw.filled_raute(0.8 + (c_bande/2), 0.5, c_bande/2)

    draw.filled_raute(0.8 + (c_bande/2), 0.625, c_bande/2)

    draw.filled_raute(0.275, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.35, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.425, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.575, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.65, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.725, 0.25 - (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.275, 0.75 + (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.35, 0.75 + (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.425, 0.75 + (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.575, 0.75 + (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.65, 0.75 + (c_bande_2/2), c_bande/2)

    draw.filled_raute(0.725, 0.75 + (c_bande_2/2), c_bande/2)
    
    #Spieler angaben
    draw.set_pen_color(color.BLACK)
    draw.text(0.1,0.75,"Spieler 1 eingelocht :")
    draw.text(0.9,0.75,"Spieler 2 eingelocht :")