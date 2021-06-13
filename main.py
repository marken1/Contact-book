from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import config_db

# pripojeni databaze
cursor = config_db.db_con.cursor()


# funkce
def update_contact():
    id = t1.get()
    first_name = t2.get()
    last_name = t3.get()
    email = t4.get()
    address = t5.get()
    tel = t6.get()
    if messagebox.askyesno('Aktualizace kontaktu', 'Opravdu chcete aktualizovat kontakt?'):
        query = (
            f'UPDATE contacts SET Jméno="{first_name}", Příjmení="{last_name}", Email="{email}", Adresa="{address}", Telefon="{tel}" WHERE ID="{id}"')
        cursor.execute(query)
        config_db.db_con.commit()
        clear()
    else:
        return True


def add_contact():
    first_name = t2.get()
    last_name = t3.get()
    email = t4.get()
    address = t5.get()
    tel = t6.get()
    if messagebox.askyesno('Přidání kontatku', 'Opravdu chcete přidat kontakt?'):
        query = (
            f'INSERT INTO contacts(ID, Jméno, Příjmení, Email, Adresa, Telefon) VALUES(null, "{first_name}", "{last_name}", "{email}", "{address}", "{tel}")')
        cursor.execute(query)
        config_db.db_con.commit()
        clear()
    else:
        return True


def delete_contact():
    id = t1.get()
    if messagebox.askyesno('Odebraní kontaktu', 'Opravdu chcete odebrat tento kontakt?'):
        query = (f'DELETE FROM contacts WHERE ID = "{id}"')
        cursor.execute(query)
        config_db.db_con.commit()
        clear()
    else:
        return True


def clear():
    query = ('SELECT ID, Jméno, Příjmení, Email, Adresa, Telefon FROM contacts')
    cursor.execute(query)
    result = cursor.fetchall()
    config_db.db_con.commit()
    update(result)


def search():
    q2 = q.get()
    query = (
        f'SELECT ID, Jméno, Příjmení, Email, Adresa, Telefon FROM contacts WHERE Jméno LIKE "%{q2}%" OR Příjmení LIKE "%{q2}%" OR Adresa LIKE "%{q2}%"')
    cursor.execute(query)
    result = cursor.fetchall()
    update(result)


def get_contact(arg1):
    rowid = trv.identify_row(arg1.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])


def update(result):
    trv.delete(*trv.get_children())
    for i in result:
        trv.insert('', 'end', values=i)


def heading(arg1):
    arg1.heading(1, text='ID')
    arg1.heading(2, text='Jméno')
    arg1.heading(3, text='Příjmení')
    arg1.heading(4, text='Email')
    arg1.heading(5, text='Adresa')
    arg1.heading(6, text='Telefon')


window = Tk()
q = StringVar()
t1, t2, t3, t4, t5, t6 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

wrap1 = LabelFrame(window, text='Kontakty')
wrap1.pack(fill='both', expand='yes', padx=20, pady=10)
wrap2 = LabelFrame(window, text='Vyhledat')
wrap2.pack(fill='both', expand='yes', padx=20, pady=10)
wrap3 = LabelFrame(window, text='Kontakt data')
wrap3.pack(fill='both', expand='yes', padx=20, pady=10)
lbl0 = Label(wrap1, text='Pokuc chcete provádět opearce s kontakty, klikněte dvakratá')
lbl0.pack(side=tkinter.BOTTOM, padx=10)

trv = ttk.Treeview(wrap1, columns=(1, 2, 3, 4, 5, 6), show='headings', height=10)
heading(trv)
trv.pack()
trv.bind('<Double 1>', get_contact)

# select vsech kontaktu
query = ('SELECT ID, Jméno, Příjmení, Email, Adresa, Telefon FROM contacts')
cursor.execute(query)
myresult = cursor.fetchall()
update(myresult)

#  Vyhledání
lbl1 = Label(wrap2, text='Vyhledat')
lbl1.pack(side=tkinter.LEFT, padx=10)
e1 = Entry(wrap2, textvariable=q)
e1.pack(side=tkinter.LEFT, padx=6)
bt1 = Button(wrap2, text='Vyhledat', command=search)
bt1.pack(side=tkinter.LEFT, padx=6)
cbtn = Button(wrap2, text='Vyčistit', command=clear)
cbtn.pack(side=tkinter.LEFT, padx=6)

# Data kotaktů
lbl2 = Label(wrap3, text='ID')
lbl2.grid(row=0, column=0, padx=5, pady=3)
e2 = Entry(wrap3, textvariable=t1)
e2.grid(row=0, column=1, padx=5, pady=3)

lbl3 = Label(wrap3, text='Jméno')
lbl3.grid(row=1, column=0, padx=5, pady=3)
e3 = Entry(wrap3, textvariable=t2)
e3.grid(row=1, column=1, padx=5, pady=3)

lbl4 = Label(wrap3, text='Příjmení')
lbl4.grid(row=2, column=0, padx=5, pady=3)
e4 = Entry(wrap3, textvariable=t3)
e4.grid(row=2, column=1, padx=5, pady=3)

lbl5 = Label(wrap3, text='Email')
lbl5.grid(row=3, column=0, padx=5, pady=3)
e5 = Entry(wrap3, textvariable=t4)
e5.grid(row=3, column=1, padx=5, pady=3)

lbl6 = Label(wrap3, text='Adresa')
lbl6.grid(row=4, column=0, padx=5, pady=3)
e6 = Entry(wrap3, textvariable=t5)
e6.grid(row=4, column=1, padx=5, pady=3)

lbl7 = Label(wrap3, text='Telefon')
lbl7.grid(row=5, column=0, padx=5, pady=3)
e7 = Entry(wrap3, textvariable=t6)
e7.grid(row=5, column=1, padx=5, pady=3)

up_btn = Button(wrap3, text='Upravit kontakt', command=update_contact)
up_btn.grid(row=6, column=0, padx=5, pady=3)
add_bt = Button(wrap3, text='Přidat kontakt', command=add_contact)
add_bt.grid(row=6, column=1, padx=5, pady=3)
del_btn = Button(wrap3, text='Odebrat kontakt', command=delete_contact)
del_btn.grid(row=6, column=2, padx=5, pady=3)

window.title('Kontaktní knížka')
window.geometry('1400x700')
window.mainloop()
