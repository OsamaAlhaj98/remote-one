# Online Laptop Shopping System
# NO FUNCTIONS USED — only loops, if/else, lists, dictionaries

# -------------------------
#        CONSTANTS
# -------------------------
BASE_PRICE = 1200
GST_RATE = 0.05
DISCOUNT_THRESHOLD_1 = 1500
DISCOUNT_THRESHOLD_2 = 2000
SHIPPING_THRESHOLD = 2000
SHIPPING_LOW = 20
SHIPPING_HIGH = 10
MAX_CONFIGS = 3

# Additional costs
PROCESSOR_COST = {"i5": 0, "i7": 200, "i9": 400}
RAM_COST = {"8GB": 0, "16GB": 100, "32GB": 200}
DISPLAY_COST = {"Full HD": 0, "4K UHD": 300}
SSD_COST = {"256GB": 0, "512GB": 150, "1TB": 300}

# -------------------------
#       STOCK INPUT
# -------------------------
stock_input = input("Enter the number of laptops available in stock (non-negative integer): ").strip()
while not (stock_input.isdigit() and int(stock_input) >= 0):
    stock_input = input("Invalid. Enter a non-negative integer for stock: ").strip()

available_stock = int(stock_input)
print("Available stock set to:", available_stock)
print()

# List to store configurations
configs = []

config_count = 0

# ============================
#   MAIN CONFIGURATION LOOP
# ============================
continue_config = "yes"

while config_count < MAX_CONFIGS and available_stock > 0 and continue_config == "yes":

    print("Configuring Laptop #", config_count + 1)

    # -------------------------
    #     PROCESSOR INPUT
    # -------------------------
    proc_choice = input("Choose processor (i5, i7, i9): ").strip()
    while proc_choice not in PROCESSOR_COST:
        proc_choice = input("Invalid. Choose processor (i5, i7, i9): ").strip()

    # -------------------------
    #       RAM INPUT
    # -------------------------
    ram_choice = input("Choose RAM (8GB, 16GB, 32GB): ").strip()
    while ram_choice not in RAM_COST:
        ram_choice = input("Invalid. Choose RAM (8GB, 16GB, 32GB): ").strip()

    # -------------------------
    #     DISPLAY INPUT
    # -------------------------
    disp_choice = input("Choose display (Full HD, 4K UHD): ").strip()
    while disp_choice not in DISPLAY_COST:
        disp_choice = input("Invalid. Choose display (Full HD, 4K UHD): ").strip()

    # -------------------------
    #       SSD INPUT
    # -------------------------
    ssd_choice = input("Choose SSD (256GB, 512GB, 1TB): ").strip()
    while ssd_choice not in SSD_COST:
        ssd_choice = input("Invalid. Choose SSD (256GB, 512GB, 1TB): ").strip()

    # -------------------------
    #     QUANTITY INPUT
    # -------------------------
    qty_input = input("Enter quantity (1 to {}): ".format(available_stock)).strip()
    while not (qty_input.isdigit() and 1 <= int(qty_input) <= available_stock):
        qty_input = input("Invalid. Enter quantity (1 to {}): ".format(available_stock)).strip()

    quantity = int(qty_input)

    # -------------------------
    #     PRICE CALCULATIONS
    # -------------------------
    unit_price = BASE_PRICE + PROCESSOR_COST[proc_choice] + RAM_COST[ram_choice] + DISPLAY_COST[disp_choice] + SSD_COST[ssd_choice]
    subtotal = unit_price * quantity

    # Discount
    if subtotal > DISCOUNT_THRESHOLD_2:
        discount_rate = 0.10
    elif subtotal > DISCOUNT_THRESHOLD_1:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount_amount = round(subtotal * discount_rate, 2)

    # Shipping
    if subtotal < SHIPPING_THRESHOLD:
        shipping = SHIPPING_LOW
    else:
        shipping = SHIPPING_HIGH

    total_after_discount_shipping = round(subtotal - discount_amount + shipping, 2)
    gst_amount = round(total_after_discount_shipping * GST_RATE, 2)
    total_with_gst = round(total_after_discount_shipping + gst_amount, 2)

    # -------------------------
    #     STORE RESULT
    # -------------------------
    config = {
        "Processor": proc_choice,
        "RAM": ram_choice,
        "Display": disp_choice,
        "SSD": ssd_choice,
        "Quantity": quantity,
        "Unit Price": unit_price,
        "Subtotal": round(subtotal, 2),
        "Discount Rate": discount_rate,
        "Discount Amount": discount_amount,
        "Shipping": shipping,
        "Total After Discount & Shipping": total_after_discount_shipping,
        "GST Amount": gst_amount,
        "Total With GST": total_with_gst
    }

    configs.append(config)

    # Update stock
    available_stock -= quantity
    config_count += 1

    print("Configuration added. Remaining stock:", available_stock)
    print()

    # Ask user if they want to continue
    if config_count < MAX_CONFIGS and available_stock > 0:
        continue_config = input("Do you want to add another configuration? (yes/no): ").strip().lower()
        while continue_config not in ("yes", "no"):
            continue_config = input("Invalid. Enter yes/no: ").strip().lower()

# ============================
#       SUMMARY OUTPUT
# ============================

print("\n=== PURCHASE SUMMARY ===\n")

if len(configs) == 0:
    print("No configurations were made. Nothing to purchase.")
else:
    total_laptops = 0
    total_before_discount = 0.0
    total_discount = 0.0
    final_total_with_gst = 0.0

    i = 1
    for c in configs:
        print("Laptop Configuration #", i)
        print(" Processor:", c["Processor"])
        print(" RAM:", c["RAM"])
        print(" Display:", c["Display"])
        print(" SSD:", c["SSD"])
        print(" Quantity:", c["Quantity"])
        print(" Unit Price: $", format(c["Unit Price"], ".2f"))
        print(" Subtotal: $", format(c["Subtotal"], ".2f"))
        print(" Discount ({:.0f}%): -$".format(c["Discount Rate"] * 100), format(c["Discount Amount"], ".2f"))
        print(" Shipping: $", format(c["Shipping"], ".2f"))
        print(" Total after Discount & Shipping: $", format(c["Total After Discount & Shipping"], ".2f"))
        print(" GST (5%): $", format(c["GST Amount"], ".2f"))
        print(" Final Total (with GST): $", format(c["Total With GST"], ".2f"))
        print("--------------------------------------")

        total_laptops += c["Quantity"]
        total_before_discount += c["Subtotal"]
        total_discount += c["Discount Amount"]
        final_total_with_gst += c["Total With GST"]

        i = i + 1

    print("\nFINAL TOTALS:")
    print(" Total laptops purchased:", total_laptops)
    print(" Total before discount: $", format(total_before_discount, ".2f"))
    print(" Total discount: -$", format(total_discount, ".2f"))
    print(" Final amount including GST: $", format(final_total_with_gst, ".2f"))

print("\nThank you for using the Online Laptop Shopping System!")
