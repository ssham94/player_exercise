class player:
    lives = 5
    gold_coins = 0
    health_points = 10

    def __str__(self):
        return f"You have {self.lives} lives, {self.gold_coins} gold, and {self.health_points} HP"

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()

    def restart(self):
        self.lives = 5
        self.gold_coins = 0
        self.health_points = 0

    def do_battle(self, damage_taken):
        self.health_points -= damage_taken
        if self.health_points <= 0:
            self.restart()
    

player1 = player()
print(player1)

# Testing that collect_treasure is working as intended
for i in range(9):
    player1.collect_treasure()
print(player1)

# This should cause the player to level up
player1.collect_treasure()
print(player1)

# Testing to see if do_battle is working as intended
player1.do_battle(5)
print(player1)

# This should cause call on the restart functyion
player1.do_battle(5)
print(player1)