from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_rec import Face_Rec
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x700+0+0")
        self.root.title("Facial Recognition System")

        #first image
        img=Image.open(r"C:\Users\ROHAN\Downloads\oxford.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\ROHAN\Downloads\students.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=500,height=130)


        #third image
        img2=Image.open(r"C:\Users\ROHAN\Downloads\classroom.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=500,height=130)

        #backgroud image
        img3=Image.open(r"C:\Users\ROHAN\Downloads\stargazing3.webp")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(f_lbl3,text="FACE RECOGNITION SMART ATTENDANCE MANAGEMENT SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\ROHAN\Downloads\animestud.png")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_lbl3,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=165,width=220,height=220)

        b1_1=Button(f_lbl3,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=200,y=365,width=220,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\ROHAN\Downloads\face_d.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(f_lbl3,image=self.photoimg5,command=self.detect_face,cursor="hand2")
        b2.place(x=500,y=165,width=220,height=220)

        b2_1=Button(f_lbl3,text="Detect Face",command=self.detect_face,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
        b2_1.place(x=500,y=365,width=220,height=40)

        #Attendance button
        img6=Image.open(r"C:\Users\ROHAN\Downloads\attendance.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(f_lbl3,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b3.place(x=800,y=165,width=220,height=220)

        b3_1=Button(f_lbl3,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
        b3_1.place(x=800,y=365,width=220,height=40)


        #Train button
        img8=Image.open(r"C:\Users\ROHAN\Downloads\train2.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(f_lbl3,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=1100,y=165,width=220,height=220)

        b5_1=Button(f_lbl3,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="red")
        b5_1.place(x=1100,y=365,width=220,height=40)

    
    def open_img(self):
        os.startfile("data")


    #Function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def detect_face(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Rec(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()