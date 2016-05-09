from tkinter import *
from math import *
import threading
import time
import random

class jeu:
    def __init__(self):
        self.numero_canvas=1
        self.debut_time=time.time()
        self.real_time=0
        self.end_time=0

        self.more_meteores=1

        self.tab_destroy_time=[]
        self.destroy_firetab=[]
        self.destroy_comets=[]
        
        self.root = Tk()
        self.root.title("Jeu")
        self.firetab=[]
        self.comets=[]
        self.score=0
         

        self.canvas = Canvas(self.root,width=960,height=540,highlightthickness=0)
        self.canvas2 = Canvas(self.root,width=960,height=540,highlightthickness=0)
        self.canvas.grid(column=0,row=0)
        self.canvas2.grid(column=0,row=0)
        
        self.photo = PhotoImage(file="pictures/rocket.png")
        self.fire_pic = PhotoImage(file="pictures/missile.png")
        self.comets_pic = PhotoImage(file="pictures/comets.png")
        self.back_pic = PhotoImage(file="pictures/background.png")
        
        self.explosion_pic1 = PhotoImage(file="pictures/explosions/explosion1.png")
        self.explosion_pic2 = PhotoImage(file="pictures/explosions/explosion2.png")
        self.explosion_pic3 = PhotoImage(file="pictures/explosions/explosion3.png")
        self.explosion_pic4 = PhotoImage(file="pictures/explosions/explosion4.png")
        self.explosion_pic5 = PhotoImage(file="pictures/explosions/explosion5.png")
        
        self.x=200
        self.y=400
        self.x2=900
        self.y2=0

       
        
        self.canvas.create_image(self.x,self.y,image=self.photo)
        
        self.canvas.focus_set()
        
        self.canvas.bind("<Key>",self.move)
        self.canvas.bind("<Button-1>",self.create_new_fire)
        self.canvas2.bind("<Key>",self.move)
        self.canvas2.bind("<Button-1>",self.create_new_fire)
        
        self.create_new_comets()
        self.printer()
        self.root.mainloop()
        
    def move(self,event):
        
        if ((event.char=="z") or (event.char=="Z")or (event.char=="w")or (event.char=="W"))and (self.y>32):            
            self.y=self.y-8
            self.y2=self.y2+3
        
        elif ((event.char=="s") or (event.char=="S"))and (self.y<512):            
            self.y=self.y+8
            self.y2=self.y2-3
            
        elif ((event.char=="q") or (event.char=="Q")or (event.char=="a")or (event.char=="A"))and(self.x>64):            
            self.x=self.x-8
            self.x2=self.x2+3
            
        elif ((event.char=="d") or (event.char=="D"))and(self.x<904):            
            self.x=self.x+8
            self.x2=self.x2-3
        
        
    def create_new_fire(self,event):
        
        depx=10*(event.x-self.x)/sqrt((event.x-self.x)**2+(event.y-self.y)**2)
        depy=10*(event.y-self.y)/sqrt((event.x-self.x)**2+(event.y-self.y)**2)
        self.firetab=self.firetab+[[self.x,self.y,depx,depy]]
        
    def create_new_comets(self):
        self.comets_time=time.time()
        self_comets_y=0
        self_comets_x=random.randint(200,900)
        depx=2*(self.x)/sqrt((self_comets_x)**2+(self_comets_y)**2)
        depy=2*(self.y)/sqrt((self_comets_x)**2+(self_comets_y)**2)        
        self.comets=self.comets+[[self_comets_x,self_comets_y,-depx,depy]]
       
    def collision(self): 
        
        for i in range(len(self.firetab)):
            for j in range(len(self.comets)):
                if (self.comets[j][0]>self.firetab[i][0]) and self.comets[j][0]<(self.firetab[i][0]+65):
                    if (self.comets[j][1]>self.firetab[i][1]) and self.comets[j][1]<(self.firetab[i][1]+65):
                        self.destroy_comets.append(j)
                        self.destroy_firetab.append(i)
                        self.tab_destroy_time=self.tab_destroy_time+[[0,0,0]]
                        

    def printer(self):
        if self.numero_canvas==1:
            canvas=self.canvas
            self.numero_canvas=2
           
        else:
            canvas=self.canvas2
            self.numero_canvas=1
        
        self.end_time=time.time()
        self.real_time=self.end_time-self.debut_time
        self.real_time=round(self.real_time,2)
        
        canvas.grid_forget()
        canvas.delete("all")
        self.debut_time=self.end_time
            
        for i in self.firetab:
            i[0]=i[0]+i[2]
            i[1]=i[1]+i[3]        

        canvas.create_image(self.x2,self.y2,image=self.back_pic)
        
        for i in self.firetab:
            canvas.create_image(i[0],i[1],image=self.fire_pic)
                
        for i in self.comets:
            i[0]=i[0]+i[2]
            i[1]=i[1]+i[3]
                
        for i in self.comets:
            canvas.create_image(i[0],i[1],image=self.comets_pic)
        canvas.create_image(self.x,self.y,image=self.photo)
        self.collision()
        canvas.grid(row=0,column=0)
        
        for k in range(len(self.destroy_firetab)):
            if self.destroy_firetab[k]!="none":
                i=self.destroy_firetab[k]
                
                
                if self.tab_destroy_time[k][0]==0:
                    
                    
                    self.tab_destroy_time[k][1]=self.firetab[i][0]
                    self.tab_destroy_time[k][2]=self.firetab[i][1]

                    self.comets.pop(self.destroy_comets[k])
                    self.firetab.pop(self.destroy_firetab[k])
                    
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic1)
                    
                elif self.tab_destroy_time[k][0]<=10 and self.tab_destroy_time[k][0]!=0:
                
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic2)
                    
                elif self.tab_destroy_time[k][0]<=15 and self.tab_destroy_time[k][0]>10:
                
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic3)
                    
                elif self.tab_destroy_time[k][0]<=20 and self.tab_destroy_time[k][0]>15 :
             
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic4)
      
                elif self.tab_destroy_time[k][0]<=25 and self.tab_destroy_time[k][0]>20 :
        
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic5)
             
                elif self.tab_destroy_time[k][0]<=35 and self.tab_destroy_time[k][0]>25 :
                    
                    self.destroy_firetab[k]="none"
                    
                self.tab_destroy_time[k][0]=self.tab_destroy_time[k][0]+1

            
        if (self.end_time-self.comets_time)>=2/(self.more_meteores/500):
            self.comets_time=self.end_time
            self.create_new_comets()

        self.more_meteores=self.more_meteores+1
        threading.Timer(0.00005, self.printer).start()

jeu()
