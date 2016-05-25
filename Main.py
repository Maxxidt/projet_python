from tkinter import *
import apifile as af


class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connexion")
        self.canvas = Canvas(self.root,width=1000,height=150,highlightthickness=0)
        self.canvas2 = Canvas(self.root,width=1000,height=300,highlightthickness=0)
        back_pic = PhotoImage(file="pictures/background.png")
        join_pic = PhotoImage(file="pictures/join.png")
        self.canvas2.create_image(500,275,image=back_pic)
        self.canvas2.create_image(500,150,image=join_pic)
        self.sign_in()
        self.sign_up()
        
        self.canvas2.grid(row=0)
        self.canvas.grid(row=1)
        self.root.mainloop()

    def sign_in(self):
        title= Label(self.canvas, text="Sign In")
        title.grid(row=0,column=2)
        mail_title= Label(self.canvas, text="E-Mail:")
        mail_title.grid(row=1,column=1)

        mail = Entry(self.canvas, textvariable=StringVar())
        mail.grid(row=1,column=2)


        psw_title= Label(self.canvas, text="Password:")
        psw_title.grid(row=2,column=1)

        psw = Entry(self.canvas, textvariable=StringVar())
        psw.grid(row=2,column=2)


        button = Button(self.canvas, text="Submit", command=lambda:af.api.connexion(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=3,column=2)
    def sign_up(self):
        title=Label(self.canvas, text="Sign Up")
        title.grid(row=0,column=4)

        mail_title= Label(self.canvas, text="E-Mail:")
        mail_title.grid(row=1,column=3)

        mail = Entry(self.canvas, textvariable=StringVar())
        mail.grid(row=1,column=4)


        psw_title= Label(self.canvas, text="Password:")
        psw_title.grid(row=2,column=3)

        psw = Entry(self.canvas, textvariable=StringVar())
        psw.grid(row=2,column=4)


        button = Button(self.canvas, text="Submit", command=lambda:af.api.create_new_user(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=3,column=4)



main()
