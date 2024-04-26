from boat import Boat
from customer import Customer
from booking import Booking
from tkinter import messagebox, simpledialog

class  Node:
    def __init__(self, data):
        self.data = data
        self.prev= None
        self.next= None

class Function:
    def __init__(self):
        self.head = None
    def bcode_exists(self, bcode):
        current_boat = self.head
        while current_boat is not None:
            if current_boat.data.bcode == bcode:
                return True
            current_boat = current_boat.next
        return False
    def add_to_head(self, data):
        if not self.bcode_exists(data[0]):
            # Create the appropriate object based on the length of the data
            if len(data) == 6:  # Boat data
                new_data = Boat(*data)
            else:
                print("Invalid data")
                return
            new_node = Node(new_data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            print(f"Mã thuyền {data[0]} đã tồn tại.")

    def display_data(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def search_by_bcode(self, bcode):
        current = self.head
        while current is not None:
            if current.data.bcode == bcode:
                return current.data
            current = current.next
        return None

    def delete_by_bcode(self, bcode):
        current = self.head
        while current is not None:
            if current.data.bcode == bcode:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def sort_by_bcode(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            next_node = current.next
            while next_node is not None:
                if current.data.bcode > next_node.data.bcode:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def add_before_bcode(self, new_boat, xCode):
        if self.head is None or self.head.data.bcode == xCode:
            self.add_to_head(new_boat)
            return
        current = self.head
        while current.next is not None and current.next.data.bcode != xCode:
            current = current.next
        if current.next is None:
            print(f"Không tìm thấy mã thuyền {xCode}")
            return
        new_boat = Boat(*new_boat)
        new_node = Node(new_boat)
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def delete_before_bcode(self, xCode):
        if self.head is None or self.head.data.bcode == xCode:
            return
        if self.head.next and self.head.next.data.bcode == xCode:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head.next
        while current.next is not None and current.next.data.bcode != xCode:
            current = current.next
        if current.next is None:
            print(f"Không tìm thấy mã thuyền {xCode}")
            return
        current.prev.next = current.next
        current.next.prev = current.prev

    def add_to_end(self, data):
        # Kiểm tra xem mã thuyền đã tồn tại chưa
        if not self.ccode_exists(data[0]):
            # Tạo đối tượng phù hợp dựa trên độ dài của dữ liệu
            if len(data) == 3:  # Dữ liệu thuyềng
                new_data = Customer(*data)
            else:
                print("Dữ liệu không hợp lệ")
                return
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                new_node.prev = current
        else:
            print(f"Mã thuyền {data[0]} đã tồn tại.")

    def ccode_exists(self, ccode):
        current_customer = self.head
        while current_customer is not None:
            if isinstance(current_customer.data, Customer) and current_customer.data.ccode == ccode:
                return True
            current_customer = current_customer.next
        return False

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            current = self.head
            while current is not None:
                f.write(str(current.data))
                current = current.next

    def search_by_ccode(self, ccode):
        current = self.head
        while current is not None:
            if isinstance(current.data, Customer) and current.data.ccode == ccode:
                return current.data
            current = current.next
        return None

    def delete_by_ccode(self, ccode):
        current = self.head
        while current is not None:
            if isinstance(current.data, Customer) and current.data.ccode == ccode:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

class BookingSystem(Function):
    def add_to_end(self, data):
    # Kiểm tra xem mã đặt chỗ đã tồn tại chưa
        if not self.booking_exists(data[0], data[1]):
            # Tạo đối tượng Booking mới
            new_booking = Booking(*data)
            new_node = Node(new_booking)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                new_node.prev = current
        else:
            print(f"Đặt chỗ với mã thuyền {data[0]} và mã khách hàng {data[1]} đã tồn tại.")

    def display_booking_data(self):
        current = self.head
        while current is not None:
            if isinstance(current.data, Booking):
                print(current.data.bcode, current.data.ccode, current.data.seat_booked)
            current = current.next

    def sort_by_bcode_ccode(self):
        if self.head is None or self.head.next is None:
            return
        current = self.head
        while current.next is not None:
            next_node = current.next
            while next_node is not None:
                if (current.data.bcode > next_node.data.bcode) or \
                   (current.data.bcode == next_node.data.bcode and current.data.ccode > next_node.data.ccode):
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def booking_exists(self, bcode, ccode):
        current = self.head
        while current is not None:
            if isinstance(current.data, Booking) and current.data.bcode == bcode and current.data.ccode == ccode:
                return True
            current = current.next
        return False