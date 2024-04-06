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
    def get_login_enter_password():
        #create a variable for get password from input password box
        valueEditText = Password_Entry.get()
        if valueEditText == "":
            messagebox.showerror("Error" , "please enter password!") #alert dialog error
        else:
            #calling function for read App_Password file and load decrypt password 
            Check_App_Password()
            #check user passwrod for login 
            if valueEditText == App_Password_Decrypt :
                messagebox.showinfo("Success" , "Password is correct") ##alert dialog successfully login
                #close Window Login and open window Menu
                Window_Login.destroy()
                Menu()
            else:
                messagebox.showerror("Error" , "Password is wrong ") #alert dialog error login

    #---------------------------------------------------
    #Button login
    Button_Login = Button(frame , text="Login" , width=20 , bg="green" , fg="white" , command=get_login_enter_password)
    Button_Login.pack()
    Button_Login.place(x=68 , y=180)
    Button_Login_Style = ("Centaur" , 17 , "bold")
    Button_Login.configure(font=Button_Login_Style)
    #---------------------------------------------------
    Window_Login.mainloop()
    #---------------------------------------------------
    

#________________________________End login gui code_________________________________
#________________________________Menu gui code_________________________________
def Menu():
    #---------------------------------------------------
    #variable class Tk from tkinter lib
    Window_Menu = Tk()
    #---------------------------------------------------
    #customize window app
    Window_Menu.title("PASSAM (menu)")
    Window_Menu.config(bg= "#353535")
    Window_Menu.geometry("800x500")
    Window_Menu.resizable(False , False)
    #enter your image.ico location with two \\
    Window_Menu.iconbitmap("E:\\project\\PasswordManager\\iconApp.ico")
    #---------------------------------------------------
    #text Menu in header app
    Text_Menu = Label(Window_Menu , text="Passam" , bg="#353535" , fg="white" , width=10)
    Text_Menu.pack()
    #Text_Welcome.place(x=250 , y=20)
    Text_Menu_Style = ("Caveat" , 50 , "bold")
    Text_Menu.configure(font=Text_Menu_Style)
    
    #---------------------------------------------------
    #the frame box item button add 
    Frame_Add = Frame(Window_Menu , bg="#555454" , width=150 , height=150)
    Frame_Add.pack()
    Frame_Add.place(x=150 , y=120)
    #image button add
    Add_Image = Image.open("add.png")
    Add_Image = Add_Image.resize((100 , 100))
    Add_Image = ImageTk.PhotoImage(Add_Image)
    #define a function to be called when the button is clicked
    def button_add_clicked():
        pass
    #create the button with the image
    Button_add = Button(Frame_Add ,image= Add_Image , command=button_add_clicked)
    Button_add.pack()
    Button_add.image_names = Add_Image
    Button_add.place(x=23 , y=23)
    
    #---------------------------------------------------
    #the frame box item button delete 
    Frame_Del = Frame(Window_Menu , bg="#555454" , width=150 , height=150)
    Frame_Del.pack()
    Frame_Del.place(x=500 , y=120)
    #image button delete
    Del_Image = Image.open("delete.png")
    Del_Image = Del_Image.resize((100 , 100))
    Del_Image = ImageTk.PhotoImage(Del_Image)
    #define a function to be called when the button is clicked
    def button_del_clicked():
        pass
    #create the button with the image
    Button_Del = Button(Frame_Del ,image= Del_Image , command=button_del_clicked)
    Button_Del.pack()
    Button_Del.image_names = Del_Image
    Button_Del.place(x=23 , y=23)
    
    #---------------------------------------------------
     #the frame box item button view 
    Frame_View = Frame(Window_Menu , bg="#555454" , width=150 , height=150)
    Frame_View.pack()
    Frame_View.place(x=325 , y=300)
    #image button View
    View_Image = Image.open("list.png")
    View_Image = View_Image.resize((100,100))
    View_Image = ImageTk.PhotoImage(View_Image)
    #define a function to be called when the button is clicked
    def button_view_clicked():
        pass
    #create the button with the image
    Button_View = Button(Frame_View ,image= View_Image , command=button_view_clicked)
    Button_View.pack()
    Button_View.image_names = View_Image
    Button_View.place(x=23 , y=23)
    #---------------------------------------------------
    
    #---------------------------------------------------
    #start window 
    Window_Menu.mainloop
    #---------------------------------------------------
#________________________________End Menu gui code_________________________________
#_________________________________End GUI CODE_____________________________

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
def Check_App_Password():
    global App_Password_Decrypt
    #read App_Password file for decrypt
    File_App_Password = open('App_Password' , 'r')
    File_App_Password = File_App_Password.read()
    #decrypt user password 
    Load_key_File()
    App_Password_Decrypt = fernet.decrypt(File_App_Password.encode()).decode()
    
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







