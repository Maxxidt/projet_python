from tkinter import *
import apifile as af
import jeu as jeu
class score:
    def __init__(self,email):
        root=Tk()
        
        back_pic = PhotoImage(file="pictures/background.png")
        best_pic = PhotoImage(file="pictures/bestmenu.png")
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

        canvas = Canvas(root,width=960,height=540,highlightthickness=0)
        canvas.create_image(0,0,image=back_pic)
        canvas.create_image(500,275,image=best_pic)

        jeu.jeu.print_numbers(self,canvas,str(int(af.api.best_score(email)*10)),570,250)

        canvas.grid()
        
        root.mainloop()
        import menu as menu
        menu.menu(email)


