from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Rec:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="blue",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\ROHAN\Downloads\face_recognition.png")
        img_top=img_top.resize((650,900),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl_top=Label(self.root,image=self.photoimg_top)
        f_lbl_top.place(x=0,y=55,width=650,height=900)

        img_top2=Image.open(r"C:\Users\ROHAN\Downloads\robot2.png")
        img_top2=img_top2.resize((950,900),Image.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        f_lbl_top2=Label(self.root,image=self.photoimg_top2)
        f_lbl_top2.place(x=650,y=55,width=850,height=700)

        btn1=Button(f_lbl_top2,text="DETECT FACE",cursor="hand2",command=self.face_recog,font=("times new roman",13,"bold"),width=16,bg="green",fg="white")
        btn1.place(x=450,y=350,width=200,height=40)

    #Attendance
    def mark_attendance(self,i,r,n,d):
        with open("rohan.csv","r+",newline="\n") as f:
            my_datalist=f.readline()
            name_list=[]
            for line in my_datalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) or (n not in name_list) or (r not in name_list) or (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scale_factor,min_neighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scale_factor,min_neighbours)

            co_ord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from student where ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where ID="+str(id))
                r=my_cursor.fetchone()

                my_cursor.execute("select dep from student where ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select ID from student where ID="+str(id))
                i=my_cursor.fetchone()



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept.:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                co_ord=[x,y,w,y]

            return co_ord
            
        def recognize(img,clf,Face_Rec):
            co_ord=draw_boundary(img,Face_Rec,1.1,10,(255,255,255),"Face",clf)
            return img
            
        Face_Rec=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap=cv2.VideoCapture(0)

        while True:
            ret,img=cap.read()
            img=recognize(img,clf,Face_Rec)
            cv2.imshow("Welcome to face recognition",img)
                
            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_Rec(root)
    root.mainloop()