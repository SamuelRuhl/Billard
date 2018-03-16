import pygame

import color

import draw

def reibung(v):

    #if (v >= 0) and (v - 0.00005 <= 0):
     #   v = 0
    #if (v <= 0) and (v + 0.00005 >= 0):
     #   v = 0
    if v > 0:
        v = v * 0.986
    if v < 0:
        v = v * 0.986
    if abs(v) < 0.00001:
        v = 0


    return v

class kugel:
    def __init__(self, x, y, v_x, v_y, r, number):

        self.x = x

        self.y = y

        self.v_x = v_x

        self.v_y = v_y

        self.r = r

        #self.color = color

        self.number = number

    def draw_kugel(self):

        if self.number == 0:
            draw.set_pen_color(color.WHITE)
        if self.number == 1:
            draw.set_pen_color(color.YELLOW)
        if self.number == 2:
            draw.set_pen_color(color.BLUE)
        if self.number == 3:
            draw.set_pen_color(color.RED)
        if self.number == 4:
            draw.set_pen_color(color.VIOLET)
        if self.number == 5:
            draw.set_pen_color(color.ORANGE)
        if self.number == 6:
            draw.set_pen_color(color.DARK_GREEN)
        if self.number == 7:
            draw.set_pen_color(color.BROWN)
        if self.number == 8:
            draw.set_pen_color(color.BLACK)
        if self.number == 9:
            draw.set_pen_color(color.YELLOW)
        if self.number == 10:
            draw.set_pen_color(color.BLUE)
        if self.number == 11:
            draw.set_pen_color(color.RED)
        if self.number == 12:
            draw.set_pen_color(color.VIOLET)
        if self.number == 13:
            draw.set_pen_color(color.ORANGE)
        if self.number == 14:
            draw.set_pen_color(color.DARK_GREEN)
        if self.number == 15:
            draw.set_pen_color(color.BROWN)

        #draw.set_pen_color(self.color)
        draw.filled_circle(self.x, self.y, self.r)
        if self.number >= 8:
            draw.set_pen_color(color.WHITE)
            draw.filled_circle(self.x, self.y, self.r * 0.8)
        draw.set_pen_color(color.BLACK)
        if self.number == 0:
            draw.set_pen_color(color.WHITE)
        draw.text(self.x, self.y, str(self.number))


    def move(self):

        c_bande = 0.02
        c_bande_2 = 0.02 * (1000 / 600)

        self.x = self.x + self.v_x
        self.y = self.y + self.v_y

        self.v_x = reibung(self.v_x)
        self.v_y = reibung(self.v_y)

        if self.y <= 0.75 - (c_bande_2 * 0.75) and self.y >= 0.25 + (c_bande_2 * 0.75):
            if (self.x + self.r) >= 0.8 or (self.x - self.r) <= 0.2:
                self.v_x = -self.v_x
                if (self.x + self.r) > 0.8:
                    self.x -= ((self.x + self.r) - 0.8) * 2
                if (self.x - self.r) < 0.2:
                    self.x -= ((self.x - self.r) - 0.2) * 2

        if self.x >= 0.2 + (c_bande * 0.75) and self.x <= 0.5 - (c_bande * 0.75) or\
                self.x >= 0.5 + (c_bande * 0.75) and self.x <= 0.8 - (c_bande * 0.75):
            if ((self.y + (self.r * (1000 / 600))) >= 0.75) or ((self.y - (self.r * (1000 / 600))) <= 0.25):
                self.v_y = -self.v_y
                if ((self.y + (self.r * (1000 / 600))) > 0.75):
                    self.y -= ((self.y + self.r * (1000 / 600)) - 0.75) * 2
                if ((self.y - (self.r * (1000 / 600))) < 0.25):
                    self.y -= (self.y - self.r * (1000 / 600) - 0.25) * 2

        #if (self.v_x == 0) and (self.v_y == 0):
        #    return True
        #else:
        #    return False

    def kollision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y

        # Abstand zum Qudrat
        norm_dist = dx * dx + dy * dy
        
        
        # Skalarprodkte
        v1d = self.v_x * dx + self.v_y * dy
        v2d = other.v_x * dx + other.v_y * dy

        # neue Geschwindigkeiten bestimmen
#        if v1d <= 0 and v2d <= 0:
        self.v_x = self.v_x - dx * (v1d - v2d) / norm_dist
        self.v_y = self.v_y - dy * (v1d - v2d) / norm_dist

        other.v_x = other.v_x - dx * (v2d - v1d) / norm_dist
        other.v_y = other.v_y - dy * (v2d - v1d) / norm_dist



