import random
import ast

from classes.game_classes import Character, Product, Shop, Inventory

def battle(hero, monster):
    print("FIGHT!")
    print("*******************************************")
    print(f'{hero.name} vs {monster.name}')
    hero.get_maxhp()
    hero.hp = hero.max_hp
    monster.hp = monster.max_hp
    while True:
        dmg = hero.attack()
        dodge = monster.dodge()
        if dodge == True:
            dmg = 0
        monster.hp = monster.hp - dmg
        print(f'Hero deal {dmg} to monster')
        print(f'Monster hp: {round(monster.hp)}/{round(monster.max_hp)}')
        if monster.hp < 0:
            monster.hp = 0
            print(f'Monster hp: {monster.hp}/{monster.max_hp}')
            print(f'{hero.name} wins! Congratulation!')
            hero.money += monster.money
            break

        dmg = monster.attack()
        dodge = hero.dodge()
        if dodge == True:
            dmg = 0
        hero.hp = hero.hp - dmg
        print(f'Monster deal {dmg} to hero')
        print(f'Hero hp: {round(hero.hp)}/{round(hero.max_hp)}'),
        if hero.hp < 0:
            hero.hp = 0
            print(f'Hero hp: {hero.hp}/{round(hero.max_hp)}'),
            print(f'{monster.name} wins! You died!')
            break
    return hero, monster

def main():

    hero = Character(0, 0, 0, 0, 0, 0, 0)
    monster = Character(0, 0, 0, 0, 0, 0, 0)

    basic_helmet = Product('Basic Helmet',2,0,0,20,1)
    basic_armor = Product('Basic Armor',1,1,3,50,1)
    basic_wand = Product('Basic Wand',0,3,0,15,1)

    store = [basic_helmet, basic_armor, basic_wand]
    T1_shop = Shop(store)
    hero_item = []


    print("Start new game or create new character?")
    print("Press 1 if you wanna create new character\nPress 2 to continue")
    while True:
        start_choice = int(input())
        if start_choice == 1:
            print(f'1 - Your strenght: 0 \n2 - Your dexterity: 0\n3 - Your intelligence: 0')
            points = 10
            hero.get_name()
            hero.add_pionts(points)
            break
        elif start_choice == 2:
            hero_name = input("Hero name: ")
            hero = hero.open_game(hero_name)
            break



    while True:
        print("What would you do? ")
        print("1 - Fight with a monster!\n2 - Check your stats\n3 - Check how many monsters did you kill\n4 - Save the game\n5 - Buy Item\n6 - Show items\n7 - Quit")
        to_do_choice = int(input())
        try:
            if to_do_choice == 1:
                monster = monster.get_monster()
                print(monster.name)
                monster.show_stats()
                fight = input("Press Y if you wan't to fight!")
                fight = fight.upper()
                if fight == 'Y':
                    hero, monster = battle(hero,monster)
                    if monster.hp == 0:
                        monster.kills_count(monster.name)
                        hero.check_level_up()
                    else:
                        print("Musisz udać się na odpoczynek")
                else:
                    print("RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUN!!!!!")
            elif to_do_choice == 2:
                hero.show_stats()
            elif to_do_choice == 3:
                print(Character.T1_monsters)
            elif to_do_choice == 4:
                hero_monsters = Character.T1_monsters
                hero.save_game(hero, hero_monsters)
            elif to_do_choice == 5:
                print("")
                T1_shop.show_all()
                check_item = int(input('Index: '))
                hero_items = Inventory(hero_item)
                if check_item < 3:
                    item_name = T1_shop.buy(check_item, hero.money, hero.level)
                    check = hero_items.item_in_inv(item_name)
                    if check == False:
                        if item_name == None:
                            print("Czegos brakuje")
                        else:
                            if item_name == 'Basic Helmet':
                                hero.change_stats(basic_helmet.name, basic_helmet.strenght, basic_helmet.intel,
                                                  basic_helmet.dex, basic_helmet.price)
                                hero_item.append(item_name)
                                hero_items = Inventory(hero_item)
                            elif item_name == 'Basic Armor':
                                hero.change_stats(basic_armor.name, basic_armor.strenght, basic_armor.intel,
                                                  basic_armor.dex, basic_armor.price)
                                hero_item.append(item_name)
                                hero_items = Inventory(hero_item)
                            elif item_name == 'Basic Wand':
                                hero.change_stats(basic_wand.name, basic_wand.strenght, basic_wand.intel,
                                                  basic_wand.dex,
                                                  basic_wand.price)
                                hero_item.append(item_name)
                                hero_items = Inventory(hero_item)
                            else:
                                print()
                    else:
                        print("Item is already bought!")
                else:
                    print("Wrong number!")

            elif to_do_choice == 6:
                hero_items.show_items()
            elif to_do_choice == 7:
                break
            else:
                raise ValueError
        except(TypeError, ValueError):
            print()
        else:
            print()



if __name__ == '__main__':
    main()



