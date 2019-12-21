import random
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def restart():
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        restart()


def intro(state):
    print_pause("You find yourself standing in an open field, \n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + state['random_enemies'] +
                " is somewhere around here,\nand has been"
                " terrifying the nearby village.")
    print_pause("In front of you are two passageways.\n")


def field(state):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")
    travel(state)


def house(state):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when " +
                "the door opens and out steps a "
                + state['random_enemies'] + ".")
    print_pause("Eep! This is the " + state['random_enemies'] + "'s house!")
    print_pause("The " + state['random_enemies'] + " attacks you!")
    confidence(state)
    choice_to_attack(state)


def cave(state):
    if "weapon" in state['items']:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all\n"
                    "the good stuff. It's just an empty cave now.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the " + state['random_weapon'] + ".")
        print_pause("You discard your silly old dagger and "
                    "take " + state['random_weapon'] + " with you.\n")
        state['items'].append("weapon")
    print_pause("You walk back out to the field.")
    field(state)


def choice_to_attack(state):
    attack_choice = input("Would you like to (1) fight or (2) run away?\n")
    if attack_choice == '2':
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        field(state)
    elif attack_choice == '1':
        if "weapon" in state['items']:
            print_pause("From above the Gods are watching you approching the "
                        + state['random_enemies'] + ".")
            print_pause("They flip up a magical coin to decide your faith.")
            if "heads" in state['random_coin']:
                bad_luck(state)
            elif "tails" in state['random_coin']:
                good_luck(state)
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the "
                        + state['random_enemies'] + ".")
            game_over()
        restart()
    else:
        choice_to_attack(state)


def confidence(state):
    if "weapon" in state['items']:
        print_pause("You feel confident in your victory "
                    "because of your powerful weapon.\n")
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")


def good_luck(state):
    print_pause("Fortunatly the Gods are on your side.")
    print_pause("The " + state['random_weapon'] +
                " shines brightly in your hand "
                "as you brace yourself for the attack.")
    print_pause("But the " + state['random_enemies'] + " takes one look at "
                "your shiny new toy and runs away!")
    print_pause("You have rid the town of the "
                + state['random_enemies'] + ". "
                "You are victorious!\n")
    print_pause("VICTORY\n")


def bad_luck(state):
    print_pause("It isn't your lucky day, the Gods don't seem to support you.")
    print_pause("Even with the " + state['random_weapon']
                + " in your hand the "
                + state['random_enemies'] + "\nhas bigger power than you.\n")
    game_over()


def game_over():
    print_pause("Unfortunatly you have been defeated!\n")
    print_pause("GAME OVER\n")


def travel(state):
    choice = input("Please enter 1 or 2. \n")
    if choice == '1':
        house(state)
    elif choice == '2':
        cave(state)
    else:
        field(state)


def play_game():
    enemies = ['troll', 'pirate', 'dragon', 'gorgon', 'orc',
               'black widow', 'basilisk', 'wizzard', 'mummy']
    weapons = ['magical Sword of Ogoroth', 'magical Arrow of Artemis',
               'magical Sword of Freyr', 'magical Hammer of Thor']
    coin = ["heads", "tails"]
    state = {
      "random_enemies": random.choice(enemies),
      "random_weapon": random.choice(weapons),
      "random_coin": random.choice(coin),
      "items": []
    }
    intro(state)
    field(state)


play_game()
