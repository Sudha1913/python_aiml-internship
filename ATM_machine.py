# Initial balance and PIN
balance = 1000
pin = "1234"

# Function to check balance
def check_balance():
    print("Current Balance:", balance)


# Function to deposit money
def deposit_money():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully")
        print("Updated Balance:", balance)

    else:
        print("Invalid amount")


# Function to withdraw money
def withdraw_money():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining Balance:", balance)


# Function to change PIN
def change_pin():
    global pin

    old_pin = input("Enter current PIN: ")

    if old_pin == pin:

        new_pin = input("Enter new PIN: ")
        pin = new_pin

        print("PIN changed successfully")

    else:
        print("Incorrect PIN")


# Main program using while loop
while True:

    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        change_pin()

    elif choice == "5":
        print("Thank you for using ATM !!")
        break

    else:
        print("Invalid choice")