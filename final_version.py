import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
import cx_Oracle    
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cx_Oracle

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UCM Library Login")
        self.root.geometry("800x600")
        self.set_background("LIBRARY.jpg")  # Change the path accordingly
        self.create_widgets()

    def create_widgets(self):
        login_frame = tk.Frame(self.root, bg='#ffffff', padx=10, pady=10)
        login_frame.place(relx=0.5, rely=0.6, anchor='center')

        title_label = tk.Label(self.root, text="UCM Library Login", font=("Helvetica", 24), bg='#ffffff', fg='#ff5733')
        title_label.place(relx=0.5, rely=0.4, anchor='center')

        user_label = tk.Label(login_frame, text="Username:", bg='#ffffff', font=("Helvetica", 14))
        user_label.pack(pady=5)
        self.user_entry = tk.Entry(login_frame, font=("Helvetica", 14))
        self.user_entry.pack(pady=5)

        pass_label = tk.Label(login_frame, text="Password:", bg='#ffffff', font=("Helvetica", 14))
        pass_label.pack(pady=5)
        self.user_pass = tk.Entry(login_frame, show="*", font=("Helvetica", 14))
        self.user_pass.pack(pady=5)

        sign_in_button = tk.Button(login_frame, text="Sign In", font=("Helvetica", 14), command=self.login)
        sign_in_button.pack(pady=20)

        self.center_window(800, 600)

    def login(self):
        username = "Geeks"
        password = "12345"
        entered_username = self.user_entry.get()
        entered_password = self.user_pass.get()

        if entered_username == username and entered_password == password:
            messagebox.showinfo(title="Login Successful", message="You have logged in successfully")
            self.open_library_management()
        elif entered_username == username and entered_password != password:
            messagebox.showwarning(title='Wrong password', message='Please check your password')
        elif entered_username != username and entered_password == password:
            messagebox.showwarning(title='Wrong username', message='Please check your username')
        else:
            messagebox.showerror(title="Login Failed", message="Invalid Username and password")

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def set_background(self, image_path):
        image = Image.open(r"C:\Users\shara\OneDrive\Desktop\DBTheory Project 2024 June19\Python Project 1\LIBRARY.jpg")
        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.root, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def open_library_management(self):
        self.root.destroy()  # Close the login window
        root = tk.Tk()
        obj = LibraryManagementSystem(root)
        root.mainloop()


class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # =====================Variables=========================================================================
        self.member_var=StringVar()
        self.ref_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()

        # =======================TitleLabel======================================================================
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="white",fg="crimson",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        def time(): 
            string = strftime('%I:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(lbltitle, font = ('times new roman',15, 'bold'),background = 'purple',foreground = 'white') 
        lbl.place(x=0,y=0,width=150) 
        time() 
        
        # ======Dataframe======================================================================================
        DataFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=12,padx=20,relief=RIDGE,fg="darkgreen",
                                                font=("arial",12,"bold"),text="Library Membership Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=12,padx=20,relief=RIDGE,fg="darkgreen",
                                            font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        # ===========Buttonframe================================================================================
        ButtonFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        # ===================================ButtonFrame=====================================
        btnAddData=Button(ButtonFrame,command=self.add_data,text="ADD DATA",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(ButtonFrame,command=self.showData,text="SHOW DATA",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,command=self.mDelete,text="DELETE",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=23,bg="crimson",fg="white")
        btnExit.grid(row=0,column=5)

        # =======Framedetails===================================================================================
        FrameDetails=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMenber=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",
                                                        font=("arial",12,"bold"),width=27)
        comMenber['value']=("Admin Staf","Lecturer","Student")
        comMenber.current(0)
        comMenber.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref_var,width=29)
        txtref.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.title_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Surname:",padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Post Code:",padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile Number:",padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
   
        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdate.grid(row=7,column=3)
   
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice,width=29)
        txtActualPrice.grid(row=8,column=3)

        # ===================================DataframeRight====================================
         # ===================================textBox====================================
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        # ===================================ListBox====================================
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        ListOfBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming',"Secrete Rahshy",'Python CookBook','Into to Machine Learning','Fluent Python','progrmming Python','The Algorithm','The tecnich Python',
                                                        'Machine tecno','My Python','Joss Ellif guru','Elite Jungle python','Jungli Python','Mumbai Python','Pune Python','Guru Of Python','Yellow Dragan','Red python',
                                                        'Machine python','Advance Python','Inton Python','RedChilli Python','Ishq Python']
        def SelectBook(event=""):
            value=str(bookList.get(bookList.curselection()))
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5487")
                self.booktitle_var.set("Python manual")
                self.auther_var.set("Paull berry")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.375")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic Of Pythpn")
                self.auther_var.set("ZED A.SHAW")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.725")

            
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Intro to python Comp Science")
                self.auther_var.set("John Zhelle")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.500")

            
            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic Of Pythpn")
                self.auther_var.set("Ref.Kapil Kamble")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.289")

            
            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID2546")
                self.booktitle_var.set("Python Cookbook")
                self.auther_var.set("Brian Jones")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.354")

            
            elif (x=="Into to Machine Learning"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Intro to Machine Learning")
                self.auther_var.set("Sarah Guaido")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.725")



        bookList=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        bookList.bind('<<ListboxSelect>>',SelectBook)
        bookList.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=bookList.yview)

        for item in ListOfBooks:
            bookList.insert(END,item)
        
        # =======Scrollbar=====================================================================================
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1460,height=150)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("member","ref","title","firtname","lastname","adress1",
                                            "adress2","postid","mobile","bookid","booktitle","auther","dateborrowed",
                                            "datedue","days","latereturnfine","dateoverdue","finalprice")
                                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("member",text="Member Type")
        self.library_table.heading("ref",text="Reference No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firtname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
   
        self.library_table.column("member",width=100)
        self.library_table.column("ref",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firtname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        self.library_table.pack(fill=BOTH,expand=1)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # =======================Function Declaration==================================================
        
    def add_data(self):
        if self.member_var.get()=="" or self.postcode_var.get()=="":
            tkinter.messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = cx_Oracle.connect("system", "admin", "localhost:1521/xe")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into library values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18)", (
                    self.member_var.get(),
                    self.ref_var.get(),
                    self.title_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                tkinter.messagebox.showinfo("Success", "Member has been inserted")
            except cx_Oracle.Error as e:
                tkinter.messagebox.showerror("Error", f"Must be enter Integer number, PRN NO & ID NO is Primery Key: {str(e)}")

    def update_data(self):
     if self.ref_var.get() == "":
        tkinter.messagebox.showerror("Error", "All Fields Are Required")
     else:
        try:
            conn = cx_Oracle.connect("system", "admin", "localhost:1521/xe")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE library 
                SET Member_type=:1, FirstName=:2, LastName=:3, Address1=:4, Address2=:5, PostCode=:6, Mobile=:7,
                    Bookid=:8, Booktitle=:9, Auther=:10, DateBorrowed=:11, DateDue=:12, DaysOfBook=:13, LateReturnFine=:14,
                    DateOverDue=:15, FinalPrice=:16 
                WHERE PRN_No=:17 AND ID_No=:18
            """, (
                self.member_var.get(), self.firstname_var.get(), self.lastname_var.get(), 
                self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), 
                self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), 
                self.auther_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), 
                self.daysonbook.get(), self.lateratefine_var.get(), self.dateoverdue.get(), 
                self.finallprice.get(), self.ref_var.get(), self.id_var.get()
            ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            tkinter.messagebox.showinfo("UPDATE", "Record has been updated successfully")
        except cx_Oracle.Error as e:
            tkinter.messagebox.showerror("Error", str(e))

    def fetch_data(self):
        try:
            conn = cx_Oracle.connect("system", "admin", "localhost:1521/xe")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM library")
            rows = my_cursor.fetchall()
            if rows:
                self.library_table.delete(*self.library_table.get_children())
                for row in rows:
                    self.library_table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except cx_Oracle.Error as e:
            tkinter.messagebox.showerror("Error", str(e))

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0])
        self.ref_var.set(row[1])
        self.title_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue.set(row[16])
        self.finallprice.set(row[17])

    def mDelete(self):
        if self.ref_var.get() == "":
            tkinter.messagebox.showinfo("ERROR", "First Select the Member!!")
        else:
            try:
                conn = cx_Oracle.connect("system", "admin", "localhost:1521/xe")
                my_cursor = conn.cursor()
                query = "DELETE FROM library WHERE PRN_No = :prn_no"
                value = {'prn_no': self.ref_var.get()}
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                tkinter.messagebox.showinfo("DELETE", "Member has been Deleted successfully")
            except cx_Oracle.Error as e:
                tkinter.messagebox.showerror("Error", str(e))

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def reset(self):
        self.member_var.set("")
        self.ref_var.set("")
        self.title_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set
   

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.ref_var.get() + "\n") 
        self.txtBox.insert(END,"ID No:\t\t"+ self.title_var.get() + "\n")           
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")   
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")   
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")   
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")   
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")   
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")   
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")   
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")   
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")   
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")   
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")   
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook.get() + "\n")   
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.lateratefine_var.get() + "\n")   
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue.get() + "\n")   
        self.txtBox.insert(END,"FinallPrice:\t\t"+ self.finallprice.get() + "\n")   
        
   
            

if __name__ == "__main__":
    root = tk.Tk()
    obj = LoginApp(root)
    root.mainloop()
