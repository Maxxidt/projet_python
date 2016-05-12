from tkinter import *
import apifile as af


class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connexion")
        self.sign_in()
        self.sign_up()
        self.root.mainloop()

    def sign_in(self):
        title= Label(self.root, text="Sign In")
        title.grid(row=0,column=2)
        mail_title= Label(self.root, text="E-Mail:")
        mail_title.grid(row=1,column=1)

        mail = Entry(self.root, textvariable=StringVar())
        mail.grid(row=1,column=2)


        psw_title= Label(self.root, text="Password:")
        psw_title.grid(row=2,column=1)

        psw = Entry(self.root, textvariable=StringVar())
        psw.grid(row=2,column=2)


        button = Button(self.root, text="Submit", command=lambda:af.api.connexion(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=3,column=2)
    def sign_up(self):
        title=Label(self.root, text="Sign Up")
        title.grid(row=0,column=4)

        mail_title= Label(self.root, text="E-Mail:")
        mail_title.grid(row=1,column=3)

        mail = Entry(self.root, textvariable=StringVar())
        mail.grid(row=1,column=4)


        psw_title= Label(self.root, text="Password:")
        psw_title.grid(row=2,column=3)

        psw = Entry(self.root, textvariable=StringVar())
        psw.grid(row=2,column=4)


        button = Button(self.root, text="Submit", command=lambda:af.api.create_new_user(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=3,column=4)



main()
