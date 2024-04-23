class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def bcode_exists(self, bcode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == bcode:
                return True
            cur_node = cur_node.next
        return False
    
    def ccode_exists(self, ccode):
        cur_node = self.head
        while cur_node:
            if hasattr(cur_node.data, 'ccode') and cur_node.data.ccode == ccode:
                return True
            cur_node = cur_node.next
        return False

    def add_to_head(self, new_boat):
        if not self.bcode_exists(new_boat.bcode):
            new_node = Node(new_boat)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            print(f"A boat with bcode {new_boat.bcode} already exists.")
            
    def add_to_end(self, data):
        ccode, cus_name, phone = data
        if not self.ccode_exists(ccode):
            new_customer = Customer(ccode, cus_name, phone)
            new_node = Node(new_customer)
            if self.head is None:
                self.head = new_node
            else:
                cur_node = self.head
                while cur_node.next:
                    cur_node = cur_node.next
                cur_node.next = new_node
                new_node.prev = cur_node
        else:
            print(f"A customer with ccode {ccode} already exists.")


    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(' | ')
                self.add_to_head(data)
                
    def add_to_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def delete_node(self, code):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == code or cur_node.data.ccode == code:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                return
            cur_node = cur_node.next

    def search(self, xCode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == xCode:
                return cur_node
            cur_node = cur_node.next
        return None

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            cur_node = self.head
            while cur_node:
                boat = cur_node.data
                file.write(f"{boat.bcode} | {boat.boat_name} | {boat.seat} | {boat.booked} | {boat.depart_place} | {boat.rate}\n")
                cur_node = cur_node.next

    def display(self):
        cur_node = self.head
        while cur_node:
            boat = cur_node.data
            available_seat = boat.seat - boat.booked
            print(f"{boat.bcode} | {boat.boat_name} | {boat.seat} | {boat.booked} | {boat.depart_place} | {boat.rate} | {available_seat}")
            cur_node = cur_node.next
        
    def delete_by_bcode(self, bcode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == bcode:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                return
            cur_node = cur_node.next
            
    def delete_by_ccode(self, ccode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.ccode == ccode:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                return
            cur_node = cur_node.next


    def sort_by_bcode(self):
        if self.head is None:
            return

        cur_node = self.head
        while cur_node.next:
            next_node = cur_node.next
            while next_node:
                if cur_node.data.bcode > next_node.data.bcode:
                    cur_node.data, next_node.data = next_node.data, cur_node.data
                next_node = next_node.next
            cur_node = cur_node.next
            
    def add_before_node(self, data, xCode):
        new_boat = Boat(*data)
        new_node = Node(new_boat)

        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == xCode:
                new_node.prev = cur_node.prev
                new_node.next = cur_node
                if cur_node.prev:
                    cur_node.prev.next = new_node
                cur_node.prev = new_node
                if cur_node == self.head:
                    self.head = new_node
                return
            cur_node = cur_node.next
            
    def delete_before_node(self, xCode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == xCode and cur_node.prev:
                self.delete_by_bcode(cur_node.prev.data.bcode)
                return
            cur_node = cur_node.next
            
    def add_booking(self, booking, boats, customers):
        # Kiểm tra xem mã thuyền và mã khách hàng có tồn tại không
        if boats.bcode_exists(booking.bcode) and customers.ccode_exists(booking.ccode):
            if not self.head:
                self.head = Node(booking)
            else:
                new_node = Node(booking)
                new_node.next = self.head
                self.head = new_node
        else:
            print("Mã thuyền hoặc mã khách hàng không tồn tại.")

    def sort_booking(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            node = self.head
            while node.next:
                if (node.data.bcode, node.data.ccode) > (node.next.data.bcode, node.next.data.ccode):
                    node.data, node.next.data = node.next.data, node.data
                    swapped = True
                node = node.next

class Boat:
    def __init__(self, bcode, boat_name, seat, booked, depart_place, rate):
        self.bcode = bcode
        self.boat_name = boat_name
        self.seat = int(seat)
        self.booked = int(booked)
        self.depart_place = depart_place
        self.rate = float(rate)
        
class Customer:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone

class Booking:
    def __init__(self, bcode, ccode, seat):
        self.bcode = bcode
        self.ccode = ccode
        self.seat = int(seat)

class BookingList:
    def __init__(self):
        self.head = None

    def add_booking(self, booking):
        if not self.head:
            self.head = Node(booking)
        else:
            new_node = Node(booking)
            new_node.next = self.head
            self.head = new_node

    def sort_booking(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            node = self.head
            while node.next:
                if (node.data.bcode, node.data.ccode) > (node.next.data.bcode, node.next.data.ccode):
                    node.data, node.next.data = node.next.data, node.data
                    swapped = True
                node = node.next

    def bcode_exists(self, bcode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.bcode == bcode:
                return True
            cur_node = cur_node.next
        return False

    def ccode_exists(self, ccode):
        cur_node = self.head
        while cur_node:
            if cur_node.data.ccode == ccode:
                return True
            cur_node = cur_node.next
        return False

    def add_to_end(self, data):
        bcode, ccode, seat = data
        if not self.bcode_exists(bcode) and not self.ccode_exists(ccode):
            new_booking = Booking(bcode, ccode, seat)
            new_node = Node(new_booking)
            if self.head is None:
                self.head = new_node
            else:
                cur_node = self.head
                while cur_node.next:
                    cur_node = cur_node.next
                cur_node.next = new_node
                new_node.prev = cur_node
        else:
            print(f"A booking with bcode {bcode} or ccode {ccode} already exists.")

    def input_data(self):
        bcode = input("Enter boat code: ")
        ccode = input("Enter customer code: ")
        seat = int(input("Enter number of seats to be booked: "))
        self.add_booking(bcode, ccode, seat)

    def sort_booking(self):
        if self.head is None:
            return

        cur_node = self.head
        while cur_node.next:
            next_node = cur_node.next
            while next_node:
                if cur_node.data.bcode + cur_node.data.ccode > next_node.data.bcode + next_node.data.ccode:
                    cur_node.data, next_node.data = next_node.data, cur_node.data
                next_node = next_node.next
            cur_node = cur_node.next

    def display_booking(self):
        cur_node = self.head
        while cur_node:
            booking = cur_node.data
            print(f"{booking.bcode} | {booking.ccode} | {booking.seat}")
            cur_node = cur_node.next
            
    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(' | ')
                self.add_to_end(data)
                
    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            cur_node = self.head
            while cur_node:
                boat = cur_node.data
                file.write(f"{boat.bcode} | {boat.boat_name} | {boat.seat} | {boat.booked} | {boat.depart_place} | {boat.rate}\n")
                cur_node = cur_node.next

boat_list = DoublyLinkedList()
customers = DoublyLinkedList()
boat_list.load_from_file("boat_booking/boats.txt")
customers.load_from_file("boat_booking/customer.txt")

# To add a new boat to the head of the list, you can use the add_to_head method:
new_boat = ['B06', 'NewBoat', '15', '0', 'PG', '20']
boat_list.add_to_head(new_boat)

booking_list = BookingList()
booking_list.add_booking(Booking('B01', 'C01', 2), boat_list, customers)
booking_list.sort_booking()
booking_list.save_to_file('booking.txt')


