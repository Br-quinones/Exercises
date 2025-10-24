class BankAccount:
    bank_name = "Banco Dev"

    def __init__(self, owner_name,initial_balance):
        self.owner_name = owner_name
        self.balance = initial_balance

    def __str__(self):
        return f"Titular: {self.owner_name} & Saldo: ${self.balance}"

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposito exitoso de ${amount}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Retiro exitoso de ${amount}")

# Creamos cuenta
account_01 = BankAccount("Fulano",500)

# Verificamos a que banco pertence
print(f"Esta cuenta pertence al banco: {BankAccount.bank_name}")

# Imprimimos el __str__
print(account_01)

# Introduzimos 100 $
account_01.deposit(100)

# Retiramos 240 $
account_01.withdraw(250)

# Imprimimos el __str__
print(account_01)

# 47 minutos