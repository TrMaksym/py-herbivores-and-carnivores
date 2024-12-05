class Animal:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"

class Herbivore(Animal):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False

    def hide(self):
        self.hidden = not self.hidden
        print(f"{self.name} is now {'hidden' if self.hidden else 'visible'}.")

class Carnivore(Animal):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False

    def bite(self, herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden:
                print(f"{self.name} cannot bite {herbivore.name} because they are hidden.")
            else:
                herbivore.take_damage(50)
                print(f"{self.name} bit {herbivore.name}. {herbivore.name}'s health: {herbivore.health}")
        else:
            print(f"{self.name} cannot bite another carnivore.")
