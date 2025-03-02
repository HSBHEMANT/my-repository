from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")
        #variable
        self.var_contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
#title
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img6=Image.open(r"D:\hotel managemnet system\images\logo1.jpg")
        img6=img6.resize((110,50),Image.LANCZOS)#high image level to low image level
        self.photoimg6=ImageTk.PhotoImage(img6)

        labling=Label(self.root,image=self.photoimg6,bd=0,relief=RIDGE)
        labling.place(x=0,y=0,width=110,height=50)
#roombookingframe
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="room booking",font=("times new roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #creating all the labels
        lbl_cus_contact=Label(LabelFrameleft,text="customer contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cus_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("times new roman",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        #cust_name
        check_in=Label(LabelFrameleft,text="check in",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in.grid(row=1,column=0,sticky=W)

        txtcheckin=ttk.Entry(LabelFrameleft,textvariable=self.var_check_in,width=29,font=("times new roman",12,"bold"))
        txtcheckin.grid(row=1,column=1)
        #fetch data button
        btnadd=Button(LabelFrameleft,command=self.fetch_contact,text="fetch data",font=("times new roman",8,"bold"),bg="black",fg="gold",width=8)
        btnadd.place(x=345,y=4)

        #mother_name
        lblcheck_out=Label(LabelFrameleft,text="check out",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblcheck_out.grid(row=2,column=0,sticky=W)

        txtcheck_out=ttk.Entry(LabelFrameleft,textvariable=self.var_check_out,font=("times new roman",12,"bold"),width=29)
        txtcheck_out.grid(row=2,column=1)
        #gender
        label_roomtype=Label(LabelFrameleft,text="room type",font=("times new roman",12,"bold"))
        label_roomtype.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from details")
        ide=my_cursor.fetchall()
        combo_roomtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

       #postcode
        lblavailableroom=Label(LabelFrameleft,font=("times new roman",12,"bold"),text="room available",padx=2,pady=6)
        lblavailableroom.grid(row=4,column=0,sticky=W)

        #txtavailableroom=ttk.Entry(LabelFrameleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=29)
        #txtavailableroom.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomno from details")
        rows=my_cursor.fetchall()
        combo_roomno=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)
        #mobilenumber
        lblmeal=Label(LabelFrameleft,text="meal",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,font=("times new roman",12,"bold"),width=29)
        txtmeal.grid(row=5,column=1)
        #email
        lblnoofdays=Label(LabelFrameleft,text="no of days",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofday,font=("times new roman",12,"bold"),width=29)
        txtnoofdays.grid(row=6,column=1)
        
        lblpaidtax=Label(LabelFrameleft,text="paid tax",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpaidtax.grid(row=7,column=0,sticky=W)

        txtpaidtax=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,font=("times new roman",12,"bold"),width=29)
        txtpaidtax.grid(row=7,column=1)



        lblsubtotal=Label(LabelFrameleft,text="sub total",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblsubtotal.grid(row=8,column=0,sticky=W)

        txtsubtotal=ttk.Entry(LabelFrameleft,textvariable=self.var_total,font=("times new roman",12,"bold"),width=29)
        txtsubtotal.grid(row=8,column=1)


        lbltotalcost=Label(LabelFrameleft,text="total cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbltotalcost.grid(row=9,column=0,sticky=W)

        txttotalcost=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,font=("times new roman",12,"bold"),width=29)
        txttotalcost.grid(row=9,column=1)
        #bill 
        btnbill=Button(LabelFrameleft,text="bill",command=self.total,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

#buttons
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

        #rightsideimage
        img3=Image.open(r"D:\hotel managemnet system\images\image3.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)#high image level to low image level
        self.photoimg3=ImageTk.PhotoImage(img3)

        labling=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        labling.place(x=760,y=55,width=520,height=200)

        #table frame on the right side
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=435,y=280,width=860,height=260)
        
        lblsearchby=Label(tableframe,font=("times new roman",12,"bold"),text="search by",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("contact","room")
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
        d_table.place(x=0,y=50,width=860,height=180)
        #creating the  scroll bar
        scroll_x=ttk.Scrollbar(d_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(d_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(d_table,column=("contact","check in","check out","roomtype","room","meal","noofdays")
        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        #heading shows the heading in the column
        self.room_table.heading("contact",text="contact")
        self.room_table.heading("check in",text="check in")
        self.room_table.heading("check out",text="check out")
        self.room_table.heading("roomtype",text="roomtype")
        self.room_table.heading("room",text="room")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("noofdays",text="noofdays")
        

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("check in",width=100)
        self.room_table.column("check out",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("room",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_check_in.get()=="":
            messagebox.showerror("error","you have to fill all the forms",parent=self.root)#in this we have created the function of add button with validation
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_check_in.get(),self.var_check_out.get(),
                self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofday.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","your room has been booked")
            except Exception as es:
               messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
     
    def fetch_data(self):
               conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
               my_cursor=conn.cursor()
               my_cursor.execute("select * from room")
               rows=my_cursor.fetchall()
               if len(rows)!=0:
                   self.room_table.delete(*self.room_table.get_children())
               for i in rows:
                self.room_table.insert("",END,values=i)

                conn.commit
                conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofday.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
           my_cursor=conn.cursor()
           my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,room=%s,meal=%s,noofdays=%s where contact=%s",
                             (self.var_check_in.get(),self.var_check_out.get(),
                self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofday.get(),self.var_contact.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","room details has updated succesfully")

    def mdelete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofday.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")

    
        
    def fetch_contact(self):
        if self.var_contact.get()=="":
              messagebox.showerror("error","please enter contact number")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
             my_cursor=conn.cursor()
             query=("select name from customer where mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             if row==None:
                messagebox.showerror("error","this number not found",parent=self.root)
        
             else:
                  conn.commit()
                  conn.close()
                   

        showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
        showdataframe.place(x=450,y=55,width=300,height=180)

        lblname=Label(showdataframe,text="name:",font=("arial",12,"bold"))
        lblname.place(x=0,y=0)

        lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
        lbl.place(x=90,y=0)

        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        query=("select gender from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()


        lblgender=Label(showdataframe,text="gender:",font=("arial",12,"bold"))
        lblgender.place(x=0,y=30)

        lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
        lbl2.place(x=90,y=30)

        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        query=("select email from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()


        lblemail=Label(showdataframe,text="email:",font=("arial",12,"bold"))
        lblemail.place(x=0,y=60)

        lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
        lbl3.place(x=90,y=60)

        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        query=("select nationality from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()


        lblnationality=Label(showdataframe,text="nationality:",font=("arial",12,"bold"))
        lblnationality.place(x=0,y=90)

        lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
        lbl4.place(x=90,y=90)

        conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
        my_cursor=conn.cursor()
        query=("select address from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()


        lbladdress=Label(showdataframe,text="address:",font=("arial",12,"bold"))
        lbladdress.place(x=0,y=120)

        lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
        lbl4.place(x=90,y=120)

   #search system
    def search(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room where  "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close() 
        
             
        

    def total(self):
        inDate=self.var_check_in.get()
        outDate=self.var_check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofday.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="1" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)
        

        elif (self.var_meal.get()=="2" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)

        elif  (self.var_meal.get()=="3" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)

        elif  (self.var_meal.get()=="1" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)
             
        elif  (self.var_meal.get()=="2" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)
            
        elif   (self.var_meal.get()=="3" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)

        elif   (self.var_meal.get()=="1" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)
            
        elif  (self.var_meal.get()=="2" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)
            
        elif  (self.var_meal.get()=="3" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_total.set(ST)
            self.var_actualtotal.set(TT)

        
            
            



        
 


        
       
if __name__ == "__main__":
        root=Tk()
        obj=roombooking(root)
        root.mainloop()        