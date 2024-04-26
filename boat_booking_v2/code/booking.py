class Booking:
    def __init__(self, bcode, ccode, seat_booked):
        self.bcode = bcode
        self.ccode = ccode
        self.seat_booked = int(seat_booked)
        
    def __str__(self):
        return f"{self.bcode} | {self.ccode} | {self.seat_booked}\n"