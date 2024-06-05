import tkinter
import tkinter.messagebox
from tkinter import *
import mysql.connector as sqlcon
import random as rd
from tkinter.messagebox import showinfo, showerror
from tkcalendar import DateEntry
from PIL import ImageTk

con = sqlcon.connect(host="localhost", user="root", password="")
cur = con.cursor()
cur = con.cursor(buffered=True)
cur.execute("create database if not exists Hospital")
cur.execute("use Hospital")
cur.execute("create table if not exists data"
            "("
            "user varchar(255),"
            "passw varchar(255))")
cur.execute("create table if not exists appointment"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")
cur.execute("create table if not exists appointment_details"
            "("
            "idno varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")


def show_info():
    showinfo(title="Информация", message="Успешный вход")


def show_error():
    showerror(title="Ошибка", message="Сообщение об ошибке")


def login():
    username = entry_username.get()
    password = entry_password.get()

    cur.execute("SELECT * FROM data WHERE user = %s AND passw = %s", (username, password))
    result = cur.fetchall()

    if result:
        showinfo("Успешный вход", "Вход выполнен успешно!")

        root.destroy()
    else:
        showerror("Ошибка", "Неверное имя пользователя или пароль")


def register():
    username = entry_username.get()
    password = entry_password.get()

    cur.execute("INSERT INTO data (user, passw) VALUES (%s, %s)", (username, password))

    showinfo("Успешная регистрация", "Регистрация выполнена успешно!")


def delet():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            cur.execute("DELETE FROM data  WHERE user=%s and passw=%s", (username, password))

            con.commit()
            showinfo("удаление", "Удаление успешно")
        except tkinter.TclError:
            showerror("Ошибка", "Пользователь с таким именем не существует")
    else:
        showerror("Ошибка", "Заполните все поля")

def quit_tk():

    root.destroy()

    exit()
def disable_event():
    pass


root = Tk()
background_image = ImageTk.PhotoImage(file='log.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.title("Вход и регистрация")
root.geometry("250x250")


label_username = Label(root, text="Имя пользователя:")
label_username.pack()
entry_username = Entry(root)
entry_username.pack()

label_password = Label(root, text="Пароль:")
label_password.pack()
entry_password = Entry(root, show="*")
entry_password.pack()

btn_login = Button(root, text="Войти", command=login)
btn_login.pack()

btn_register = Button(root, text="Зарегистрироваться", command=register)
btn_register.pack()

btn_delete = Button(root, text="Удалить", command=delet)
btn_delete.pack()

btn_close = Button(root, text="Выход", command=quit_tk)
btn_close.pack()



def close_window():
    root.destroy()

root.mainloop()
def entry():
    global e1, e2, e3, e4, e5, e6
    p1 = e1.get()
    p2 = e2.get()
    p3 = e3.get()
    p4 = e4.get()
    p5 = e5.get()
    p6 = e6.get()

    query = 'insert into appointment values("{}", "{}", "{}", "{}", "{}", "{}")'.format(p1, p2, p3, p4, p5, p6)
    con.commit()
    cur.execute(query)

    tkinter.messagebox.showinfo("Готово", "Вы зарегестрированы")


def register():
    global e1, e2, e3, e4, e5, e6
    root1 = Tk()
    label = Label(root1, text="Регистрация", font='arial 15 bold')
    label.pack()
    frame = Frame(root1, height=500, width=300)
    frame.pack()
    l1 = Label(root1, text="Личный номер")
    l1.place(x=10, y=130)
    e1 = tkinter.Entry(root1)
    e1.place(x=100, y=130)
    l2 = Label(root1, text="Имя")
    l2.place(x=10, y=170)
    e2 = tkinter.Entry(root1)
    e2.place(x=100, y=170)
    l3 = Label(root1, text="Возраст")
    l3.place(x=10, y=210)
    e3 = tkinter.Entry(root1)
    e3.place(x=100, y=210)
    l4 = Label(root1, text="Пол М/Ж")
    l4.place(x=10, y=250)
    e4 = tkinter.Entry(root1)
    e4.place(x=100, y=250)
    l5 = Label(root1, text="Телефон")
    l5.place(x=10, y=290)
    e5 = tkinter.Entry(root1)
    e5.place(x=100, y=290)
    l6 = Label(root1, text="Группа крови")
    l6.place(x=10, y=330)
    e6 = tkinter.Entry(root1)
    e6.place(x=100, y=330)
    b1 = Button(root1, text="Зарегистрировать", command=entry)
    b1.place(x=110, y=370)

    root.resizable(False, False)
    root1.mainloop()


def apo_details():
    global x1, x2, h, p1, p2, p3, o, x4, x3
    p1 = x2.get()
    p2 = x3.get()
    p3 = x4.get()
    if int(p1) == 1:
        i = ("Д. Савченко \nКабинет №. 10")
        j = ("Д. Белова \nКабинет №. 11")
        q = (i, j)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nДата:-", p2,
               "\nВремя:-", p3,
               '\nЗапись no:-', o)

        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)

    elif int(p1) == 2:
        i = ("Д. Абрамова \nКабинет №. 16")
        j = ("Д. Ефремова \nКабинет №. 17")
        q = (i, j)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nДата:-", p2,
               "\nВремя:-", p3,
               '\nЗапись №:-', o)
        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)

    elif int(p1) == 3:
        i = ("Д. Олегов \nКабинет №. 12")
        j = ("Д. Димидов \nКабинет №. 13")
        q = (i, j)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nДата:-", p2,
               "\nВремя:-", p3,
               '\nЗапись №:-', o)
        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)

    elif int(p1) == 4:
        i = ("Д. Октанов, \nКабинет №. 18")
        j = ("Д. Леонидов \nКабинет №. 19")
        q = (i, j)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nДата:-", p2,
               "\nВремя:-", p3,
               '\nЗапись №:-', o)
        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)
    elif int(p1) == 5:
        i = ("Д. Решетова \nКабинет №. 14")
        j = ("Д. Боброва \nКабинет №. 15")
        q = (i, j)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nДата:-", p2,
               "\nВремя:-", p3,
               '\nзапись №:-', o)
        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)
    elif int(p1) == 6:
        i = ("Д. Имранов \nКабинет №. 001")
        j = ("Д. Овечкина \nКабинет №. 002")
        k = ("Д. Алясова \nКабинет №. 003")
        l = ("Д. Артемов \nКабинет №. 004")
        q = (i, j, k, l)
        h = rd.choice(q)
        u = (23, 34, 12, 67, 53, 72)
        o = rd.choice(u)
        det = ("Ваша запись:", h,
               "\nдата:-", p2,
               "\nвремя:-", p3,
               '\nзапись №:-', o)
        query = 'replace into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1, h, p2, p3, o)
        cur.execute(query)
        tkinter.messagebox.showinfo("Детали записи", det)
    else:
        tkinter.messagebox.showwarning('Ошибка', 'Введите правильные данные')


#  For appointment
def get_apoint():
    global x1, x2, x3, x4
    p1 = x1.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))
    dat = cur.fetchall()
    a = []
    for i in dat:
        a.append(i)
    if len(a) == 0:
        tkinter.messagebox.showwarning("Ошибка", "Информация не найдена!!!")
    else:
        root3 = Tk()
        label = Label(root3, text="Запись", font='arial 25 bold')
        label.pack()
        frame = Frame(root3, height=500, width=350)
        frame.pack()
        if i[3] == 'M' or i[3] == 'm':
            x = ""
            name2 = Label(root3, text=i[1])
            name2.place(x=80, y=80)
        else:
            x = ""
            name2 = Label(root3, text=i[1])
            name2.place(x=80, y=80)
        for i in dat:
            name = Label(root3, text='Имя:')
            name.place(x=50, y=80)
            name1 = Label(root3, text=x)
            name1.place(x=120, y=80)
            age = Label(root3, text='Возраст:-')
            age.place(x=50, y=100)
            age1 = Label(root3, text=i[2])
            age1.place(x=100, y=100)
            phone = Label(root3, text='Номер:-')
            phone.place(x=50, y=120)
            phone1 = Label(root3, text=i[4])
            phone1.place(x=100, y=120)
            bg = Label(root3, text='Группа крови:')
            bg.place(x=50, y=140)
            bg1 = Label(root3, text=i[5])
            bg1.place(x=150, y=140)

        L = Label(root3, text='Отделения')
        L.place(x=50, y=220)
        L1 = Label(root3, text="1.Хирург ")
        L1.place(x=50, y=250)
        L2 = Label(root3, text='2.Терапевт')
        L2.place(x=50, y=270)
        L3 = Label(root3, text='3.Нефролог')
        L3.place(x=50, y=290)
        L4 = Label(root3, text='4.Невролог')
        L4.place(x=50, y=310)
        L5 = Label(root3, text='5.Гинеколог')
        L5.place(x=50, y=330)
        L6 = Label(root3, text='6.Рентген')
        L6.place(x=50, y=350)
        L7 = Label(root3, text='№ Отделения')
        L7.place(x=50, y=370)
        x2 = tkinter.Entry(root3)
        x2.place(x=130, y=370)

        L7 = Label(root3, text=('введите дату')).place(x=50, y=400)
        x3 = DateEntry(root3, date_pattern='yyyy-mm-dd')
        x3.place(x=130, y=400)

        L8 = Label(root3, text=('Время')).place(x=50, y=430)
        x4 = tkinter.Entry(root3)
        x4.place(x=130, y=430)

        B1 = Button(root3, text='Принять', command=apo_details)
        B1.place(x=120, y=480)
        root3.resizable(False, False)
        root3.mainloop()


def get_del():
    global x1
    p1 = x1.get()
    cur.execute('DELETE from appointment where idno=(%s)', (p1,))
    dat = cur.fetchone()
    if dat:
        tkinter.messagebox.showinfo('Удаление', 'Удаление успешно')
    else:
        tkinter.messagebox.showinfo('Удаление', 'Удаление успешно')


def delet_user():
    global x1
    root8 = Tk()
    label = Label(root8, text="Удаление", font='arial 25 bold')
    label.pack()
    frame = Frame(root8, height=250, width=250)
    frame.pack()
    l1 = Label(root8, text="Личный номер.")
    l1.place(x=10, y=130)
    x1 = tkinter.Entry(root8)
    x1.place(x=100, y=130)
    b1 = Button(root8, text='Принять', command=get_del)
    b1.place(x=100, y=160)
    root8.resizable(False, False)
    root8.mainloop()
def apoint():
    global x1
    root2 = Tk()
    label = Label(root2, text="Запись", font='arial 25 bold')
    label.pack()
    frame = Frame(root2, height=250, width=250)
    frame.pack()
    l1 = Label(root2, text="Личный номер.")
    l1.place(x=10, y=130)
    x1 = tkinter.Entry(root2)
    x1.place(x=100, y=130)
    b1 = Button(root2, text='Принять', command=get_apoint)
    b1.place(x=100, y=160)
    root2.resizable(False, False)
    root2.mainloop()


def lst_doc():
    root4 = Tk()

    l = ["Д. Савченко", "Д. Белова", "Д. Абрамова", "Д. Ефремова", "Д. Олегов", "Д. Димидов", "Д. Октанов",
         "Д. Леонидов",
         "Д. Решетова", "Д. Боброва", 'Д. Имранов', 'Д. Овечкина',
         'Д. Алясова', 'Д. Артемов']
    m = ["Хирург", "Хирург", "Терапевт", "Терапевт", "Нефролог", "Нефролог",
         "Невролог", "Невролог", "Гинеколог",
         "Гинеколог", 'Рентген', 'Рентген', 'Узи', 'Узи']
    n = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    frame = Frame(root4, height=500, width=500)
    frame.pack()

    l1 = Label(root4, text='Доктора')
    l1.place(x=20, y=10)
    count = 20
    for i in l:
        count = count + 20
        l = Label(root4, text=i)
        l.place(x=20, y=count)

    l2 = Label(root4, text='Отдел')
    l2.place(x=140, y=10)
    count1 = 20
    for i in m:
        count1 = count1 + 20
        l3 = Label(root4, text=i)
        l3.place(x=140, y=count1)

    l4 = Label(root4, text='№ кабинета')
    l4.place(x=260, y=10)
    count2 = 20
    for i in n:
        count2 = count2 + 20
        l5 = Label(root4, text=i)
        l5.place(x=260, y=count2)
    root.resizable(False, False)
    root4.mainloop()


def ser_avail():
    root5 = Tk()
    frame = Frame(root5, height=500, width=500)
    frame.pack()
    l1 = Label(root5, text='Доступные услуги')
    l1.place(x=20, y=10)
    f = ["Ультразвук", "Рентген", "Флюрография", "МРТ", "Анализ крови", "Диагностика", "ЭКГ", "Кровь на химию",
         "Лаборатория"]
    count1 = 20
    for i in f:
        count1 = count1 + 20
        l3 = Label(root5, text=i)
        l3.place(x=20, y=count1)
    l2 = Label(root5, text='Кабинет №')
    l2.place(x=140, y=10)
    g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count2 = 20
    for i in g:
        count2 = count2 + 20
        l4 = Label(root5, text=i)
        l4.place(x=140, y=count2)
    l5 = Label(root5, text='Чтобы записаться на услугу обратитесь к администратору')
    l5.place(x=20, y=240)
    root5.resizable(False, False)
    root5.mainloop()


def modify():
    global x3, x4, choice, new, x5, root6
    p1 = x3.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))

    dat = cur.fetchall()
    a = []
    for i in dat:
        a.append(i)
    if len(a) == 0:
        tkinter.messagebox.showwarning("Ошибка", "Данные не найдены!!")
    else:
        root6 = Tk()
        frame = Frame(root6, height=500, width=500)
        frame.pack()
        l1 = Label(root6, text='Изменение данных', font="arial 15 bold")
        l1.place(x=75, y=10)
        l2 = Label(root6, text='Что вы хотите изменить')
        l2.place(x=50, y=200)
        l4 = Label(root6, text='1.Возраст')
        l4.place(x=50, y=240)
        l6 = Label(root6, text='2.Номер тел.')
        l6.place(x=50, y=260)
        l7 = Label(root6, text='3.Группа крови')
        l7.place(x=50, y=280)
        x2 = Label(root6, text='Номер:')
        x2.place(x=50, y=330)
        x4 = tkinter.Entry(root6)
        choice = x4.get()
        x4.place(x=100, y=330)
        for i in dat:
            name = Label(root6, text='Имя:')
            name.place(x=50, y=80)
            name1 = Label(root6, text=i[1])
            name1.place(x=150, y=80)
            age = Label(root6, text='Возраст:')
            age.place(x=50, y=100)
            age1 = Label(root6, text=i[2])
            age1.place(x=150, y=100)
            gen = Label(root6, text='Пол:')
            gen.place(x=50, y=120)
            gen1 = Label(root6, text=i[3])
            gen1.place(x=150, y=120)
            pho = Label(root6, text='Номер:')
            pho.place(x=50, y=140)
            pho1 = Label(root6, text=i[4])
            pho1.place(x=150, y=140)
            bg = Label(root6, text='Группа крови:')
            bg.place(x=50, y=160)
            bg1 = Label(root6, text=i[5])
            bg1.place(x=150, y=160)
        b = Button(root6, text='Принять', command=do_modify)
        b.place(x=50, y=400)
        L1 = Label(root6, text='Старые данные')
        L1.place(x=50, y=50)
        L2 = Label(root6, text='Новые данные')
        L2.place(x=50, y=360)
        x5 = tkinter.Entry(root6)
        new = x5.get()
        x5.place(x=160, y=360)

        root6.resizable(False, False)
        root6.mainloop()


def do_modify():
    global ad, x3, x4, x5
    ad = x3.get()
    choice = x4.get()
    new = x5.get()
    if choice == '1':
        cur.execute('UPDATE appointment SET age={} WHERE idno={}'.format(new, ad))
    elif choice == '2':
        cur.execute('UPDATE appointment SET phone={} WHERE idno={}'.format(new, ad))
    elif choice == '3':
        cur.execute('UPDATE appointment SET bg={} WHERE idno={}'.format(new, ad))
    else:
        pass
    root6.destroy()
    tkinter.messagebox.showinfo("Готово", "Данные обновлены")


choice = None
new = None
ad = None


def mod_sub():
    global x3, ad
    root7 = Tk()
    label = Label(root7, text="Обновление", font='arial 25 bold')
    label.pack()
    frame = Frame(root7, height=200, width=200)
    frame.pack()
    l1 = Label(root7, text="Личный номер.")
    l1.place(x=10, y=130)
    x3 = tkinter.Entry(root7)
    x3.place(x=100, y=130)
    ad = x3.get()
    b1 = Button(root7, text='Принять', command=modify)
    b1.place(x=100, y=160)
    root7.resizable(False, False)
    root7.mainloop()


def search_data():
    global x3, ad
    root7 = Tk()
    label = Label(root7, text="Поиск данных", font='arial 25 bold')
    label.pack()
    frame = Frame(root7, height=200, width=200)
    frame.pack()
    l1 = Label(root7, text="Личный номер.")
    l1.place(x=10, y=130)
    x3 = tkinter.Entry(root7)
    x3.place(x=100, y=130)
    ad = x3.get()
    b1 = Button(root7, text='Принять', command=view_data)
    b1.place(x=100, y=160)
    root7.resizable(False, False)
    root7.mainloop()


def view_data():
    global p1
    p1 = x3.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))

    dat = cur.fetchall()
    print(dat)
    a = []
    for i in dat:
        a.append(i)
    if len(a) == 0:
        tkinter.messagebox.showwarning("Ошибка", "Данные не найдены!!")
    else:
        det = a
        tkinter.messagebox.showinfo("Подробности записи", det)


root = Tk()
root.geometry('1040x800')
background_image = ImageTk.PhotoImage(file='bg1.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
image4 = ImageTk.PhotoImage(file="search.png")
image1 = ImageTk.PhotoImage(file="exit.png")
image2 = ImageTk.PhotoImage(file="list.png")
image3 = ImageTk.PhotoImage(file="reg.png")
image5 = ImageTk.PhotoImage(file="usl.png")
image6 = ImageTk.PhotoImage(file="zapis.png")
image7 = ImageTk.PhotoImage(file="change.png")
image8 = ImageTk.PhotoImage(file="del.png")
b1 = Button(image=image3, command=register)
b2 = Button(image=image6, command=apoint)
b3 = Button(image=image2, command=lst_doc)
b4 = Button(image=image5, command=ser_avail)
b7 = Button(image=image4, command=search_data)
b5 = Button(image=image7, command=mod_sub)
b6 = Button(image=image1, command=quit_tk)
b8 = Button(image=image8, command=delet_user)
b1.place(x=25, y=120)
b3.place(x=110, y=10)
b4.place(x=390, y=10)
b7.place(x=970, y=10)
b2.place(x=25, y=185)
b5.place(x=700, y=10)
b6.place(x=950, y=720)
b8.place(x=25, y=720)

root.resizable(False, False)
root.mainloop()
