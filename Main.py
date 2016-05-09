from tkinter import *
import apifile as af


class main:
    def __init__(self):
        root = Tk()
        root.title("Connexion")
        self.sign_in(root)
        self.sign_up(root)
        root.mainloop()

    def sign_in(self,root):
        title= Label(root, text="Sign In")
        title.grid(row=0,column=2)
        mail_title= Label(root, text="E-Mail:")
        mail_title.grid(row=1,column=1)

        mail = Entry(root, textvariable=StringVar())
        mail.grid(row=1,column=2)


        psw_title= Label(root, text="Password:")
        psw_title.grid(row=2,column=1)

        psw = Entry(root, textvariable=StringVar())
        psw.grid(row=2,column=2)


        button = Button(root, text="Submit", command=lambda:af.api.connexion(af.api,mail.get(),psw.get()))
        button.grid(row=3,column=2)
    def sign_up(self,root):
        title=Label(root, text="Sign Up")
        title.grid(row=0,column=4)

        mail_title= Label(root, text="E-Mail:")
        mail_title.grid(row=1,column=3)

        mail = Entry(root, textvariable=StringVar())
        mail.grid(row=1,column=4)


        psw_title= Label(root, text="Password:")
        psw_title.grid(row=2,column=3)

        psw = Entry(root, textvariable=StringVar())
        psw.grid(row=2,column=4)


        button = Button(root, text="Submit", command=lambda:af.api.create_new_user(af.api,mail.get(),psw.get()))
        button.grid(row=3,column=4)

main()

