from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow
from Hotel import HotelManagementSystem 
import mysql.connector
from tkinter import messagebox
import random
import time
import datetime


def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

          # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\a.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0,relwidth=1, relheight=1)

        
        # Frame for login content
        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=150, width=340, height=450)

        
        # Login icon
        img1 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=120, y=10)

         # Get Started label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=90, y=95)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=200)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=230, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=270)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=300, width=270)

          # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=350, width=120, height=35)

         # Register button
        registerbtn = Button(frame, text="New User Register",  font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=400, width=160)

        # Forgot button
        forgotbtn = Button(frame, command=self.forgot_password_window,text="Forgot Password?",  font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=10, y=420, width=160)


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to Hotel Management System ")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    return
            conn.commit()
            conn.close()

            # reset  password
    

# reset password

    def reset_pass(self):
                if self.combo_security_Q.get()=="Select":
                     messagebox.showerror("Error","Select Security Question",parent=self.root2)
                elif self.txt_security.get()=="":
                    messagebox.showerror("Error","Please enter the answer",parent=self.root2)
                elif self.txt_newpass.get()=="":
                    messagebox.showerror("Error","Please enter the new password",parent=self.root2)
                else:
                      conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="hotel")
                      my_cursor = conn.cursor()
                      query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                      value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_SecurityA)
                      my_cursor.execute(query,value)
                      row=my_cursor.fetchone()
                      if row==None:
                          messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
                      else:
                          query=("update register set password=%s where email=%s")
                          value=(self.txt_newpass.get(),self.txtuser.get())
                          my_cursor.execute(query,value)

                          conn.commit()
                          conn.close()
                          messagebox.showinfo("Info","your password has been reset ,please login new password",parent=self.root2)
                          self.root2.destroy()


                def return_login(self):
                    self.root.destroy()
   

    
                          
                        
                    
    


               

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
             conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="hotel")
             my_cursor = conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row = my_cursor.fetchone()
             #print(row)
             if row==None:
                 messagebox.showerror("My Error","Please enter the valid user name")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forget Password")
                 self.root2.geometry("340x450+610+170")

                 l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                 l.place(x=0,y=10,relwidth=1)

                 security_Q_lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                 security_Q_lbl.place(x=50, y=80)

                 self.combo_security_Q = ttk.Combobox(self.root2,  font=("times new roman", 15, "bold"), state='readonly')
                 self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
                 self.combo_security_Q.place(x=50, y=110, width=250)
                 self.combo_security_Q.current(0)

                 security_A_lbl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                 security_A_lbl.place(x=50, y=150)

                 security_A_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                 security_A_entry.place(x=50, y=180, width=250)

                 new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                 new_password.place(x=50, y=220)

                 self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                 self.txt_newpass.place(x=50, y=250, width=250)


                 btn=Button(self.root2,text="Reset",font=("times new roman", 15, "bold"),fg="white",bg="green")
                 btn.place(x=100,y=290)



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New Registration")
        self.root.geometry("1600x900+0+0")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # bg image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="dark green", bg="white")
        register_lbl.place(x=20, y=20)

        # label and entry
        # row 1
        fname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_lbl.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_lbl.place(x=370, y=100)

        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=130, width=250)

        # row 2
        contact_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_lbl.place(x=50, y=170)

        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=200, width=250)

        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=370, y=170)

        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=200, width=250)

        # row 3
        security_Q_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q_lbl.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state='readonly')
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A_lbl.place(x=370, y=240)

        security_A_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        security_A_entry.place(x=370, y=270, width=250)

        # row 4
        pswd_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd_lbl.place(x=50, y=310)

        pswd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        pswd_entry.place(x=50, y=340, width=250)

        confirm_pswd_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd_lbl.place(x=370, y=310)

        confirm_pswd_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"), show="*")
        confirm_pswd_entry.place(x=370, y=340, width=250)

        # check button
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the terms and conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # buttons
        img = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        
        
        
        
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data, image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)

      
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, command=self.return_login,borderwidth=0, cursor="hand2")
        b2.place(x=330, y=420, width=200)

    # function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="hotel")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
    self.var_fname.get(),
    self.var_lname.get(),
    self.var_contact.get(),
    self.var_email.get(),
    self.var_securityQ.get(),
    self.var_securityA.get(),
    self.var_pass.get()
))

               

               
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully")

    


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root 
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # 1st image
        img1 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\taj.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1400, height=140)

        # ===== logo image =====
        img2 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\logo2.jpg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        
        # title 
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="white", relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1400, height=50)

        # ===== main frame =====
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ===== MENU =====
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ===== btn frame =====
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",command=self.Room_Details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ===== right side image =====
        img3 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\hotels.jpg")
        img3 = img3.resize((1300, 600), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1200, height=600)

        # ===== additional images =====
        img4 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\5.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\2.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
    
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = roombooking(self.new_window)

    def Room_Details(self):
        self.new_window = Toplevel(self.root)
        self.app =  RoomDetails(self.new_window)

       



if __name__=="__main__":
    main()
   
