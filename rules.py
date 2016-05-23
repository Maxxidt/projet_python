from tkinter import *
import menu as menu
class rules:
    def __init__(self,email):
        root = Tk()

        
        canvas = Canvas(root,width=960,height=540,highlightthickness=0)
        rules_text_pic = PhotoImage(file="pictures/rules_text.png")
        canvas.create_image(480,270,image=rules_text_pic)
        
        canvas.grid()

        root.mainloop()
        menu.menu(email)

