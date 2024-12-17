from datetime import *
import random


class FlightReservation:
    def __init__(self):
        self.reservation = {
            "economy" : {},
            "business" : {},
            "first class": {}
        }
    def booking(self, classtpye,  passengername,trip_type, flight_day,departure, destination, date_of_return, birthdate, email, phone):
        number = ["flight123", "flight321"]
        seatnum = random.randint(1,300)
        flight_number = random.choice(number)
        
        classtpye = classtpye.lower().strip()
        if classtpye not in self.reservation:
            print("Please input valid class. (Economy/Business/First class)")
            return
        file_txt=f"finals/{classtpye.lower()}.txt"



        if trip_type.lower() == "round-trip":
            if not date_of_return:
                date_of_return = input("Enter the date of return: format(MM/DD/YY): ")
        date =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.reservation[classtpye][seatnum] = {
            "departure" :  departure,
            "destination" : destination,
            "trip_type" :trip_type,
            "flight_Day" : flight_day,
            "date_of_return" : date_of_return,
            "time_booked" :date,
            "destination" : destination,
            "flight_number":flight_number,
            "passenger_name" : passengername,
            "birthdate" : birthdate,
            "email" : email,
            "phone" : phone




        }
        
        
             
        deatils= f"Departure: {departure}\nDestination : {destination}\nClass : {classtpye}\nTrip_type : {trip_type}\nFlight Day : {flight_day} \
            \nReturn : {date_of_return} \nSeatnumber : {seatnum} \nTime booked : {date}\nPassenger Name : {passengername}\
            \nbirth_date : {birthdate}\nEmail : {email}\nPhone : {phone}\nFlight_number : {flight_number}\n\n"

        with open(file_txt, "a") as f:
            f.write(deatils)
 
        return deatils
    def canceling(self, classtype, seatnumber, passengername):
        if classtype not in self.reservation:
            print("Please input valid class. (Economy/Business/First class)")
            return
        if seatnumber not in self.reservation[classtype]:
            print("This seat number is not booked.")
            return
        passengerdetail = self.reservation[classtype][seatnumber]
        if passengerdetail['passenger_name'] !=  passengername:
            print("There is no Passenger name that matches in our system.")
            return
        date =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.reservation[classtype].pop(seatnumber)
        print(f"\nCancel confirmed.\nPassenger name : {passengername}\nseatnumber : {seatnumber}\nclass : {classtype}\nTime canceled :  {date}\nDestination : {passengerdetail['destination']}\nFlight day : {passengerdetail['flight_Day']}\n")
    def view_reservation(self, classtype):
        if classtype not in self.reservation:
            print("Please input valid class. (Economy/Business/First class)")
            return
        print(f"These are the reservation for class {classtype}.")
        if not self.reservation[classtype]:
            print()
            print(f"No Reservation for this class {classtype}")
            return
        else:
            for seatnumber, detail in self.reservation[classtype].items():
                print(f"\nSeatnumber : {seatnumber}\nPassenger name : {detail['passenger_name']}\nDate of flight: {detail['flight_Day']}\nHedead to : {detail['destination']}\n")


        