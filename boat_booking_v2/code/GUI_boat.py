import tkinter as tk
from tkinter import messagebox, simpledialog
from Boat_system import Function, BookingSystem
            
boats = Function()
customers = Function()
booking = BookingSystem()

def load_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(' | ')
            if file_name == "data/boat.txt":
                boats.add_to_head(data)
            elif file_name == "data/customer.txt":
                customers.add_to_end(data)

def load_boats():
    try:
        load_from_file("data/boat.txt")
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
    new_boat = [bcode, boat_name, seat, booked, depart_place, rate]
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

def save_boats():
    try:
        boats.save_to_file("data/boat.txt")
        messagebox.showinfo("Thông báo", "Đã lưu danh sách thuyền thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu danh sách thuyền: {e}")

def search_boat():
    bcode = simpledialog.askstring("Tìm kiếm thuyền", "Nhập mã thuyền:")
    boat = boats.search_by_bcode(bcode)
    if boat:
        messagebox.showinfo("Thông báo", f"Thông tin thuyền: {boat}")
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy thuyền với mã đã cho")

def delete_boat():
    bcode = simpledialog.askstring("Xóa thuyền", "Nhập mã thuyền:")
    if boats.delete_by_bcode(bcode):
        messagebox.showinfo("Thông báo", "Đã xóa thuyền")
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy thuyền với mã đã cho")

def add_boat_before():
    xCode = simpledialog.askstring("Thêm thuyền", "Nhập mã thuyền để thêm trước:")
    if xCode:
        # Hiển thị hộp thoại để nhập thông tin thuyền mới
        bcode = simpledialog.askstring("Thêm thuyền mới", "Nhập mã thuyền:")
        boat_name = simpledialog.askstring("Thêm thuyền mới", "Nhập tên thuyền:")
        seat = simpledialog.askinteger("Thêm thuyền mới", "Nhập số ghế:")
        booked = simpledialog.askinteger("Thêm thuyền mới", "Nhập số ghế đã đặt:")
        depart_place = simpledialog.askstring("Thêm thuyền mới", "Nhập nơi khởi hành:")
        rate = simpledialog.askfloat("Thêm thuyền mới", "Nhập tỷ lệ:")

        # Tạo thuyền mới và thêm vào danh sách trước thuyền có mã là xCode
        new_boat = [bcode, boat_name, seat, booked, depart_place, rate]
        boats.add_before_bcode(new_boat, xCode)

        messagebox.showinfo("Thông báo", "Đã thêm thuyền mới trước thuyền có mã " + xCode)
        
def delete_boat_before():
    xCode = simpledialog.askstring("Xóa thuyền", "Nhập mã thuyền để xóa trước:")
    if xCode:
        if boats.bcode_exists(xCode):
            boats.delete_before_bcode(xCode)
            messagebox.showinfo("Thông báo", "Đã xóa thành công trước thuyền có mã "+xCode)
        else:
            messagebox.showerror("Lỗi", f"Mã thuyền {xCode} không tồn tại trong danh sách.")

def load_customers():
    try:
        # Tải dữ liệu khách hàng từ file
        load_from_file("data/customer.txt")
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
        new_customer = [ccode, cus_name, phone]
        customers.add_to_end(new_customer)

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
            customer_info += f"Mã khách hàng: {customer.ccode}, Tên khách hàng: {customer.cus_name}, Số điện thoại: {customer.phone}\n"

            # Chuyển sang nút tiếp theo
            current_node = current_node.next

        # Hiển thị thông tin tất cả các khách hàng
        messagebox.showinfo("Thông báo", customer_info)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể hiển thị danh sách khách hàng: {e}")

def search_customer():
    try:
        # Hiển thị hộp thoại để nhập mã khách hàng
        ccode = simpledialog.askstring("Tìm kiếm khách hàng", "Nhập mã khách hàng:")

        # Tìm kiếm khách hàng theo mã
        customer = customers.search_by_ccode(ccode)

        if customer is not None:
            # Hiển thị thông tin khách hàng
            messagebox.showinfo("Thông báo", f"Mã khách hàng: {customer.ccode}, Tên khách hàng: {customer.cus_name}, Số điện thoại: {customer.phone}")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy khách hàng với mã đã cho")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tìm kiếm khách hàng: {e}")

def delete_customer():
    try:
        # Hiển thị hộp thoại để nhập mã khách hàng
        ccode = simpledialog.askstring("Xóa khách hàng", "Nhập mã khách hàng:")

        # Xóa khách hàng theo mã
        if customers.delete_by_ccode(ccode):
            messagebox.showinfo("Thông báo", "Đã xóa khách hàng")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy khách hàng với mã đã cho")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xóa khách hàng: {e}")

def save_customers():
    try:
        # Lưu danh sách khách hàng vào file
        customers.save_to_file("data/customer.txt")
        messagebox.showinfo("Thông báo", "Đã lưu danh sách khách hàng thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu danh sách khách hàng: {e}")

def sort_boats():
    try:
        # Sắp xếp danh sách thuyền theo mã thuyền
        boats.sort_by_bcode()
        messagebox.showinfo("Thông báo", "Đã sắp xếp danh sách thuyền theo mã thuyền")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp danh sách thuyền: {e}")

def add_booking():
    bcode = simpledialog.askstring("Nhập", "Nhập mã thuyền:")
    ccode = simpledialog.askstring("Nhập", "Nhập mã khách hàng:")
    seat_booked = simpledialog.askinteger("Nhập", "Nhập số lượng ghế muốn đặt:")

    # Kiểm tra xem mã thuyền và mã khách hàng có tồn tại trong danh sách không
    boat = boats.search_by_bcode(bcode)
    customer = customers.search_by_ccode(ccode)

    # Kiểm tra điều kiện để chấp nhận dữ liệu đặt chỗ
    if boat is None or customer is None:
        messagebox.showerror("Lỗi", "Mã thuyền hoặc mã khách hàng không tồn tại.")
        return False
    elif booking.booking_exists(bcode, ccode):
        messagebox.showerror("Lỗi", "Đã tồn tại đặt chỗ với mã thuyền và mã khách hàng này.")
        return False
    elif boat.seat == boat.booked:
        messagebox.showinfo("Thông tin", "Thuyền đã hết chỗ.")
        return False
    elif seat_booked <= (boat.seat - boat.booked):
        # Dữ liệu được chấp nhận và thêm vào cuối danh sách đặt chỗ
        booking.add_to_end([bcode, ccode, seat_booked])
        boat.booked += seat_booked
        messagebox.showinfo("Thành công", "Đặt chỗ thành công.")
        return True
    else:
        messagebox.showerror("Lỗi", "Không đủ chỗ ngồi.")
        return False
        
def display_bookings():
    try:
        # Lấy nút đầu tiên của danh sách đặt chỗ
        current_node = booking.head

        # Tạo một chuỗi để lưu thông tin của tất cả các đặt chỗ
        booking_info = ""

        # Duyệt qua danh sách đặt chỗ
        while current_node is not None:
            # Lấy thông tin đặt chỗ
            booking_data = current_node.data

            # Thêm thông tin đặt chỗ vào chuỗi
            booking_info += f"Mã thuyền: {booking_data.bcode}, Mã khách hàng: {booking_data.ccode}, Số ghế đã đặt: {booking_data.seat_booked}\n"

            # Chuyển sang nút tiếp theo
            current_node = current_node.next

        # Hiển thị thông tin tất cả các đặt chỗ
        messagebox.showinfo("Thông báo", booking_info)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể hiển thị danh sách đặt chỗ: {e}")

def save_bookings():
    try:
        # Lưu danh sách đặt chỗ vào file
        booking.save_to_file("data/booking.txt")
        messagebox.showinfo("Thông báo", "Đã lưu danh sách đặt chỗ thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu danh sách đặt chỗ: {e}")

def sort_bookings():
    try:
        # Sắp xếp danh sách đặt chỗ theo mã thuyền và mã khách hàng
        booking.sort_by_bcode_ccode()
        messagebox.showinfo("Thông báo", "Đã sắp xếp danh sách đặt chỗ")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp danh sách đặt chỗ: {e}")
        
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hệ thống đặt chỗ thuyền")

# Tạo các frame cho Boat, Customer và Booking với khoảng cách
frame_boat = tk.Frame(root, padx=10)
frame_boat.pack(side=tk.LEFT)

frame_customer = tk.Frame(root, padx=10)
frame_customer.pack(side=tk.LEFT)

frame_booking = tk.Frame(root, padx=10)
frame_booking.pack(side=tk.LEFT)

# Tạo tiêu đề cho mỗi cột
label_boat = tk.Label(frame_boat, text="Boat", font=("Arial", 16, "bold"))
label_boat.pack()

label_customer = tk.Label(frame_customer, text="Customer", font=("Arial", 16, "bold"))
label_customer.pack()

label_booking = tk.Label(frame_booking, text="Booking", font=("Arial", 16, "bold"))
label_booking.pack()

# Tạo các nút cho Boat
load_boats_button = tk.Button(frame_boat, text="Tải dữ liệu thuyền", command=load_boats)
load_boats_button.pack()

add_boat_button = tk.Button(frame_boat, text="Thêm thuyền mới", command=add_boat)
add_boat_button.pack()

sort_boats_button = tk.Button(frame_boat, text="Sắp xếp danh sách thuyền", command=sort_boats)
sort_boats_button.pack()

display_boats_button = tk.Button(frame_boat, text="Hiển thị danh sách thuyền", command=display_boats)
display_boats_button.pack()

save_boats_button = tk.Button(frame_boat, text="Lưu danh sách thuyền", command=save_boats)
save_boats_button.pack()

search_boat_button = tk.Button(frame_boat, text="Tìm kiếm thuyền", command=search_boat)
search_boat_button.pack()

delete_boat_button = tk.Button(frame_boat, text="Xóa thuyền", command=delete_boat)
delete_boat_button.pack()

add_boat_before_button = tk.Button(frame_boat, text="Thêm thuyền trước", command=add_boat_before)
add_boat_before_button.pack()

delete_boat_before_button = tk.Button(frame_boat, text="Xóa thuyền trước", command=delete_boat_before)
delete_boat_before_button.pack()

# Tạo các nút cho Customer
load_customers_button = tk.Button(frame_customer, text="Tải dữ liệu khách hàng", command=load_customers)
load_customers_button.pack()

add_customer_button = tk.Button(frame_customer, text="Thêm khách hàng mới", command=add_customer)
add_customer_button.pack()

delete_customer_button = tk.Button(frame_customer, text="Xóa khách hàng", command=delete_customer)
delete_customer_button.pack()

display_customers_button = tk.Button(frame_customer, text="Hiển thị danh sách khách hàng", command=display_customers)
display_customers_button.pack()

search_customer_button = tk.Button(frame_customer, text="Tìm kiếm khách hàng", command=search_customer)
search_customer_button.pack()

save_customers_button = tk.Button(frame_customer, text="Lưu danh sách khách hàng", command=save_customers)
save_customers_button.pack()

# Tạo nút cho Booking
add_booking_button = tk.Button(frame_booking, text="Thêm đặt chỗ mới", command=add_booking)
add_booking_button.pack()

display_bookings_button = tk.Button(frame_booking, text="Hiển thị danh sách đặt chỗ", command=display_bookings)
display_bookings_button.pack()

save_bookings_button = tk.Button(frame_booking, text="Lưu danh sách đặt chỗ", command=save_bookings)
save_bookings_button.pack()

sort_bookings_button = tk.Button(frame_booking, text="Sắp xếp danh sách đặt chỗ", command=sort_bookings)
sort_bookings_button.pack()

# Hiển thị cửa sổ
root.mainloop()
