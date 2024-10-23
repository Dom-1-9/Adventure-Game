from time import sleep
import random  # Import the needed methods and modules


# This function is used to print a statement and then pause for 2 seconds
def print_pause(statement):
    sleep(2)
    print(statement)


# Intro function to print out displays at the start of the game
def intro(house_owner):
    print_pause(
        "You find yourself standing in an open field,"
        " filled with grass and yellow wildflowers."
    )
    print_pause(
        f"Rumor has it that a {house_owner} is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) dagger."
    )


# Field function is for options anytime the player is at the field
def field(weapon, house_owner, options):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    action = option1("What would you like to do?\n (Please enter 1 or 2)\n")
    if action == "1":  # Call the house function for option 1
        house(weapon, house_owner, options)
    # Else call the cave function when the player picks option 2
    elif action == "2":
        cave(weapon, house_owner, options)


# The house function to specify what happens when the user
# is at the door of the house.
def house(weapon, house_owner, options):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps "
        f"a {house_owner}."
    )
    print_pause(f"Eep! This is the {house_owner}'s house!")
    print_pause(f"The {house_owner} attacks you!")
    # When with dagger then player should feel under-prepared
    if weapon == "dagger":
        print_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger."
        )
        fight(
            weapon, house_owner, options
        )  # Call the fight function to ask the players option
    else:
        fight(
            weapon, house_owner, options
        )  # Call the fight function to ask the players option


# The fight function is for player's option when the door is opened
def fight(weapon, house_owner, options):
    action = option1("Would you like to (1) fight or (2) run away?")
    if action == "1":
        # If player fights with a dagger,he should get defeated
        if weapon == "dagger":
            print_pause("\nYou do your best...")
            print_pause(f"but your dagger is no match for the {house_owner}.")
            print_pause("You have been defeated!")
        else:  # If player fights with the sword, then he should win.
            print_pause(
                f"As the {house_owner} moves to attack, "
                "you unsheath your new sword."
            )
            print_pause(
                "The Sword of Ogoroth shines brightly in your hand "
                "as you brace yourself for the attack."
            )
            print_pause(
                f"But the {house_owner} takes one look at your "
                "shiny new toy and runs away!"
            )
            print_pause(
                f"You have rid the town of the {house_owner}. "
                "You are victorious"
            )
        Outro()  # When the game ends, calls the outro function.
    elif action == "2":
        print_pause(
            "You run back into the field. Luckily you don't "
            "seem to have been followed"
        )
        field(
            weapon, house_owner, options
        )  # Call the fiels function, to go back to the field


# The cave function is for opitons when the player is at the cave
def cave(weapon, house_owner, option):
    if weapon == "dagger":
        # When the at the cave, he should change the weapon to a sword
        weapon = "Sword of Ogoroth"
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger and take the sword with you."
        )
        print_pause("You walk back out to the field.")
        field(weapon, house_owner, option)
    else:  # If already at the cave, then he should get back to the field.
        print_pause("You peer cautiously into the cave.")
        print_pause(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now."
        )
        print_pause("You walk back out to the field.")
        field(weapon, house_owner, option)


# The option1 function is to check the players response
# for inputs with 1 or 2 options
def option1(statement):
    # Continue prompting the user until the response
    # is either 1 or 2
    while True:
        option = input(statement)
        if option in ["1", "2"]:
            break
        else:
            continue
    return option


# The option2 function is to check the players response
# for inputs with "n" or "y" options
def option2(statement):
    while True:
        # Continue prompting the user until the
        # response is either "n" or "y"
        option = input(statement)
        if option in ["n", "y"]:
            break
        else:
            continue
    return option


# The outro function is to ask the player if he/she will
# like to play at the end of each game.
def Outro():
    while True:
        action = option2("Would you like to play again? (y/n)")
        if action == "y":
            print_pause("Excellent! Restarting the game...\n")
            play_game()
            break
        elif action == "n":
            print_pause("\nThanks for playing! see you next time.")
            break
        else:
            continue


# This function follows the order of the game
def play_game():
    weapon = "dagger"
    options = [
        "dragon",
        "priate",
        "gorgon",
        "troll",
        "gorgon",
        "troll",
        "wicked fairie",
    ]
    house_owner = random.choice(options)
    intro(house_owner)
    field(weapon, house_owner, options)


play_game()  # Call the play_game function to start the game.
