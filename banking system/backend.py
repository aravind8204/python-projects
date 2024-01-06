import datetime
import sqlite3
import os

con = sqlite3.connect("user.db")
conn = sqlite3.connect("acc.db")
cursor = con.cursor()
cur = conn.cursor()
con.execute("CREATE TABLE IF NOT EXISTS users (accno VARCHAR(13),name VARCHAR(25),mobile INT(10),email VARCHAR(30),address VARCHAR(100),pin INT(4))")
con.commit()

def new_acc(accno,name,mobile,email,address,pin):
    con = sqlite3.connect("user.db")
    conn = sqlite3.connect("acc.db")
    cursor = con.cursor()
    cur = conn.cursor()
    AC="Acc_"+accno
    string="CREATE TABLE IF NOT EXISTS "+AC+" (id INTEGER PRIMARY KEY AUTOINCREMENT,dat datetime,desc VARCHAR(50),debit INT(10),credit INT(10),balance INT(15) DEFAULT 0)"
    con.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",(accno,name,mobile,email,address,pin))
    conn.execute(string)
    con.commit()
    conn.commit()

def credit(acc=" ",pin=" ",des=" ",cred=" "):
    con = sqlite3.connect("user.db")
    conn = sqlite3.connect("acc.db")
    cursor = con.cursor()
    cur = conn.cursor()
    AC="Acc_"+acc
    cursor.execute("SELECT accno,pin FROM users WHERE accno=?",(acc,))
    rows=cursor.fetchall()
    row=rows[0]
    if(pin==row[1]):
        cursor.execute("SELECT accno,name,email FROM users WHERE accno=?",(acc,))
        detail=cursor.fetchall()
        s1="SELECT balance FROM "+AC+" ORDER BY id DESC"
        cur.execute(s1)
        bal=cur.fetchone()
        balance_credit=bal[0]-cred
        print("Balance Amount: ",balance_credit)
        t=datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        cur.execute("INSERT INTO "+AC+" VALUES(NULL,?,?,?,?,?)",(t,des,0,cred,balance_credit))
        conn.commit()
        return detail
    else:
        print("Incorrect details")

def debit(acc=" ",pin=" ",des=" ",deb=" "):
    con = sqlite3.connect("user.db")
    conn = sqlite3.connect("acc.db")
    cursor = con.cursor()
    cur = conn.cursor()
    AC="Acc_"+acc
    cursor.execute("SELECT accno,pin FROM users WHERE accno=?",(acc,))
    rows=cursor.fetchall()
    row=rows[0]
    if(pin==row[1]):
        cursor.execute("SELECT accno,name,email FROM users WHERE accno=?",(acc,))
        detail=cursor.fetchall()
        s1="SELECT balance FROM "+AC+" ORDER BY id DESC"
        cur.execute(s1)
        bal=cur.fetchone()
        if (bal==None):
            balance_debit=0+deb
            print("Balance Amount: ",balance_debit)
        else:
            balance_debit=bal[0]+deb
            print("Balance Amount: ",balance_debit)
        t=datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        cur.execute("INSERT INTO "+AC+" VALUES(NULL,?,?,?,?,?)",(t,des,deb,0,balance_debit))
        conn.commit()
        return detail
    else:
        print("Incorrect details")

def acc_update(name="",mobile="",email="",addr="",accno=" "):
    con = sqlite3.connect("user.db")
    cursor = con.cursor()
    cursor.execute("UPDATE users SET name=? OR mobile=? OR email=? OR address=? WHERE accno=?",(name,mobile,email,addr,accno))
    con.commit()

def fetch_acno():
    con = sqlite3.connect("user.db")
    conn = sqlite3.connect("acc.db")
    cursor = con.cursor()
    cur = conn.cursor()
    cursor.execute("SELECT accno FROM users")
    row=cursor.fetchall()
    return row

def view(accno=" ",pin=" "):
    AC="Acc_"+accno
    con = sqlite3.connect("user.db")
    cursor = con.cursor()
    conn = sqlite3.connect("acc.db")
    cur = conn.cursor()
    cursor.execute("SELECT name,mobile,email,address FROM users WHERE accno=? AND pin=?",(accno,pin))
    rows=cursor.fetchall()
    cur.execute("SELECT balance FROM "+AC+" ORDER BY id DESC")
    row=cur.fetchone()
    return rows[0],row[0]
#view("9134332777656",1221)
#debit("1881286357",1303,"deposit",500)
#validation("6354744017",4546)
#new_acc("6354741243","chandru",7484674635,"syavysx@gmail.com","dbucibudaibciuhadu",9999)

conn.close()
con.close()