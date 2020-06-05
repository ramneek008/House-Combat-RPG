from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("What's up, dude!")
dave.talk()

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input("1. watermelon\n2. cheese\n3. carrot\n")
dave.fight(fight_with)