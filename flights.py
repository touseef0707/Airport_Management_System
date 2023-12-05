import mysql.connector
from prettytable import PrettyTable
import datetime
from planes import planes
from pilots import pilot
from flight_attendants import flight_attendants

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()

class flight:                 #FLIGHT CLASS HAVE ALL THE METHODS THAT MANIPULATE DATA IN FLIGHT TABLE
    @staticmethod
    def details():
        sql="select * from flight"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['flightID','plane_name','Pa_Count','FA_Count','pilot_name','departure','arrival','flight_date','dept_hr','arvl_hr','st_avail','type','return_date','status'])
        for c in results:
                table.add_row(c)
        print(table)
        mydb.commit()

    @staticmethod
    def new_flight():
        planes.details()
        plane_name=input("Enter name of plane you want to register for the flight: ")

        sql=f"select type from planes where plane_name='{plane_name}'"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        plane_type=None
        for c in results:
            plane_type=c[0].lower()

        flightID=input("Enter flight number: ")
        print(" ")
        Pa_Count=0
        FA_Count=0

        print("Available Pilots")
        pilot.availablePilots()

        pilot_name=input("Enter name of pilot: ")
        departure=input("from: ")
        arrival=input("to: ")  
        flight_date=input("Enter the flight date(yyyy-mm-dd): ")
        dept_hr=input("Enter time of departure(hh:mm:ss): ")
        arvl_hr=input("Enter time of arrival(hh:mm:ss): ")
        return_date=input("Enter the return date(yyyy-mm-dd): ")
        st_avail=0

        flight_attendants.availableFlightAttendants()
        if plane_type.lstrip()=='private':
            FA_Count=FA_Count+1
            fa_name=input("Enter name of the flight attendant: ")
            sql=f"update flight_attendants set flightID='{flightID}' where E_name='{fa_name}'"
            mycursor.execute(sql)
            mydb.commit()
        elif plane_type.lstrip()=='commercial':
            FA_Count=FA_Count+4
            for i in range(1,5):
                fa_name=input(f"Enter name of the flight attendant {i}: ")
                sql=f"update flight_attendants set flightID='{flightID}' where E_name='{fa_name}'"
                mycursor.execute(sql)
                mydb.commit()

        sql=f"select st_avail from planes where plane_name='{plane_name}'"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        for c in results:
            st_avail=st_avail+c[0]
        mydb.commit()
        
        sql=f"insert into flight values('{flightID}','{plane_name}',{Pa_Count},{FA_Count},'{pilot_name}','{departure}','{arrival}','{flight_date}','{dept_hr}','{arvl_hr}',{st_avail},'{plane_type.lstrip()}','{return_date}','waiting')"
        mycursor.execute(sql)
        mydb.commit()

        sql=f"update pilots set flightID='{flightID}' where E_name='{pilot_name}'"
        mycursor.execute(sql)
        mydb.commit()

    @staticmethod
    def availableFlights():
        today=datetime.date.today()
        sql=f"select flightID,flight_date,departure,arrival,st_avail from flight where flight_date!='{today}'"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['flightID','flight_date','departure','arrival','st_avail'])
        for c in results:
            table.add_row(c)
        print(table)
    
    @staticmethod
    def returnFlights():                    #THIS METHOD IS USED TO CHANGE STATUS OF FLIGHTS  (WAITING,PREPARING FLIGHT,IN FLIGHT,RETURNED)
        today=datetime.date.today()
        yesterday = today - datetime.timedelta(days = 1)
        tomorrow = today + datetime.timedelta(days = 1)
        sql=f"select flight_date,flightID,return_date from flight"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        for c in results:
            if c[0]==today:
                sql=f"update flight set status='in flight' where flight_date='{c[0]}'"
                mycursor.execute(sql)
                mydb.commit()
            elif c[2]==today:
                sql=f"update flight set status='returned' where flight_date='{c[0]}'"
                mycursor.execute(sql)
                mydb.commit()
                a=c[1]
                flight.pfaReturned(a)
            elif c[0]==tomorrow:
                sql=f"update flight set status='preparing flight' where flight_date='{c[0]}'"
                mycursor.execute(sql)
                mydb.commit()
    
    def pfaReturned(flightID):  #THIS METHOD WILL UPDATE THE PILOTS AND FLIGHT ATTENDANTS TABLE AFTER THEIR FLIGHT HAS BEEN SUCCESSFUL AND THEY WILL BE AVAILABLE FOR NEW FLIGHTS
        sql=f"update pilots set flightID=NULL where flightID='{flightID}'"
        mycursor.execute(sql)
        mydb.commit()
        sql=f"update flight_attendants set flightID=NULL where flightID='{flightID}'"
        mycursor.execute(sql)
        mydb.commit()
        
