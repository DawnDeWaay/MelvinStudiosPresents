# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Physics Philip", color="#FFFF00")


# The game starts here.

label start:

    scene bg mountain

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tensegrity normal

    e "You’re the only force I want acting on me today, baby"

    menu:
        "Philip asks you out to coffee, do you accept?"

        "Take me Physics Philip":
            "Yes"

        "Nah Philip chopped asf":
            "Nah"

    label after_menu:

     "After having my drink, I got on with my morning."

    return
