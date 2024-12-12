from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

class detailsroom:
    def __init__(self, root):
        self.root = root    
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

          # Title
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="white")
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # Logo image
        img2 = Image.open(r"C:\Users\Mabbi\Desktop\HOTEL MS\images\hotel images\logo2.jpg")
        img2 = img2.resize((100, 50), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=50)

        # Label frame 
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 12, "bold"), pady=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

           # Labels and entries

        # Customer contact
        lbl_cust_floor = Label(labelframeleft, text="Floor:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_floor.grid(row=0, column=0, sticky=W,padx=20)

        enty_floor = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        enty_floor.grid(row=0, column=1, sticky=W)


        lbl_RoomNo = Label(labelframeleft, text="RoomNo:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W,padx=20)

        enty_RoomNo = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        lbl_RoomType= Label(labelframeleft, text="RoomType:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W,padx=20)

        enty_RoomType = ttk.Entry(labelframeleft, font=("Arial", 13, "bold"), width=20)
        enty_RoomType.grid(row=2, column=1, sticky=W)



         # Button Frame inside Label Frame
        btn_frame2 = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=250, width=425, height=40)

        btnAdd = Button(btn_frame2,  text="Add", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame2,  text="Update", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame2, text="Delete", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame2, text="Reset", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnReset.grid(row=0, column=3, padx=1)

          # Table Frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("Arial", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)






if __name__ == "__main__":
    root = Tk()
    obj = detailsroom(root)
    root.mainloop()
