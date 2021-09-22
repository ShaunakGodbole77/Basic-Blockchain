import sqlite3

def DatabaseCreation():
    #creating a database
    conn = sqlite3.connect("BlocksData.db")

    #creating a cursor
    c = conn.cursor()

    #creating a table
    c.execute("""CREATE TABLE BlocksInfo (
                MinedBy text,
                CurrentHash text,
                PreviousHash text,
                HeaderTransactions text,
                TimeStamp text,
                Nonce text,
                BlockLimit integer
                ) """)

    #commiting to database
    conn.commit()
    #closing connection
    conn.close()


def AddBlock(recieved):
    msg = recieved.split("_")
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()

    BlockData = [msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6]]

    c.execute("INSERT INTO BlocksInfo VALUES (?,?,?,?,?,?,?)",BlockData)
    conn.commit()
    conn.close()
    DisplayAllData()


def DisplayAllData():
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("SELECT * FROM BlocksInfo")
    items = c.fetchall()
    print("------------------------------------------------------------BLOCKCHAIN----------------------------------------------------------------------------------------------------")
    print("MINED-BY\t\tCURRENT-HASH\t\tPREVIOUS-HASH\t\tHEADER-TRANSACTIONS\t\tTIME-STAMP\t\tNONCE\t\tBLOCKLIMIT")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for item in items:
        print(item[0]+"\t\t"+item[1]+"\t\t"+item[2]+"\t\t"+item[3]+"\t\t"+item[4]+"\t\t"+item[5]+"\t\t"+str(item[6]))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    conn.commit()
    conn.close()


def DisplayGenesis():
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("SELECT * FROM BlocksInfo")
    print(c.fetchone())
    conn.commit()
    conn.close()


def DisplaySome(number):
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("SELECT * FROM BlocksInfo")
    print(c.fetchmany(number))
    conn.commit()
    conn.close()


def SearchDatabase(keyword):
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("SELECT * FROM BlocksInfo WHERE (MinedBy+CurrentHash+PreviousHash+HeaderTransactions+TimeStamp+Nonce+BlockLimit) LIKE '%{}%'".format(keyword))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def DeleteRecord(number):
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("DELETE from BlocksInfo WHERE rowid = {}".format(number))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.execute("VACUUM")
    conn.close()


def GetHash():
    conn = sqlite3.connect("BlocksData.db")
    c = conn.cursor()
    c.execute("SELECT * FROM BlocksInfo")
    length = c.fetchall()
    conn.commit()
    c.execute("SELECT * FROM BlocksInfo WHERE rowid = {}".format(len(length)))
    items = c.fetchall()
    print(items)
    conn.commit()
    conn.close()
    for i in items:
        item1 = list(i)
        print(item1)
    item = item1[1]
    item2 = item1[2]
    print(item2)
    print(item)
    newitem = str(item) +str(item2)
    return newitem


# DatabaseCreation()
#DisplayAllData()
#print(GetHash())
#for i in range(20):
  #  DeleteRecord(1)
#DisplayAllData()