import sqlite3

def reverserDatabase():
    conn = sqlite3.connect("reverse.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE reverse("
                     username text,
                     inter_Privatekey text,
                     inter_Publickey text,
                     Publickey text
                     )""")

    conn.commit()
    conn.close()

