#The file follows the route of Velvet

#This timeline is dialouge heavy, SO for the time mechanic we'd prbably need to figure out things here 
#add bar fight
#add illusion of random- roll more dice
#dnd actions! NOT DND
#use up more timeee



#IMPORTANTTTT! The sprites always layer ontop of eachother instead of hiding the previous. Still having sorted that out yet.


label velvet:
scene gamerbasement

menu:
    "Roll the dice!":
            t "a perfect D20. Your DnD character flawlessly swoons the tiefling! She offers a hand to you, stepping to toward the dancing crowd...."
            t "...Something seems off. She's not quite as 'won over' as you thought?"
            jump intoDNDsuccess
        
    "Roll the dice...":
            t "It's a natural all right. A natural one."
            jump intoDNDfail
    
label DPS_Problem:
scene tarven
o "Just give it over, you're hurting the kid not helping them. That dragon should be back with its mom! With dragon-kind!"
g "But I'm a GOOD dad!! Shiny is happy with me."
menu:
    "Help Reg":
        t "You step in to intervene, putting yourself between the officals and the goblin."
            # idk what to put here but I need OPTIONS people
        $ time - 3
    "Help Officials":
        t "You block the goblins escape as the officials close in. They rummage through his bag and pull out..."
        t "A entire fucking dragon. A baby one, but still. It's actually kind of cute for a dangerous, fire monster! It appears to be sleeping soundly, not aware of the chaos going on even as it's taken out of the bag."
        $ time - 1
    "Stay a distant bystander":
        t "Whatever-- That's not your problem."
        jump intoDNDsuccess

label intoDNDsuccess:
scene tavern
show velvet_neutral with dissolve:
    xzoom 0.5 yzoom 0.5

t "!!Immediately engaged with the action, the world itself leaks into reality until you find yourself sitting in the tavern."
t "Despite your flawlessly executed pick-up line, The tiefling, Velvet, doesn't seem particularly engaged."
v "Hmph. I havent heard that one before. Honestly, maybe we could we get to know eachother instead of just 'diving right in?' You've got some nerve."


menu:
    "Flirt":
        hide velvet_neutral
        show velvet_angry:
            xzoom 0.5 yzoom 0.5

        t "Her brows furrow as she stares at you-- she's clearly irritated."
        v "Are you kidding? You think that's gonna work on me??"
        
        jump datefailV
    "Ask her about her interests":
        hide velvet_neutral
        show velvet_happy:
            xzoom 0.5 yzoom 0.5
        t "She stares off for a second as her head leans to one side, thinking over your incredibly open-ended question."
        v "Hm... well I love hanging out with my friends! I really like Squeaker, but they wander too much for me. My friend William is more my speed-- he's got that homebody personality."
        t "Velvet pauses to look at your puzzled expression. When the realization hits her, you notice the teifling's ears perk up."
        v "Oh! Squeaker is a mouse that hangs around here. Sweet thing. They're just so cute-- they fit right into my hand when they decide to sit still for once!"
        jump postive
    "QUICK! OVER THERE":
            t "The dragon-child protective services are shouting at a some goblin. One of the officials knocks his drink to the ground. Strangely, as the glass shatters, mud spills out instead of wine?"
            $ time - 2
            jump DPS_Problem
    "Listen to passing conversations":
            t "Alright. You listen in on the chatter around you instead of any sort of date."
            t "Nearby you hear people yelling at a goblin who's holding a cup of mud. Another murmur around the room is about a feral-man eating horse of some sort." 
            t "Strangly though, neither are the populaur subject among these strangers."
            t "Happy voices of a new couple, a cat and a rat, seem to hold peoples attention more than any other fantastical beast."
            $ time - 5




label datefailV:
hide velvet_neutral
show velvet_angry:
    xzoom 0.5 yzoom 0.5
v "Y'know what? I'll just go, actually. No point in trying to have a conversation if you're gonna be a creep."
jump start

label postive:
menu:
    "William? That one rich dude?":
        hide velvet_neutral
        show velvet_happy:
            xzoom 0.5 yzoom 0.5
        v "Yes! He's a delight! I'm surprised you know him! It's quite hard to become close with someone so sophisticated. I certainly have my ways, though. Tehe~"
        t "Time flies as you two converse. Your chatter goes until the day fades away. She seems delighted with how the date has turned out."
        jump velvetdate

    "A mouse? You... hang out with rodents?":
        hide velvet_neutral
        show velvet_angry:
            xzoom 0.5 yzoom 0.5
        v "Well SORRY if that's an issue. Hmph! I can just go--you CLEARLY have no taste. Sorry, but not sorry."
        jump start

label velvetdate:
    $ datedvelvet = True
    
    t "And so, you and this tiefling agree to meet up another time, in another land."

    jump start

label intoDNDfail:
scene tavern


t "As the real world fades away, a fantasy one makes itself known."
show velvet_happy with dissolve:
        xzoom 0.5 yzoom 0.5
t  "Words fumble out of your mouth as you try to woo the lady. Something about your awkward stumbling makes her smile."

menu:
    "Apologize":
        hide velvet_neutral
        show velvet_happy:
            xzoom 0.5 yzoom 0.5
        t "The woman waves her hands."
        v "No, no its alright-- hehe~! It's endearing--really!"
        jump positiveF
    "Ask her about her horns":
        hide velvet_neutral
        show velvet_angry:
            xzoom 0.5 yzoom 0.5
        t "She frowns and looks away from you. For a moment, the two of you sit in uncomfortable silence."
        v "I hope you actually came here for a date. I'm a person, not a zoo animal for you to stare at."
        jump negativeF


label positiveF:
    hide velvet_neutral
    show velvet_happy:
        xzoom 0.5 yzoom 0.5
    t "Time flies by as you two chat away. Soon the sunlight outside fades, and its time to leave."
    v "This was really lovely! If you want, would you like to meet up again?"
    jump velvetquestion

#Make the dialouge and general interections longer IF we dont fix the time issue.

label velvetquestion:
menu:
    "I'd love to!":
        jump velvetdate
    "...Nah.":
        hide velvet_happy
        show velvet_shocked:
            xzoom 0.5 yzoom 0.5
        jump start

label negativeF:
    show velvet_angry:
        xzoom 0.5 yzoom 0.5
    t "Her expression turns sour and her tone loses its warmth."
    v "I don't mind awkward dates, but I don't put up with a rude ones."
    jump start

return