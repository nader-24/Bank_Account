class bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(f"{self.name} have $ {self.__balance:.2f}.")

    def deposit(self, deposit):
        if deposit:
            self.__balance = self.__balance + deposit
            print(f"You successfully deposit $ {deposit:.2f}.")
            self.get_balance()
        else:
            print("plaese Enter a positive value")

    def withdraw(self, withdraw):
        if (self.__balance - withdraw) >= 0:
            print(f"you successfuly withdraw $ {withdraw:.2f}. ")
            self.__balance = self.__balance-withdraw
            self.get_balance()
        else:
            print("You don't have $ {withdraw:.2f}")
            self.get_balance()
