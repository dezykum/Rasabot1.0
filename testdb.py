import sqlite3


con = sqlite3.connect('docdatabase.db')

with con:

    cur = con.cursor()
    cur.execute("select * from docdetails WHERE specialization='Cardiologist'")
    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print ("{:6} {:10} {:2} {:2}  {:10}  {:10}".format(col_names[0], col_names[1], col_names[2],col_names[3],col_names[4],col_names[5]))
    list = []
    for row in rows:
        data = "{:<6} {:<10}   {:2}   {:2}  {:10}  {:10}".format(row[0], row[1], row[2],row[3],row[4],row[5])
        list.append(data)
    
    for value in list:
        print (value)

    