from employees import employee
from flights import flight
from flight_attendants import flight_attendants
from pilots import pilot
from passengers import passengers
from planes import planes

flight.returnFlights()

while True:
    print("_"*25,"Welcome To Emirates Airlines Management System","_"*25)
    print(" ")
    print("1. Employee Management System")
    print("2. Flight Management System")
    print("3. Passengers Management System")
    print("4. Planes Management System")
    print("5. Pilots and Flight Attendants Details")
    print("6. Exit")
    print(" ")
    choice=int(input("Select an option from the above: "))
    print(" ")

    if choice==1:
        while True:
            print("1. See Employee Details")
            print("2. Add New Employee")
            print("3. Update Employee Details")
            print("4. Remove an Employee")
            ch=int(input("Select an option from the above: "))
            print(" ")
            if ch==1:
                print("1. Employee Table")
                print("2. See Number of Employees")
                ch=int(input("Select an option from the above: "))
                print(" ")
                if ch==1:
                    employee.details()
                elif ch==2:
                    print("1.Number of employees by designation")
                    print("2.Number of employees by department")
                    print("3.Total number of employees")
                    ch=int(input("Select an option from the above: "))
                    print(" ")
                    if ch==1:
                        employee.countDesig()
                    elif ch==2:
                        employee.countDepart()
                    elif ch==3:
                        employee.countTotal()
                    else:
                        print("Wrong Input")
                else :
                    print("Wrong Input")

            elif ch==2:
                # employee.add()
                try:
                    employee.add()
                except Exception:
                    print("Error! Wrong inputs")
            elif ch==3:
                try:
                    employee.update()
                except Exception:
                    print("Error! Wrong inputs")
            elif ch==4:
                try:
                    employee.remove()
                except Exception:
                    print("Error! Wrong inputs")
            else:
                print("Wrong Input...")
            print(" ")
            ch=input("Do you want to perform more operations in Employee Management System (y/n)?: ")
            if ch in 'nN':
                break

    elif choice==2:
        while True:
            print("1. See All Flight Details")
            print("2. See Available Flight Details")
            print("3. Register New Flight")
            ch=int(input("Select an option from the above: "))
            print(" ")
            if ch==1:
                flight.details()
            elif ch==2:
                flight.availableFlights()
            elif ch==3:
                try:
                    flight.new_flight()
                    flight.returnFlights()
                except Exception:
                    print("Error! Wrong inputs")
            else:
                print("Wrong Input...")
            print(" ")
            c=input("Do you want to perform more operations in Flight Management System (y/n)?: ")
            if c in 'nN':
                break

    elif choice==3:
        while True:
            print("1. See Passenger Details")
            print("2. New Passenger")
            ch=int(input("Select an option from the above: "))
            print(" ")
            if ch==1:
                passengers.details()
            elif ch==2:
                try:
                    passengers.new_passenger()
                except Exception:
                    print("Error! Wrong Inputs")
            else:
                print("Wrong Input...")
            print(" ")
            c=input("Do you want to perform more operations in Passenger Management System (y/n)?: ")
            if c in 'nN':
                break
    
    elif choice==4:
        while True:
            print("1. See Fleet Details")
            print("2. Update Fleet Details")
            print("3. Add New Fleet")
            ch=int(input("Select an option from the above: "))
            print(" ")
            if ch==1:
                planes.details()
            elif ch ==2:
                try:
                    planes.update()
                except Exception:
                    print("Error! Wrong Inputs")
            elif ch==3:
                try:
                    planes.new_plane()
                except Exception:
                    print("Error! Wrong Inputs")
            else:
                print("Wrong Input...")
            print(" ")
            ch=input("Do you want to perform more operations in Planes Management System (y/n)?: ")
            if ch in 'nN':
                break

    elif choice==5:
        while True:
            print("1.Pilots Details")
            print("2.Flight Attendants Details")
            print("3.Available Pilots")
            print("4.Available Flight Attendants")
            ch=int(input("Select an option from the above: "))
            print(" ")
            if ch==1:
                pilot.details()
            elif ch==2:
                flight_attendants.details()
            elif ch==3:
                pilot.availablePilots()
            elif ch==4:
                flight_attendants.availableFlightAttendants()
            else:
                print("Wrong Chioce")
            print(" ")
            ch=input("Do you want to perform more operations in Pilots and Flight Attendants Management System (y/n)?: ")
            if ch in 'nN':
                break

    elif choice==6:
        print(" ")
        break
    else:
        print("Wrong Input!... ")
    ch=input("Do you want to perform more operations in Emirates Airlines Management System (y/n)?: ")
    print(" ")
    if ch in 'nN':
        break