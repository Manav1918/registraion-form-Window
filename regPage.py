from tkinter import *
from tkinter.messagebox import showinfo,showerror
import pymysql

class Registration:        
    def form():
        
        try:
            connection = pymysql.connect(host='localhost',user='root',db='test2')
        except:
            print("You are not connected to server(localhost)")
        else:
            cur = connection.cursor()
            print('Connected Successfully! feel the form')
            
#=============form design=========================
        rForm = Tk()
        rForm.title("New User Registration")
        rForm.geometry('300x500')
        rForm.config(bg='powder blue')
        formName = Label(rForm,text='New User Registration',fg='blue',
                         font=('arial',20,'bold')).pack()
#       Get user full name=========================
        L1 = Label(rForm,text='Enter Your Name*')
        L1.place(x=30,y=100)
        regUser = Entry(rForm)
        regUser.place(x=140,y=100)
#       Get user email id========================
        L2 = Label(rForm,text='Email*')
        L2.place(x=30,y=130)
        regEmail = Entry(rForm)
        regEmail.place(x=140,y=130)
#       Get user password ========================
        L3 = Label(rForm,text='Enter Password*')
        L3.place(x=30,y=160)
        regPass = Entry(rForm)
        regPass.place(x=140,y=160)
#       confirm password==========================
        L4 = Label(rForm,text='Confirm Password*')
        L4.place(x=30,y=185)
        confirm = Entry(rForm)
        confirm.place(x=140,y=185)
#       Check All details=========================
        def register():
            u,e = regUser.get(),regEmail.get()
            p,cp = regPass.get(),confirm.get()
            if len(u)==0 or len(e)==0 or len(p)==0:
                showerror('All fields required','All fields are required to fill.')
            elif len(p)<8:
                showinfo('Warning','Password must be atleast 8 character long')
            elif p!=cp:
                showerror('password mismatch','Password Mismatched.')
            else:
                #print(e,p)
                try:
                    query = "INSERT INTO users (username,email, password) VALUES (%s,%s,%s )"
                    val= (u,e,p)
                    cur.execute(query,val)
                    connection.commit()  # to make changes in db
                    
                except Exception as ek:
                    print(ek,'\nThere is an error in registering')
                else:
                    print(cur.rowcount,' record inserted')    
                    print(u,' You are Registered Successfully!')
                    showinfo('registered','you are registered Successfully \n %s'%u)
                    cur.close()
                    connection.close()
                    rForm.destroy()# now close form window

        copyri8 = Label(rForm,text='Designed and developed by: Pawan Sir @CID',bg='powder blue')
        copyri8.pack(side=BOTTOM,pady=3)    
        submit = Button(rForm,text='Register',fg='white',bg='green',width=30,command=register)
        submit.place(x=30,y=300)
        
        rForm.mainloop()
    
