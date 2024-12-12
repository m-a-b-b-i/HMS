from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from CUStomer import Cust_Win
from Room import roombooking
from Details import RoomDetails 

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

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="black", fg="white", bd=0, cursor="hand1")
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

    def logout(self):
        self.root.destroy()

    

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
