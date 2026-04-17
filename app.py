class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""

    def registration(self, id, name):
        self.id = id
        self.name = name
        print("Registration successful")

    def display(self):
        print("Customer ID:", self.id)
        print("Name:", self.name)


class Account:
    def __init__(self, acc_no=1, balance=100):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("-------------------------")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            print("-------------------------")
        else:
            self.balance -= amount
            print("Withdrawal:", amount)
            print("-------------------------")

    def show_balance(self):
        print("Current Balance:", self.balance)
        print("-------------------------")


class Transaction:
    def __init__(self, trans_id, amount):
        self.trans_id = trans_id
        self.amount = amount

    def display_transaction(self):
        print("Transaction ID:", self.trans_id, "Amount:", self.amount)
        print("-----------------------------------")
customer = Customer()
account = Account()
transactions = []
t_id = 0

while True:
    print("\n---------- BANK SYSTEM ------------")
    print("1. REGISTRATION")
    print("2. DEPOSIT")
    print("3. WITHDRAWAL")
    print("4. BALANCE")
    print("5. CUSTOMER DETAILS")
    print("6. TRANSACTION HISTORY")
    print("7. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_id = input("Enter User Id: ")
        if len(user_id) <= 20:
            name = input("Enter User Name: ")
            customer.registration(user_id, name)
        else:
            print("!!User id is too long!!")

    elif choice == 2:
        dep = int(input("Enter amount to deposit: "))
        account.deposit(dep)
        account.show_balance()
        t_id += 1
        transactions.append(Transaction(t_id, dep))

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        account.withdrawal(amt)
        account.show_balance()
        t_id += 1
        transactions.append(Transaction(t_id, amt))

    elif choice == 4:
        account.show_balance()

    elif choice == 5:
        customer.display()

    elif choice == 6:
        print("Transaction History:")
        for t in transactions:
            t.display_transaction()

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
