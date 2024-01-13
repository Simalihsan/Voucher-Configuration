from voucheritem import VoucherItem

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