import mysql.connector
from prettytable import PrettyTable
from flights import flight
import datetime

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()

class passengers:                 #PASSENGERS CLASS HAVE ALL THE METHODS THAT MANIPULATE DATA IN PASSENGERS TABLE
    @staticmethod
    def details():
        sql="select * from passengers"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['Passenger Id','Name','Nationality','Flight Number'])
        for c in results:
                table.add_row(c)
        print(table)
        mydb.commit()
        
    @staticmethod
    def new_passenger():
        print('*'*50,"Available Destinations",'*'*50)
        flight.availableFlights()
        flightID=input("Select flight number: ")
        print(" ")
        print("Enter the details below for documentation purposes ")

        sql=f"select P_ID from passengers"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        P_ID=1
        if results:
            c=results[-1][0]
            P_ID=c+1
        
            
        name=input("Name of passenger: ")
        nationality=input("Nationality of passenger: ")
        planetype=input("Private / Commercial : ")
        
        if planetype=="Private":
            print("Ticket Costs: 8000dhs ")
        else:    
            print("Ticket Costs : 4000dhs")

        sql=f"insert into passengers values({P_ID},'{name}','{nationality}','{flightID}')"
        mycursor.execute(sql)
        mydb.commit()

        sql=f"update flight set Pa_Count=Pa_Count+1  where flightID='{flightID}'"
        mycursor.execute(sql)
        mydb.commit()

        sql=f"update flight set st_avail=st_avail-1  where flightID='{flightID}'"
        mycursor.execute(sql)
        mydb.commit()

        sql=f"select departure,arrival,flight_date,st_avail,dept_hr,arvl_hr from flight where flightID='{flightID}' "
        mycursor.execute(sql)
        results=mycursor.fetchall()
        depart=None
        arrival=None
        flight_date=None
        dept_hr=None
        arvl_hr=None
        st_avail=None
        for c in results:
            depart=c[0]
            arrival=c[1]
            flight_date=c[2]
            st_avail=c[3]
            dept_hr=c[4]
            arvl_hr=c[5]
            
        print(" ")    
        print("COllECT YOUR TICKET BELOW")
        print(" ")
        print('*'*10,'Ticket','*'*10)
        print(" ")
        print("Passenger ID: ",P_ID)
        print("Name:         ",name)
        print("Nationality:  ",nationality)
        print("Flight ID:    ",flightID)
        print("From:         ",depart)
        print("To:           ",arrival)
        print("Flight Date:  ",flight_date)
        print("Departure Hr :",dept_hr)
        print("Arrival Hr:   ",arvl_hr)
        print("Seat Number:  ",st_avail)
        print("*"*28)
        print("----- Happy Journey :) ----- ")
        print("*"*28)
        