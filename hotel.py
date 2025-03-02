from tkinter import*
from PIL import Image, ImageTk
from customer import cust_win
from room import roombooking
from details import DetailsRoom
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

    def reportfun(self):
         self.new_window=Toplevel(self.root)
         self.app=report(self.new_window)
        




        

        



if __name__ == "__main__":
        root=Tk()
        obj=hotelmng(root)
        root.mainloop()



        