from room import Room
from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude!")
dave.set_weakness("cheese")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a table and ornate golden decorations on each wall.");
dining_hall.set_character(dave)

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    monster = current_room.get_character()
    if monster is not None:
        monster.describe()
    command = input("> ")
    current_room = current_room.move(command)