from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, account_id, balance, interest_rate):
        super().__init__(account_id, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_id, balance, overdraft_limit):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

class Transaction:
    def __init__(self, account_id, transaction_type, amount):
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount

class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account_balance(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account.balance
        return None

    def deposit(self, account_id, amount):
        for account in self.accounts:
            if account.account_id == account_id:
                account.deposit(amount)
                self.record_transaction(account_id, "deposit", amount)
                return True
        return False

    def withdraw(self, account_id, amount):
        for account in self.accounts:
            if account.account_id == account_id:
                account.withdraw(amount)
                self.record_transaction(account_id, "withdrawal", amount)
                return True
        return False

    def record_transaction(self, account_id, transaction_type, amount):
        transaction = Transaction(account_id, transaction_type, amount)
        # code to record the transaction

# Sample usage
savings_account = SavingsAccount(1001, 1000, 0.05)
checking_account = CheckingAccount(1002, 500, 1000)
john_doe = Customer("John Doe", "123 Main St", "555-1234")
john_doe.add_account(savings_account)
john_doe.add_account(checking_account)
john_doe.deposit(1001, 500)
john_doe.withdraw(1002, 800)
print(john_doe.get_account_balance(1001))
print(john_doe.get_account_balance(1002))


