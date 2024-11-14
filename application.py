#Python simple Banking Application

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = input("Enter an amount to be deposited: ")

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
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
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("that is not a valid choice")

    print("thank you! Have a nice day!")


if __name__ == '__main__':
    main()