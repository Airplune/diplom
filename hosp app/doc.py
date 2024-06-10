import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import mysql.connector as sqlcon

con = sqlcon.connect(host="localhost", user="root", password="", database="hospital")
cur = con.cursor()
cur = con.cursor(buffered=True)


def insert_data():
    fio = entry_fio.get()
    Phone = entry_Phone.get()
    Kval = entry_Kval.get()
    sql = "INSERT INTO doctors (fio, Phone, Kval) VALUES (%s, %s, %s)"
    val = (fio, Phone, Kval)
    cur.execute(sql, val)
    con.commit()
    display_data()


def update_data():
    fio = entry_fio.get()
    Kval = entry_Kval.get()
    sql = "UPDATE doctors SET fio = %s WHERE fio = %s"
    val = (Kval, fio)
    cur.execute(sql, val)
    con.commit()
    display_data()


def delete_data():
    fio = entry_fio.get()
    sql = "DELETE FROM doctors WHERE fio = %s"
    val = (fio,)
    cur.execute(sql, val)
    con.commit()
    display_data()


def display_data():
    cur.execute("SELECT * FROM doctors")
    result = cur.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    for row in result:
        tree.insert("", "end", values=row)


root = Tk()
root.title("регистрация сотрудника")
root.geometry("1100x600")
background_image = ImageTk.PhotoImage(file='bg2.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_fio = Label(root, text="ФИО:")
label_fio.grid(row=0, column=0)

entry_fio = Entry(root)
entry_fio.grid(row=0, column=1)

label_Phone = Label(root, text="Телефон:")
label_Phone.grid(row=1, column=0)

entry_Phone = Entry(root)
entry_Phone.grid(row=1, column=1)

label_Kval = Label(root, text="Квалификация:")
label_Kval.grid(row=2, column=0)

entry_Kval = Entry(root)
entry_Kval.grid(row=2, column=1)

btn_insert = Button(root, text="Добавить", command=insert_data)
btn_insert.grid(row=3, column=0)

btn_update = Button(root, text="Изменить", command=update_data)
btn_update.grid(row=3, column=1)

btn_delete = Button(root, text="Удалить", command=delete_data)
btn_delete.grid(row=3, column=2)

tree = ttk.Treeview(root, columns=("ID", "ФИО", "Номер", "Спец."))
tree.heading("ID", text="ID")
tree.heading("ФИО", text="ФИО")
tree.heading("Номер", text="Номер")
tree.heading("Спец.", text="Спец.")
tree.grid(row=4, column=0, columnspan=3)

display_data()
root.mainloop()
