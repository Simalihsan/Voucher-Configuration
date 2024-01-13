from voucheritem import VoucherItem
from voucherconfiguration import VoucherConfiguration
from vouchersystem import VoucherSystem

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