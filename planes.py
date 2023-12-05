import mysql.connector
from prettytable import PrettyTable
import datetime

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()

class planes:                 #PLANES CLASS HAVE ALL THE METHODS THAT MANIPULATE DATA IN PLANES TABLE
    @staticmethod
    def new_plane():
        plane_name=input("Enter name of plane: ")
        fleet_count=int(input("Enter fleet count: "))
        st_avail=int(input("Number of seats per plane: "))
        type1=input("Enter the type of plane: ")
        
        sql=f"insert into planes values('{plane_name}',{fleet_count},{st_avail},'{type1}')"
        mycursor.execute(sql)
        mydb.commit()
        
    @staticmethod
    def update():
        planes.details()
        plane_name=input("Enter name of plane: ")
        num=int(input("Number of planes added to fleet: "))
        print(num," ",plane_name," planes added to fleet...")
        
        sql=f"update planes set fleet_count=fleet_count+{num} where plane_name='{plane_name}'"
        mycursor.execute(sql)
        mydb.commit()
        
    @staticmethod    
    def details():
        sql="select * from planes"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['plane_name', 'fleet_count','st_avail','type'])
        for c in results:
                table.add_row(c)
        print(table)