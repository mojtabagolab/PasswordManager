#import package GUI
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image


#_________________________________ALL GUI CODE_____________________________

#_________________________________sign up gui code_________________________________

def SignUp():
    #---------------------------------------------------
    #variable class Tk from tkinter lib
    Window_SignUp = Tk()
    #---------------------------------------------------
    #customize window app
    Window_SignUp.title("PASSAM (sign up)")
    Window_SignUp.config(bg= "#353535")
    Window_SignUp.geometry("800x500")
    Window_SignUp.resizable(False , False)
    #enter your image.ico location with two \\
    Window_SignUp.iconbitmap("E:\\project\\PasswordManager\\ProjectFile\\iconApp.ico")
    #---------------------------------------------------
    #image icon app in window
    #enter your image.ico location with two \\
    Passam_Image_Icon = Image.open("E:\\project\\PasswordManager\\ProjectFile\\logo.jpg")
    Passam_Image_Icon = Passam_Image_Icon.resize((320 , 210))
    Tk_Passam_Image = ImageTk.PhotoImage(Passam_Image_Icon)
    Passam_Image_Lable = Label(Window_SignUp ,image=Tk_Passam_Image )
    Passam_Image_Lable.place(x=50 , y=140)
    #---------------------------------------------------
    #text welcome in header app
    Text_Welcome = Label(Window_SignUp , text="Welcome" , bg="#353535" , fg="white" , width=10)
    Text_Welcome.pack()
    #Text_Welcome.place(x=220 , y=20)
    Text_Welcome_Style = ("Caveat" , 50 , "bold")
    Text_Welcome.configure(font=Text_Welcome_Style)
    #---------------------------------------------------
    #text enter password
    Text_Enter_Password = Label(Window_SignUp , text="Enter Password for Sign up" , bg="#353535" , fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=440 , y=150)
    Text_Enter_Password_Style = ("Comic Sans Ms" , 15 , "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    #---------------------------------------------------
    #edit text enter password
    Password_Entry = Entry(Window_SignUp , width=33)
    Password_Entry.pack()
    Password_Entry.place(x=395 , y=220)
    Password_Entry_Style = ("Arial")
    Password_Entry.configure(font=Password_Entry_Style)
    #---------------------------------------------------
    #function click button sign up 
    def Click_Button_SignUp():
        #variable for get input password entry
        valueEditText = Password_Entry.get()
        #check value input
        if valueEditText == "":
            #show error message
            messagebox.showerror("Error" , "Please Fill password Field")
        else:
            #show success message
            messagebox.showinfo("Success" , "Sign up successfully")
            #write a value in CheckUser.txt when user sign up
            Write_Check_User()
    #---------------------------------------------------
    #Button sign up
    Button_SignUp = Button(Window_SignUp , text="Sign Up" , width=20 , bg="green" , fg="white" , command=Click_Button_SignUp)
    Button_SignUp.pack()
    Button_SignUp.place(x=450 , y=280)
    Button_SignUp_Style = ("Centaur" , 17 , "bold")
    Button_SignUp.configure(font=Button_SignUp_Style)

    Window_SignUp.mainloop()
#________________________________End sign up gui code_________________________________

#_________________________________LOGIN gui code_________________________________
def Login():
    #---------------------------------------------------
    #variable class Tk from tkinter lib
    Window_Login = Tk()
    #---------------------------------------------------
    #customize window app
    Window_Login.title("PASSAM (login)")
    Window_Login.config(bg= "#353535")
    Window_Login.geometry("800x500")
    Window_Login.resizable(False , False)
    Window_Login.iconbitmap("iconApp.ico")
    #---------------------------------------------------
    #text Login in header app
    Text_Login = Label(Window_Login , text="Login" , bg="#353535" , fg="white" , width=10)
    Text_Login.pack()
    #Text_Welcome.place(x=220 , y=20)
    Text_Login_Style = ("Caveat" , 50 , "bold")
    Text_Login.configure(font=Text_Login_Style)
    #---------------------------------------------------
    #frame box item login
    frame = Frame(Window_Login , bg="#555454" , height=350 , width=400)
    frame.pack()
    frame.place(x=200 , y=120)
    #---------------------------------------------------
    #text enter password
    Text_Enter_Password = Label(frame , text="Enter Password for Login" , bg="#555454" , fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=70 , y=50)
    Text_Enter_Password_Style = ("Comic Sans Ms" , 15 , "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    #---------------------------------------------------
    #edit text enter password
    Password_Entry = Entry(frame , width=25)
    Password_Entry.pack()
    Password_Entry.place(x=65 , y=110)
    Password_Entry_Style = ("Arial")
    Password_Entry.configure(font=Password_Entry_Style)
    #---------------------------------------------------
    #function click button login
    #---------------------------------------------------
    #Button login
    Button_SignUp = Button(frame , text="Login" , width=20 , bg="green" , fg="white")
    Button_SignUp.pack()
    Button_SignUp.place(x=68 , y=180)
    Button_SignUp_Style = ("Centaur" , 17 , "bold")
    Button_SignUp.configure(font=Button_SignUp_Style)
    #---------------------------------------------------

    Window_Login.mainloop()


#create txt file for check sign up user
File_Check_User = open("CheckUser.txt" , "a")
#read txt file for check sign up user
File_Check_User = open("CheckUser.txt" , "r")


def Write_Check_User():
    File_Check_User = open("CheckUser.txt" , "w")
    File_Check_User.write("1")
    File_Check_User.close()

if File_Check_User.read() == "":
    SignUp()
else:
    Login()




