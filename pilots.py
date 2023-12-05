import mysql.connector
from prettytable import PrettyTable
import datetime

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()

class pilot:                 #PILOT CLASS HAVE ALL THE METHODS THAT MANIPULATE DATA IN PILOTS TABLE                                              
    @staticmethod
    def details():
        sql='select * from pilots'
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['Pilot Id', 'Name','Flight Number'])
        for c in results:
            table.add_row(c)
        print(table)
             
    @staticmethod
    def availablePilots():
        sql="select E_name from pilots where flightID is NULL"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['Pilot Name'])
        for c in results:
            table.add_row(c)
        print(table)