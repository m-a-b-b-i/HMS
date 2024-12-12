from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

class roombooking:
    def __init__(self, root):
        self.root = root    
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Variables 
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("times new roman", 12, "bold"), pady=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Labels and entries

        # Customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("Arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(labelframeleft, command=self.fetch_data, text="Fetch Data", font=("Arial", 8, "bold"), bg="black", fg="white", width=8)
        btnFetchData.place(x=347, y=4)

        # Check-in Date
        check_in_date = Label(labelframeleft, text="Check-in Date:", font=("Arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("Arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_Check_out = Label(labelframeleft, text="Check-out Date:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("Arial", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)

        # Room type (should be Combobox)
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)


       

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("Arial", 13, "bold"), width=27, state="readonly")
        combo_RoomType['values'] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        #txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=("Arial", 13, "bold"), width=29)
       # txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomNo FROM details")
        rows = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("Arial", 13, "bold"), width=27, state="readonly")
        combo_RoomType['values'] = rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4, column=1)


        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=("Arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No of Days:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=("Arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, text="Paid Tax:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("Arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("Arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("Arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # ==== BILL BUTTON ====
        btnBill = Button(labelframeleft,command=self.total, text="Bill", font=("Arial", 12, "bold"), bg="black", fg="white", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Button Frame inside Label Frame
        btn_frame2 = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=400, width=425, height=40)

        btnAdd = Button(btn_frame2, command=self.add_data, text="Add", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame2, command=self.update_data, text="Update", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame2, command=self.delete_data, text="Delete", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame2, command=self.reset, text="Reset", font=("Arial", 12, "bold"), bg="black", fg="white", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="Search By:", font=("Arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_search['value'] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, command=self.search, text="Search", font=("Arial", 12, "bold"), bg="black", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, command=self.fetch_data, text="Show All", font=("Arial", 12, "bold"), bg="black", fg="white", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Room_Table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("contact", text="Contact")
        self.Room_Table.heading("checkin", text="Check-in")
        self.Room_Table.heading("checkout", text="Check-out")
        self.Room_Table.heading("roomtype", text="Room Type")
        self.Room_Table.heading("roomavailable", text="Room Available")
        self.Room_Table.heading("meal", text="Meal")
        self.Room_Table.heading("noofdays", text="No of Days")

        self.Room_Table["show"] = "headings"

        self.Room_Table.column("contact", width=100)
        self.Room_Table.column("checkin", width=100)
        self.Room_Table.column("checkout", width=100)
        self.Room_Table.column("roomtype", width=100)
        self.Room_Table.column("roomavailable", width=100)
        self.Room_Table.column("meal", width=100)
        self.Room_Table.column("noofdays", width=100)

        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()
                                                                                       ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s", (
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()
                                                                                                                                           ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            if not delete:
                return

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="hotel")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate - inDate).days)

        if self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury":
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single":
            q1 = float(300)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double":
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury":
            q1 = float(600)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "lunch" and self.var_roomtype.get() == "Single":
            q1 = float(600)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "lunch" and self.var_roomtype.get() == "Double":
            q1 = float(600)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury":
            q1 = float(500)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single":
            q1 = float(500)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double":
            q1 = float(500)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.1))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = roombooking(root)
    root.mainloop()

