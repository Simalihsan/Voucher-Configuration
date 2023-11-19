class VoucherItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: Rs.{self.amount}"

class VoucherConfiguration:
    def __init__(self, voucher_number, max_items):
        self.voucher_number = voucher_number
        self.max_items = max_items
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
            print(f"{item.description} added to the voucher.")
        else:
            print("Maximum items reached for this voucher.")

    def calculate_total_amount(self):
        total_amount = sum(item.amount for item in self.items)
        return total_amount

    def display_voucher(self):
        print(f"Voucher Number: {self.voucher_number}")
        for item in self.items:
            print(item)
        print(f"Total Amount: Rs.{self.calculate_total_amount()}")

class VoucherSystem:
    def __init__(self):
        self.vouchers = {}

    def create_voucher(self, voucher_number, max_items):
        if voucher_number not in self.vouchers:
            self.vouchers[voucher_number] = VoucherConfiguration(voucher_number, max_items)
            print(f"Voucher {voucher_number} created.")
        else:
            print("Voucher number already exists.")

    def add_item_to_voucher(self, voucher_number, item):
        if voucher_number in self.vouchers:
            self.vouchers[voucher_number].add_item(item)
        else:
            print("Voucher number does not exist.")

    def display_voucher_details(self, voucher_number):
        if voucher_number in self.vouchers:
            self.vouchers[voucher_number].display_voucher()
        else:
            print("Voucher number does not exist.")

# Creating a Voucher System
voucher_system = VoucherSystem()

# Creating Vouchers
voucher_system.create_voucher("00001001", 9)

# Creating Voucher Items
item1 = VoucherItem("Books", 5000)
item2 = VoucherItem("Laboratory Equipment", 10000)
item3 = VoucherItem("Software License", 5000)
item4 = VoucherItem("Tuition Fee", 20000)
item5 = VoucherItem("Library Fund", 5000)
item6 = VoucherItem("Electricity cost", 5000)
item7 = VoucherItem("Internet", 5000)
item8 = VoucherItem("Vehicle Points Fee", 7000)
item9 = VoucherItem("Others Funds", 5000)

# Adding Items to Vouchers
voucher_system.add_item_to_voucher("00001001", item1)
voucher_system.add_item_to_voucher("00001001", item2)
voucher_system.add_item_to_voucher("00001001", item3)
voucher_system.add_item_to_voucher("00001001", item4)
voucher_system.add_item_to_voucher("00001001", item5)
voucher_system.add_item_to_voucher("00001001", item6)
voucher_system.add_item_to_voucher("00001001", item7)
voucher_system.add_item_to_voucher("00001001", item8)
voucher_system.add_item_to_voucher("00001001", item9)

# Displaying Voucher Details
voucher_system.display_voucher_details("00001001")

