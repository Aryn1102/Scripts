dict={
        "Raj":{
        "pin":1234,
        "balance":1000
    },
    "Rahul":{
        "pin":5678,
        "balance":2000
    }
}

input_name=input("Enter your name: ")
input_pin=int(input("Enter your pin: "))
if input_name in dict:
    if dict[input_name]["pin"]==input_pin:
        print("Welcome",input_name)
        print("Your balance is:",dict[input_name]["balance"])

enquiry = input("Do you want to check your balance? (yes/no): ")
if enquiry.lower() == "yes":
    print("Your balance is:", dict[input_name]["balance"])

deposit = input("Do you want to deposit money? (yes/no): ")
if deposit.lower() == "yes":
    deposit_amount = float(input("Enter the amount to deposit: "))
    dict[input_name]["balance"] += deposit_amount
    print("Deposit successful. Your new balance is:", dict[input_name]["balance"])

withdraw = input("Do you want to withdraw money? (yes/no): ")
if withdraw.lower() == "yes":
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if withdraw_amount <= dict[input_name]["balance"]:
        dict[input_name]["balance"] -= withdraw_amount
        print("Withdrawal successful. Your new balance is:", dict[input_name]["balance"])
    else:
        print("Insufficient balance.")

transfer = input("Do you want to transfer money? (yes/no): ")
if transfer.lower() == "yes":
    recipient_name = input("Enter the recipient's name: ")
    if recipient_name in dict:
        transfer_amount = float(input("Enter the amount to transfer: "))
        if transfer_amount <= dict[input_name]["balance"]:
            dict[input_name]["balance"] -= transfer_amount
            dict[recipient_name]["balance"] += transfer_amount
            print("Transfer successful. Your new balance is:", dict[input_name]["balance"])
        else:
            print("Insufficient balance.")
    else:
        print("Recipient not found.")