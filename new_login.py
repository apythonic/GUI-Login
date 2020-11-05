from tkinter import *
import tkinter.font as font
import tkinter.messagebox

import time
import shelve



class Visual:
    def __init__(self,old_root):

        old_root.destroy()

        self.root = Tk()
        self.win_size = self.root.geometry("800x500")

        self.color = self.root.configure(bg="black")
        self.font = font.Font(size= 30)

        self.home_screen()

    def home_screen(self):

        # just title on the home screen
        title = Label(self.root, text= "WELCOME USER , PLEASE LOGIN BELOW ",padx= 200,anchor= "center" ,bg="grey")
        title.place(relx= 0.5, rely= 0.0 , anchor= "n")

        # the login fields and the enter button
        self.entery()


    def entery(self):

        # a text that says "username" next to the input field
        user_text = Label(self.root, text= "USERNAME :", bg="grey")
        # the username input field
        username = Entry(self.root, width= 50)

        # a text that says "password" next to the input field
        passw_text = Label(self.root, text= "PASSWORD :", bg= "grey")
        # the password input field
        password = Entry(self.root, width= 50, show="*")

        # puts the text and the user input fields on the screen
        user_text.place(rely= 0.1, anchor= "nw")
        username.place(relx= 0.1, rely= 0.1, anchor= "nw")

        # puts the text and the user input fields on the screen
        passw_text.place(rely= 0.2,anchor= "nw")
        password.place(relx= 0.1, rely= 0.2, anchor= "nw")


        # button that is clicked when finished with inputing your login information

        submit = Button(self.root, text= "ENTER", padx= 80, pady= 10, command=lambda :Login(username_clear=username,
                                                                                            password_clear= password,
                                                                                            root= self.root,
                                                                                            user_input= username.get(),
                                                                                            passw_input= password.get()))
        submit.place(relx= 0.6, rely= 0.2, anchor= "sw")
        self.root.mainloop()

class Login:
    def __init__(self, username_clear , password_clear , root, user_input, passw_input):

        username_clear.delete(0,END)
        password_clear.delete(0,END)

        self.root = root

        self.user_input = user_input
        self.passw_input = passw_input

        self.login_check()

    def login_check(self):
        with shelve.open("data","c") as data:

            key, value = self.user_input , self.passw_input


            if key in data and value == data[key]:

                welcome = Label(self.root, text= f"WELCOME BACK \n{self.user_input.upper()}", padx= 200, pady= 50)
                welcome.place(relx= 0.2, rely= 0.5, anchor= "nw")

                time.sleep(2)
                welcome.destroy()

                question = Label(self.root, text="Do you wish to open the game ping pong?").place(relx= 0.45,rely= 0.4,anchor="n")

                game = Button(self.root, text="Yes",command=lambda:self.game(root=self.root)).place(relx= 0.4, rely=0.5,anchor="n")
                no_game = Button(self.root, text="NO",command=lambda :self.end(root=self.root)).place(relx= 0.5, rely= 0.5,anchor="n")

            if "" in data :
                del data[""]

            elif key not in data or value != data[key]:

                wrong= Label(self.root, text="Wrong Username or Password", padx =200)
                wrong.place(relx= 0.1, rely= 0.5,anchor= "nw")

                question = Entry(self.root, width= 20)
                question.place(relx= 0.25, rely=0.6, anchor="nw")

                question_text = Label(self.root, text= "Are You A New User? Yes / No : ")
                question_text.place(relx= 0.01, rely= 0.6, anchor= "nw")

                enter_answ = Button(self.root, text= "ENTER", width= 30, command= lambda : self.answer_check(answer=question.get()))
                enter_answ.place(relx= 0.6, rely= 0.6)
                self.root.mainloop()

    def answer_check(self, answer):

        if answer.lower() == "yes":
            New_user(root=self.root)
        if answer.lower() == "no" :
            Visual(old_root=self.root)

    def game(self,root):
        root.destroy()

        import ping_pong

    def end(self,root):
        root.destroy()

class New_user:
    def __init__(self, root):

            root.destroy()

            self.new_root = Tk()
            self.win_size = self.new_root.geometry("800x500")
            self.color = self.new_root.configure(bg="black")
            self.font = font.Font(size=30)

            self.home_screen()

    def home_screen(self):
        title = Label(self.new_root, text="CREATE NEW USER LOGIN ", padx=200, anchor="center", bg="grey")
        title.place(relx=0.5, rely=0.0, anchor="n")

        self.regestration()

    def regestration(self):
        user_text = Label(self.new_root, text="USERNAME :", bg="grey")
        username = Entry(self.new_root, width=50)

        passw_text = Label(self.new_root, text="PASSWORD :", bg="grey")
        password = Entry(self.new_root, width=50,show="*")

        user_text.place(rely=0.1, anchor="nw")
        username.place(relx=0.1, rely=0.1, anchor="nw")

        passw_text.place(rely=0.2, anchor="nw")
        password.place(relx=0.1, rely=0.2, anchor="nw")

        submit = Button(self.new_root, text="CREATE USER", padx=80, pady=10, command=lambda :self.save_new_user(username= username,
                                                                                                                password= password))
        submit.place(relx=0.6, rely=0.2, anchor="sw")


    def save_new_user(self, username, password):

        with shelve.open("data","c") as data:

            key = username.get()

            if key in data:
                tkinter.messagebox.showinfo("FAIL","Username Already In use\nPLease Retry")

                New_user(root=self.new_root)

            if key not in data:
                data[username.get()] = password.get()

                login_retry = Button(self.new_root ,text="LOGIN", width= 80, command=lambda :self.succes(button=login_retry))
                login_retry.place(relx= 0.15, rely= 0.8)

            if key == "":
                del data[""]
                tkinter.messagebox.showinfo("FAIL", "Please Enter A Username")
                New_user(root=self.new_root)


    def succes(self,button):

        button.destroy()

        succes_login = Label(self.new_root, text="YOU HAVE SUCCESFULLY CREATED A NEW USER , CLICK BELOW TO LOGIN IN ",
                       padx=200)
        succes_login.place(relx=0.0, rely=0.7, anchor="sw")

        Button(self.new_root, text="Click HERE TO LOGIN", width= 100, command=lambda :self.retry_login()).place(relx= 0.05, rely= 0.6)

        self.new_root.mainloop()

    def retry_login(self):
        Visual(old_root=self.new_root)


root = Tk()
main = Visual(root)
