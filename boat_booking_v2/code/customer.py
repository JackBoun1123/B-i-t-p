class Customer:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
    def __str__(self):
        return f"{self.ccode} | {self.cus_name} | {self.phone}\n"