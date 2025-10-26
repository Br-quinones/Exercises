# Crear una instancia de Player: hero = Player("Hero", 100, 15)
# Crear una instancia de Enemy: goblin = Enemy("Goblin", 50, 5)
# Imprimir el estado inicial (ej: print(f"{goblin.name} tiene {goblin.health} de vida."))
# Hacer que el héroe ataque al goblin: hero.attack(goblin)
# Imprimir el estado del goblin de nuevo para ver cómo bajó su vida.
# Reto extra: Intenta usar un bucle while que continúe mientras goblin.is_alive() sea True, y que el hero ataque en cada iteración.

class Enemy:
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense

    def __str__(self):
        return f"Nombre: {self.name} | Salud: {self.health} | Defensa: {self.defense}"

    def take_damage(self, damage_amount):
        if (self.defense - damage_amount) < 0:
            self.health = self.health + (self.defense - damage_amount)
        
        if self.health < 0:
            self.health  = 0

    def is_alive(self):
        return self.health > 0

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def __str__(self):
        return f"Nombre: {self.name} | Salud: {self.health} | ataque: {self.attack_power}"

    def attack(self, target):
        if isinstance(target,Enemy):
            target.take_damage(self.attack_power)

hero = Player("Arthas", 100, 25)
goblin = Enemy("Goblin", 50, 10)

print("--- Competidores para la batalla ---")
print(hero)
print(goblin)

print("------------------------------------")
while goblin.is_alive() :
    print(goblin)
    hero.attack(goblin)
print("------------------------------------")

print(f"{goblin.name} ha sido derrotado por {hero.name}.")

# 50 minutos