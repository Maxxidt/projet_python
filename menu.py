from tkinter import *
import threading
import jeu as jeu

class menu:
    def __init__(self,email):
        ##########################################################################
        self.root = Tk()
        self.root.title("Menu")
        
        ##########################################################################
        #variables
        self.email=email
        self.which_canvas=1
        self.position_fire=245
        
        ##########################################################################
        #canvas
        self.canvas1 = Canvas(self.root,width=960,height=540,highlightthickness=0)
        self.canvas2 = Canvas(self.root,width=960,height=540,highlightthickness=0)
        
        ##########################################################################
        #loaads the pictures
        self.back_pic = PhotoImage(file="pictures/background.png")
        self.welc_pic = PhotoImage(file="pictures/welcome.png")
        self.game_pic = PhotoImage(file="pictures/game.png")
        self.rules_pic = PhotoImage(file="pictures/rules.png")
        self.credits_pic = PhotoImage(file="pictures/credits.png")
        self.fire_pic = PhotoImage(file="pictures/missile.png")
        self.score_pic = PhotoImage(file="pictures/score.png")
        self.quit_pic = PhotoImage(file="pictures/quit.png")
        
        ##########################################################################
        #creates the action
        self.canvas1.focus_set()
        self.canvas2.focus_set()
        self.canvas1.bind("<Key>",self.where_is_fire)
        self.canvas2.bind("<Key>",self.where_is_fire)

        ##########################################################################
        #loop
        self.boucle()
        self.root.mainloop()


    ##########################################################################
    #Name: boucle
    #Point: calls the fonction to make the menu work
    ##########################################################################
    def boucle(self):
        
        if self.which_canvas==1:
            canvas=self.canvas1
            self.which_canvas=2
        else:
            canvas=self.canvas2
            self.which_canvas=1
        canvas.grid_forget()
        canvas.delete("all")
        self.printer(canvas)
        
        canvas.grid(row=0)
        threading.Timer(0.1, self.boucle).start()


    ##########################################################################
    #Name: open_sub_section
    #Point: depends on the choice of the user, launches an other window, or closes the menu
    ##########################################################################
    def open_sub_section(self):
        if  self.position_fire==245:
            self.root.destroy()
            jeu.jeu(self.email)
        elif  self.position_fire==310:
            self.root.destroy()
            import rules as ru
            ru.rules(self.email)
        elif self.position_fire==375:
            self.root.destroy()
            import score as sc
            sc.score(self.email)
        elif self.position_fire==440:
            self.root.destroy()
            import credit as cd
            cd.credit(self.email)
        elif self.position_fire==505:
            self.root.destroy()


    ##########################################################################
    #Name: printer
    #Point: print the pictures
    ##########################################################################
    def printer(self,canvas):
        canvas.create_image(0,0,image=self.back_pic)
        canvas.create_image(500,130,image=self.welc_pic)
        canvas.create_image(500,245,image=self.game_pic)
        canvas.create_image(505,310,image=self.rules_pic)
        canvas.create_image(515,375,image=self.score_pic)
        canvas.create_image(500,440,image=self.credits_pic)
        canvas.create_image(500,505,image=self.quit_pic)
        canvas.create_image(350,self.position_fire,image=self.fire_pic)


    ##########################################################################
    #Name: where_is_fire
    #Point: move the cursor
    ##########################################################################
    def where_is_fire(self,event):
        if event.keycode==40 or event.char=="S" or event.char=="s":#down
            if self.position_fire!=505:
                self.position_fire=self.position_fire+65
            else:
                self.position_fire=245
        elif event.keycode==38 or event.char=="Z" or event.char=="z" or event.char=="w" or event.char=="W": #up
            if self.position_fire!=245:
                self.position_fire=self.position_fire-65
            else:
                self.position_fire=505
        elif event.keycode==13:
            self.open_sub_section()

        
