import mysql.connector
from prettytable import PrettyTable
import datetime

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Rainyjoke@123", database = "airportms")
mycursor=mydb.cursor()


class employee:      #EMPLOYEE CLASS INCLUDES ALL THE METHODS THAT MANIPULATES THE DATA IN EMLOYEE TABLE
    @staticmethod
    def details():
        sql="SELECT * from employee"  
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['E_ID', 'E_name','E_nationality','date_of_join','designation','department','salary','gender'])
        for c in results:
                table.add_row(c)
        print(table)
        mydb.commit()
        
    @staticmethod
    def add():
        # Setting Employee ID using incrementation
        sql="select E_ID from employee"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        id=0
        # E_ID=0
        if results:
            id=results[-1]
            id=id[0]
            
        E_ID=id+1
    
        E_name=input("Enter employee name: ")
        E_nationality=input("Enter nationality: ")
        gender=input("Gender (M/F): ")
        date_of_join=input("Enter date of join(yyyy-mm-dd): ")
        designation=input("Enter designation: ")
        department=input("Enter department: ")
        salary=float(input("Enter salary: "))

        # inserting values into table employee 
        sql=f"insert into employee values({E_ID},'{E_name}','{E_nationality}','{date_of_join}','{designation}','{department}',{salary},'{gender}')"
        mycursor.execute(sql)
        mydb.commit()
    
        # to update pilot and flight attendant details if a new employee is added under the same designations 
        if designation=="pilot":
            sql=f"insert into pilots values({E_ID},'{E_name}',NULL)"
            mycursor.execute(sql)
            mydb.commit()
        elif designation=="flight attendant":
            sql=f"insert into flight_attendants values({E_ID},'{E_name}',NULL)"
            mycursor.execute(sql)
            mydb.commit()
        # to display the details of the added employee
        print("Employee Added")
        print(" ")
        sql=f"select * from employee where E_ID={E_ID}"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        table = PrettyTable(['E_ID', 'E_name','E_nationality','date_of_join','designation','department','salary','gender'])
        for c in results:
                table.add_row(c)
        print(table)
        
    @staticmethod
    def update():
        print(" ")
        E_ID=int(input("Enter Employee ID: "))
        designation=input("Enter new designation of employee: ")
        department=input("Enter new department: ")
        # since we are updating the disgnation of employee 
        # if old designation is pilot then the pilots data should also be cleared from the pilot table 
        sql=f"select E_ID from pilots"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        for c in results:
            if c[0]==E_ID:
                sql=f"delete from pilots where E_ID={c[0]}"
                mycursor.execute(sql)
        # if old designation is flight_attendant then the flight attendants data should be cleared from the flight_attendant table
        sql=f"select E_ID from flight_attendants"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        for c in results:
            if c[0]==E_ID:
                sql=f"delete from flight_attendants where E_ID={c[0]}"
                mycursor.execute(sql)
        # updating the values
        sql=f"update employee set designation = '{designation}' where E_ID = {E_ID}"
        mycursor.execute(sql)
        mydb.commit()
        sql=f"update employee set department = '{department}' where E_ID = {E_ID}"
        mycursor.execute(sql)
        mydb.commit()
        print(" ")

        sql=f"select E_name from employee where E_ID={E_ID}"
        mycursor.execute(sql)
        results=mycursor.fetchall()
        E_name=None
        for c in results:
            E_name=c[0]
        # if the designation is updated to pilot then we must add the desired data into the fields of pilot table
        if designation=="pilot":
            sql=f"insert into pilots values({E_ID},'{E_name}',NULL)"
            mycursor.execute(sql)
            mydb.commit()
        # if the designation is updated to flight attendants then we must add the desired data into the fields of flight attendants table
        elif designation=="flight attendant":
            sql=f"insert into flight_attendants values({E_ID},'{E_name}',NULL)"
            mycursor.execute(sql)
            mydb.commit()

        ch=input("Do you want to update salary too(y/n)? ")
        if ch=='y':
            salary=float(input("Enter salary: "))
            sql=f"update employee set salary = {salary} where E_ID = {E_ID}"
            mycursor.execute(sql)
            mydb.commit()
            
    # Different methods to perform count operation in employee table
    @staticmethod
    def countDesig():
        sql=f"select designation,count(designation) from employee group by designation"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        table=PrettyTable(['Designation','Number of Employees'])
        for c in results:
            table.add_row(c)
        print(table)
    @staticmethod
    def countDepart():
        sql=f"select department,count(department) from employee group by department"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        table=PrettyTable(['Department','Number of Employees'])
        for c in results:
            table.add_row(c)
        print(table)
    @staticmethod
    def countTotal():
        sql=f"select count(*) from employee"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        table=PrettyTable(['Number of Employees'])
        for c in results:
            table.add_row(c)
        print(table)

    @staticmethod
    def remove():
        E_id=int(input("Enter the employee id: "))
        ch=input("Are You Sure You Want To Remove The Employee: ")
        
        if ch in 'Yy':
            sql=f"delete from employee where E_ID={E_id}"
            mycursor.execute(sql)
            mydb.commit()

            sql=f"select E_ID from pilots where E_ID={E_id}"
            mycursor.execute(sql)
            results=mycursor.fetchall()
            E_ID=None
            for c in results:
                E_ID=c[0]
            if E_ID==E_id:
                sql=f"delete from pilots where E_ID={E_id}"
                mycursor.execute(sql)
                mydb.commit()
            
            mycursor.execute(f"select E_ID from flight_attendants")
            results=mycursor.fetchall()
            E_ID=None
            for c in results:
                E_ID=c[0]
            if E_ID==E_id:
                sql=f"delete from flight_attendants where E_ID={E_id}"
                mycursor.execute(sql)
                mydb.commit()
        else:
            print("Cancelled...")
            print(" ")