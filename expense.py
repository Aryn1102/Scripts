def main():
    balance=0.0
    transactions=[]

    program= show_menu()
    while program != 7:
        if program == 1:
            balance, transactions = add_income(balance, transactions)
        elif program == 2:
            balance, transactions = add_expense(balance, transactions)
        elif program == 3:
            view_transactions(transactions)
        elif program == 4:
            transactions = delete_transaction(transactions)
        elif program == 5:
            show_balance(balance)
        elif program == 6:
            show_summary(transactions)
        program= show_menu()

def show_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Delete Transaction")
    print("5. Show Balance")
    print("6. Show Summary")
    print("7. Exit")
    return int(input("Select an option: "))

def add_income(balance, transactions):
    transaction_type = "Income"
    input_amount = get_amount()
    category = input("Enter category: ")
    description = input("Enter description: ")
    balance += input_amount
    transactions.append({ "type": transaction_type, "amount": input_amount, "category": category, "description": description })
    return balance, transactions

def add_expense(balance, transactions):
    transaction_type = "Expense"
    input_amount = get_amount()
    category = input("Enter category: ")
    description = input("Enter description: ")
    balance -= input_amount
    transactions.append({ "type": transaction_type, "amount": input_amount, "category": category, "description": description })
    return balance, transactions

def view_transactions(transactions):
    for transaction in transactions:
        print(f"{transaction['type']}: ${transaction['amount']:.2f}")

def delete_transaction(transactions):
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction['type']}: ${transaction['amount']:.2f}")
    index = int(input("Enter the index of the transaction to delete: "))
    if 1 <= index <= len(transactions):
        del transactions[index - 1]
    return transactions

def show_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def show_summary(transactions):
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == "Income")
    total_expense = sum(transaction['amount'] for transaction in transactions if transaction['type'] == "Expense")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Net Balance: ${total_income - total_expense:.2f}")

def get_amount():
    return float(input("Enter amount: "))

if __name__ == "__main__":
    main()