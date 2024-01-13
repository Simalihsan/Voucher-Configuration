from voucheritem import VoucherItem
from voucherconfiguration import VoucherConfiguration

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