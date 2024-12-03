# ENCAPSULATION IS ABOUT BUNDLING THE DATA (variables) AND METHODS THAT OPERATES ON THE DATA INTO A SINGLE UNIT (class) WHILE RESTRICTING ACCESS TO SOME OF THE OBJECT'S COMPONENTS.

class BankAccount:
     def __init__(self, account_number, balance):
          self.__account_number = account_number
          self.__balance = balance

     def deposit(self, amount):
          if amount > 0:
               self.__balance += amount
               print(f"{amount} deposite. New balance is {self.__balance}.")
          else:
               print("Invalid amount.")

     def withdraw(self, amount):
          if 0 < amount <= self.__balance:
               self.__balance -= amount
               print(f"{amount} withdrawn. Remaining balance is {self.__balance}")
          else:
               print("Insufficient Funds")

     def get_balance(self):
          return self.__balance

account = BankAccount(123456, 500)
account.deposit(200)
account.withdraw(100)
print(account.get_balance())