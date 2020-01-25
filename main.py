from classes.game import bcolors,Person
from classes.magic import Spell
from classes.inventory import Item
# Create Black Magic

fire=Spell("Fire",10,100,"black")
thunder=Spell("Thunder",10,100,"black")
blizzard=Spell("Blizzard",10,100,"black")
meteor=Spell("Meteor",20,200,"black")
quake=Spell("Quake",14,140,"black")

#Create White Magic
cure=Spell("Cure",12,120,"white")
cura=Spell("Cura",18,200,"white")

#Create Some Items
potion=Item("Potion","potion","Heals 50 Hp",50)
hiPotion=Item("Hi-Potion","potion","Heals 100 Hp",100)
superPotion=Item("Super-Potion","potion","Heals 500 Hp",500)
elixer=Item("Elixer","elixer","Fully Restores MP/HP of One Party Member",9999)
hielixer=Item("MegaElixer","elixer","Fully Restores Party's HP/MP",9999)
grenade=Item("Grenade","attack","deals 500 damage",500)




# Instantiate People
player_spells=[fire,thunder,blizzard,meteor,cure,cura,quake]
player_items=[potion,hiPotion,superPotion,elixer,hielixer,grenade]
player=Person(460,65,60,34,player_spells,player_items)
enemy=Person(1200,65,45,25,[],[])

running=True
i=0
print(bcolors.FAIL+bcolors.BOLD+"AN ENEMY ATTACKS!"+bcolors.ENDC)

while running:
    print("===================")
    player.choose_action()
    choice=input("choose Action :")
    index=int(choice)-1
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("You Attacked For",dmg,"points of damage.")
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose magic :"))-1

        if magic_choice==-1:
            continue



        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()

        current_mp=player.get_mp()
        if spell.cost>current_mp:
            print(bcolors.FAIL+"\n Not Enough Mp\n"+ bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type=='white':
            player.heal(magic_dmg)
            print(bcolors.OKBLUE+"\n"+spell.name+"heals for", str(magic_dmg),"HP"+bcolors.ENDC)

        elif spell.type=="Black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n"+ spell.name + "deals",str(magic_dmg))

    elif index==2:
        player.choose_items()
        item_choice=int(input("Choose Item :"))-1

        if item_choice==-1:
            continue

        item=player.items[item_choice]
        if item.type=="potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN+"\n"+item.name+" Heals For",str(item.prop),"HP"+bcolors.ENDC)





    enemy_choice=1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacks For",enemy_dmg)

    print("-----------------------")
    print("Enemy Hp",bcolors.FAIL + str(enemy.get_hp())+"/" + str(enemy.get_max_hp()) + bcolors.ENDC+"\n")
    print("Your Hp",bcolors.OKGREEN+ str(player.get_hp())+"/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your mp",bcolors.OKGREEN+str(player.get_mp())+"/"+str(player.get_max_mp())+ bcolors.ENDC+"\n")

    if enemy.get_hp()==0:
        print(bcolors.OKGREEN + "YOu Win" + bcolors.ENDC)
        running=False

    elif player.get_hp()==0:
        print(bcolors.FAIL + "Your Enemy Has Defeated You"+bcolors.ENDC)
        running=False
