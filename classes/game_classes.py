import random
import ast

class Character:

    T1_monsters = {}

    def __init__(self, name, hp, strength, dex, intel, money, level):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.int = intel
        self.money = money
        self.max_hp = hp
        self.level = level


    def get_name(self):
        self.name = input("What's the name of your hero?: ")

    def get_maxhp(self):
        self.max_hp = 10 + self.strength * 1 + self.dex * 0.7 + self.int * 0.5

    def add_pionts(self,get_points):
        i = 0
        while i < get_points:
            print("Distribute point:")
            try:
                print("1 - Your strenght:" + str(self.strength) + "\n2 - Your dexterity: " + str(self.dex) + "\n3 - Your intelligence: " + str(self.int))
                choise = int(input("Add point to your statistics: "))
                if choise == 1:
                    self.strength += 1
                elif choise == 2:
                    self.dex += 1
                elif choise == 3:
                    self.int += 1
                else:
                    raise ValueError
            except(TypeError, ValueError):
                print("Wrong number")
            else:
                i += 1
        Character.get_maxhp(self)

    def open_game(self, name):

        try:
            with open(f'{name}.txt') as fopen:
                line = fopen.readline().split(',')
                l7 = line[7].replace(']','')
                hero = Character(name, 0, int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(l7))
            return hero
        except (FileNotFoundError):
            print("Niepoprawna nazwa pliku!")




    def open_monsters(self, name):

        file = open(f'{name}_monsters.txt', "r", encoding='UTF-8')
        contents = file.read()
        monsters = ast.literal_eval(contents)
        monsters = Character.T1_monsters
        file.close()
        return monsters


    def save_game(self,hero, monsters):
        with open(f'{self.name}.txt', 'w') as f:
            name = hero.name
            hp = hero.hp
            strenght = hero.strenght
            dex = hero.dex
            int = hero.int
            money = hero.money
            max_hp = hero.max_hp
            level = hero.level
            save_hero = [name, hp, strenght, dex,int, money, max_hp, level]
            f.write(str(save_hero))

            with open(f'{self.name}_monsters.txt', 'w', encoding='UTF-8') as f:
                f.write(str(Character.T1_monsters))



    def show_stats(self):
        print(f'Max hp =  {round(self.max_hp)}\nHp = {round(self.hp)}\nStrenght = {self.strength}\nDexyerity = {self.dex}\nIntelligence = {self.int}\nMoney = {self.money}\nLevel = {self.level}')

    def get_monster(self):
        with open('Tier1_monsters', encoding='UTF-8') as f:
            lines = f.read().splitlines()
            monster = random.choice(lines)
            goblins = monster.split(',')
            monster = Character(goblins[0], int(goblins[1]), int(goblins[2]), int(goblins[3]), int(goblins[4]),int(goblins[5]),int(goblins[6]))
            return monster

    def attack(self):
        basic_attack = 5 + self.strength * 0.5 + self.dex * 0.2
        l_attack = basic_attack - 0.13*basic_attack
        m_attack = basic_attack + 0.13 * basic_attack
        attack_dmg = random.randrange(int(l_attack), int(m_attack))

        return attack_dmg

    def dodge(self):
        chance = random.choices(range(0,100), k = self.dex)
        chech_chance = random.choice(range(0,100))
        if chech_chance in chance:
            return True
        else:
            return False

    def kills_count(self, name):
        if self.name in Character.T1_monsters.keys():
            Character.T1_monsters[self.name] += 1
        else:
            Character.T1_monsters[self.name] = 1


    def check_level_up(self):
        if self.level == 0:
            if len(Character.T1_monsters.keys()) == 3:
                print('You hero is now level 1!\n You unlock new spell!\nYou can now buy items to your hero!')
                self.level = 1
                return Character.add_pionts(self,get_points=5)
            else:
                print("You don't kill enough monsters!")
        else:
            print()

    def change_stats(self, name, strenght, intel, dex, price):
        self.strength += strenght
        self.int += intel
        self.dex += dex
        self.money -= price



class Product:
    def __init__(self, name, strenght, intel, dex, price, level):
        self.name = name
        self.strenght = strenght
        self.intel = intel
        self.dex = dex
        self.price = price
        self.level = level

    def product_show(self):
        print(self.name.title(), self.strenght, self.intel, self.dex, self.price, self.level)

    def product_buy(self, money, level):
        if self.level > level:
            print('You dont have enuogh level')
        else:
            if money >= self.price:
                print('Sold')
                return self.name
            else:
                "Its too expensive"




class Shop:
    def __init__(self, products=[]):
        self.products = products

    def show_all(self):
        for index, item in enumerate(self.products):
            print(index, end=' - ')
            Product.product_show(item)

    def buy(self, index, wallet, level):
        selected = self.products[index]
        return Product.product_buy(selected, wallet, level)

class Inventory:
    def __init__(self, inv = []):
        self.inv = inv

    def item_in_inv(self, name):
        return name in self.inv


    def show_items(self):
        print(f'Your items: {self.inv}')





