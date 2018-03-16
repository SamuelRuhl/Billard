
import draw
import color
import bowl

class spieler():
    
    def __init__(self,num):
        self.hole_in = []
        self.num = num
        self.kugel_art = None
        
    def strike(self,kugel):
        self.hole_in.append(kugel)
        if self.hole_in[0].number == 0:
            del self.hole_in[0]
        else:
            if self.hole_in[0].number < 8 :
                self.kugel_art = 'voll'
            if self.hole_in[0].number > 8 :
                self.kugel_art = 'halb'
    
    def draw_holeins(self):
        y = 0.72
        if (self.num - 1) :
            x = 0.925
        else:
            x = 0.125
        for i,kugel in enumerate(self.hole_in):
            kugel.x = x
            kugel.y = y - 0.05 * i
            kugel.draw_kugel()
            
            
    
        