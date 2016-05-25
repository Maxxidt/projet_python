import sqlite3
from tkinter import *


class api :
    ##########################################################################
    #Name: best_score
    #Point: gives the user's score
    ##########################################################################
    def best_score(email):
        connection = sqlite3.connect('listplayer.db')
        cursor = connection.execute("SELECT Email,Score FROM players")
        for i in cursor:
            if i[0]==email:
                return i[1]

    

    ##########################################################################
    #Name: connexion
    #Point: obvious
    ##########################################################################
    def connexion(self,address,password,root):
        
        import menu as menu
        check=0
        connection = sqlite3.connect('listplayer.db')
        cursor = connection.execute("SELECT Email, Password FROM players")
        for i in cursor:
            
            if i[0]==address:
                check=1
                if i[1]==password:
                    print('ok')
                    root.destroy()
                    menu.menu(address)
                
                    
                else:
                    print('wrong password')
        if check==0:
            print('this adress is not registered')
            
        connection.close()


    ##########################################################################
    #Name: create_new_user
    #Point: obvious
    ##########################################################################
    def create_new_user(self,address,password,root):
        
        import menu as menu
        check=0
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address)
        
        if match == None:
            print("It's not an E-Mail address")
        elif password=="":
            print("Please Enter a valid password")
        else:
            connection = sqlite3.connect('listplayer.db')
            connection.execute("""CREATE TABLE IF NOT EXISTS players (Email TEXT,Password TEXT,Score INTEGER)""")
            cursor = connection.execute("SELECT Email, Password FROM players")
            for i in cursor:
                if i[0]==address:
                    print("This Email is already registered")
                    check=1
            if check==0:
                connection.execute('''INSERT INTO players (Email, Password, Score) VALUES ("'''+address+'''","'''+password+'''",'''+str(0)+''')''')
                connection.commit()
                connection.close()
                print("Account created")
                root.destroy()
                menu.menu(address)
                
                
    ##########################################################################
    #Name: save_score
    #Point: only if the score is better
    ##########################################################################
    def save_score(email,score):
        
        connection = sqlite3.connect('listplayer.db')
        cursor = connection.execute("SELECT Email,Score FROM players")
        for i in cursor:
            
            if i[0]==email and i[1]<score:
                connection.execute('''UPDATE players SET Score ='''+str(score)+'''  WHERE Email == "'''+email+'''"''')
                
        connection.commit()

        connection.close()

