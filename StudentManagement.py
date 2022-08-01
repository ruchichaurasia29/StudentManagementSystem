from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector



root=Tk()
root.geometry("1300x780")
root.title("COLLEGE MANAGEMENT SYSTEM")

def insert_data():
    u3 = name1_entry.get()
    c3 = pas_entry.get()
    if u3 == 'admin' and c3 == '123':
        rt = Tk()
        rt.geometry("1300x780")
        rt.title("COLLEGE MANAGEMENT SYSTEM")


        def home():
            fh = Frame(rt, bd=5, width=1050, height=560, bg="pink", relief=RAISED)
            img = Image.open("hotel.png")
            img = img.resize((80,80))
            my = ImageTk.PhotoImage(img)
            label = Label(fh,image=my)
            label.place(x=0, y=0)
            fh.place(x=220, y=80)


        def student():
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


            f4=Frame(rt,bd=5, width=1050, height=560 ,relief=RAISED)
            f6 = Frame(f4, bd=5, width=380, height=550, relief=RAISED)
            Label(f6, text="MANAGE STUDENT DETAILS", font=("lucida", 14, "bold")).place(x=40, y=6)
            name = Label(f6, text="Name", font=("lucida", 10, "bold"))
            name.place(x=30, y=55)
            roll = Label(f6, text="Roll No.", font=("lucida", 10, "bold"))
            roll.place(x=30, y=95)
            Email = Label(f6, text="Email", font=("lucida", 10, "bold"))
            Email.place(x=30, y=135)
            birth = Label(f6, text="Date Of Birth", font=("lucida", 10, "bold"))
            birth.place(x=30, y=170)
            phone = Label(f6, text="Phone No.", font=("lucida", 10, "bold"))
            phone.place(x=30, y=205)
            gender = Label(f6, text="Gender", font=("lucida", 10, "bold"))
            gender.place(x=30, y=245)
            course = Label(f6, text="Course", font=("lucida", 10, "bold"))
            course.place(x=30, y=285)
            branch = Label(f6, text="Branch", font=("lucida", 10, "bold"))
            branch.place(x=30, y=325)
            father = Label(f6, text="Father's Name", font=("lucida", 10, "bold"))
            father.place(x=30, y=365)
            mother = Label(f6, text="Mother's Name", font=("lucida", 10, "bold"))
            mother.place(x=30, y=405)

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

            name_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=name_var)
            name_entry.place(x=170, y=55)
            roll_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=roll_var)
            roll_entry.place(x=170, y=95)
            email_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=email_var)
            email_entry.place(x=170, y=135)
            birth_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=birth_var)
            birth_entry.place(x=170, y=170)
            phone_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=phone_var)
            phone_entry.place(x=170, y=205)
            gender_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=gender_var)
            gender_entry.place(x=170, y=245)
            course_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=course_var)
            course_entry.place(x=170, y=285)
            branch_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=branch_var)
            branch_entry.place(x=170, y=325)
            father_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=father_var)
            father_entry.place(x=170, y=365)
            mother_entry = Entry(f6, bd=3, font=("lucida", 10, "bold"), textvariable=mother_var)
            mother_entry.place(x=170, y=405)

            Button(f6, text="ADD", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=add).place(x=50, y=445)
            Button(f6, text="UPDATE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                  command=update).place(x=200, y=445)
            Button(f6, text="DELETE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=delete).place(x=50, y=495)
            Button(f6, text="CLEAR", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                  command=clear).place(x=200, y=495)
            f6.place(x=0,y=0)


            f7 = Frame(f4, bd=5, width=660, height=540, relief=RAISED)

            s = Label(f7, text="SEARCH BY", font=("lucida", 10))
            s.place(x=0, y=10)
            s_combo = ttk.Combobox(f7, textvariable=search_by, font=("lucida", 12), width=8)
            s_combo['values'] = ("Name")
            s_combo.place(x=85, y=10)

            s_entry = Entry(f7, textvariable=search_txt, font=("lucida", 12), width=15)
            s_entry.place(x=190, y=10)

            Button(f7, text="SEARCH", width=8, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=search_data).place(x=340, y=5)
            Button(f7, text="SHOW ALL", width=9, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=show).place(x=440, y=5)
            Button(f7, text="EXIT", width=8, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=quit).place(x=550, y=5)

            f8 = Frame(f7, bd=5, relief=RAISED)
            scroll_x = Scrollbar(f8, orient=HORIZONTAL)
            scroll_y = Scrollbar(f8, orient=VERTICAL)
            table = ttk.Treeview(f8, columns=(
                "name", "roll", "email", "birth", "phone", "gender", "course", "branch", "father", "mother"),
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
            f8.place(x=0, y=50, width=648, height=490)
            f7.place(x=380, y=0)
            f4.place(x=220, y=80)


        def fees():
            def add():
                if erp_entry.get() == "" or s_name_entry.get() == "" or rol_entry.get() == "" or fath_entry.get() == "" or sem_entry.get() == "" or year_entry.get() == "" or phon_entry.get() == "" or total_entry.get() == "" or dep_entry.get() == "" or due_entry.get() == "":
                    tmsg.showinfo("Insert status", "Please fill all fields")
                else:
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("insert into fee values('" + erp_entry.get() + "','" + s_name_entry.get() + "','" + rol_entry.get() + "','" + fath_entry.get() + "','" + sem_entry.get() + "','" + year_entry.get() + "', '" + phon_entry.get() + "' , '" + total_entry.get() + "','" + dep_entry.get() + "','" + due_entry.get() + "')")
                    cursor.execute("commit")
                    tmsg.showinfo("Insert Status", "Inserted Successfully")
                    show()
                    clear()
                    con.close()

            def clear():
                erp_entry.delete(0, END)
                s_name_entry.delete(0, END)
                rol_entry.delete(0, END)
                fath_entry.delete(0, END)
                sem_entry.delete(0, END)
                year_entry.delete(0, END)
                phon_entry.delete(0, END)
                total_entry.delete(0, END)
                dep_entry.delete(0, END)
                due_entry.delete(0, END)


            def show():
                con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                cursor = con.cursor()
                cursor.execute("select * from fee")
                rows = cursor.fetchall()
                if len(rows)!= 0:
                    table.delete(*table.get_children())
                    for row in rows:
                        table.insert('', END, values=row)
                    cursor.execute("commit")
                con.close()

            def get_cursor(event):
                cur1 = table.focus()
                content = table.item(cur1)
                r = content['values']
                erp_var.set(r[0])
                s_name_var.set(r[1])
                rol_var.set(r[2])
                fath_var.set(r[3])
                sem_var.set(r[4])
                year_var.set(r[5])
                phon_var.set(r[6])
                total_var.set(r[7])
                dep_var.set(r[8])
                due_var.set(r[9])

            def delete():
                if (s_name_entry.get() == ""):
                    tmsg.showinfo("Status", "Name is compulsary")
                else:
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("delete from fee where s_name='" + s_name_var.get() + "'")
                    cursor.execute("commit")
                    tmsg.showinfo("Delete Status", "Deleted Successfully")
                    show()
                    clear()
                    con.close()

            f2 = Frame(rt, bd=5, width=1050, height=560, relief=RAISED)
            fa= Frame(f2 ,bd=5, width=380, height=550, relief=RAISED)
            Label(fa,text="MANAGE FEES DETAILS", font=("lucida", 14, "bold")).place(x=60, y=6)
            erp = Label(fa, text="ERP ID", font=("lucida", 10, "bold"))
            erp.place(x=30, y=65)
            s_name = Label(fa, text="Student Name", font=("lucida", 10, "bold"))
            s_name.place(x=30, y=105)
            roll_no = Label(fa, text="Roll Number", font=("lucida", 10, "bold"))
            roll_no.place(x=30, y=145)
            fath = Label(fa, text="Father's name", font=("lucida", 10, "bold"))
            fath.place(x=30, y=180)
            sem = Label(fa, text="Semester", font=("lucida", 10, "bold"))
            sem.place(x=30, y=215)
            year = Label(fa, text="Year", font=("lucida", 10, "bold"))
            year.place(x=30, y=255)
            phon = Label(fa, text="Phone No.", font=("lucida", 10, "bold"))
            phon.place(x=30, y=295)
            total = Label(fa, text="Total fees", font=("lucida", 10, "bold"))
            total.place(x=30, y=335)
            dep = Label(fa, text="Deposited Amount", font=("lucida", 10, "bold"))
            dep.place(x=30, y=375)
            due = Label(fa, text="Due Amount", font=("lucida", 10, "bold"))
            due.place(x=30, y=415)


            erp_var = StringVar()
            s_name_var = StringVar()
            rol_var = StringVar()
            fath_var = StringVar()
            sem_var = StringVar()
            year_var = StringVar()
            phon_var = StringVar()
            total_var = StringVar()
            dep_var = StringVar()
            due_var = StringVar()
            search_by = StringVar()
            search_txt = StringVar()

            erp_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=erp_var)
            erp_entry.place(x=170, y=65)
            s_name_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=s_name_var)
            s_name_entry.place(x=170, y=105)
            rol_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=rol_var)
            rol_entry.place(x=170, y=145)
            fath_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=fath_var)
            fath_entry.place(x=170, y=180)
            sem_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=sem_var)
            sem_entry.place(x=170, y=215)
            year_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=year_var)
            year_entry.place(x=170, y=255)
            phon_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=phon_var)
            phon_entry.place(x=170, y=295)
            total_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=total_var)
            total_entry.place(x=170, y=335)
            dep_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=dep_var)
            dep_entry.place(x=170, y=375)
            due_entry = Entry(fa, bd=3, font=("lucida", 10, "bold"), textvariable=due_var)
            due_entry.place(x=170, y=415)

            fa.place(x=0,y=0)

            fc=Frame(f2,bd=5, width=150, height=550, relief=RAISED)
            Button(fc, text="ADD", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=add).place(x=15, y=25)
            Button(fc, text="UPDATE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   ).place(x=15, y=85)
            Button(fc, text="DELETE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=delete).place(x=15, y=145)
            Button(fc, text="CLEAR", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=clear).place(x=15, y=205)
            Button(fc, text="SEARCH", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   ).place(x=15, y=265)
            Button(fc, text="SHOW ALL", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=show).place(x=15, y=325)
            Button(fc, text="EXIT", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=quit).place(x=15, y=385)

            fd = Frame(f2, bd=5, width=510, height=550, relief=RAISED)

            s = Label(fd, text="SEARCH BY", font=("lucida", 12))
            s.place(x=0, y=10)
            s_combo = ttk.Combobox(fd, textvariable=search_by, font=("lucida", 12), width=15)
            s_combo['values'] = ("Student_Name")
            s_combo.place(x=120, y=10)

            s_entry = Entry(fd, textvariable=search_txt, font=("lucida", 12), width=20)
            s_entry.place(x=290, y=10)


            fe = Frame(fd, bd=5, relief=RAISED)
            scroll_x = Scrollbar(fe, orient=HORIZONTAL)
            scroll_y = Scrollbar(fe, orient=VERTICAL)
            table = ttk.Treeview(fe, columns=(
                "erp", "s_name", "rol", "fath", "sem", "year", "phon", "total", "dep", "due"),
                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=table.xview)
            scroll_y.config(command=table.yview)
            table.heading("erp", text="ERP ID")
            table.heading("s_name", text="Student Name")
            table.heading("rol", text="Roll Number")
            table.heading("fath", text="Father's Name")
            table.heading("sem", text="Semester")
            table.heading("year", text="Year")
            table.heading("phon", text="Phone Number")
            table.heading("total", text="Total Amount")
            table.heading("dep", text="Deposited Amount")
            table.heading("due", text="Due Amount")
            table['show'] = 'headings'
            table.column("erp", width=130)
            table.column("s_name", width=130)
            table.column("rol", width=130)
            table.column("fath", width=130)
            table.column("sem", width=130)
            table.column("year", width=130)
            table.column("phon", width=130)
            table.column("total", width=130)
            table.column("dep", width=130)
            table.column("due", width=130)
            table.pack(fill=BOTH, expand=True)
            table.bind('<ButtonRelease-1>', get_cursor)
            show()
            fe.place(x=0, y=50, width=500, height=490)
            fd.place(x=530,y=0)
            fc.place(x=380,y=0)
            f2.place(x=220, y=80)


        def staff():
            def add():
                if Ename_entry.get() == "" or EID_entry.get() == "" or email1_entry.get() == "" or birth1_entry.get() == "" or phone1_entry.get() == "" or gender1_entry.get() == "" or salary_entry.get() == "" or age_entry.get() == "" or desig_entry.get() == "" or doj_entry.get() == "":
                    tmsg.showinfo("Insert status", "Please fill all fields")
                else:
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("insert into emp values('" + Ename_entry.get() + "','" + EID_entry.get() + "','" + email1_entry.get() + "','" + birth1_entry.get() + "','" + phone1_entry.get() + "','" + gender1_entry.get() + "', '" + salary_entry.get() + "' , '" + age_entry.get() + "','" + desig_entry.get() + "','" + doj_entry.get() + "')")
                    cursor.execute("commit")
                    tmsg.showinfo("Insert Status", "Inserted Successfully")
                    show()
                    clear()
                    con.close()

            def clear():
                Ename_entry.delete(0, END)
                EID_entry.delete(0, END)
                email1_entry.delete(0, END)
                birth1_entry.delete(0, END)
                phone1_entry.delete(0, END)
                gender1_entry.delete(0, END)
                salary_entry.delete(0, END)
                age_entry.delete(0, END)
                desig_entry.delete(0, END)
                doj_entry.delete(0, END)
                s_entry.delete(0, END)
                s_combo.delete(0, END)

            def show():
                con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                cursor = con.cursor()
                cursor.execute("select * from emp")
                rows = cursor.fetchall()
                if len(rows)!= 0:
                    table.delete(*table.get_children())
                    for row in rows:
                        table.insert('', END, values=row)
                    cursor.execute("commit")
                con.close()

            def get_cursor(event):
                cur1 = table.focus()
                content = table.item(cur1)
                r = content['values']
                Ename_var.set(r[0])
                EID_var.set(r[1])
                email1_var.set(r[2])
                birth1_var.set(r[3])
                phone1_var.set(r[4])
                gender1_var.set(r[5])
                salary_var.set(r[6])
                age_var.set(r[7])
                desig_var.set(r[8])
                doj_var.set(r[9])


            def update():
                if Ename_entry.get() == "" or EID_entry.get() == "" or email1_entry.get() == "" or birth1_entry.get() == "" or phone1_entry.get() == "" or gender1_entry.get() == "" or salary_entry.get() == "" or age_entry.get() == "" or desig_entry.get() == "" or doj_entry.get() == "":
                    tmsg.showinfo("Update status", "Please fill all fields")
                else:
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("update emp set Email1=%s  where Ename =%s",(email1_var.get(), Ename_var.get()))
                    cursor.execute("commit")
                    tmsg.showinfo("Update Status", "Updated Successfully")
                    show()
                    clear()
                    con.close()

            def delete():
                if (Ename_entry.get()== ""):
                    tmsg.showinfo("Status", "Name is compulsary")
                else:
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("delete from emp where EID='" + EID_var.get() + "'")
                    cursor.execute("commit")
                    tmsg.showinfo("Delete Status", "Deleted Successfully")
                    show()
                    clear()
                    con.close()

            def search_data():
                con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                cursor = con.cursor()
                cursor.execute("select * from emp where " + search_by1.get() + " LIKE '%" + search_txt1.get() + "%'")
                rows = cursor.fetchall()
                if len(rows)!= 0:
                    table.delete(*table.get_children())
                    for row in rows:
                        table.insert('', END, values=row)
                    con.commit()
                con.close()


            f3=Frame(rt, bd=5, width=1050, height=560, relief=RAISED)
            f9=Frame(f3,bd=5, width=1040, height=260, relief=RAISED)
            Label(f9, text="MANAGE EMPLOYEE DETAILS", font=("lucida", 14, "bold")).place(x=40, y=6)
            Ename = Label(f9, text="Employee Name", font=("lucida", 10, "bold"))
            Ename.place(x=10, y=55)
            EID = Label(f9, text="Employee ID", font=("lucida", 10, "bold"))
            EID.place(x=10, y=95)
            Email1 = Label(f9, text="Email", font=("lucida", 10, "bold"))
            Email1.place(x=10, y=135)
            birth1 = Label(f9, text="Date Of Birth", font=("lucida", 10, "bold"))
            birth1.place(x=10, y=170)
            phone1 = Label(f9, text="Phone No.", font=("lucida", 10, "bold"))
            phone1.place(x=10, y=205)
            gender1 = Label(f9, text="Gender", font=("lucida", 10, "bold"))
            gender1.place(x=300, y=55)
            salary = Label(f9, text="Salary", font=("lucida", 10, "bold"))
            salary.place(x=300, y=95)
            age = Label(f9, text="Age", font=("lucida", 10, "bold"))
            age.place(x=300, y=135)
            desig= Label(f9, text="Designation", font=("lucida", 10, "bold"))
            desig.place(x=300, y=170)
            doj = Label(f9, text="Date Of Joining", font=("lucida", 10, "bold"))
            doj.place(x=300, y=205)

            Ename_var = StringVar()
            EID_var = StringVar()
            email1_var = StringVar()
            birth1_var = StringVar()
            phone1_var = StringVar()
            gender1_var = StringVar()
            salary_var = StringVar()
            age_var = StringVar()
            desig_var = StringVar()
            doj_var = StringVar()
            search_by1 = StringVar()
            search_txt1 = StringVar()


            Ename_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=Ename_var)
            Ename_entry.place(x=130, y=55)
            EID_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=EID_var)
            EID_entry.place(x=130, y=95)
            email1_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=email1_var)
            email1_entry.place(x=130, y=135)
            birth1_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=birth1_var)
            birth1_entry.place(x=130, y=170)
            phone1_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=phone1_var)
            phone1_entry.place(x=130, y=205)
            gender1_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=gender1_var)
            gender1_entry.place(x=420, y=55)
            salary_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=salary_var)
            salary_entry.place(x=420, y=95)
            age_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=age_var)
            age_entry.place(x=420, y=135)
            desig_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=desig_var)
            desig_entry.place(x=420, y=170)
            doj_entry = Entry(f9, bd=3, font=("lucida", 10, "bold"), textvariable=doj_var)
            doj_entry.place(x=420, y=205)

            Button(f9, text="ADD", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=add).place(x=900, y=25)
            Button(f9, text="UPDATE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=update).place(x=900, y=75)
            Button(f9, text="DELETE", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=delete).place(x=900, y=125)
            Button(f9, text="CLEAR", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                  command=clear).place(x=900, y=175)
            f9.place(x=0, y=0)


            f10 = Frame(f3,bd=5, width=1040, height=290, relief=RAISED)
            s = Label(f10, text="SEARCH BY", font=("lucida", 12))
            s.place(x=0, y=10)
            s_combo = ttk.Combobox(f10, textvariable=search_by1, font=("lucida", 12), width=19)
            s_combo['values'] = ("Employee_Name")
            s_combo.place(x=110, y=10)

            s_entry = Entry(f10, textvariable=search_txt1, font=("lucida", 12), width=29)
            s_entry.place(x=330, y=10)

            Button(f10, text="SEARCH", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=search_data).place(x=640, y=5)
            Button(f10, text="SHOW ALL", width=11, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=show).place(x=770, y=5)
            Button(f10, text="EXIT", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                   command=quit).place(x=910, y=5)

            fb=Frame(f10,bd=5, relief=RAISED)
            scroll_x = Scrollbar(fb, orient=HORIZONTAL)
            scroll_y = Scrollbar(fb, orient=VERTICAL)
            table = ttk.Treeview(fb, columns=(
                "Ename", "EID", "email1", "birth1", "phone1", "gender1", "salary", "age", "desig", "DOJ"),
                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=table.xview)
            scroll_y.config(command=table.yview)
            table.heading("Ename", text="Employee Name")
            table.heading("EID", text="Employee ID")
            table.heading("email1", text="Email")
            table.heading("birth1", text="Date Of Birth")
            table.heading("phone1", text="Phone Number")
            table.heading("gender1", text="Gender")
            table.heading("salary", text="Salary")
            table.heading("age", text="Age")
            table.heading("desig", text="Designation")
            table.heading("DOJ", text="Date Of Joining")
            table['show'] = 'headings'
            table.column("Ename", width=100)
            table.column("EID", width=100)
            table.column("email1", width=100)
            table.column("birth1", width=100)
            table.column("phone1", width=100)
            table.column("gender1", width=100)
            table.column("salary", width=100)
            table.column("age", width=100)
            table.column("desig", width=100)
            table.column("DOJ", width=100)
            table.pack(fill=BOTH, expand=True)
            table.bind('<ButtonRelease-1>', get_cursor)
            show()
            fb.place(x=0,y=50, width=1030, height=230)
            f10.place(x=0, y=260)
            f3.place(x=220,y=80)

        def exam():
            def btech():
                def total():
                    try:
                        a1 = int(f_entry.get())
                    except:
                        a1 = 0
                    try:
                        b1 = int(d_entry.get())
                    except:
                        b1 = 0
                    try:
                        c1 = int(m_entry.get())
                    except:
                        c1 = 0
                    try:
                        d1 = int(o_entry.get())
                    except:
                        d1 = 0
                    try:
                        e1 = int(p_entry.get())
                    except:
                        e1 = 0
                    try:
                        f1 = int(h_entry.get())
                    except:
                        f1 = 0
                    try:
                        g1 = int(j_entry.get())
                    except:
                        g1 = 0

                    total_marks=a1+b1+c1+d1+e1+f1+g1
                    percent=(total_marks/700)*100

                    if percent>85:
                        gd="A"
                    elif (percent>=70 and percent<=85):
                        gd="B"
                    else:
                        gd="C"

                    if sname_entry.get() == "" or f_entry.get() == "" or d_entry.get() == "" or m_entry.get() == "" or o_entry.get() == "" or p_entry.get() == "" or r_entry.get() == "" or h_entry.get() == "" or j_entry.get() == "":
                        tmsg.showinfo("Insert status", "Please fill all fields")
                    else:
                        text.insert(END, f'\nStudent Name\t\t\t{sname_entry.get()}')
                        text.insert(END, f'\nRoll Number\t\t\t{r_entry.get()}')
                        text.insert(END,f'\n--------------------------------------------------------------------------------------------')
                        text.insert(END, '\n\nSubject\t\t\tMarks Obtained')
                        if f_entry.get() != "":
                            text.insert(END, f'\nFLAT\t\t\t{f_entry.get()}')
                        if d_entry.get() != "":
                            text.insert(END, f'\nDSA\t\t\t{d_entry.get()}')
                        if m_entry.get() != "":
                            text.insert(END, f'\nMathematics\t\t\t{m_entry.get()}')
                        if o_entry.get() != "":
                            text.insert(END, f'\nOperating system\t\t\t{o_entry.get()}')
                        if p_entry.get() != "":
                            text.insert(END, f'\nPYTHON\t\t\t{p_entry.get()}')
                        if h_entry.get() != "":
                            text.insert(END, f'\nHuman Behaviour\t\t\t{h_entry.get()}')
                        if j_entry.get() != "":
                            text.insert(END, f'\nJAVA\t\t\t{j_entry.get()}')

                        text.insert(END, f'\n\nTotal marks obtained :\tRs.{total_marks}\n')
                        text.insert(END, f'\nPercentage :\t{percent}%')
                        text.insert(END, f'\nGrade : {gd}')

                        con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                        cursor = con.cursor()
                        cursor.execute(
                            "insert into btech values('" + sname_entry.get() + "','" + r_entry.get() + "','" + f_entry.get() + "','" + d_entry.get() + "','" + m_entry.get() + "','" + o_entry.get() + "', '" + p_entry.get() + "' , '" + h_entry.get() + "','" + j_entry.get() + "','" + str(total_marks) + "', '" + str(percent) + "','" + gd + "')")
                        cursor.execute("commit")
                        tmsg.showinfo("Insert Status", "Inserted Successfully")
                        show()
                        reset()
                        con.close()

                def reset():
                    sname_entry.delete(0, END)
                    f_entry.delete(0, END)
                    d_entry.delete(0, END)
                    m_entry.delete(0, END)
                    o_entry.delete(0, END)
                    p_entry.delete(0, END)
                    r_entry.delete(0, END)
                    h_entry.delete(0, END)
                    j_entry.delete(0, END)
                    per_entry.delete(0, END)
                    tot_entry.delete(0, END)
                    g_entry.delete(0, END)

                def show():
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("select * from btech")
                    rows = cursor.fetchall()
                    if len(rows)!= 0:
                        table.delete(*table.get_children())
                        for row in rows:
                            table.insert('', END, values=row)
                        cursor.execute("commit")
                    con.close()

                def get_cursor(event):
                    cur = table.focus()
                    content = table.item(cur)
                    r = content['values']
                    sname_var.set(r[0])
                    f_var.set(r[2])
                    d_var.set(r[3])
                    m_var.set(r[4])
                    o_var.set(r[5])
                    p_var.set(r[6])
                    r_var.set(r[1])
                    h_var.set(r[7])
                    j_var.set(r[8])
                    tot_var.set(r[9])
                    per_var.set(r[10])
                    g_var.set(r[11])

                def search():
                    con = mysql.connector.connect(host='localhost', user='root', password='', database='employee')
                    cursor = con.cursor()
                    cursor.execute("select * from btech where " + search_by.get() + " LIKE '%" + search_txt.get() + "%'")
                    rows = cursor.fetchall()
                    if len(rows)!= 0:
                        table.delete(*table.get_children())
                        for row in rows:
                            table.insert('', END, values=row)
                        con.commit()
                    con.close()


                fr = Frame(rt, bd=5, width=1050, height=560, relief=RAISED)
                fs = Frame(fr, bd=5, width=640, height=300, relief=RAISED)
                Label(fs, text="BTECH - ALL DEPARTMENT", font=("lucida", 14, "bold")).place(x=10, y=6)
                sname = Label(fs, text="Student Name", font=("lucida", 10, "bold"))
                sname.place(x=10, y=55)
                f = Label(fs, text="FLAT", font=("lucida", 10, "bold"))
                f.place(x=10, y=95)
                d = Label(fs, text="DSA", font=("lucida", 10, "bold"))
                d.place(x=10, y=135)
                m = Label(fs, text="Mathematics", font=("lucida", 10, "bold"))
                m.place(x=10, y=170)
                o= Label(fs, text="Operating System", font=("lucida", 10, "bold"))
                o.place(x=10, y=205)
                p = Label(fs, text="PYTHON", font=("lucida", 10, "bold"))
                p.place(x=10, y=240)
                r = Label(fs, text="Roll Number", font=("lucida", 10, "bold"))
                r.place(x=310, y=55)
                h = Label(fs, text="Human Behaviour", font=("lucida", 10, "bold"))
                h.place(x=310, y=95)
                j = Label(fs, text="JAVA", font=("lucida", 10, "bold"))
                j.place(x=310, y=135)
                tot = Label(fs, text="TOTAL", font=("lucida", 10, "bold"))
                tot.place(x=310, y=170)
                per = Label(fs,text="PERCENTAGE", font=("lucida", 10, "bold"))
                per.place(x=310, y=205)
                g = Label(fs, text="GRADE", font=("lucida", 10, "bold"))
                g.place(x=310, y=240)

                sname_var = StringVar()
                f_var = StringVar()
                d_var = StringVar()
                m_var = StringVar()
                o_var = StringVar()
                p_var = StringVar()
                r_var = StringVar()
                h_var = StringVar()
                j_var = StringVar()
                tot_var = StringVar()
                per_var = StringVar()
                g_var = StringVar()
                search_by = StringVar()
                search_txt = StringVar()

                sname_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=sname_var)
                sname_entry.place(x=130, y=55)
                f_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=f_var)
                f_entry.place(x=130, y=95)
                d_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=d_var)
                d_entry.place(x=130, y=135)
                m_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=m_var)
                m_entry.place(x=130, y=170)
                o_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=o_var)
                o_entry.place(x=130, y=205)
                p_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=p_var)
                p_entry.place(x=130, y=240)
                r_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=r_var)
                r_entry.place(x=430, y=55)
                h_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=h_var)
                h_entry.place(x=430, y=95)
                j_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=j_var)
                j_entry.place(x=430, y=135)
                tot_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=tot_var)
                tot_entry.place(x=430, y=170)
                per_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=per_var)
                per_entry.place(x=430, y=205)
                g_entry = Entry(fs, bd=3, font=("lucida", 10, "bold"), textvariable=g_var)
                g_entry.place(x=430, y=240)
                fs.place(x=0, y=0)

                ft = Frame(fr, bd=5, relief=RAISED)
                Label(ft, text="MARKS ANALYSIS", font=("lucida", 10, "bold")).pack(pady=15)
                scr = Scrollbar(ft, orient=VERTICAL)
                scr.pack(side=RIGHT, fill=Y)
                text = Text(ft, font=("lucida", 10, "bold"), yscrollcommand=scr.set)
                text.pack(fill=BOTH)
                scr.config(command=text.yview)
                ft.place(x=640, y=0, width=400, height=470)

                fu = Frame(fr, bd=5, width=400, height=80, relief=RAISED)
                Button(fu, text="TOTAL", width=11, height=2, font=("lucida", 12), bd=5,command=total).place(x=10, y=7)
                Button(fu, text="UPDATE", width=11, height=2, font=("lucida", 12), bd=5).place(x=135, y=7)
                Button(fu, text="RESET", width=11, height=2, font=("lucida", 12), bd=5, command=reset).place(x=260, y=7)
                fu.place(x=640, y=470)

                fv=Frame(fr,bd=5, width=640, height=250, relief=RAISED)
                s = Label(fv, text="SEARCH BY", font=("lucida", 10))
                s.place(x=0, y=10)
                s_combo = ttk.Combobox(fv, font=("lucida", 12), width=11)
                s_combo['values'] = ("Student_Name")
                s_combo.place(x=90, y=10)

                s_entry = Entry(fv, font=("lucida", 12), width=17)
                s_entry.place(x=220, y=10)

                Button(fv, text="SEARCH", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                      command=search).place(x=390, y=5)
                Button(fv, text="SHOW ALL", width=10, height=1, bg="#e14f45", fg="white", font=("lucida", 12), bd=5,
                       command=show).place(x=510, y=5)


                fw = Frame(fv, bd=5, relief=RAISED)
                scroll_x = Scrollbar(fw, orient=HORIZONTAL)
                scroll_y = Scrollbar(fw, orient=VERTICAL)
                table = ttk.Treeview(fw, columns=(
                    "sname","r", "f", "d", "m", "o", "p", "h", "j", "tot","per","g"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=table.xview)
                scroll_y.config(command=table.yview)
                table.heading("sname", text="Student_Name")
                table.heading("r", text="Roll Number")
                table.heading("f", text="FLAT")
                table.heading("d", text="DSA")
                table.heading("m", text="Mathematics")
                table.heading("o", text="Operating System")
                table.heading("p", text="PYTHON")
                table.heading("h", text="Human behaviour")
                table.heading("j", text="JAVA")
                table.heading("tot", text="TOTAL")
                table.heading("per", text="PERCENTAGE")
                table.heading("g", text="GRADE")

                table['show'] = 'headings'
                table.column("sname", width=100)
                table.column("r", width=100)
                table.column("f", width=100)
                table.column("d", width=100)
                table.column("m", width=100)
                table.column("o", width=100)
                table.column("p", width=100)
                table.column("h", width=100)
                table.column("j", width=100)
                table.column("tot", width=100)
                table.column("per", width=100)
                table.column("g", width=100)
                table.pack(fill=BOTH, expand=True)
                table.bind('<ButtonRelease-1>', get_cursor)
                show()
                fw.place(x=0, y=50, width=620, height=200)
                fv.place(x=0, y=300)
                fr.place(x=220, y=80)



            f2 = Frame(rt, bd=5, width=1050, height=560 ,relief=RAISED)
            Label(f2, text="SELECT YOUR COURSE", font=("calibri", 18, "bold")).place(x=390, y=14)
            Button(f2, text="BTECH", width=16, height=6, fg="blue", font=("calibri", 18), bd=5,
                   command=btech).place(x=10, y=80)
            Button(f2, text="BSC", width=16, height=6, fg="pink", font=("calibri", 18),
                   bd=5,
                   ).place(x=275, y=80)
            Button(f2, text="BBA", width=16, height=6, fg="green", font=("calibri", 18),
                   bd=5,
                   ).place(x=540, y=80)
            Button(f2, text="MBA", width=16, height=6, fg="orange", font=("calibri", 18), bd=5,
                   ).place(x=805, y=80)
            Button(f2, text="BA", width=16, height=6, fg="red", font=("calibri", 18),
                   bd=5,
                   ).place(x=10, y=310)
            f2.place(x=220, y=80)

        f = Frame(rt, bd=5, width=1049, height=80, relief=RAISED)
        Label(f, text="COLLEGE MANAGEMENT SYSTEM", font=("calibri", 24, "bold")).place(x=320, y=14)
        f.place(x=220, y=0)

        f1=Frame(rt, bd=5, width=220, height=640, relief=RAISED)

        Button(f1, text="HOME", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=home).place(x=10, y=100)
        Button(f1, text="STUDENT\nMANAGEMENT", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=student).place(x=10, y=190)
        Button(f1, text="STAFF\nMANAGEMENT", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=staff).place(x=10, y=280)
        Button(f1, text="FEES\nMANGEMENT", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=fees).place(x=10, y=370)
        Button(f1, text="EXAM\nMANAGEMENT", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=exam).place(x=10, y=460)

        Button(f1, text="Exit", width=17, height=2, bg="#e14f45", fg="white", font=("calibri", 15), bd=5,
               command=quit).place(x=10, y=550)

        f1.place(x=0,y=0)

    elif u3 != 'admin' and c3 != '123':
        tmsg.showerror("Invalid", "invalid username and password")
    elif u3 != 'admin' and c3 == '123':
        tmsg.showerror("Invalid", "invalid username")
    elif u3 == 'admin' and c3 != '123':
        tmsg.showerror("Invalid", "invalid password")

    else:
        tmsg.showerror("Invalid", "invalid password")



def clear1():
    name1_entry.delete(0, END)
    pas_entry.delete(0, END)

f5 = Frame(root, bd=5, width=370, height=300, relief=RAISED)
f5.place(x=450,y=140)
head=Label(f5,text="Admin Login",font=("calibri", 26), width=14)
head.place(x=60,y=13)
name1 = Label(f5, text="Username", font=("lucida", 12, "bold")).place(x=30, y=75)
pas = Label(f5, text="Password", font=("lucida", 12, "bold")).place(x=30, y=119)

name1_entry = Entry(f5,bd=3,font=("lucida", 12, "bold"))
name1_entry.place(x=130, y=75)
pas_entry = Entry(f5,bd=3,font=("lucida", 12, "bold"))
pas_entry.place(x=130, y=119)

Button(f5, text="Login", width=10, height=1, bg="#e14f45", fg="white",font=("calibri", 15),bd=3,command=insert_data).place(x=50, y=170)
Button(f5, text="Reset", width=10, height=1, bg="#e14f45", fg="white",font=("calibri", 15),bd=3,command=clear1).place(x=190, y=170)
Button(f5, text="Exit", width=10, height=1, bg="#e14f45", fg="white",font=("calibri", 15),bd=3,command=quit).place(x=140, y=220)


root.mainloop()


