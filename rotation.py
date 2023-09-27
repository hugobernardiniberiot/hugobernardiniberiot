import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

window= tk.Tk()

def verta(c1,c2,p1,p2,ang):
    vo1= c1-p1
    vo2= c2-p2
    if p1<c1 and p2<c2 or p1>c1 and p2>c2:
        anga = math.degrees(math.atan(vo2/vo1))
    elif p1<c1 and p2>c2:
        anga = math.degrees(math.atan(vo2/vo1))
        
    print(anga)
    if anga<1:
        anga*=-1
    return(ang- anga)
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def rot (self, c1,c2,ang):
        if self.x< c1 and self.y< c2 or self.x > c1 and self.y < c2 or self.x < c1 and self.y> c2 or self.x>c1 and self.y >c2:
            vertal = verta(c1,c2,self.x,self.y,ang)
            print("vertal",vertal)
        
            
        

        vo1= c1-self.x
        print("vo1",vo1)
        
        vo2= c2-self.y
        print("vo2",vo2)
        xy = vo1**2 +vo2**2
        hyp=math.sqrt(xy)
        print(hyp)
        vertal= math.radians(vertal)
        if self.x< c1 and self.y< c2 or self.x>c1 and self.y>c2:
            xfact=(math.cos(vertal))*(hyp)
            print("xfact",xfact)
            yfact=(math.sin(vertal))*(hyp)
            print(yfact)
        elif self.x < c1 and self.y> c2:
            xfact=(math.sin(vertal))*(hyp)
            print("xfact",xfact)
            yfact=(math.cos(vertal))*(hyp)
            print(yfact)

        
        if self.x > c1 and self.y < c2:
            self.nx= c1+xfact
            self.ny= c2-yfact
        elif self.x< c1 and self.y< c2:    
            self.nx= c1-xfact
            self.ny= c2+yfact
        elif self.x < c1 and self.y> c2:
            self.nx= c1+xfact
            self.ny= c2+yfact
        elif self.x>c1 and self.y > c2:
            self.nx =c1+xfact
            self.ny= c2+yfact


xi1= float(input("x"))
xi2=float(input("y"))
d2xi1= float(input("x"))
d2xi2=float(input("y"))
cn1=float(input("cn1"))
cn2=float(input("cn2"))
an=float(input("angulo"))

p1=point(xi1,xi2)
p1.rot(cn1,cn2,an)

p2=point(d2xi1,d2xi2)
p2.rot(cn1,cn2,an)

print( p1.nx)
print (p1.ny)
xpoints= np.array([xi1,cn1,p1.nx,d2xi1,p2.nx])
ypoints= np.array([xi2,cn2,p1.ny,d2xi2,p2.ny])
plt.plot(xpoints,ypoints,'o')
plt.show()
        
        
