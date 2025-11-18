# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Defining characters!
define t = Character("Narrator")
define g = Character("Gun Wick")
define n = Character("Norman")
define v = Character("Velvet")
define j = Character("Jessi")
define w = Character("William After")
define c = Character("Cat")
define r = Character("Rat")

#Defining images!
image streetside = "streetside.png"
image streetside2 = "streetside.png"
image crimealley = "crimealley.png"
image gundate = "emptygun_dateroon.png"
image outsidebar = "bar_frontoutside.png"
image bar = "bar.png"
image barsit = "bar_sit.png"
image cafe = "cafe.png"
image bathroom = "bathroom.png"
image diner = "fancydiner.png"
image outsidediner = "fancydiner_outside"
image fancydinertable = "fancydiner_table"
image incar = "inside of car.png"
image tavern = "tavern.png"

image rat = "rat_notlooking.png"
image ratsee = "rat_look.png"
image ratwow = "rat_SHOCKED.png"
image ratlove = "rat_love.png"

image william_neutral = "williamafter.png"
image william_angry = "williamafterangry.png"
image william_happy = "williamafterhappy.png"
image william_shocked = "williamaftershock.png"



#General variables!
default time = 25
default datednarrator = False
default datedgunwick = False
default datednorman = False
default datedvelvet = False
default datedjessi = False
default datedwilliamafter = False
default numberofdates = 0

#NOW the game starts

#label phone:

label start:
    scene phone

    #Norman's variables that reset everytime the game resests
    default wetclothes = False
    default witnesscatrat = False
    default flirtwithnarrator = False
    default goneintobar = False

    #William's variable that reset everytime the game resests
    default williamdemand = False

    #General variable that resets when the game resests
    $ time = 25

    #Very crude method of determining how many dates the player has been on
    #Please recommend any smarter methods you may come up with

    if datednarrator == True:
        $ numberofdates + 1
    else:
        pass
    if datedgunwick == True:
        $ numberofdates + 1
    else:
        pass
    if datedgunwick == True:
        $ numberofdates + 1
    else:
        pass
    if datednorman == True:
        $ numberofdates + 1
    else:
        pass
    if datedvelvet == True:
        $ numberofdates + 1
    else:
        pass
    if datedjessi == True:
        $ numberofdates + 1
    else:
        pass
    if datedwilliamafter == True:
        $ numberofdates + 1
    else:
        pass
    
    #Trying to let the player know how many dates they have been on and possibly who they were with

    if numberofdates == 1:
        t "So far, you have dated 1 person out of 6."
    else:
        pass

    if numberofdates >= 2:
        t "So far you have dated [numberofdates] out of 6 people."
    else:
        pass

    if numberofdates == 6:
        t "You have dated everyone! Impressive."
        jump secretending
    else:
        pass

    t "Four lovely options to date! Pick at your pace. No rush here friend. Take your time! All the time in the world right here. On your phone. Yep!"

menu:
    "Willaim After":
        if datedwilliamafter == True:
            t "You've already dated this person, are you sure you want to continue?"
            menu:
                "Yes":
                    pass
                "No":
                    jump start
        else:
            pass
        t "An older and very refined gentleman. Quite a sucessful investor in a pizza chain."
        jump william_after
    "Norman":
        if datednorman == True:
            t "You've already dated this person, are you sure you want to continue?"
            menu:
                "Yes":
                    pass
                "No":
                    jump start
        else:
            pass
        t "The average one. You probabaly choose water over any other drink option too huh? No judgement here though."
        jump norman
    "Velvet":
        if datedvelvet == True:
            t "You've already dated this person, are you sure you want to continue?"
            menu:
                "Yes":
                    pass
                "No":
                    jump start
        else:
            pass
        t "Whats not to love about whimsy and a woman with horns?"
        jump velvet
    "Jessi":
        if datedjessi == True:
            t "You've already dated this person, are you sure you want to continue?"
            menu:
                "Yes":
                    pass
                "No":
                    jump start
        else:
            pass
        t "If attitude had a form instead of just being a concept, this is her."
        jump jessi
    
#The Norman content that was here is now on norman.rpy

return