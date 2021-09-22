import sqlite3
import MinerCode
import BlocksDatabase

global n
n =0
def TransactionDatabaseCreation():
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE TransactionsInfo (
                    Sender text,
                    Reciever text,
                    Value text,
                    TransactionID text
                    ) """)

    c.execute("""CREATE TABLE PendingTransactions (
                        Sender text,
                        Reciever text,
                        Value text,
                        ID text
                        ) """)

    conn.commit()
    conn.close()


def BlockCreater():
    while True:
        conn = sqlite3.connect("TransactionData1.db")
        c = conn.cursor()
        c.execute("SELECT * from PendingTransactions")
        lentocheck = c.fetchall()
        conn.commit()
        if len(lentocheck) >= 1:
            print(lentocheck)
            MinerCode.miner(lentocheck)
            conn = sqlite3.connect("TransactionData1.db")
            c = conn.cursor()
            c.execute("DELETE from PendingTransactions WHERE rowid = {}".format(1))
            conn.commit()
            for i in lentocheck:
                added = list(i)
                c.execute("INSERT INTO TransactionsInfo VALUES (?,?,?,?)",added)
                conn.commit()
            conn.execute("VACUUM")
            conn.close()
            break
        else:
            continue

def CreateTransaction(sender,reciever,value,id):
    # print("-----------------------------------------------------------------------------------------------")
    # print(sender)
    # print(reciever)
    # print("-----------------------------------------------------------------------------------------------")
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()
    Transactiondata = [sender,reciever,value,id]
    c.execute("INSERT INTO PendingTransactions VALUES (?,?,?,?)",Transactiondata)
    conn.commit()
    conn.close()
    print("success")
    BlockCreater()

def display():
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()
    c.execute("SELECT * from TransactionsInfo")
    data = c.fetchall()
    # for item in data:
    print("----------------------------------------------------TRANSACTION DATABASE ---------------------------------------------------------------")
    print("SENDER","\t\t","RECEIVER","\t\t","AMOUNT","\t","TRANSACTION ID")
    print("-------------------------------------------------------------------------------------------------------------------")
    for item in data:
        print(str(item[0]) + "\t\t" + str(item[1]) + "\t\t" + str(item[2]) + "\t" + str(item[3]))
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    return data
    conn.commit()
    conn.close()

def DeleteRecord(num):
    conn = sqlite3.connect("TransactionData1.db")
    c = conn.cursor()
    c.execute("DELETE from TransactionsInfo WHERE rowid = {}".format(num))
    conn.commit()
    conn.execute("VACUUM")
    conn.close()

# TransactionDatabaseCreation()
#display()
#for i in range(20):
 #   DeleteRecord(1)
#CreateTransaction("shaunak@viit.ac.in","jaydaf@viit.ac.in","200","1")
#CreateTransaction("shivam@viit.ac.in","shaunak@viit.ac.in","200","2")
#display()