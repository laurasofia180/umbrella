import MySQLdb

db = MySQLdb.connect("10.131.137.188") #Abrir la conexion de la base de datos
cursor = db.cursor()
cursor.execute("lmunozm")
cursor.execute ("SELCT * FROM lmunozm") #query para ver la bd

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        

db.close()
