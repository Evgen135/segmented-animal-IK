import segment
class Creature:
    def __init__(self,seg=segment.Segment, lenn=15, boddy=[],speed=4, width=800, height=800):
        self.lenn=lenn
        self.boddy=boddy
        self.seg=seg
        self.width = width
        self.height = height
        self.speed=speed

    def creature(self):
        r1=30#forma
        for i in range (0,self.lenn):
            r=r1-i*(r1/(self.lenn-1))
            self.boddy.append(self.seg(self.width*0.5-i*r1,self.height*0.5,0,0.5*r,r/2,i*10))
        # return self.boddy[i]

        
    def update_s(self):
        head =self.boddy[0]
        a =atan2(mouseY-head.y,mouseX-head.x)
        
        delta=a-head.angle
        while delta<-PI:
            delta+=2*PI
        while delta>PI:
            delta-=2*PI
        head.angle+=0.06*delta #speed rotation im mause
        
        # head.angle=a
        head.x+=self.speed*cos(head.angle)
        head.y+=self.speed*sin(head.angle)
        for i in range(1,self.lenn):
            c = self.boddy[i]
            p = self.boddy[i-1]
            c.update(p)


        
    def display(self):
        # for i in range (0,self.lenn):
        #     self.boddy[i].display()
        
        head=self.boddy[0]
        #noFill()
        pushMatrix()
        translate(head.x,head.y)
        rotate(head.angle)
        fill(head.hue,100,100)
        arc(0,0,head.radius*2.5,head.radius*2,-0.6*PI,0.6*PI) #pervi "head.radius*" eto dlinna head
        fill("#FFFFFF")
        
        circle(head.radius/2,head.radius/1.4,13) #glaza
        circle(head.radius/2,-head.radius/1.4,13)   
        noFill 
        popMatrix()
        
            
        for i in range (0,self.lenn-1):
            s=self.boddy[i]
            s.display() #1
            stroke(0)#4 create line
            next = self.boddy[i+1]
            x1=s.x+s.radius*cos(s.angle-0.5*PI)
            y1=s.y+s.radius*sin(s.angle-0.5*PI)
            x2=next.x+next.radius*cos(next.angle-0.5*PI)
            y2=next.y+next.radius*sin(next.angle-0.5*PI)
            line(x1,y1,x2,y2)
            
            x1=s.x+s.radius*cos(s.angle+0.5*PI)
            y1=s.y+s.radius*sin(s.angle+0.5*PI)
            x2=next.x+next.radius*cos(next.angle+0.5*PI)
            y2=next.y+next.radius*sin(next.angle+0.5*PI)
            line(x1,y1,x2,y2)
             
    def  drawfin(self):
        for i in range(2,5):
            s=self.boddy[i]
            pushMatrix()
            translate(s.x,s.y)
            rotate(s.angle)
            line(0,0,-3*s.distanse,0)
            popMatrix()

                    
            
