from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from getpass import getpass
import mysql.connector
from room import roombooking
from details import DetailsRoom
from customer import cust_win
from register import register
from hotel import hotelmng
import random
import time
import datetime
def main():
    win=Tk()
    app=Login_win(win)
    win.mainloop()

class Login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
       

        self.bg=ImageTk.PhotoImage(file=r"D:\hotel managemnet system\images\beach.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open(r"D:\hotel managemnet system\images\login.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username_lbl=Label(frame,text="email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpassword=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)
        

        img2=Image.open(r"D:\hotel managemnet system\images\user.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"D:\hotel managemnet system\images\pass.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)


        loginbtn=Button(frame,text="login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground=
                        "white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New user register",command=self.rigister_data,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        passwordbtn=Button(frame,text="Forget password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        passwordbtn.place(x=10,y=370,width=160)

    def rigister_data(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)

        
    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
           messagebox.showerror("error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpassword.get()=="ashu":
          messagebox.showinfo("success","welcome to the site")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),self.txtpassword.get()
            ))
            row=my_cursor.fetchone()
        if  row==None:
            messagebox.showerror("error","Invalid username and password")
        else:
            open_main=messagebox.askyesno("YesNo","acess only admin")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=hotelmng(self.new_window)
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()

    def reset(self):
        if self.combo_security_q.get()=="select":
            messagebox.showerror("error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("error","please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            values=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("info","your password has been updated please login again with new one",parent=self.root2)
                


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Hemant@123",database="hotelmanagement",port=3306)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            values=(self.txtuser.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="Selct Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_q.place(x=50,y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("select","your birth place","your first friend","your pet name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

         
                security_a=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_a.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

                


                        



        
            


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

        b1=Button(frame,image=self.photoimg3,command=self.loginow,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
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

    def loginow(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_win(self.new_window)



class hotelmng:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

        #firstimage
        img1=Image.open(r"D:\hotel managemnet system\images\hotel12.jpg")
        img1=img1.resize((1540,140),Image.LANCZOS)#high image level to low image level
        self.photoimg1=ImageTk.PhotoImage(img1)

        labling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labling.place(x=0,y=0,width=1540,height=140)
       
       
        #logo
        img2=Image.open(r"D:\hotel managemnet system\images\logo1.jpg")
        img2=img2.resize((230,140),Image.LANCZOS)#high image level to low image level
        self.photoimg2=ImageTk.PhotoImage(img2)

        labling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labling.place(x=0,y=0,width=230,height=140)

        #title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #menu
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        #framebutton
        Btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        Btn_frame.place(x=0,y=35,width=230,height=190)

        cst_btn=Button(Btn_frame,text="CUSTOMER",command=self.details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cst_btn.grid(row=0,column=0)

        room_btn=Button(Btn_frame,text="ROOM",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)

        details_btn=Button(Btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn=Button(Btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn=Button(Btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)

        #IMAGE3s
        img3=Image.open(r"D:\hotel managemnet system\images\image3.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)#high image level to low image level
        self.photoimg3=ImageTk.PhotoImage(img3)

        labling=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        labling.place(x=225,y=0,width=1310,height=590)
        #down image
        img4=Image.open(r"D:\hotel managemnet system\images\image4.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)#high image level to low image level
        self.photoimg4=ImageTk.PhotoImage(img4)

        labling=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        labling.place(x=0,y=225,width=230,height=210)
        
        img5=Image.open(r"D:\hotel managemnet system\images\image5.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)#high image level to low image level
        self.photoimg5=ImageTk.PhotoImage(img5)

        labling=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        labling.place(x=0,y=420,width=230,height=190)
        
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    
        
    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)



    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
        




        


            
        


          
          
if __name__=="__main__":
   main()
   