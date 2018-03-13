import pygame

import color

import draw

def reibung(v):
#    if v >= 0 and (v * 0.99995 <= 0):
#        v = 0
#    if v <= 0 and (v * 0.99995 >= 0):
#        v = 0
    if v > 0:
        v *= 0.995
    if v < 0:
        v *= 0.995
    return v

class kugel:
    def __init__(self, x, y, v_x, v_y, r,farbe,num):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r
        self.farbe = farbe
        self.num = num
        
    
    def get_x(self):

        return self.x

    def get_y(self):

        return self.y

    def get_v_x(self):

        return self.v_x

    def get_v_y(self):

        return self.v_y

    def get_r(self):

        return self.r

    def set_x(self, x):

        self.x = x

    def set_y(self, y):

        self.y = y

    def set_v_x(self, v_x):

        self.v_x = v_x

    def set_v_y(self, v_y):

        self.v_y = v_y

    def draw_kugel(self):
        draw.set_pen_color(self.farbe)
        draw.filled_circle(self.x, self.y, self.r)
        if self.num > 7 :
            draw.set_pen_color(color.WHITE)
            draw.filled_circle(self.x,self.y,self.r * 0.8)
        if self.num == 0 :
            draw.set_pen_color(color.WHITE)
            draw.text(self.x,self.y,str(self.num))
        else:
            draw.set_pen_color(color.BLACK)
            draw.text(self.x,self.y,str(self.num))
    
    def move(self):
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y

        self.v_x = reibung(self.v_x)
        self.v_y = reibung(self.v_y)

        if (self.x + self.r) >= 0.8 or (self.x - self.r) <= 0.2:
            self.v_x = -self.v_x

        if ((self.y + (self.r * (1000/600))) >= 0.75) or ((self.y - (self.r * (1000/600))) <= 0.25):
            self.v_y = -self.v_y
            
    def move_to(self,x,y):
        self.v_x = (x - self.x) * 0.05
        self.v_y = (y - self.y) *0.05
        
    def kollision(self,other):
        dx = other.x - self.x
        dy = other.y - self.y
        
        #Abstand zum Qudrat
        norm_dist = dx * dx + dy * dy
        
        #Skalarprodkte
        v1d = self.v_x * dx + self.v_y * dy
        v2d = other.v_x * dx + other.v_y * dy
        
        #neue Geschwindigkeiten bestimmen
        self.v_x = self.v_x - dx * (v1d - v2d)/norm_dist
        self.v_y = self.v_y - dy * (v1d - v2d)/norm_dist
        
        other.v_x = other.v_x - dx * (v2d - v1d)/norm_dist
        other.v_y = other.v_y - dy * (v2d - v1d)/norm_dist
    