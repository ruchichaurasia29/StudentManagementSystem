from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
import mysql.connector

rt = Tk()
rt.geometry("1300x780")
rt.title("STUDENT MANAGEMENT SYSTEM")


def add():
    if name_entry.get() == "" or roll_entry.get() == "" or email_entry.get() == "" or birth_entry.get() == "" or phone_entry.get() == "" or gender_entry.get() == "" or course_entry.get() == "" or branch_entry.get() == "" or father_entry.get() == "" or mother_entry.get() == "":
        tmsg.showinfo("Insert status", "Please fill all fields")
    else:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Student_Record')
        cursor = con.cursor()
        cursor.execute(
            "insert into stud values('" + name_entry.get() + "','" + roll_entry.get() + "','" + email_entry.get() + "','" + birth_entry.get() + "','" + phone_entry.get() + "','" + gender_entry.get() + "', '" + course_entry.get() + "' , '" + branch_entry.get() + "','" + father_entry.get() + "','" + mother_entry.get() + "')")
        cursor.execute("commit")
        tmsg.showinfo("Insert Status", "Inserted Successfully")
        show()
        clear()
        con.close()

def clear():
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    email_entry.delete(0, END)
    birth_entry.delete(0, END)
    phone_entry.delete(0, END)
    gender_entry.delete(0, END)
    course_entry.delete(0, END)
    branch_entry.delete(0, END)
    father_entry.delete(0, END)
    mother_entry.delete(0, END)
    s_entry.delete(0, END)
    s_combo.delete(0, END)


def show():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Student_Record')
    cursor = con.cursor()
    cursor.execute("select * from stud")
    rows = cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', END, values=row)
        cursor.execute("commit")
    con.close()


def get_cursor(event):
    cur = table.focus()
    content = table.item(cur)
    r = content['values']
    name_var.set(r[0])
    roll_var.set(r[1])
    email_var.set(r[2])
    birth_var.set(r[3])
    phone_var.set(r[4])
    gender_var.set(r[5])
    course_var.set(r[6])
    branch_var.set(r[7])
    father_var.set(r[8])
    mother_var.set(r[9])


def update():
    if name_entry.get() == "" or roll_entry.get() == "" or email_entry.get() == "" or birth_entry.get() == "" or phone_entry.get() == "" or gender_entry.get() == "" or course_entry.get() == "" or branch_entry.get() == "" or father_entry.get() == "" or mother_entry.get() == "":
        tmsg.showinfo("Update status", "Please fill all fields")
    else:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Student_Record')
        cursor = con.cursor()
        cursor.execute("update stud set Email=%s , course=%s , branch=%s  where name=%s",
                       (email_var.get(), course_var.get(), branch_var.get(), name_var.get()))
        cursor.execute("commit")
        tmsg.showinfo("Update Status", "Updated Successfully")
        show()
        clear()
        con.close()


def delete():
    if (name_entry.get() == ""):
        tmsg.showinfo("Status", "Name is compulsary")
    else:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Student_Record')
        cursor = con.cursor()
        cursor.execute("delete from stud where name='" + name_var.get() + "'")
        cursor.execute("commit")
        tmsg.showinfo("Delete Status", "Deleted Successfully")
        show()
        clear()
        con.close()


def search_data():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Student_Record')
    cursor = con.cursor()
    cursor.execute("select * from stud where " + search_by.get() + " LIKE '%" + search_txt.get() + "%'")
    rows = cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', END, values=row)
        con.commit()
    con.close()
    
    

f = Frame(rt, bd=5, width=1269, height=80, relief=RAISED)
Label(f, text="STUDENT MANAGEMENT SYSTEM", font=("calibri", 24, "bold")).place(x=420, y=14)
f.place(x=0, y=0)




f1 = Frame(rt, bd=5, width=500, height=560, relief=RAISED)
Label(f1, text="MANAGE STUDENT DETAILS", font=("lucida", 14, "bold")).place(x=100, y=6)
name = Label(f1, text="Name", font=("lucida", 10, "bold"))
name.place(x=80, y=65)
roll = Label(f1, text="Roll No.", font=("lucida", 10, "bold"))
roll.place(x=80, y=105)
Email = Label(f1, text="Email", font=("lucida", 10, "bold"))
Email.place(x=80, y=145)
birth = Label(f1, text="Date Of Birth", font=("lucida", 10, "bold"))
birth.place(x=80, y=180)
phone = Label(f1, text="Phone No.", font=("lucida", 10, "bold"))
phone.place(x=80, y=215)
gender = Label(f1, text="Gender", font=("lucida", 10, "bold"))
gender.place(x=80, y=255)
course = Label(f1, text="Course", font=("lucida", 10, "bold"))
course.place(x=80, y=295)
branch = Label(f1, text="Branch", font=("lucida", 10, "bold"))
branch.place(x=80, y=335)
father = Label(f1, text="Father's Name", font=("lucida", 10, "bold"))
father.place(x=80, y=375)
mother = Label(f1, text="Mother's Name", font=("lucida", 10, "bold"))
mother.place(x=80, y=415)



name_var = StringVar()
roll_var = StringVar()
email_var = StringVar()
birth_var = StringVar()
phone_var = StringVar()
gender_var = StringVar()
course_var = StringVar()
branch_var = StringVar()
father_var = StringVar()
mother_var = StringVar()
search_by = StringVar()
search_txt = StringVar()




name_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=name_var)
name_entry.place(x=220, y=65)
roll_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=roll_var)
roll_entry.place(x=220, y=105)
email_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=email_var)
email_entry.place(x=220, y=145)
birth_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=birth_var)
birth_entry.place(x=220, y=180)
phone_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=phone_var)
phone_entry.place(x=220, y=215)
gender_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=gender_var)
gender_entry.place(x=220, y=255)
course_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=course_var)
course_entry.place(x=220, y=295)
branch_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=branch_var)
branch_entry.place(x=220, y=335)
father_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=father_var)
father_entry.place(x=220, y=375)
mother_entry = Entry(f1, bd=3, font=("lucida", 10, "bold"), textvariable=mother_var)
mother_entry.place(x=220, y=415)




Button(f1, text="ADD", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command = add).place(x=10, y=475)
Button(f1, text="UPDATE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command = update).place(x=130, y=475)
Button(f1, text="DELETE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command = delete).place(x=250, y=475)
Button(f1, text="CLEAR", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command = clear).place(x=370, y=475)
f1.place(x=0,y=80)




f2 = Frame(rt, bd=5, width=769, height=560, relief=RAISED)
s = Label(f2, text="SEARCH BY", font=("lucida", 12))
s.place(x=0, y=10)
s_combo = ttk.Combobox(f2, textvariable=search_by, font=("lucida", 12), width=14)
s_combo['values'] = ("Name")
s_combo.place(x=100, y=10)

s_entry = Entry(f2, textvariable=search_txt, font=("lucida", 12), width=19)
s_entry.place(x=260, y=10)

Button(f2, text="SEARCH", width=8, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command=search_data).place(x=450, y=5)
Button(f2, text="SHOW ALL", width=9, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command=show).place(x=550, y=5)
Button(f2, text="EXIT", width=8, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
command=quit).place(x=660, y=5)





f3 = Frame(f2, bd=5, relief=RAISED)
scroll_x = Scrollbar(f3, orient=HORIZONTAL)
scroll_y = Scrollbar(f3, orient=VERTICAL)
table = ttk.Treeview(f3, columns=("name", "roll", "email", "birth", "phone", "gender", "course", "branch", "father", "mother"),
                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)
table.heading("name", text="Name")
table.heading("roll", text="Roll Number")
table.heading("email", text="Email")
table.heading("birth", text="Date Of Birth")
table.heading("phone", text="Phone Number")
table.heading("gender", text="Gender")
table.heading("course", text="Course")
table.heading("branch", text="Branch")
table.heading("father", text="Father's Name")
table.heading("mother", text="Mother's Name")



table['show'] = 'headings'



table.column("name", width=100)
table.column("roll", width=100)
table.column("email", width=100)
table.column("birth", width=100)
table.column("phone", width=100)
table.column("gender", width=100)
table.column("course", width=100)
table.column("branch", width=100)
table.column("father", width=100)
table.column("mother", width=100)
table.pack(fill=BOTH, expand=True)
table.bind('<ButtonRelease-1>', get_cursor)
show()
f3.place(x=0, y=50, width=760, height=500)
f2.place(x=500, y=80)




rt.mainloop()
