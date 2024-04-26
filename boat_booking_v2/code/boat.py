class Boat:
    def __init__(self, bcode, boat_name, seat, booked, depart_place, rate):
        self.bcode = bcode
        self.boat_name = boat_name
        self.seat = int(seat)
        self.booked = int(booked)
        self.depart_place = depart_place
        self.rate = float(rate)
    
    def __str__(self):
        return f"{self.bcode} | {self.boat_name} | {self.seat} | {self.booked} | {self.depart_place} | {self.rate}\n"

