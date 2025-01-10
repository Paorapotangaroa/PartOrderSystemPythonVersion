# Collect inputs
vendor_code = input("What is the 3-4 digit Vendor Code?").upper()
model_num = input("What is the model number?")
sku = input("What is the sku number?")
cust_name = input("What is the customer's name?").upper()
part = input("What part are you ordering?").upper()
part_description = input("Briefly describe the part. Example: Throw Pillow").upper()
quantity = input("Quantity? Example one(1)").upper()
nine_mil_num = input("What is the 9Mil number?")
first_initial = cust_name.split()[0][0]
last_name = cust_name.split()[-1]
delivery_date = input("What was the delivery date?").upper()
paying_party = input("Who is paying? Example: RC Willey or Factory").upper()
notes = input("Any additional notes? Example: Cust is paying or inconvenience or RC Willey lost part").upper()

# Field 2
while_tracker = input(f"Copy and Paste in Field 2. {vendor_code}\n Enter Y to continue to the next step").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 2. {vendor_code}\n Enter Y to continue to the next step").upper()

# Field 3
field3_value = model_num + "/" + part
while_tracker = input(f"Copy and Paste in Field 3. Enter Y to continue to the next step {field3_value}").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 3. Enter Y to continue to the next step {field3_value}").upper()

# Field 7
field7_value = first_initial + " " + last_name + " " + nine_mil_num + " " + sku
input("Hit Enter 3 Times")
while_tracker = input(f"Copy and Paste in Field 7. Enter Y to continue to the next step {field7_value}").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 7. Enter Y to continue to the next step {field7_value}").upper()

# Field 8
while_tracker = input("Copy and Paste in Field 8. Enter Y to continue to the next step PRT81").upper()
while while_tracker != "Y":
    while_tracker = input("Copy and Paste in Field 8. Enter Y to continue to the next step PRT81").upper()

# Field 14
field14_value = paying_party + " Expense " + "(Notes: " + notes + ")"
input("Enter to Field 14")
while_tracker = input(f"Copy and Paste in Field 14. Enter Y to continue to the next step {field14_value}").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 14. Enter Y to continue to the next step {field14_value}").upper()

# Field 15
field15_line1 = quantity + " " + part_description
field15_line2 = "Model#" + model_num + " " + delivery_date
field15_line3 = input("Copy and Paste in Field 15 Line 3. Enter Y to continue to the next step").upper()
while_tracker = input(f"Copy and Paste in Field 15 Line 1. Enter Y to continue to the next step {field15_line1}").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 15 Line 1. Enter Y to continue to the next step {field15_line1}").upper()
while_tracker = input(f"Copy and Paste in Field 15 Line 2. Enter Y to continue to the next step {field15_line2}").upper()
while while_tracker != "Y":
    while_tracker = input(f"Copy and Paste in Field 15 Line 2. Enter Y to continue to the next step {field15_line2}").upper()
while_tracker = input(f"Copy and Paste in Field 15 Line 3. Enter Y to continue to the next step {field15_line3}").upper()

# Compose email
employee_name = input("What is your name? (Default: Toa Pita)").strip() or "Toa Pita"
po_num = input("What is the PO number?")
email_message = (
    "Subject: PO#" + po_num + "\n\n"
    + "Hello,\n\n"
    + "I just wanted to confirm that you received our order for PO#" + po_num + ". Can I get an ETA?\n\n"
    + "Thanks!\n\n"
    + employee_name
)
print(email_message)
