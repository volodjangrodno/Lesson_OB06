# Определение класса Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} наносит удар {other.name}, у {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


# Определение класса Game
class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        round_counter = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_counter}")
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            round_counter += 1

        if self.player.is_alive():
            print(f"\n{self.player.name} победил!")
        else:
            print(f"\n{self.computer.name} победил!")


# Создание экземпляров героев и начало игры
player = Hero("Игрок")
computer = Hero("Компьютер")

game = Game(player, computer)
game.start()