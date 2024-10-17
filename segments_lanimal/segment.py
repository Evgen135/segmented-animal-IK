class Segment:
    def __init__(self,x=float,y=float,angle=float,distanse=float,radius=float,hue=float):
        self.x=x
        self.y=y
        self.angle=angle
        self.distanse=distanse
        self.radius=radius
        self.hue=hue
        
    def update(self, prev):
        a=atan2(prev.y-self.y,prev.x-self.x)
        self.angle=a
        d=sqrt(pow(prev.x-self.x,2)+pow(prev.y-self.y,2))
        if d>self.distanse:
            delta=d-self.distanse
            self.x+=delta*cos(self.angle)
            self.y+=delta*sin(self.angle)
        
    def display(self):
        fill(self.hue,100,100) #2
        noStroke() #?
        pushMatrix()
        translate(self.x,self.y)
        rotate(self.angle)
        circle(0,0,2*self.radius)
        line(0,0,self.distanse,0)
        popMatrix()
    
