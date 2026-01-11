class DigitalWallet():
    def __init__(self, owner_name, initial_balance=0):
        self.owner = owner_name
        self.__balance = initial_balance
        self.__history = []

    def __str__(self):
        return f"The user {self.owner} have a balance of {self.__balance}$"

    @property
    def balance(self):
        return self.__balance
    
    @property
    def history(self):
        history_copy = self.__history
        return history_copy
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("Only are valid numbers") 
        elif amount < 0:
            print(f"A negative deposit is invalid:") 
        else:
            self.__balance += amount
            self.__history.append(f"+{amount}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Only are valid numbers") 
        elif amount < 0:
            print(f"A negative deposit is invalid:")
        elif self.__balance - amount < 0:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            self.__history.append(f"-{amount}")

my_wallet = DigitalWallet(owner_name="Br_quinones",initial_balance=100)
