# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('my.db')
#Создание курсора
c = conn.cursor()

'''
c.execute("CREATE TABLE if not exists users1 (id INTEGER PRIMARY KEY ASC AUTOINCREMENT UNIQUE,name varchar, password varchar)")
c.execute("INSERT INTO users1 (name,password) VALUES ('admin','123')")
conn.commit()
'''
c.execute('SELECT * FROM users1')
result = c.fetchall()
m=[]
for item in result:
    print(item)
    m.append(item)

'''
rowcol=input("введите номер строки")
c.execute("UPDATE users1 SET name = 'ad' WHERE id='%s'"%(rowcol));
conn.commit()

c.execute('SELECT * FROM users1')

result = c.fetchall()
for item in result:
    print(item)
    
'''

'''
c.execute('SELECT * FROM users1')
row = c.fetchone()
#выводим список пользователей в цикле
while row is not None:
   print("id:"+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
   row = c.fetchone()
'''

'''

#Функция занесения пользователя в базу
def add_user(username,userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()





#Создание таблицы
c.execute("CREATE TABLE if not exists users (id integer auto_increment primary key ASC,name varchar, password varchar)")
#Наполнение таблицы
c.execute("INSERT INTO users (name,password) VALUES ('admin','123')")
#Подтверждение отправки данных в базу
conn.commit()


#Вводим данные
name = input("Введите Логин\n")
passwd = input("Введите Пароль\n")
print('\n')


# Показываем результат.
result = c.fetchall()
for item in result:
    print(item)

#Делаем запрос в базу
print("Список пользователей:\n")
c.execute('SELECT * FROM users')
row = c.fetchone()
#выводим список пользователей в цикле
while row is not None:
   print("id:"+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
   row = c.fetchone()

'''

#Завершение соединения
c.close()
conn.close()


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Tk
'''  
  
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
  
'''

def edit(event):
   # x = table.get_children()
    print(table.item(table.selection()[0])['values'][0])
    table.item(table.selection(), text="", values=("1", "2","3"))
  
root = tk.Tk()
headings=('id', 'name', 'pass')
#table = Table(root, headings=('id', 'name', 'pass'), rows=m)


table = ttk.Treeview(root, show="headings", selectmode="browse")
table["columns"]=headings
table["displaycolumns"]=headings
  
for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

  
for row in m:
            table.insert('', tk.END, values=tuple(row))

 
scrolltable = tk.Scrollbar(root, command=table.yview)
table.configure(yscrollcommand=scrolltable.set)
scrolltable.pack(side=tk.RIGHT, fill=tk.Y)

table.pack(expand=tk.YES, fill=tk.BOTH)
  


table.pack(expand=tk.YES, fill=tk.BOTH)
table.bind("<Double-Button-1>",edit)

root.mainloop()


