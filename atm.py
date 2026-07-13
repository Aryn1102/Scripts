import sys

def main():
    password = 1234
    balance = 0
    transaction_history_list = []
    login(password)
    while True:
        program = show_menu()
        if program == 1:
            print(f"Your balance is: {check_balance(balance)}")
        elif program == 2:
            balance = deposit(balance, transaction_history_list)
        elif program == 3:
            balance = withdraw(balance, transaction_history_list)
        elif program == 4:
            password = change_pin(password)
        elif program == 5:
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def login(password):
    count = 0
    while True:
        pin = int(input("Enter your PIN: "))
        if pin == password:
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN. Please try again.")
            count+=1
            if count == 3:
                sys.exit("Too many incorrect attempts. Please try again later.")
            
def show_menu():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")
    return int(input("Enter your choice: "))

def check_balance(balance):
    return balance

def deposit(balance, transaction_history_list):
    input_amount = float(get_amount("Enter the amount to deposit: "))
    if input_amount > 0:
        balance = check_balance(balance) + input_amount
        check_balance(balance)
        transaction_history(input_amount, 0, transaction_history_list)
        return balance

def withdraw(balance, transaction_history_list):
    input_amount = get_amount("Enter the amount to withdraw: ")
    balance = check_balance(balance)
    if input_amount > 0 and input_amount <= balance:
        balance -= input_amount
        transaction_history(0, input_amount, transaction_history_list)
        return balance
    else:
        print("Insufficient funds or invalid amount.")
    return balance

def transaction_history(deposit_amount, withdraw_amount, transaction_history_list):
    if deposit_amount > 0:
        transaction_history_list.append(("Deposit: ", deposit_amount))
    if withdraw_amount > 0:
        transaction_history_list.append(("Withdrawal: ", withdraw_amount))
    return transaction_history_list

def change_pin(password):
    password = int(get_amount("Enter your new PIN: "))   
    print("PIN changed successfully!")
    return password

def  get_amount(prompt):
    amount = float(input(prompt))
    return amount

def exit_program():
    sys.exit("Exiting the program. Goodbye!")