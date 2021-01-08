#!/usr/bin/env python3


# a user model
class Player:
    def read_inv(self):
        return self.inv

    def add_inv(self, item):
        self.inv.append(item)

    def choose_name(self, choice):
        self.name= choice

    def return_name(self):
        return self.name

    def hurt(self, dam):
        self.hp -= dam
        print(f"Ouch! The hero was hurt and now has {self.hp} hit points remaining!")

    def powerkick(self):
        if self.mana >= 3:
            damage= random.randint(10,18) + self.strength
            print(f"{self.name} lashes out with a powerful KICK!")
            self.mana -= 3
            return damage
        else:
            print("You don't have enough mana to use this move!")
            return 0

    def equip(self, item):
        if item in self.inv:
            if item in armor.keys():
                self.hp += armor[item]
        else:
            print("You don't have " + item)
