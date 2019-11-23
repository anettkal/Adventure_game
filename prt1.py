import time
import random

items = []
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def enemy_string(template, enemies):
    output = []
    index = 0
    while index < len(template):
        if template[index:index+11] == '{{enemies}}':
            output.append(random.choice(enemies))
            index += 11
        else:
            output.append(template[index])
            index += 1
    output = ''.join(output)
    return output

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")

    enemies = ['troll', 'pirate', 'dragon', 'gorgon']
    template = 'Rumor has it that a {{enemies}} is somewhere around here, and has been terrifying the nearby village.'
    enemy_string(template,enemies)

    print_pause("In front of you are two passageways.")

def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("Please enter 1 or 2. ")
    if choice == '2':
        cave()

def cave():
    if "weapon" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the magical weapon with you.")
        items.append("weapon")

    print_pause("You walk back out to the field.")
    field()

intro()
field()
