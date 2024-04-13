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
        #close menu page and open add password page
        Window_Menu.destroy()
        Add()
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
        Window_Menu.destroy()
        Passwords()
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
#________________________________Add Password page gui code_________________________________
def Add():
    #---------------------------------------------------
    #variable class Tk from tkinter lib
    Window_Add = Tk()
    #---------------------------------------------------
    #customize window app
    Window_Add.title("PASSAM (add password)")
    Window_Add.config(bg= "#353535")
    Window_Add.geometry("800x500")
    Window_Add.resizable(False , False)
    Window_Add.iconbitmap("iconApp.ico")
    #---------------------------------------------------
    #text Add password in header app
    Text_Add_Password = Label(Window_Add , text="Add Password" , bg="#353535" , fg="white" , width=12)
    Text_Add_Password.pack()
    #Text_Welcome.place(x=220 , y=20)
    Text_Add_Password_Style = ("Caveat" , 50 , "bold")
    Text_Add_Password.configure(font=Text_Add_Password_Style)
    #---------------------------------------------------
    #image icon app in window
    #enter your image.ico location with two \\
    Passam_Image_Icon = Image.open("E:\\project\\PasswordManager\\logo4.jpg")
    Passam_Image_Icon = Passam_Image_Icon.resize((300 , 210))
    Tk_Passam_Image = ImageTk.PhotoImage(Passam_Image_Icon)
    Passam_Image_Lable = Label(Window_Add ,image=Tk_Passam_Image )
    Passam_Image_Lable.place(x=30 , y=160)
    #---------------------------------------------------
    #button back 
    Back_Image = Image.open("back.png")
    Back_Image = Back_Image.resize((25 , 25))
    Back_Image = ImageTk.PhotoImage(Back_Image)
    #define a function to be called when the button is clicked
    def button_back_clicked():
        #close window add password and open menu page
        Window_Add.destroy()
        Menu()
    #create the button back with the image
    Button_Back = Button(Window_Add , image=Back_Image , command=button_back_clicked)
    Button_Back.pack()
    Button_Back.place(x=40 , y= 30)
    #---------------------------------------------------
    #the frame box items 
    frame = Frame(Window_Add , bg="#555454" , width=400 , height=350)
    frame.pack()
    frame.place(x=370, y=120)
    #---------------------------------------------------
    #Enter Platform name Text
    Text_Platform_Name = Label(frame, text = "Enter Platform Name" ,bg="#555454", fg='white')
    Text_Platform_Name.pack()
    Text_Platform_Name.place(x=100, y=5)
    Text_Platform_Name_Text_Style = ("Comic Sans Ms" , 15 , "bold")
    Text_Platform_Name.configure(font=Text_Platform_Name_Text_Style)
    #---------------------------------------------
    #edit text enter Platform name
    Platform_Name_Entry = Entry(frame , width=25 )
    Platform_Name_Entry.pack()
    Platform_Name_Entry.place(x=65, y=50)
    Platform_Name_Entry_Text_Style = ('Arial')
    Platform_Name_Entry.configure(font=Platform_Name_Entry_Text_Style)
    #---------------------------------------------
    #Enter Account Username Text
    Text_Enter_Account = Label(frame, text = "Enter Account Username" ,bg="#555454", fg='white')
    Text_Enter_Account.pack()
    Text_Enter_Account.place(x=80, y=95)
    Text_Enter_Account_Text_Style = ("Comic Sans Ms" , 15 , "bold")
    Text_Enter_Account.configure(font=Text_Enter_Account_Text_Style)
    #---------------------------------------------
    #edit text enter account username 
    Account_Entry = Entry(frame , width=25 )
    Account_Entry.pack()
    Account_Entry.place(x=65, y=140)
    Account_Entry_Text_Style = ('Arial')
    Account_Entry.configure(font=Account_Entry_Text_Style)
    #---------------------------------------------
    #Enter Account Password Text
    Text_Enter_Password = Label(frame, text = "Enter Account Password" ,bg="#555454", fg='white')
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=80, y=185)
    Text_Enter_Password_Text_Style = ("Comic Sans Ms" , 15 , "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Text_Style)
    #---------------------------------------------
    #edit text enter account password 
    Password_Entry = Entry(frame , width=25 )
    Password_Entry.pack()
    Password_Entry.place(x=65, y=230)
    Password_Entry_Text_Style = ('Arial')
    Password_Entry.configure(font=Password_Entry_Text_Style)
    #---------------------------------------------
    def button_save_clicked():
        #_________________________________________________________
        #get value edit text
        Value_Platform_Name_Entry = Platform_Name_Entry.get()
        Value_Account_Entry = Account_Entry.get()
        Value_Password_Entry = Password_Entry.get()
        #_________________________________________________________
        if Value_Platform_Name_Entry and Value_Account_Entry and Value_Password_Entry != "":
            result = Value_Platform_Name_Entry + " " + ":" + " " + Value_Account_Entry + " " + "=" + " " + Value_Password_Entry
            #_________________________________________________________
            #encrypt user password with fernet
            All_Password_Encrypt = fernet.encrypt(result.encode()).decode()
            #create txt file for save user encrypt passwrod
            File_All_Password = open('All_Password' , 'a')
            File_All_Password.write(All_Password_Encrypt + "\n")
            File_All_Password.close()
            result = ""
            #_________________________________________________________
            messagebox.showinfo("Success" , "save info successfully")
        else:
            messagebox.showerror("Error" , "please fill filed")
    #---------------------------------------------
    #button save password
    Button_save_password = Button(frame , text="Save" , width=17 , bg= "black", fg = "white" , command=button_save_clicked) 
    Button_save_password.pack()
    Button_save_password.place(x=87, y=285)
    Button_save_passwrod_Text_Style = ("Centaur" , 17 , "bold")
    Button_save_password.configure(font=Button_save_passwrod_Text_Style)
    #---------------------------------------------------
    #start window add
    Window_Add.mainloop()
    #---------------------------------------------------

#________________________________End Add Password page gui code_________________________________
#________________________________View All Password page gui code_________________________________
def Passwords():
    #---------------------------------------------------
    #variable class Tk from tkinter lib
    Window_Passwords = Tk()
    #---------------------------------------------------
    #customize window app
    Window_Passwords.title("PASSAM (list passwords)")
    Window_Passwords.config(bg= "#353535")
    Window_Passwords.geometry("800x500")
    Window_Passwords.resizable(False , False)
    Window_Passwords.iconbitmap("iconApp.ico")
    #---------------------------------------------------
    #text Add password in header app
    Text_list_Password = Label(Window_Passwords , text="List Passwords" , bg="#353535" , fg="white" , width=12)
    Text_list_Password.pack()
    #Text_Welcome.place(x=220 , y=20)
    Text_list_Password_Style = ("Caveat" , 50 , "bold")
    Text_list_Password.configure(font=Text_list_Password_Style)
    #---------------------------------------------------
    #image icon app in window
    #enter your image.ico location with two \\
    Passam_Image_Icon = Image.open("E:\\project\\PasswordManager\\logo2.jpg")
    Passam_Image_Icon = Passam_Image_Icon.resize((300 , 210))
    Tk_Passam_Image = ImageTk.PhotoImage(Passam_Image_Icon)
    Passam_Image_Lable = Label(Window_Passwords ,image=Tk_Passam_Image )
    Passam_Image_Lable.place(x=30 , y=160)
    #---------------------------------------------------
    #button back 
    Back_Image = Image.open("back.png")
    Back_Image = Back_Image.resize((25 , 25))
    Back_Image = ImageTk.PhotoImage(Back_Image)
    #define a function to be called when the button is clicked
    def button_back_clicked():
        #close window add password and open menu page
        Window_Passwords.destroy()
        Menu()
    #create the button back with the image
    Button_Back = Button(Window_Passwords , image=Back_Image , command=button_back_clicked)
    Button_Back.pack()
    Button_Back.place(x=40 , y= 30)
    #---------------------------------------------------
    View_All_Passwords()
    List_of_Passwords = File_All_Password
    List_Passwords = Listbox(Window_Passwords , height=13 , width=35 , bg="white" , fg="#04757c")
    for item in List_of_Passwords :
        Password_Decrypt = fernet.decrypt(item.encode()).decode()
        result = str(List_of_Passwords.index(item)) + "-" + " " + Password_Decrypt
        List_Passwords.insert(END , result)
        List_Passwords.pack()
        List_Passwords.place(x=360 , y=115)
        List_Passwords_Text_Style = ("Centaur" , 17 , "bold")
        List_Passwords.configure(font = List_Passwords_Text_Style)
    #---------------------------------------------------
    #start window 
    Window_Passwords.mainloop()
#________________________________End View All Password page gui code_________________________________

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
def View_All_Passwords():
    global File_All_Password
    #read App_Password file for decrypt
    File_All_Password = open('All_Password' , 'r')
    File_All_Password = File_All_Password.readlines()
    #decrypt user password 
    Load_key_File()
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







