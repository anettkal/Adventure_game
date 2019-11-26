import random
import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)

def restart():
    play_again = input("Would you like to play again? (y/n)")
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        restart()

def intro(random_enemies):
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + random_enemies + " is somewhere around here," \
    ' and has been terrifying the nearby village.')
    print_pause("In front of you are two passageways.\n")

def field(items, random_enemies, random_weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    travel(items, random_enemies, random_weapon)

def cave(items, random_enemies, random_weapon):
    if "weapon" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the " + random_weapon + " .")
        print_pause("You discard your silly old dagger and"
                    "take " + random_weapon + " with you.")
        items.append("weapon")
    print_pause("You walk back out to the field.")
    field(items, random_enemies, random_weapon)

def house(items, random_enemies, random_weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when"
                "the door opens and out steps a " + random_enemies + ".")
    print_pause("Eep! This is the " + random_enemies + " 's house!")
    print_pause("The " + random_enemies + " attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")
    attack_choice = input("Would you like to (1) fight or (2) run away?")
    if attack_choice == '2':
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.\n")
        field()
    elif attack_choice == '1':
        if "weapon" in items:
            print_pause("As the " + random_enemies + " moves to attack,"
                        "you unsheath your new weapon.")
            print_pause(random_weapon + " shines brightly in your hand"
                        "as you brace yourself for the attack.")
            print_pause("But the  " + random_enemies + " takes one look at"
                        "your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + random_enemies + " ."
                        "You are victorious!")
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " + random_enemies + ".")
            print_pause("You have been defeated!")
        restart()

def travel(items, random_enemies, random_weapon):
    choice = input("Please enter 1 or 2. \n")
    if choice == '1':
        house(items, random_enemies, random_weapon)
    elif choice == '2':
        cave(items, random_weapon)
    else:
        field(items, random_enemies)

def play_game():
    items = []
    enemies = ['troll', 'pirate', 'dragon', 'gorgon', 'orc', 'black widow', 'basilisk', 'wizzard', 'mummy']
    weapons = ['magical Sword of Ogoroth', 'magical Arrow of Artemis', 'magical Sword of Freyr', 'magical Hammer of Thor']
    random_enemies = random.choice(enemies)
    random_weapon = random.choice(weapons)
    intro(random_enemies)
    field(items, random_enemies, random_weapon)

#state = {
#  "random_enemies": "a",
#  "random_weapon": "",
#  "items": []
#}

play_game()
