# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character('Second', color="#FF6600", window_background="gui/textboxorange.png", window_ypos=765, what_ypos=384, who_ypos=350)
define g = Character('Green', color="#66CC00", window_background="gui/textboxgreen.png", window_ypos=765, what_ypos=384, who_ypos=350)
define y = Character('Yellow', color="#FFCC00", window_background="gui/textboxyellow.png", window_ypos=765, what_ypos=384, who_ypos=350)
define r = Character('Red', color="#CC0000", window_background="gui/textboxred.png", window_ypos=765, what_ypos=384, who_ypos=350)
define b = Character('Blue', color="#33CCFF", window_background="gui/textboxblue.png", window_ypos=765, what_ypos=384, who_ypos=350)
define m = Character("[mcname]", who_prefix="{color=[namecol]}", who_suffix="{/color}")


# The game starts here.

label start:


    scene bg defaulto
    with fade

    "I...What happened...? Where am I?"
    "Wait... I...I can't remember?"
    "My face...I don't... look right...I...need to..."
    "A new face. A new skin..."

    "{b}Pick a color?{/b}"
    call color_select

    "{b}Hollowhead?{/b}"
    call head_select
    "I am a [head]head."

    "{b}Accessories?{/b}"
    call appearance_select

    "{b}Some pronouns?{/b}"
    call pronoun_select
    "My pronouns are [they]/[them]."

    "{b}What's your name?{/b}"
    call name_select
    m "Yes, [mcname] is a good name!"

    if mcname == "Changeling":
        m "After all, it is my actual name!"

    scene bg defaulto
    with fade

    show mc happy at right
    m "This is me?"
    hide mc




    show second sleepy at right

    # These display lines of dialogue.

    o "Hello!"

    m "Hi"

    o "This is a test."

    g "green is talking now!"

    y "now yellow..."

    r "And red!"

    b "blue is here too...!"

    # This ends the game.

    return


label name_select:

    $ mcname = renpy.input("Type out a name, please!", default = "Changeling")
    $ mcname = mcname.strip()

    if mcname in ["Red", "Yellow", "Blue", "Orange", "Green", "Purple", "Second", "The Second Coming", "Second Coming", "Pink", "Orchid", "Dark Blue", "Regular Blue", "Gold"]:
       "I don't think that'll work out very well... I should pick another name."
       $ mcname="Changeling"
       jump name_select

    if mcname in ["Mango", "Dark", "Deserved", "Chosen", "Reckoning", "Mango Tango", "The Dark Lord", "Dark Lord", "The Chosen One", "Chosen One", "King"]:
       ":/"
       "I'm not naming myself after a fucking war criminal."
       $ mcname="Changeling"
       jump name_select

    if mcname == "Victim":
        "Absolutely {b}not{/b}."
        $ mcname="Changeling"
        jump name_select

    if mcname in ["Noogai", "Noogai3", "Alan", "Alan Becker"]:
        "..."
        "...No..."
        "Unless you're the actual Alan, playing this game."
        "Sorry if you are. Now get off of my game."
        "This foul creation was not made for official animator eyes."
        $ mcname="Changeling"
        jump name_select

    if mcname == "Blueberry":
        "That depressed motherfucker? No way."
        "Sorry. Sorry. I don't know what came over me."
        "I don't even know anyone by that name."
        "Still not naming myself that."
        $ mcname="Changeling"
        jump name_select

    if mcname == "":
        "How about...Darling?"
        $ mcname="Darling"
return

label color_select:

        $ namecol="#696969"

return

label appearance_select:
# put text here

return

label pronoun_select:
menu:
     "Pick a set of pronouns!"

     "She/Her":
         $ they = "she"
         $ them = "her"

     "He/Him":
         $ they = "he"
         $ them = "him"

     "They/Them":
         $ they = "they"
         $ them = "them"

     "It/Its":
         $ they = "it"
         $ them = "its"


return

label head_select:
menu:
     "Are you a hollow or filled head?"

     "Hollow":
         $ head = "hollow"

     "Filled":
         $ head = "filled"


return
