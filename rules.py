from tkinter import *
import menu as menu
class rules:
    def __init__(self,email):
        root = Tk()

        
        canvas = Canvas(root,width=960,height=540,highlightthickness=0)
        back_pic = PhotoImage(file="pictures/background.png")
        rules_pic = PhotoImage(file="pictures/rules.png")
        rules_text_pic = PhotoImage(file="pictures/rules_text.png")
        canvas.create_image(0,0,image=back_pic)
        canvas.create_image(475,30,image=rules_pic)
        canvas.create_image(475,300,image=rules_text_pic)
        
        canvas.grid()

        root.mainloop()
        menu.menu(email)
        

