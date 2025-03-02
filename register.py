from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("register")
        self.root.geometry("1600x900+0+0")
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
#images
        self.bg=ImageTk.PhotoImage(file=r"D:\hotel managemnet system\images\beach.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"D:\hotel managemnet system\images\flower.jpg")

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        security_q=Label(frame,text="Selct Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("select","your birth place","your first friend","your pet name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

         
        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_a.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,show="*",textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms and Conditions",font=("times new roman",15),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        img2=Image.open(r"D:\hotel managemnet system\images\register.jpg")
        img2=img2.resize((100,50),Image.LANCZOS)#high image level to low image level
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(frame,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=100,y=420,width=150)

        img3=Image.open(r"D:\hotel managemnet system\images\loginnow.jpg")
        img3=img3.resize((200,40),Image.LANCZOS)#high image level to low image level
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(frame,image=self.photoimg3,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=150)
        

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("error","all fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("error","please agree the terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","user already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                  self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),
                                  self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()
                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","registration successfull")
            
        







if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()  #to close the window