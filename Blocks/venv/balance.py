import sqlite3
import TransactionDatabase
import datetime
def balance():
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE Balance (
        Name text,
        Balance text,
        Email  text
    )""")
    conn.commit()
    conn.close()


def balancecreate(message):
    msg = message.split('-')
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    c.execute("INSERT INTO Balance VALUES (?,?,?)",msg)
    conn.commit()
    conn.close()
    print("success")

def display():
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    c.execute("SELECT * from Balance")
    data = c.fetchall()

    # from here 
    print("------------------------------------------------BALANCE DATABASE------------------------------------------------")
    print("NAME","\t\t","BALANCE","\t\t","EMAIL")
    print("-------------------------------------------------------------------------------------------------------------------")
    for item in data:
        print(str(item[0]) + "\t\t" + str(item[1]) + "\t" + str(item[2]) + "\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    # till here - changes done by geervani
    # print(data)
    conn.commit()
    conn.close()
    return data

def first(msg):
    msg = msg.split('-')
    msg = msg[0] + "-" + "1000" + "-" + msg[1]
    balancecreate(msg)

def check_balance(name):
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    c.execute("SELECT * from Balance WHERE Email = '{}'".format(name))
    data = c.fetchall()
    # print(data)
    conn.commit()
    conn.close()
    return data[0][1]

def transact(msg):
    message = msg.split()    #message format = payer payervalue payee payeevalue amounttransacted
    value1 = check_balance(message[0])
    value2 = check_balance(message[2])

    if value1 == message[1] and value2 == message[3]:
        value1 = str(float(value1) - float(message[4]))
        value2 = str(float(value2) + float(message[4]))
        updater(message[0],value1)
        updater(message[2],value2)
        print("Transaction successfull")

        # transactionid = random.randinit(0,100)
        TransactionDatabase.CreateTransaction(message[0],message[2],message[4],datetime.datetime.now())
    else: print("Transaction Failed")


def updater(name,value):
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    c.execute("UPDATE Balance SET Balance = ? WHERE Email = ?",(value,name))
    conn.commit()
    conn.close()



def getbalance(emailid):
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    email = str(emailid)
    c.execute("SELECT * from Balance WHERE Email = '{}' ".format(email))
    returndata = c.fetchall()
    conn.commit()
    conn.close()
    return returndata

def Delrecord(num):
    conn = sqlite3.connect("Balances.db")
    c = conn.cursor()
    c.execute("DELETE from Balance WHERE rowid = '{}'".format(num))
    conn.commit()
    conn.execute("VACUUM")
    conn.close()

# balance()
# transact("Jay 1000 Shaunak 1000 500")
# first("Reddy abc-abc@gmail.com")
# balancecreate()
#balancecreate("Jay 1000")
# print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
#print(display())
#for i in range(20):
  #  Delrecord(1)
#print(display())