#Python simple Banking Application

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = input("Enter an amount to be deposited: ")

    if amount < 0:
        print("That's not a valid amount")
    else

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Banking Application")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("that is not a valid choice")

print("thank you! Have a nice day!")
























