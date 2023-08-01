from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first image
        img=Image.open(r"C:\Users\ROHAN\Downloads\student1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\ROHAN\Downloads\student2.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=500,height=130)


        #third image
        img2=Image.open(r"C:\Users\ROHAN\Downloads\student3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=500,height=130)

        #backgroud image
        img3=Image.open(r"C:\Users\ROHAN\Downloads\stargazing.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(f_lbl3,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(f_lbl3,bd=2)
        main_frame.place(x=20,y=50,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=690,height=580)

        img3=Image.open(r"C:\Users\ROHAN\Downloads\studentgirl.webp")
        img3=img3.resize((550,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl3=Label(Left_frame,image=self.photoimg3)
        f_lbl3.place(x=5,y=0,width=720,height=130)

        #current course
        current_course=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information",font=("time new roman",12,"bold"))
        current_course.place(x=5,y=135,width=680,height=200)

        #Department
        dep_label=Label(current_course,text="Department",font=("times new roman",17,"bold"),bg="white")
        dep_label.grid(row=0,column=2)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","ECE","Electrical","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course,text="Course",font=("times new roman",17,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BE","ME","Diploma")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
        course_label=Label(current_course,text="Year",font=("times new roman",17,"bold"),bg="white")
        course_label.grid(row=1,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        course_label=Label(current_course,text="Semester",font=("times new roman",17,"bold"),bg="white")
        course_label.grid(row=1,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        course_combo.current(0)
        course_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        #Class student information
        class_student=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("time new roman",12,"bold"))
        class_student.place(x=5,y=240,width=720,height=350)

        #student id
        studentId_label=Label(class_student,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=Entry(class_student,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student,text="StudentName:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=Entry(class_student,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=Entry(class_student,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        rollno_label=Label(class_student,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=Entry(class_student,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=Entry(class_student,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_student,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phone_label=Label(class_student,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Adress
        adress_label=Label(class_student,text="Adress:",font=("times new roman",13,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        adress_entry=Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher
        teacher_label=Label(class_student,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radbtn1=ttk.Radiobutton(class_student,variable=self.var_radio1,value="Yes")
        radbtn1.grid(row=5,column=0)
        radlab1=Label(class_student,text="Take Photo Sample",font=("times new roman",9,"bold"),bg="white")
        radlab1.grid(row=6,column=0)

        radbtn2=ttk.Radiobutton(class_student,variable=self.var_radio1,value="No")
        radbtn2.grid(row=5,column=1)
        radlab2=Label(class_student,text="No Photo Sample",font=("times new roman",9,"bold"),bg="white")
        radlab2.grid(row=6,column=1)

        #bbuttons
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=225,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),width=16,bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),width=16,bg="green",fg="white")
        delete_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),width=16,bg="green",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=16,bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #Frame 2
        btn_frame2=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=260,width=715,height=35)

        take_btn=Button(btn_frame2,text="Take Photo",command=self.generate_dataset,font=("times new roman",13,"bold"),width=68,bg="blue",fg="white")
        take_btn.grid(row=0,column=0)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=690,height=580)

        img4=Image.open(r"C:\Users\ROHAN\Downloads\classtudent.webp")
        img4=img4.resize((550,130),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl4=Label(Right_frame,image=self.photoimg4)
        f_lbl4.place(x=5,y=0,width=720,height=130)

        #Search System
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=680,height=130)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="blue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll No","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=Entry(search_frame,width=11,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",13,"bold"),width=11,bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,text="Show All",font=("times new roman",13,"bold"),width=11,bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=680,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #Add data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_semester.get(),
                                                                                                         self.var_std_id.get(),
                                                                                                         self.var_std_name.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_teacher.get(),
                                                                                                         self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students Details added successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(self.var_dep.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_semester.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_teacher.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         self.var_std_id.get()                                                                                                                                                                              
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                self.fetch_data()
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #Reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #Take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="attackontitans",database="face_recognizer",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id=id+1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(self.var_dep.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_semester.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_teacher.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         self.var_std_id.get()                                                                                                                                                                              
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Load predefined data on frontal face
                clfr=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=clfr.detectMultiScale(gray,1.3,5)
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] 
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0    
                while True:
                    ret,img_frame=cap.read()
                    if face_cropped(img_frame) is not None:
                        img_id=img_id+1
                        face=cv2.resize(face_cropped(img_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user_img."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Successfully generated data sets")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        
                


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()