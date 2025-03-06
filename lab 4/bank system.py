class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print("Deposited ",amount," into account ",self.account_number)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ${amount}")
            print("Withdrew",amount," from account",self.account_number)

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Insufficient funds for transfer!")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(f"Transferred:${amount} to Account ${recipient_account.account_number}")
            recipient_account.transactions.append(f"Received: ${amount} from Account {self.account_number}")
            print("Transferred ",amount," to Account ",recipient_account.account_number)

    def get_balance(self):
        return f"Account {self.account_number} balance: ${self.balance}"

    def get_statement(self):
        print("Statement for Account", self.account_number)
        for transaction in self.transactions:
            print(transaction)

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def open_account(self, account_number, initial_deposit=0):
        new_account = Account(account_number, initial_deposit)
        self.accounts.append(new_account)
        print("New account", account_number, "opened for",self.name)

    def get_accounts(self):
        return [account.account_number for account in self.accounts]

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer", customer.name,"added to",self.name)

    def list_customers(self):
        return [customer.name for customer in self.customers]

#_________________________
# Create a bank
bank = Bank("Simple Bank")

# Create customers
mariam = Customer("mariam",101)
krkr = Customer("krkr",102)

# Add customers to the bank
bank.add_customer(krkr)
bank.add_customer(mariam)

# Open accounts
mariam.open_account("101", 1000)
krkr.open_account("102", 500)

# Get accounts
mariam_acc = mariam.accounts[0]
krkr_acc = krkr.accounts[0]

# Perform transactions
mariam_acc.deposit(500)
mariam_acc.withdraw(200)
mariam_acc.transfer(300, krkr_acc)

# Check balances
mariam_acc.get_balance()
krkr_acc.get_balance()
