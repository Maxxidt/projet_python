from tkinter import *
import apifile as af


class main:
    def __init__(self):
        ##########################################################################
        self.root = Tk()
        self.root.title("Connexion")
        
        ##########################################################################
        #canvas
        self.canvas = Canvas(self.root,width=1000,height=200,highlightthickness=0)
        self.canvas2 = Canvas(self.root,width=1000,height=300,highlightthickness=0)

        ##########################################################################
        #loads the pictures
        back_pic = PhotoImage(file="pictures/background.png")
        join_pic = PhotoImage(file="pictures/join.png")

        ##########################################################################
        #fix the pictures on the canvas
        self.canvas2.create_image(500,275,image=back_pic)
        self.canvas2.create_image(500,150,image=join_pic)

        ##########################################################################
        self.sign_in()
        self.sign_up()

        ##########################################################################
        #print the canvas
        self.canvas2.grid(row=0)
        self.canvas.grid(row=1)

        ##########################################################################
        self.root.mainloop()

        
    ##########################################################################
    #Name: sign_in
    #Point: fixes everything to allow the user to log in
    ##########################################################################
    def sign_in(self):
        
        title= Label(self.canvas, text="Sign In ->")
        title.grid(row=0,column=1)
        mail_title= Label(self.canvas, text="E-Mail:")
        mail_title.grid(row=0,column=2)

        mail = Entry(self.canvas, textvariable=StringVar())
        mail.grid(row=0,column=3)


        psw_title= Label(self.canvas, text="Password:")
        psw_title.grid(row=0,column=4)

        psw = Entry(self.canvas, textvariable=StringVar())
        psw.grid(row=0,column=5)


        button = Button(self.canvas, text="Submit", command=lambda:af.api.connexion(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=0,column=6)


    ##########################################################################
    #Name: sign_up
    #Point: fixes everything to allow the user to register
    ##########################################################################
    def sign_up(self):
        
        title=Label(self.canvas, text="                 Sign Up ->")
        title.grid(row=0,column=7)

        mail_title= Label(self.canvas, text="E-Mail:")
        mail_title.grid(row=0,column=8)

        mail = Entry(self.canvas, textvariable=StringVar())
        mail.grid(row=0,column=9)


        psw_title= Label(self.canvas, text="Password:")
        psw_title.grid(row=0,column=10)

        psw = Entry(self.canvas, textvariable=StringVar())
        psw.grid(row=0,column=11)


        button = Button(self.canvas, text="Submit", command=lambda:af.api.create_new_user(af.api,mail.get(),psw.get(),self.root))
        button.grid(row=0,column=12)



main()
