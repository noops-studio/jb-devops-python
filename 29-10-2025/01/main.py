

from datetime import date
from classes.Plan import Plan
from classes.Pilot import Pilot
from classes.Seat import Seat
from classes.Passanger import Passenger
from classes.Flight import Flight

someDate = date(2025,10,29)


# Creating an object of Pilot class
someObjectOfApilot  = Pilot(1, "John Doe", someDate, "Captain", 45)
# Creating an object of Plan class and assigning the Pilot to it
someObjectOfAplane = Plan("Boeing 747", someObjectOfApilot)

# Output Pilot and Plane details
print(f"Pilot Name is: {someObjectOfApilot.Fullname} , Pilot Rank is: {someObjectOfApilot.Rank} ")
print(f"Today's date is: {someDate} ")
print(f"Plane Name is: {someObjectOfAplane.Name} , Plane Pilot is: {someObjectOfAplane.FlightPilot.Fullname} ")

# Testing Passenger and Seat classes
_Passenger = Passenger(1, "Alice Smith", "TCK123456")
# Creating a Seat and assigning the Passenger to it
_Seat = Seat(1, 12, "A", "Economy", _Passenger)

someObjectOfAplane.boardPassengerSeat(_Passenger, _Seat)

# Output Passenger and Seat details
print(f"Passenger Name is: {_Passenger.Fullname} , Ticket Number is: {_Passenger.TicketNumber} ")
print(f"Seat Row: {_Seat.Row} , Seat Column: {_Seat.Column} , Seat Class: {_Seat.SeatClass} ")


_flight = Flight("FL123", someObjectOfAplane, False)
_flight.fly()
_flight.land()