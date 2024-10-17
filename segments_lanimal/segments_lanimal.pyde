import segment
import creature 

c1=creature.Creature(width=800, height=800)
c1.creature()



def setup():
    size(800,800)
    colorMode(RGB, 100,200,100)#3
    
def draw():
    background(300)
    c1.update_s()
    c1.display()
    c1.drawfin()
