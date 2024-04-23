import tkinter as tk
from tkinter import messagebox, simpledialog
from boat_system import DoublyLinkedList, Boat, Customer, Booking

# Tạo danh sách thuyền, khách hàng và đặt chỗ
boats = DoublyLinkedList()
customers = DoublyLinkedList()
bookings = DoublyLinkedList()

def load_boats():
    try:
        boats.load_from_file("boat_booking/boats.txt")
        messagebox.showinfo("Thông báo", "Đã tải dữ liệu thuyền thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu thuyền: {e}")

def add_boat():
    # Hiển thị hộp thoại để nhập thông tin thuyền
    bcode = simpledialog.askstring("Thêm thuyền mới", "Nhập mã thuyền:")
    boat_name = simpledialog.askstring("Thêm thuyền mới", "Nhập tên thuyền:")
    seat = simpledialog.askinteger("Thêm thuyền mới", "Nhập số ghế:")
    booked = simpledialog.askinteger("Thêm thuyền mới", "Nhập số ghế đã đặt:")
    depart_place = simpledialog.askstring("Thêm thuyền mới", "Nhập nơi khởi hành:")
    rate = simpledialog.askfloat("Thêm thuyền mới", "Nhập tỷ lệ:")

    # Tạo thuyền mới và thêm vào danh sách
    new_boat = Boat(bcode, boat_name, seat, booked, depart_place, rate)
    boats.add_to_head(new_boat)

    messagebox.showinfo("Thông báo", "Đã thêm thuyền mới")

def display_boats():
    # Lấy nút đầu tiên của danh sách
    current_node = boats.head

    # Tạo một chuỗi để lưu thông tin của tất cả các thuyền
    boat_info = ""

    # Duyệt qua danh sách
    while current_node is not None:
        # Lấy thông tin thuyền
        boat = current_node.data

        # Thêm thông tin thuyền vào chuỗi
        boat_info += f"Mã thuyền: {boat.bcode}, Tên thuyền: {boat.boat_name}, Số ghế: {boat.seat}, Số ghế đã đặt: {boat.booked}, Nơi khởi hành: {boat.depart_place}, Tỷ lệ: {boat.rate}\n"

        # Chuyển sang nút tiếp theo
        current_node = current_node.next

    # Hiển thị thông tin tất cả các thuyền
    messagebox.showinfo("Thông báo", boat_info)

def load_customers():
    try:
        # Tải dữ liệu khách hàng từ file
        customers.load_from_file("boat_booking/customers.txt")
        messagebox.showinfo("Thông báo", "Đã tải dữ liệu khách hàng thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu khách hàng: {e}")

def add_customer():
    try:
        # Hiển thị hộp thoại để nhập thông tin khách hàng
        ccode = simpledialog.askstring("Thêm khách hàng mới", "Nhập mã khách hàng:")
        cus_name = simpledialog.askstring("Thêm khách hàng mới", "Nhập tên khách hàng:")
        phone = simpledialog.askstring("Thêm khách hàng mới", "Nhập số điện thoại:")

        # Tạo khách hàng mới và thêm vào danh sách
        new_customer = Customer(ccode, cus_name, phone)
        customers.add_to_head(new_customer)

        messagebox.showinfo("Thông báo", "Đã thêm khách hàng mới")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm khách hàng mới: {e}")

def display_customers():
    try:
        # Lấy nút đầu tiên của danh sách
        current_node = customers.head

        # Tạo một chuỗi để lưu thông tin của tất cả các khách hàng
        customer_info = ""

        # Duyệt qua danh sách
        while current_node is not None:
            # Lấy thông tin khách hàng
            customer = current_node.data

            # Thêm thông tin khách hàng vào chuỗi
            customer_info += f"Mã khách hàng: {customer.ccode}, Tên khách hàng: {customer.cus_name}, Số điện thoại: {customer.phone}\\n"

            # Chuyển sang nút tiếp theo
            current_node = current_node.next

        # Hiển thị thông tin tất cả các khách hàng
        messagebox.showinfo("Thông báo", customer_info)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể hiển thị danh sách khách hàng: {e}")

def add_booking():
    try:
        # Hiển thị hộp thoại để nhập thông tin đặt chỗ
        bcode = simpledialog.askstring("Thêm đặt chỗ mới", "Nhập mã thuyền:")
        ccode = simpledialog.askstring("Thêm đặt chỗ mới", "Nhập mã khách hàng:")
        seat = simpledialog.askinteger("Thêm đặt chỗ mới", "Nhập số ghế đặt:")

        # Kiểm tra xem mã thuyền và mã khách hàng có tồn tại không
        if boats.bcode_exists(bcode) and customers.ccode_exists(ccode):
            # Tạo đặt chỗ mới và thêm vào danh sách
            new_booking = Booking(bcode, ccode, seat)
            bookings.add_to_head(new_booking)

            messagebox.showinfo("Thông báo", "Đã thêm đặt chỗ mới")
        else:
            messagebox.showerror("Lỗi", "Mã thuyền hoặc mã khách hàng không tồn tại")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm đặt chỗ mới: {e}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hệ thống đặt chỗ thuyền")

# Tạo nút để tải dữ liệu thuyền
load_boats_button = tk.Button(root, text="Tải dữ liệu thuyền", command=load_boats)
load_boats_button.pack()

# Tạo nút để thêm thuyền mới
add_boat_button = tk.Button(root, text="Thêm thuyền mới", command=add_boat)
add_boat_button.pack()

# Tạo nút để hiển thị danh sách thuyền
display_boats_button = tk.Button(root, text="Hiển thị danh sách thuyền", command=display_boats)
display_boats_button.pack()

# Tạo nút để tải dữ liệu khách hàng
load_customers_button = tk.Button(root, text="Tải dữ liệu khách hàng", command=load_customers)
load_customers_button.pack()

# Tạo nút để thêm khách hàng mới
add_customer_button = tk.Button(root, text="Thêm khách hàng mới", command=add_customer)
add_customer_button.pack()

# Tạo nút để hiển thị danh sách khách hàng
display_customers_button = tk.Button(root, text="Hiển thị danh sách khách hàng", command=display_customers)
display_customers_button.pack()

# Tạo nút để thêm đặt chỗ mới
add_booking_button = tk.Button(root, text="Thêm đặt chỗ mới", command=add_booking)
add_booking_button.pack()

# Hiển thị cửa sổ
root.mainloop()
