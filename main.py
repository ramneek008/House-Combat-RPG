from room import Room
from character import Enemy, Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a table and ornate golden decorations on each wall.");

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')


dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

regas = Enemy("Regas", "An enormous spider with countless eyes and furry legs.")
regas.set_conversation("Ssss....I'm so bored....")
regas.set_weakness("book")
ballroom.set_character(regas)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A heavy book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

# Add a new character
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello there!")
ballroom.set_character(catrina)

dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)

    elif  command  == "talk":
        # Talk to character
        pass
        
    elif command == "fight":
        # Fight with character if its enemy
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            print("What will you fight with?")
            fight_with = input("1. watermelon\n2. cheese\n3. carrot\n")

            if fight_with in backpack:
                # I have it
            else:
                # I dont have it

            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear you lost the fight.")
                print("That's the end of the game. RIP")
                dead = True
    
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant,Enemy):
                print("Seems you don't love your life..")
            else:
                inhabitant.hug()

    elif command == "take":
        # Put item in backpack and remove from room