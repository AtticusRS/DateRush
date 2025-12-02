# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Defining characters!
define t = Character("Narrator", color="#FAFAFA")
define g = Character("Gun Wick", color="#BD1755")
define n = Character("Norman", color="#C0D690")

define v = Character("Velvet", color="#C079DB")
define o = Character("Dragon Repossessor", color="#2A528C")
define rg = Character("Reg the Goblin", color="#329126")

define j = Character("Jessi", color="#4627C4")
define b = Character("Bouncer", color="#F0310C")
define e = Character("Eavesdropper", color="#5C769E")

define w = Character("William After", color="#6F1F94")
define c = Character("Cat", color="#EBA210")
define r = Character("Rat", color="#BFB6AE")


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
image gamerbasement = "gamer_basement.png"
image black = "Black.png"

#Side note for including the bouncer!!!!! Use xzoom 0.54 yzoom 0.54

image bouncer = "bouncer.png"

image rat = "rat_notlooking.png"
image ratsee = "rat_look.png"
image ratwow = "rat_SHOCKED.png"
image ratlove = "rat_love.png"

image catsneaky = "cat_sneaky.png"
image catflowers = "cat_flowers.png"

image william_neutral = "williamafter.png"
image william_angry = "williamafterangry.png"
image william_happy = "williamafterhappy.png"
image william_shocked = "williamaftershock.png"

image norman_neutral = "normanneutral.png"
image norman_happy = "normanhappy.png"
image norman_shocked = "normanshocked.png"
image norman_angry = "normanmad.png"

image velvet_neutral = "Velvet.png"
image velvet_angry = "Velvet_mad.png"
image velvet_happy = "Velvethappy.png"
image velvet_shocked = "Velvetshocked.png"

image jessi_neutral = "JessiNormal.png"
image jessi_happy = "JessiHappy.png"
image jessi_shocked = "JessiSuprise.png"
image jessi_angry = "JessiAnnoyed.png"

image gun_neutral = "gun_side.png"
image gun_angry = "gun_front.png"
image gun_shocked = "gun_tilt.png"
image gun_shocked2 = "gun_tilt_2.png"
image gun_happy = "gun_side_2.png"

#General variables!

default time = 25

#When a choice costs time, write "$ time = time - (the amount that is being subtracted)"

default max_time = 25
default datednarrator = False
default datedgunwick = False
default datednorman = False
default datedvelvet = False
default datedjessi = False
default datedwilliamafter = False
default numberofdates = 0

#Code for visible time/resource meter!
#When you want to show the meter on screen, type "show screen time_meter"
#Don't forget to hide the time meter!!!! It will persist everywhere if you don't. Hide it with "hide screen time_meter"

screen time_meter():
    bar:
        value time
        range max_time
        xalign 0.95
        yalign 0.05
        xmaximum 300  

#NOW the game starts

#label phone:

label start:
    scene phone

    hide screen time_meter

    #Norman's variables (some are being reset after each start, hence the $)
    default wetclothes = False
    $ wetclothes = False
    default witnesscatrat = False
    $ witnesscatrat = False
    default flirtwithnarrator = False
    $ flirtwithnarrator = False
    default goneintobar = False
    $ goneintobar = False
    default calledtaxi = False
    $ calledtaxi = False
    default norman5ask = False
    $ norman5ask = False
    default norman7ask = False
    $ norman7ask = False

    #William's variables (some are being reset after each start, hence the $)
    default williamdemand = False
    $ williamdemand = False
    default williamtimed = 0
    default timer_jump = 0
    default timer_range = 0
    default firsttimewithtimer = True
    $ firstimewithtimer = True
    default thinkingalot = False
    $ thinkingalot = False
    default skippedto_william = False
    $ skippedto_william = False

    #Jessi Variables!
    default blackeye = False
    $ blackeye = False

    #General variable that resets when the game resests
    $ time = 25
    $ numberofdates = 0

    #Very crude method of determining how many dates the player has been on
    #Please recommend any smarter methods you may come up with

    if datednarrator == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    if datednorman == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    if datedgunwick == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    if datedvelvet == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    if datedjessi == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    if datedwilliamafter == True:
        $ numberofdates = numberofdates + 1
    else:
        pass

    #Trying to let the player know how many dates they have been on and possibly who they were with

    if numberofdates == 1:
        t "So far, you have dated 1 person out of 6."
    else:
        pass

    if numberofdates == 6:
        t "You have dated everyone! Impressive."
        jump secretending
    else:
        if numberofdates >= 2:
            t "So far you have dated [numberofdates] out of 6 people."
        else:
            pass
        pass

    t "Four lovely options to date! Pick at your pace. No rush here friend. Take your time! All the time in the world right here. On your phone. Yep!"

menu:
    "William After":
        show william_neutral:
            xalign 0.5
            yalign 0.0
        t "An older and very refined gentleman. Quite a sucessful investor in a pizza chain."
        t "Are you sure you want to date Sir William?"
        menu:
            "Yes":
                hide william_neutral
                jump william_after
            "No thanks":
                hide william_neutral
                jump start

    "Norman":
        show norman_neutral
        t "The average one. You'd probabaly choose water over any other drink option too huh? No judgement here though."
        t "Are you sure you want to date Norman?"
        menu:
            "Yes":
                hide norman_neutral
                jump norman
            "No thanks":
                hide norman_neutral
                jump start
    
    "Velvet":
        show velvet_neutral:
            xzoom 0.5 yzoom 0.5
        t "Whats not to love about whimsy and a woman with horns?"
        t "Are you sure you want to date Velvet?"
        menu:
            "Yes":
                hide velvet_neutral
                jump velvet
            "No thanks":
                hide velvet_neutral
                jump start

    
    "Jessi":
        show jessi_neutral:
            xalign 0.5
            yalign 0.0
            yzoom 0.4
            xzoom 0.4
        t "If attitude had a form instead of just being a concept, this is her."
        t "Are you sure you want to date Jessi?"
        menu:
            "Yes":
                hide jessi_neutral
                jump jessi
            "No thanks":
                hide jessi_neutral
                jump start

return