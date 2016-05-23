from tkinter import *
import menu as menu
class credit:
    def __init__(self,email):
        root = Tk()

        
        canvas = Canvas(root,width=960,height=540,highlightthickness=0)
        credit_text_pic = PhotoImage(file="pictures/credit_text.png")
        canvas.create_image(480,270,image=credit_text_pic)
        
        canvas.grid()

        root.mainloop()
        menu.menu(email)

