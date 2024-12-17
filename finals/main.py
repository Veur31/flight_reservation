from accessories import *
from flight import *
from datetime import *
import os
def clear():
     choice = input("Go back to main menu? (Y/N): ").upper()
     if choice == 'Y':
          os.system('cls')
          main()
     else:
          os.system('cls')
flight1 = FlightReservation()
def main():
     print("\nWelcome to AirLPU\n")
     print("1.Book a Flight\n2.Cancel a Flight.\n3.View reservations\n4.Exit")
     choice = input("Enter from 1-4: ")
     print()

     if choice == "1":
          print()
          line1()
          print('Passengers Booking')
          print()
          departure =  input("Departure: ")
          destination = input("Enter your destination: ")
          classtpye = input("Enter what class. (Economy/Business/First class): ").lower()
          trip_type = input("Enter trip type: Format(round-trip/one-way) ").lower()
          flight_day = input("Date of Departure. format(MM/DD/YY): ")

         
          
          print()
          print("Personal Details")
          passengername = input("Enter your name: ")
          birthdate = input("Enter your birthdate: ")
          email = input("Enter your email: ")
          phone = input("Enter Phone number: ")
          
          
          
          
          date_of_return = None
          if trip_type == "round-trip":
               date_of_return = input("Please enter the return date (format MM/DD/YY): ")

          result = flight1.booking(classtpye, passengername,trip_type, flight_day,departure, destination,date_of_return, birthdate, email, phone )
          if result:
               print("\nDetalis of the flight")
               print(result)
          clear()
     elif choice == "2":
          print()
          line1()
          print('Cancel Booking')
          print()
          classtpye = input("Enter what class. (Economy/Business/First class): ").lower().strip()
          seatnumber = input("Enter the seatnumber: ")
          passengername= input("Enter Passenger Name: ")
          flight1.canceling(classtpye, seatnumber, passengername)
          clear()
     elif choice == "3":
          line1()
          print('View Reservation')
          print()
          classtpye = input("Enter what class. (Economy/Business/First class): ").lower()
          flight1.view_reservation(classtpye)
          print()
          clear()
     elif choice == "4":
          exit()
     else:
          print("Please input a valid number from the choice")
          main()
main()
          
          


