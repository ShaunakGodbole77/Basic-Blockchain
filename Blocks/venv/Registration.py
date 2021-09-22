import sqlite3

def registrationDatabase():
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE Registration (
                    Name text,
                    Password text,
                    ContactNumber text,
                    Email text,
                    AadharNumber text,
                    PanNumber text,
                    Passport text,
                    PublicKey text
                    ) """)

    conn.commit()
    conn.close()

def createAccount(message):
    msg = message.split('-')
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    c.execute("INSERT INTO Registration VALUES (?,?,?,?,?,?,?,?)",msg)
    conn.commit()
    conn.close()


def signIn(message,pas):
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Registration WHERE Email = '{}'".format(message))
    check = c.fetchall()
    for i in check:
        m = list(i)
        if m[1] == pas:
            conn.commit()
            conn.close()
            return True
    else:
        conn.commit()
        conn.close()
        return False


def CloseAccount(message):
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    c.execute("DELETE from Registration WHERE rowid = {}".format(message))
    conn.commit()
    conn.execute("VACUUM")
    print("Success")
    conn.close()

def reportGeneration(message):
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    listtopass = [message]
    c.execute("SELECT * FROM Registration WHERE Email = (?)",listtopass)
    report = c.fetchall()
    print("----------------------------------------------------------------BLACKLIST USER REPORT------------------------------------------------------------")
    print(report)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    conn.commit()
    conn.close()

def Display():
    conn = sqlite3.connect("RegisteredUsers1.db")
    c = conn.cursor()
    c.execute("SELECT * from Registration")
    items = c.fetchall()
    print("----------------------------------------------------REGISTRATION DATABASE ---------------------------------------------------------------")
    print("NAME","\t\t","PASSWORD","\t","CONTACT","\t","EMAIL","\t\t","AADHAR","\t","\t","PAN","\t","PASSPORT","\t","PUBLIC-KEY")
    print("-------------------------------------------------------------------------------------------------------------------")
    for item in items:
        print(str(item[0]) + "\t" + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t" + str(item[4]) + "\t" + str(item[5]) + "\t" +str(item[6]) + "\t" + str(item[7]))
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    conn.commit()
    conn.close()
    return items

# registrationDatabase()
# createAccount("aaaa aaaa 1111 aaaa 1111 1111 1111 1111")
#for i in range(50):
    #CloseAccount(1)
#Display()a

# registrationDatabase()
