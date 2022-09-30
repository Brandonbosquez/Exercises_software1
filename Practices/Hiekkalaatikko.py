#Practicas de experimento caja de arena

#Ejercicio 08 RELATIONAL DATABASES
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )

def typer(code):
    sql = " Select type, count(*) from airport where iso_country =  '"
    sql += code + "' group by type ; "
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in response:
            print(f"{row[0]} : {row[1]}")
    return

code = input("Enter the Country Code: ")
print(typer(code))