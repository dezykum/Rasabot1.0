import sqlite3 
from sqlite3 import Error 
def sql_connection(): 
    try: 
        con = sqlite3.connect('docdatabase.db')
        return con

    except Error:
 
        print(Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    # cursorObj.execute("CREATE TABLE docdetails(name text, specialization text, experience integer, rating float, availability text, datetime text)")
    cursorObj.execute("INSERT INTO docdetails VALUES('Diksha Jha', 'Cardiologist', '10 years', 9.5, 'Yes', '2017-01-04 and 10.00 A.M')")
    con.commit()
con = sql_connection()
sql_table(con)

