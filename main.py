#import package GUI
from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox
from cryptography.fernet import Fernet



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
    Window_SignUp.iconbitmap("E:\\project\\PasswordManager\\iconApp.ico")
    #---------------------------------------------------
    #image icon app in window
    #enter your image.ico location with two \\
    Passam_Image_Icon = Image.open("E:\\project\\PasswordManager\\logo.jpg")
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
    def signUp_password_input():
        #a variable for get user password input
        valueEditText = Password_Entry.get()
        #check empty input password editText
        if valueEditText == "":
            messagebox.showerror("Error" , "please enter password!")
        else:
            messagebox.showinfo("Success" , "Sign up successfully")
            #_________________________________________________________
            #calling function Check user Statment for write value in file Check_New_User
            Write_value_checkUser()
            #_________________________________________________________
            #encrypt user password with global variable (fernet)
            App_Password_Encrypt = fernet.encrypt(valueEditText.encode()).decode()
            #create txt file for save user enctype password 
            File_App_Password = open('App_Password' , 'a')
            File_App_Password.write(App_Password_Encrypt)
            File_App_Password.close()
            #_________________________________________________________
            #close Window sign up and open window login
            Window_SignUp.destroy()
            Login()

    #---------------------------------------------------
    #Button sign up
    Button_SignUp = Button(Window_SignUp , text="Sign Up" , width=20 , bg="green" , fg="white" , command= signUp_password_input)
    Button_SignUp.pack()
    Button_SignUp.place(x=450 , y=280)
    Button_SignUp_Style = ("Centaur" , 17 , "bold")
    Button_SignUp.configure(font=Button_SignUp_Style)
    #---------------------------------------------------
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
    #---------------------------------------------------
    

#________________________________End login gui code_________________________________

#_________________________________________________________
#creat text file for check user statment
File_Check_User = open('Check_New_User.txt' , 'a')
#read text file for check user statment
File_Check_User = open('Check_New_User.txt' , 'r')

#open file Check_New_User.txt and write a value in file
def Write_value_checkUser():
    File_Check_User = open('Check_New_User.txt' , 'w')
    File_Check_User.write("1")
    File_Check_User.close()
#_________________________________________________________
#function create key and save key on file key.key
def Write_Key_File():
    #check user statment for create key one more for ever 
    if File_Check_User.read() == "":
        Key = Fernet.generate_key() #create key with Fernet class
        Key_File = open("key.key" , "wb") #create file key.key and write a key in file
        Key_File.write(Key)
#_________________________________________________________
#function read key.key file value 
def Load_key_File():
    #create a global variable for encrypt user password  
    global fernet
    #read key.key file and read key in file
    Key_File = open("key.key" , "rb")
    key = Key_File.read()
    Key_File.close()
    #push the key in the global variable 
    fernet = Fernet(key) 
#_________________________________________________________




#checking user is old or new
if File_Check_User.read() == "":
    #---------------------------------------------------
    #calling functions creat key and read key for encrypt user password
    Write_Key_File()
    Load_key_File()
    #---------------------------------------------------
    #start signUp page
    SignUp()
else:
    #start login page
    Login()







