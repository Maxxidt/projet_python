from tkinter import *
from math import *
import apifile as af
import threading
import time
import random

class end_game:
    
    def __init__(self,score,email):
            af.api.save_score(email,score)

            import menu as menu
            menu.menu(email)
    
        
class jeu:
    
    def __init__(self,email):

        self.root = Tk()
        self.root.title("Jeu")
        
        ##########################################################################
        #We use two canvas to avoid blinks
        self.canvas = Canvas(self.root,width=960,height=540,highlightthickness=0)
        self.canvas2 = Canvas(self.root,width=960,height=540,highlightthickness=0)
        self.canvas.grid(column=0,row=0)
        self.canvas2.grid(column=0,row=0)
        self.numero_canvas=1

        ##########################################################################
        #here the different variables
        self.debut_time=time.time()
        self.real_time=0
        self.end_time=0
        self.comets_time=0               # time when the last comet was created
        
        self.more_meteores=1             # this number will change to allow more comets on the screen
        self.number_of_collision=0       # collision with the spaceship
        self.number_of_shoot=0           # number of time the spaceship destroyed a comet
        self.explosion_ship_number=0     # to know if the animation with fire is on for the spaceship
        self.score_final=0               # the score at the end of the game
        self.end=0                       # end of the game
        
        self.destroy_meteor_super=[]     # to know where were the comets, the superpower killed, and the step of the animation
        self.explosion_ship_statu=[]     # to know the progress of the animation (ship's explosion)
        self.tab_destroy_time=[]         # to say the step but also the position of the destruction of the comets touched by a bullet
        self.destroy_firetab=[]          # to know which bullets have to be removed
        self.destroy_comets=[]           # to know which comets have to be removed
        self.firetab=[]                  # it's where all the bullets are registered
        self.comets=[]                   # it's where all the comets are registered
        
        self.x=200                       # First position of the spaceship and the background
        self.y=400
        self.x2=900
        self.y2=0
           
        ##########################################################################
        #Here we upload the pictures
        self.photo = PhotoImage(file="pictures/rocket.png")
        self.fire_pic = PhotoImage(file="pictures/missile.png")
        
        self.comets_pic = PhotoImage(file="pictures/comets1.png") 
        self.comets_pic_2 = PhotoImage(file="pictures/comets2.png") 
        self.comets_pic_3 = PhotoImage(file="pictures/comets3.png") 
        self.comets_pic_4 = PhotoImage(file="pictures/comets4.png") 
        self.comets_pic_0 = PhotoImage(file="pictures/cometssuiv.png") 
        self.best_score_pic = PhotoImage(file="pictures/bestmenu.png")
        self.fail_pic = PhotoImage(file="pictures/fail.png")
        self.back_pic = PhotoImage(file="pictures/background.png")
        self.life_pic = PhotoImage(file="pictures/life.png")
        self.game_over_pic = PhotoImage(file="pictures/gameover.png")
        self.superpower_pic = PhotoImage(file="pictures/superpower.png")
        
        self.one_pic = PhotoImage(file="pictures/numbers/1.png")
        self.two_pic = PhotoImage(file="pictures/numbers/2.png")
        self.three_pic = PhotoImage(file="pictures/numbers/3.png")
        self.four_pic = PhotoImage(file="pictures/numbers/4.png")
        self.five_pic = PhotoImage(file="pictures/numbers/5.png")
        self.six_pic = PhotoImage(file="pictures/numbers/6.png")
        self.seven_pic = PhotoImage(file="pictures/numbers/7.png")
        self.eight_pic = PhotoImage(file="pictures/numbers/8.png")
        self.nine_pic = PhotoImage(file="pictures/numbers/9.png")
        self.zero_pic = PhotoImage(file="pictures/numbers/0.png")
        
        self.explosion_pic1 = PhotoImage(file="pictures/explosions/explosion1.png")
        self.explosion_pic2 = PhotoImage(file="pictures/explosions/explosion2.png")
        self.explosion_pic3 = PhotoImage(file="pictures/explosions/explosion3.png")
        self.explosion_pic4 = PhotoImage(file="pictures/explosions/explosion4.png")
        self.explosion_pic5 = PhotoImage(file="pictures/explosions/explosion5.png")

        ##########################################################################
        #Here we have the actions
        self.canvas.bind("<Key>",self.move_and_superpower)
        self.canvas.bind("<Button-1>",self.create_new_fire)
        self.canvas2.bind("<Key>",self.move_and_superpower)
        self.canvas2.bind("<Button-1>",self.create_new_fire)
        self.canvas.focus_set()

        ##########################################################################
        #We start the time and launch the game
        self.beginning_score=time.time()
        self.printer(email)

        ##########################################################################
        #End of the loop
        self.root.mainloop()
        end_game(self.score_final,email)


    ##########################################################################
    #Name: actualise_comets_spaceship_and_fires
    #Point: compute the new positions and print the comets spaceships and fires
    ##########################################################################
    def actualise_comets_spaceship_and_fires(self,canvas):

        for i in self.firetab:
            i[0]=i[0]+i[2]
            i[1]=i[1]+i[3]
            
        for i in self.comets:
            if i[4]==0:
                i[0]=i[0]+i[2]
                i[1]=i[1]+i[3]
                i[2]=2*(self.x-i[0])/sqrt((i[0]-self.x)**2+(i[1]-self.y)**2)
                i[3]=2*(self.y-i[1])/sqrt((i[0]-self.x)**2+(i[1]-self.y)**2)
            else:
                i[0]=i[0]+i[2]
                i[1]=i[1]+i[3]

        canvas.create_image(self.x2,self.y2,image=self.back_pic)
            
        for i in self.firetab:
            canvas.create_image(i[0],i[1],image=self.fire_pic)

        for i in self.comets:
            if i[4]==1: 
                canvas.create_image(i[0],i[1],image=self.comets_pic)
            elif i[4]==2: 
                canvas.create_image(i[0],i[1],image=self.comets_pic_2)
            elif i[4]==3: 
                canvas.create_image(i[0],i[1],image=self.comets_pic_3)
            elif i[4]==4:
                canvas.create_image(i[0],i[1],image=self.comets_pic_4)
            elif i[4]==0 :
                canvas.create_image(i[0],i[1],image=self.comets_pic_0)
        
        canvas.create_image(self.x,self.y,image=self.photo)


    ##########################################################################
    #Name: create_new_fire
    #Point: creates a new bullet depends on the place of the mouse ( when the user clicks)
    ##########################################################################
    def create_new_fire(self,event):
        
        depx=10*(event.x-self.x)/sqrt((event.x-self.x)**2+(event.y-self.y)**2)
        depy=10*(event.y-self.y)/sqrt((event.x-self.x)**2+(event.y-self.y)**2)
        self.firetab=self.firetab+[[self.x,self.y,depx,depy,0]]

        
    ##########################################################################
    #Name: create_new_comets
    #Point: creates a new comet, the red or orange ones
    ##########################################################################
    def create_new_comets(self):
        self.comets_time=time.time()
        self_comets_y=0
        self_comets_x=random.randint(200,900)
        depx=2*(self.x-self_comets_x)/sqrt((self_comets_x-self.x)**2+(self_comets_y-self.y)**2)
        depy=2*(self.y-self_comets_y)/sqrt((self_comets_x-self.x)**2+(self_comets_y-self.y)**2)       
        if len(self.comets)% 2 != 0 or len(self.comets)<3: 
            comets_number=random.randint(1,4)
            self.comets=self.comets+[[self_comets_x,self_comets_y,depx,depy,comets_number]] # don't follow the spaceship
        else :
            self.comets=self.comets+[[self_comets_x,self_comets_y,depx,depy,0]] # follow the spaceship

            
    ##########################################################################
    #Name: collision
    #Point: look out the collisions between bullets and comets
    ##########################################################################
    def collision(self): 
        for i in range(len(self.firetab)):
            for j in range(len(self.comets)):
                if ((self.comets[j][0]>self.firetab[i][0]) and self.comets[j][0]<(self.firetab[i][0]+25))or((self.comets[j][0]+59>self.firetab[i][0]) and self.comets[j][0]+59<(self.firetab[i][0]+25)):
                    if ((self.comets[j][1]>self.firetab[i][1]) and self.comets[j][1]<(self.firetab[i][1]+26))or((self.comets[j][1]+47>self.firetab[i][1]) and self.comets[j][1]+47<(self.firetab[i][1]+26)):
                        self.destroy_comets.append(j)
                        self.destroy_firetab.append(i)
                        self.tab_destroy_time=self.tab_destroy_time+[[0,0,0]]#to say the step but also the position of the destruction
                        self.number_of_shoot=self.number_of_shoot+1


    ##########################################################################
    #Name: collision_spaceship
    #Point: looks out the collisions between the spaceship and comets
    ##########################################################################
    def collision_spaceship(self):
        tab=[]
        for j in range(len(self.comets)):
            if ((self.comets[j][0]>self.x) and self.comets[j][0]<self.x+125)or((self.comets[j][0]+59>self.x) and self.comets[j][0]+59<self.x+125):
                if ((self.comets[j][1]>self.y) and self.comets[j][1]<self.y+125)or((self.comets[j][1]+47>self.y) and self.comets[j][1]+47<self.y+125):
                    tab=tab+[j]
                    self.number_of_collision=self.number_of_collision+1
                    self.explosion_ship_number=1
                    self.explosion_ship_statu=self.explosion_ship_statu+[0]
        for i in range (len(tab)):
            self.comets.pop(tab[i]) 


    ##########################################################################
    #Name: comet_out_of_window
    #Point: deletes comets wen they are outside the window
    ##########################################################################
    def comet_out_of_window(self):
        tab=[]
        for i in range(len(self.comets)):
            if self.comets[i][0]+30<0 or self.comets[i][1]-24>540 :
                tab=tab+[i]
        for i in range (len(tab)):
            self.comets.pop(tab[i])

            
    ##########################################################################
    #Name: destroy_f
    #Point: stops the game whe the user push L
    ##########################################################################
    def destroy_f(self,event):
        if event.char=="L" or event.char=="l":
            self.user_want_to_quit=1

        self.root.destroy()


    ##########################################################################
    #Name: impact_fire_comet
    #Point: creates the animation with fire to show the impact bw fires and comets
    ##########################################################################
    def impact_fire_comet(self,canvas):                            
        for k in range(len(self.tab_destroy_time)):
            if self.destroy_firetab[k]!="none":
                i=self.destroy_firetab[k]
                    
                    
                if self.tab_destroy_time[k][0]==0:
                        
                    try:
                        
                        self.tab_destroy_time[k][1]=self.firetab[i][0]
                        self.tab_destroy_time[k][2]=self.firetab[i][1]
                                
                        self.comets.pop(self.destroy_comets[k])
                        self.firetab.pop(self.destroy_firetab[k])
                    except:
                        self.destroy_firetab[k]="none"
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic1)
                        
                elif self.tab_destroy_time[k][0]<=10 and self.tab_destroy_time[k][0]!=0:
                    
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic2)
                        
                elif self.tab_destroy_time[k][0]<=15 and self.tab_destroy_time[k][0]>10:
                    
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic3)
                        
                elif self.tab_destroy_time[k][0]<=20 and self.tab_destroy_time[k][0]>15 :
                 
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic4)
          
                elif self.tab_destroy_time[k][0]<=25 and self.tab_destroy_time[k][0]>20 :
            
                    canvas.create_image(self.tab_destroy_time[k][1],self.tab_destroy_time[k][2],image=self.explosion_pic5)
                 
                elif self.tab_destroy_time[k][0]>25 :
                        
                    self.destroy_firetab[k]="none"
                        
                self.tab_destroy_time[k][0]=self.tab_destroy_time[k][0]+1


    ##########################################################################
    #Name: impact_comet_spaceship
    #Point: creates the animation with fire to show the impact bw the spaceships and comets
    ##########################################################################
    def impact_comet_spaceship(self,canvas):
        if self.explosion_ship_number == 1 :
            for i in range (len(self.explosion_ship_statu)):
                  
                        
                if self.explosion_ship_statu[i]<=10 and self.explosion_ship_statu[i]>=0:
                        
                    canvas.create_image(self.x,self.y,image=self.explosion_pic2)
                            
                elif self.explosion_ship_statu[i]<=15 and self.explosion_ship_statu[i]>10:
                        
                    canvas.create_image(self.x,self.y,image=self.explosion_pic3)
                            
                elif self.explosion_ship_statu[i]<=20 and self.explosion_ship_statu[i]>15 :
                     
                    canvas.create_image(self.x,self.y,image=self.explosion_pic4)
            
                elif self.explosion_ship_statu[i]<=25 and self.explosion_ship_statu[i]>20 :
                
                    canvas.create_image(self.x,self.y,image=self.explosion_pic5)
                     
                if  self.explosion_ship_statu[i]<26 :
                    self.explosion_ship_number=1
                    self.explosion_ship_statu[i]=self.explosion_ship_statu[i]+1
                        
                else:
                    self.explosion_ship_number=0
                    
    ##########################################################################
    #Name: impact_comet_super
    #Point: creates the animation with fire to show the impact of the superpower
    ##########################################################################
    def impact_comet_super(self,canvas):
        for i in range (len(self.destroy_meteor_super)):
                  
                        
            if self.destroy_meteor_super[i][2]<=10 and self.destroy_meteor_super[i][2]>=0:
                        
                canvas.create_image(self.destroy_meteor_super[i][0],self.destroy_meteor_super[i][1],image=self.explosion_pic2)
                            
            elif self.destroy_meteor_super[i][2]<=15 and self.destroy_meteor_super[i][2]>10:
                        
                canvas.create_image(self.destroy_meteor_super[i][0],self.destroy_meteor_super[i][1],image=self.explosion_pic3)
                            
            elif self.destroy_meteor_super[i][2]<=20 and self.destroy_meteor_super[i][2]>15 :
                     
                canvas.create_image(self.destroy_meteor_super[i][0],self.destroy_meteor_super[i][1],image=self.explosion_pic4)
            
            elif self.destroy_meteor_super[i][2]<=25 and self.destroy_meteor_super[i][2]>20 :
                
                canvas.create_image(self.destroy_meteor_super[i][0],self.destroy_meteor_super[i][1],image=self.explosion_pic5)
                     
            if  self.destroy_meteor_super[i][2]<26 :
                    
                self.destroy_meteor_super[i][2]=self.destroy_meteor_super[i][2]+1

                
    ##########################################################################
    #Name: if_fail
    #Point: if the user fails it shows the screen game over and also if it's a new best score or not
    ##########################################################################
    def if_fail(self,canvas,email):
        
        if self.number_of_collision>4:
            canvas.grid_forget()
            canvas.delete("all") 
            canvas.create_image(480,270,image=self.game_over_pic)
            canvas.bind("<Key>",self.destroy_f)
            if self.score_final<af.api.best_score(email):
                canvas.create_image(480,270,image=self.fail_pic)
            else:
                canvas.create_image(500,275,image=self.best_score_pic)
                self.print_numbers(canvas,str(int(self.score_final*10)),570,250)
            
            canvas.grid(row=0)
            self.end=1

            
    ##########################################################################
    #Name: mod
    #Point: shows the life of the user
    ##########################################################################
    def mod(self,canvas):
        canvas.create_rectangle(18,16,321,24,fill="black") 
        canvas.create_line(20,20,320,20,fill="green",width=5) 
        canvas.create_line(320-60*self.number_of_collision,20,320,20,fill="red",width=5)
        if self.number_of_collision>=1:                
            canvas.create_line(320-60*self.number_of_collision,16,320-60*self.number_of_collision,24,fill="black",width=3) 
        canvas.create_image(50,32,image=self.life_pic)

    ##########################################################################
    #Name: move_and_superpower
    #Point: creates a action regarding the key pushed by the user
    ##########################################################################
    def move_and_superpower(self,event):
    #NB : Some event.char have two options because we use a french keyboard not a swedish one, so our keys are not exactly at the same place
        tab=[]
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

        elif event.char=="L" or event.char=="l":
            self.root.destroy()
        elif (event.char=="G" or event.char=="g")and self.number_of_shoot>10:
            self.number_of_shoot=0
            
            for i in self.comets:
                self.destroy_meteor_super=self.destroy_meteor_super+[[i[0],i[1],0]] #1 = pas de choc entre meteore et feu (superpouvoir)
            self.comets=[]


    ##########################################################################
    #Name: printer
    #Point: calls the fonctions to make the game
    ##########################################################################
    def printer(self,email):
        
        #Canvas transition to avoid blink
        if self.numero_canvas==1:
            canvas=self.canvas
            self.numero_canvas=2
        else:
            canvas=self.canvas2
            self.numero_canvas=1
        #Before changing, the "life" we check if we haven't fail
        self.if_fail(canvas,email)
        if self.end!=1:
            

            #Time calculation to slow the game, to avoid an information saturation
            self.time_calc()

            #Clean the window
            canvas.grid_forget()
            canvas.delete("all")
            
            #Creation of the new window : background, comets and spaceship
            self.actualise_comets_spaceship_and_fires(canvas)
            
            self.mod(canvas)
            
            self.collision()
            self.collision_spaceship()
            
            self.impact_fire_comet(canvas)
            self.impact_comet_spaceship(canvas)

            self.comet_out_of_window()
            
            if (self.end_time-self.comets_time)>=2/(self.more_meteores/500):
                self.comets_time=self.end_time
                self.create_new_comets()

            self.score_final=int((time.time()-self.beginning_score)*10)/10
            
            
            self.print_numbers(canvas,str(int((time.time()-self.beginning_score)*10)),975,25)
            
            self.superpowerprint(canvas)
            self.impact_comet_super(canvas)
            self.more_meteores=self.more_meteores+1
            
            canvas.grid(row=0)
            
        threading.Timer(0.00001, lambda:self.printer(email)).start()


    ##########################################################################
    #Name: print_numbers
    #Point: prints the score
    ##########################################################################
    def print_numbers(self,canvas,score,x,y):
        L=len(score)
        for w in range(0,len(score)): 
            if (score[w]=="0"):
                canvas.create_image(x-35*L,y,image=self.zero_pic)
            elif (score[w]=="1"):
                canvas.create_image(x-35*L,y,image=self.one_pic)
            elif (score[w]=="2"):
                canvas.create_image(x-35*L,y,image=self.two_pic)
            elif (score[w]=="3"):
                canvas.create_image(x-35*L,y,image=self.three_pic)
            elif (score[w]=="4"):
                canvas.create_image(x-35*L,y,image=self.four_pic)
            elif (score[w]=="5"):
                canvas.create_image(x-35*L,y,image=self.five_pic)
            elif (score[w]=="6"):
                canvas.create_image(x-35*L,y,image=self.six_pic)
            elif (score[w]=="7"):
                canvas.create_image(x-35*L,y,image=self.seven_pic)
            elif (score[w]=="8"):
                canvas.create_image(x-35*L,y,image=self.eight_pic)
            elif (score[w]=="9"):
                canvas.create_image(x-35*L,y,image=self.nine_pic)
            L=L-1
    ##########################################################################
    #Name: superpowerprint
    #Point: prints the logo superpowers when the user deserves it
    ##########################################################################
    def superpowerprint(self,canvas):
        if self.number_of_shoot>10:
            canvas.create_image(850,100,image=self.superpower_pic)

    ##########################################################################
    #Name: time_calc
    #Point: computes the time
    ##########################################################################
    def time_calc(self):
        self.end_time=time.time()
        self.real_time=self.end_time-self.debut_time
        self.real_time=round(self.real_time,2)
        self.debut_time=self.end_time
  
