# Crea 2 clases: Player y Item. Donde item afecte a las estadisticas de Player. 
# los item deven ser los atributos del player

class Player:
    def __init__(self, name, health, sword, money):
        self.name   = name
        self.health = health
        self.sword  = sword
        self.money  = money

    def __str__(self):
        return f"Nombre: {self.name}|Vida: {self.health}|Arma: {self.sword.name}({self.sword.damage} atk)|Dinero: {self.money}$"
    
    def give_attack(self, target):
        target.health = target.health - self.sword.damage

        if target.health < 0:
            target.health = 0

    def is_alive(self):
        return self.health > 0

class Item:
    class Sword():
        def __init__(self, name, damage):
            self.name   = name
            self.damage = damage

# Creamos espadas
wood_sword = Item.Sword(
    name   = "Espada de madera",
    damage = 20,
    )
wood_hammer = Item.Sword(
    name   = "Martillo de madera",
    damage = 15,
    )

# Creamos a personajee
hero_01 = Player(
    name   = "Arthas",
    health = 200,
    sword  = wood_sword,
    money  = 50,
    )
hero_02 = Player(
    name   = "Malganis",
    health = 200,
    sword  = wood_hammer,
    money  = 100,
)

# Realizamos la interaccions
while hero_01.is_alive() and hero_02.is_alive() :
    hero_01.give_attack(hero_02)
    hero_02.give_attack(hero_01)

    print("-----------------------------------")
    print(hero_01)
    print(hero_02)

print("-----------------")
print("Fin del a partida")
print("-----------------")

# 61 minutos