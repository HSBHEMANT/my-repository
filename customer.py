from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        #variables this is used to connect sql data from sql and we are text variable in every other labels
        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))

        self.cus_name=StringVar()
        self.cus_mother=StringVar()
        self.cus_gender=StringVar()
        self.cus_post=StringVar()
        self.cus_mobile=StringVar()
        self.cus_email=StringVar()
        self.cus_nationality=StringVar()
        self.cus_address=StringVar()
        self.cus_idproof=StringVar()
        self.cus_idnumber=StringVar()
        #title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img6=Image.open(r"D:\hotel managemnet system\images\logo1.jpg")
        img6=img6.resize((110,50),Image.LANCZOS)#high image level to low image level
        self.photoimg6=ImageTk.PhotoImage(img6)

        labling=Label(self.root,image=self.photoimg6,bd=0,relief=RIDGE)
        labling.place(x=0,y=0,width=110,height=50)

        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",font=("times new roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #labeland entries
        lbl_cust_ref=Label(LabelFrameleft,text="customer ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=29,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)
        #cust_name
        cust_name=Label(LabelFrameleft,text="customer name",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.cus_name,width=29,font=("times new roman",12,"bold"))
        txtcname.grid(row=1,column=1)
        #mother_name
        lblmname=Label(LabelFrameleft,text="mother name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(LabelFrameleft,textvariable=self.cus_mother,font=("times new roman",12,"bold"),width=29)
        txtmname.grid(row=2,column=1)
        #gender
        label_gender=Label(LabelFrameleft,text="gender",font=("times new roman",12,"bold"))
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.cus_gender,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

       #postcode
        lblpostcode=Label(LabelFrameleft,font=("times new roman",12,"bold"),text="post code",padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        txtpostcode=ttk.Entry(LabelFrameleft,textvariable=self.cus_post,font=("times new roman",12,"bold"),width=29)
        txtpostcode.grid(row=4,column=1)
        #mobilenumber
        lblmobile=Label(LabelFrameleft,text="mobile number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(LabelFrameleft,textvariable=self.cus_mobile,font=("times new roman",12,"bold"),width=29)
        txtmobile.grid(row=5,column=1)
        #email
        lblemail=Label(LabelFrameleft,text="email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(LabelFrameleft,textvariable=self.cus_email,font=("times new roman",12,"bold"),width=29)
        txtemail.grid(row=6,column=1)
        #nationality
        lblnationality=Label(LabelFrameleft,text="nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(LabelFrameleft,textvariable=self.cus_nationality,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("indian","other")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        
        #idprooftypecombobox
        label_idproof=Label(LabelFrameleft,text="id proof",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_idproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(LabelFrameleft,textvariable=self.cus_idproof,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("adhaar card","passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #idnumber
        lblidnum=Label(LabelFrameleft,text="id number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblidnum.grid(row=9,column=0,sticky=W)

        txtidnum=ttk.Entry(LabelFrameleft,textvariable=self.cus_idnumber,font=("times new roman",12,"bold"),width=29)
        txtidnum.grid(row=9,column=1)
        #adress
        lblemail=Label(LabelFrameleft,text="address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=10,column=0,sticky=W)

        txtemail=ttk.Entry(LabelFrameleft,textvariable=self.cus_address,font=("times new roman",12,"bold"),width=29)
        txtemail.grid(row=10,column=1)

        #btn
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="add",command=self.add_data,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="update",command=self.update,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btnreset=Button(btn_frame,text="reset",command=self.reset,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=2,padx=1)

        btndelete=Button(btn_frame,text="delete",command=self.mdelete,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=3,padx=1)

        #table frame
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=435,y=50,width=860,height=490)
        
        lblsearchby=Label(tableframe,font=("times new roman",12,"bold"),text="search by",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("mobile","referal")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        self.txt_search=StringVar()
        txtidsearch=ttk.Entry(tableframe,textvariable=self.txt_search,font=("times new roman",12,"bold"),width=29)
        txtidsearch.grid(row=0,column=2)

        btnsearch=Button(tableframe,text="search",command=self.search,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(tableframe,text="showall",command=self.fetch_data,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=1)

        #showtable
        d_table=Frame(tableframe,bd=2,relief=RIDGE)
        d_table.place(x=0,y=50,width=860,height=350)
        #creating the  scroll bar
        scroll_x=ttk.Scrollbar(d_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(d_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(d_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address")
        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        #heading shows the heading in the column
        self.cust_details_table.heading("ref",text="Refer no")
        self.cust_details_table.heading("name",text="name")
        self.cust_details_table.heading("mother",text="mother name")
        self.cust_details_table.heading("gender",text="gender")
        self.cust_details_table.heading("post",text="post code")
        self.cust_details_table.heading("mobile",text="mobile")
        self.cust_details_table.heading("email",text="email")
        self.cust_details_table.heading("nationality",text="nationality")
        self.cust_details_table.heading("idproof",text="id proof")
        self.cust_details_table.heading("idnumber",text="id number")
        self.cust_details_table.heading("address",text="address")

        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.cus_mobile.get()=="" or self.cus_mother.get()=="":
            messagebox.showerror("error","you have to fill all the forms",parent=self.root)#in this we have created the function of add button with validation
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.cus_name.get(),self.cus_mother.get(),
                self.cus_gender.get(),self.cus_post.get(),self.cus_mobile.get(),self.cus_email.get(),self.cus_nationality.get(),self.cus_idproof.get(),
                self.cus_idnumber.get(),self.cus_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added")
            except Exception as es:
               messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)

                conn.commit
                conn.close()
#this will show the data in customer details column where we can also update it
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.cus_name.set(row[1]),
        self.cus_mother.set(row[2]),
        self.cus_gender.set(row[3]),
        self.cus_post.set(row[4]),
        self.cus_mobile.set(row[5]),
        self.cus_email.set(row[6]),
        self.cus_nationality.set(row[7]),
        self.cus_idproof.set(row[8]),
        self.cus_idnumber.set(row[9]),
        self.cus_address.set(row[10])

    def update(self):
        if self.cus_mobile.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
           my_cursor=conn.cursor()
           my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where referal=%s",
                             (self.cus_name.get(),self.cus_mother.get(),
                self.cus_gender.get(),self.cus_post.get(),self.cus_mobile.get(),self.cus_email.get(),self.cus_nationality.get(),self.cus_idproof.get(),
                self.cus_idnumber.get(),self.cus_address.get(),self.var_ref.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","customer details has updated succesfully")
    
    def mdelete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query="delete from customer where referal=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
 
    def reset(self):
        self.cus_name.set(""),
        self.cus_mother.set(""),
        self.var_ref.set(""),
        #self.cus_gender.set(""),
        self.cus_post.set(""),
        self.cus_mobile.set(""),
        self.cus_email.set(""),
        #self.cus_nationality.set(""),
        #self.cus_idproof.set(""),
        self.cus_idnumber.set(""),
        self.cus_address.set("")

        
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))


    def search(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from customer where  "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
            conn.close() 
        
             
        

    
    

if __name__=="__main__":
     root=Tk()
     obj=cust_win(root)
     root.mainloop()