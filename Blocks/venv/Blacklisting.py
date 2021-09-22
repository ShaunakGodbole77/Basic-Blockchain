import sqlite3
import Registration
import TransactionDatabase

def BlacklistedData():
    conn = sqlite3.connect("Blacklist.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE Blacklist(
                 Email text
                 )""")

    conn.commit()
    conn.close()


def blacklist(message):
    conn = sqlite3.connect("Blacklist.db")
    c = conn.cursor()
    listtoadd = [message]
    c.execute("INSERT INTO Blacklist VALUES (?)",listtoadd)
    conn.commit()
    conn.close()
    Registration.reportGeneration(message)



def checkBlacklist(message):
    conn = sqlite3.connect("Blacklist.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Blacklist WHERE Email = '{}'".format(message))
    check = c.fetchall()
    conn.commit()
    conn.close()
    print(check)
    if len(check)>0:
        return True
    else: return False



def trace(email):
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM TransactionsInfo Where Sender = '{}'".format(email))
    adder = c.fetchall()
    conn.commit()
    conn.close()
    if len(adder)>0:
        listTocheck = []
        for i in adder:
            j = list(i)
            if j in listTocheck:
                pass
            else:
                pre_exists = checkBlacklist(j[0])
                if pre_exists == True:
                    break
                else:
                    blacklist(j[0])
                    trace(j[1])
                    listTocheck.append(j)
    else:
        trace2(email)

def trace2(email):
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM TransactionsInfo Where Reciever = '{}'".format(email))
    adder = c.fetchall()
    conn.commit()
    conn.close()
    listTocheck = []
    for i in adder:
        j = list(i)
        if j in listTocheck:
            pass
        else:
            pre_exists = checkBlacklist(j[1])
            if pre_exists == True:
                break
            else:
                blacklist(j[1])
                listTocheck.append(j)

def display():
    conn = sqlite3.connect("Blacklist.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Blacklist")
    items = c.fetchall()
    print(items)
    conn.commit()
    conn.close()

def delrecord(num):
    conn = sqlite3.connect("Blacklist.db")
    c = conn.cursor()
    c.execute("DELETE from Blacklist WHERE rowid = '{}'".format(num))
    conn.commit()
    conn.execute("VACUUM")
    conn.close()

#BlacklistedData()
#for i in range(4):
 #   delrecord(1)
#checkBlacklist("shivam@gmail.com")
#trace("shivam@gmail.com")
#checkBlacklist("shivam@gmail.com")
#print("------TRACING COMPLETE--------")
#display()
#trace("shaunak@viit.ac.in")
#display()