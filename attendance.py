from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

my_data=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        #Variables
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        #first image
        img=Image.open(r"C:\Users\ROHAN\Downloads\faceattendance.jpeg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"C:\Users\ROHAN\Downloads\student2.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=800,y=0,width=800,height=200)

        #third image
        img2=Image.open(r"C:\Users\ROHAN\Downloads\stargazing.jpg")
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(f_lbl2,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(f_lbl2,bd=2)
        main_frame.place(x=20,y=50,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=580)

        img3=Image.open(r"C:\Users\ROHAN\Downloads\studentgirl.webp")
        img3=img3.resize((550,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl3=Label(Left_frame,image=self.photoimg3)
        f_lbl3.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=645,height=300)

        #Label and entry

        #student id
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=Entry(left_inside_frame,width=20,textvariable=self.var_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=7,pady=5,sticky=W)

        Roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Roll_entry=Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        Roll_entry.grid(row=0,column=3,padx=7,pady=5,sticky=W)

        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry=Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=7,pady=5,sticky=W)

        Department_label=Label(left_inside_frame,text="Dept:",font=("times new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Department_entry=Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman",13,"bold"))
        Department_entry.grid(row=1,column=3,padx=7,pady=5,sticky=W)

        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Time_entry=Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=7,pady=5,sticky=W)

        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=7,pady=5,sticky=W)

        Attendance_label=Label(left_inside_frame,text="Attendance(Yes/No):",font=("times new roman",13,"bold"),bg="white")
        Attendance_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Attendance_entry=Entry(left_inside_frame,width=20,textvariable=self.var_attendance,font=("times new roman",13,"bold"))
        Attendance_entry.grid(row=4,column=1,padx=7,pady=5,sticky=W)

        #bbuttons
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=715,height=35)

        save_btn=Button(btn_frame,text="import csv",command=self.import_csv,font=("times new roman",13,"bold"),width=15,bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        delete_btn=Button(btn_frame,text="export csv",command=self.export_csv,font=("times new roman",13,"bold"),width=15,bg="green",fg="white")
        delete_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),width=15,bg="green",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=15,bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=800,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=750,height=450)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Dept","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Dept",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Dept",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("ButtonRelease",self.get_cursor)

    #Fetch data
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def import_csv(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV Files","*.csv")],parent=self.root)
        with open(fln,'r') as my_file:
            csv_read=csv.reader(my_file,delimiter=",")
            for i in csv_read:
                my_data.append(i)
            self.fetch_data(my_data)

    #export csv
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV Files",".csv")],parent=self.root)
            with open(fln,mode="w",newline="") as my_file:
                exp_write=csv.writer(my_file,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :(str(es))",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()