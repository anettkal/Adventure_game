import time
import random

items = []


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


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    enemies = ['troll', 'pirate', 'dragon', 'gorgon' 'wicked fairie']
    template = 'Rumor has it that a {{enemies}} is somewhere around here,' +
    ' and has been terrifying the nearby village.'
    print_pause(enemy_string(template, enemies))
    print_pause("In front of you are two passageways.\n")


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    travel()


def travel():
    choice = input("Please enter 1 or 2. \n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()
    else:
        field()


def restart():
    play_again = input("Would you like to play again? (y/n)")
    if play_again == 'y':
        intro()
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        restart()


def cave():
    if "weapon" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    "take the magical weapon with you.")
        items.append("weapon")
    print_pause("You walk back out to the field.")
    field()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when"
                "the door opens and out steps a {{enemies}}.")
    print_pause("Eep! This is the troll's house!")
    print_pause("The {{enemies}} attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    attack_choice = input("Would you like to (1) fight or (2) run away?")
    if attack_choice == '2':
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.\n")
        field()
    elif attack_choice == '1':
        if "weapon" in items:
            print_pause("As the wicked fairie moves to attack,"
                        "you unsheath your new weapon.")
            print_pause("The Sword of Ogoroth shines brightly in your hand"
                        "as you brace yourself for the attack.")
            print_pause("But the {{enemies}} takes one look at"
                        "your shiny new toy and runs away!")
            print_pause("You have rid the town of the {{enemies}}."
                        "You are victorious!")
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the wicked fairie.")
            print_pause("You have been defeated!")
        restart()


intro()
field()
