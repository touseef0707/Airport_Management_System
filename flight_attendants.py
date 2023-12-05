import mysql.connector
from prettytable import PrettyTable
import datetime

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()

class flight_attendants:
    @staticmethod
    def details():
        sql='select * from flight_attendants'
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['Flight Attendant Id', 'Name','Flight Number'])
        for c in results:
            table.add_row(c)
        print(table)
          
    @staticmethod
    def availableFlightAttendants():
        sql="select E_name from flight_attendants where flightID is NULL"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['Name'])
        for c in results:
            table.add_row(c)
        print(table)