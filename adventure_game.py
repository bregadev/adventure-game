import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(input_prompt, options):
    while True:
        response = input(input_prompt).lower()
        for option in options:
            if option in response:
                return option

        print_pause("\n Please enter a valid response \n")


def monster_message(monster):
    print_pause("\nYou find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {monster} is somewhere "
                "around here, and has been terrifying the nearby village.")


def intro(monster, weapon):
    print_pause("\nIn front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty "
                f"(but not very effective) {weapon}.")
    scene1(monster, weapon)


def cave(monster, weapon):
    if weapon == "dagger":
        print_pause("\nYou peer cautiously into the cave.\n")
        print_pause("It turns out to be only a very small cave. \n")
        print_pause("Your eye catches a glint of metal behind a rock. \n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you. \n")
        print_pause("You walk back out to the field.\n")
        weapon = "sword"
        scene1(monster, weapon)
    else:
        print_pause("\nYou peer cautiously into the cave\n")
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.\n")
        print_pause("You walk back out to the field.\n")
        scene1(monster, weapon)


def house(monster, weapon):
    print_pause("\nYou approach the door of the house.\n")
    print_pause("You are about to knock when the door "
                f"opens and out steps a {monster}.\n")
    print_pause(f"Eep! This is the {monster} house!\n")
    print_pause(f"The {monster} attacks you!\n")
    if weapon == "dagger":
        print_pause("You feel a bit under-prepared for this, what "
                    f"with only having a tiny {weapon}.\n")
    player_choice = valid_input("Please enter 1 to fight "
                                "or 2 to run:  ", ["1", "2"])
    if player_choice == "1":
        fight(monster, weapon)
    else:
        run(monster, weapon)


def fight(monster, weapon):
    if weapon == "dagger":
        lose_game(monster, weapon)
    if weapon == "sword":
        win_game(monster, weapon)


def run(monster, weapon):
    print_pause("\nYou run back into the field. Luckily, you "
                "don't seem to have been followed.\n")
    scene1(monster, weapon)


def win_game(monster, weapon):
    print_pause(f"\nAs the {monster} moves to attack, "
                "you unsheath your new sword.\n")
    print_pause("The Sword of Ogoroth shines brightly "
                "in your hand as you brace yourself for the attack\n")
    print_pause(f"But the {monster} takes one look at your"
                "shiny new toy and runs away!\n")
    print_pause(f"You have rid the town of the {monster}."
                "You are victorious!\n")
    play_again()


def lose_game(monster, weapon):
    print_pause("\nYou do your best...\n")
    print_pause(f"but your {weapon} is no match for the {monster}.\n")
    print_pause("You have been defeated!\n")
    play_again()


def scene1(monster, weapon):
    print("""
    Enter 1 to Knock on the door of the house.\n
    Enter 2 to peer into the cave.
                        """)
    player_choice = valid_input("Please enter 1 or 2:   ", ["1", "2"])
    if player_choice == "1":
        house(monster, weapon)
    else:
        cave(monster, weapon)


def play_game():
    weapon = "dagger"
    monster_list = ["pirate", "dragon", "gorgon", "wicked fairy", "troll"]
    monster = random.choice(monster_list)
    monster_message(monster)
    intro(monster, weapon)


def play_again():
    try_again = valid_input("would you like to play again? "
                            "Please enter yes or no: ", ["yes", "no"])
    if try_again == "yes":
        print_pause("\nExcellent! Restarting the game ...")
        play_game()
    else:
        print_pause("\nThanks for playing! See you next time.\n")
        exit()


play_game()
