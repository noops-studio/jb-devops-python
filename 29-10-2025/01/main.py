

from datetime import date
from classes.Plan import Plan
from classes.Pilot import Pilot
from classes.Seat import Seat
from classes.Passanger import Passenger
someDate = date(2025,10,29)


someObjectOfApilot  = Pilot(1, "John Doe", someDate, "Captain", 45)
someObjectOfAplane = Plan("Boeing 747", someObjectOfApilot)

print(f"Pilot Name is: {someObjectOfApilot.Fullname} , Pilot Rank is: {someObjectOfApilot.Rank} ")
print(f"Today's date is: {someDate} ")
print(f"Plane Name is: {someObjectOfAplane.Name} , Plane Pilot is: {someObjectOfAplane.FlightPilot.Fullname} ")


_Passanger = Passenger(1, "Alice Smith", "TCK123456")
_Seat = Seat(1, 12, "A", "Economy", _Passanger)

print(f"Passenger Name is: {_Passanger.Fullname} , Ticket Number is: {_Passanger.TicketNumber} ")
print(f"Seat Row: {_Seat.Row} , Seat Column: {_Seat.Column} , Seat Class: {_Seat.SeatClass} ")