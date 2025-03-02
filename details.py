from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")
    #title
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
#logo
        img6=Image.open(r"D:\hotel managemnet system\images\logo1.jpg")
        img6=img6.resize((100,40),Image.LANCZOS)#high image level to low image level
        self.photoimg6=ImageTk.PhotoImage(img6)

        labling=Label(self.root,image=self.photoimg6,bd=0,relief=RIDGE)
        labling.place(x=0,y=0,width=100,height=40)
#labelframe
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="new room add",font=("times new roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=540,height=350)
#floor
        lbl_floor=Label(LabelFrameleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(LabelFrameleft,textvariable=self.var_floor,width=20,font=("times new roman",12,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
#room no
        lbl_roomno=Label(LabelFrameleft,text="Roomno",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)
        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(LabelFrameleft,textvariable=self.var_roomno,width=20,font=("times new roman",12,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)
#room type
        lbl_roomtype=Label(LabelFrameleft,text="Roomtype",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(LabelFrameleft,textvariable=self.var_roomtype,width=20,font=("times new roman",12,"bold"))
        entry_roomtype.grid(row=2,column=1,sticky=W)
        
#buttons
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="add",command=self.add_data,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="update",command=self.update,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btnreset=Button(btn_frame,text="reset",command=self.reset,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=2,padx=1)

        btndelete=Button(btn_frame,text="delete",command=self.mdelete,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=3,padx=1)
        #tableframe
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="show room details",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=600,y=55,width=600,height=350)
#scroll bar
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        self.room_table=ttk.Treeview(tableframe,column=("Floor","Roomno","Roomtype")
        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Roomno",text="Roomno")
        self.room_table.heading("Roomtype",text="Roomtype")
        

        self.room_table["show"]="headings"
        self.room_table.column("Floor",width=100)
        self.room_table.column("Roomno",width=100)
        self.room_table.column("Roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("error","you have to fill all the forms",parent=self.root)#in this we have created the function of add button with validation
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_roomno.get(),
                self.var_roomtype.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","new room added")
            except Exception as es:
               messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
               conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
               my_cursor=conn.cursor()
               my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
           my_cursor=conn.cursor()
           my_cursor.execute("update details set Floor=%s,Roomtype=%s where Roomno=%s",
                             (self.var_floor.get(),self.var_roomtype.get(),
                self.var_roomno.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","room details has updated succesfully")

    def mdelete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this room",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query="delete from details where Roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")
        

        
if __name__ == "__main__":
        root=Tk()
        obj=DetailsRoom(root)
        root.mainloop()        