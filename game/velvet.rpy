#The file follows the route of Velvet

#This timeline is dialouge heavy, SO for the time mechanic we'd prbably need to figure out things here 
#add bar fight
#add illusion of random- roll more dice
#dnd actions! NOT DND
#use up more timeee


label velvet:
    scene gamerbasement
    menu:
        "Roll the dice!":
            t "a perfect D20. Your DnD character flawlessly swoons the tiefling! She offers a hand to you, stepping to toward the dancing crowd...."
            t "...Something seems off. She's upset?"
            jump intoDNDsuccess
        
        "Roll the dice...":
            t "It's a natural all right. A natural one."
            jump intoDNDfail

label intoDNDsuccess:
scene tavern

t "Immediately engaged with the action, the world itself leaks into reality until you find yourself sitting in the tavern."
t "Despite your flawlessly executed pick-up line, The tiefling, Velvet, doesn't seem particularly engaged."
v "Hmph. I havent heard that one before. Honestly, maybe we could we get to know eachother instead of just 'diving right in?' You've got some nerve."
menu:
    "Flirt":
        t "Her brows furrow as she stares at you-- she's clearly irritated."
        v "Are you kidding? You think that's gonna work on me??"
        jump datefailV
    "Ask her about her interests":
        t "She stares off for a second as her head leans to one side, thinking over your incredibly open-ended question."
        v "Hm... well I love hanging out with my friends! I really like Squeaker, but they wander too much for me. My friend William is more my speed-- he's got that homebody personality."
        t "Velvet pauses to look at your puzzled expression. When the realization hits her, you notice the teifling's ears perk up."
        v "Oh! Squeaker is a mouse that hangs around here. Sweet thing. They're just so cute-- they fit right into my hand when they decide to sit still for once!"
        jump postive



label datefailV:
    v "Y'know what? I'll just go, actually. No point in trying to have a conversation if you're gonna be a creep."
    jump start

label postive:
menu:
    "William? That one rich dude?":
        v "Yes! He's a delight! I'm surprised you know him! It's quite hard to become close with someone so sophisticated. I certainly have my ways, though. Tehe~"
        t "Time flies as you two converse. Your chatter goes until the day fades away. She seems delighted with how the date has turned out."
        jump velvetdate

    "A mouse? You... hang out with rodents?":
        v "Well SORRY if that's an issue. Hmph! I can just go--you CLEARLY have no taste. Sorry, but not sorry."
        jump start

label velvetdate:
    $ datedvelvet = True
    
    t "And so, you and this tiefling agree to meet up another time, in another land."

    jump start

label intoDNDfail:
scene tavern
t "As the real world fades away, a fantasy one makes itself known."
t  "Words fumble out of your mouth as you try to woo the lady. Something about your awkward stumbling makes her smile."
menu:
    "Apologize":
        t "The woman waves her hands."
        v "No, no its alright-- hehe~! It's endearing--really!"
        jump positiveF
    "Ask her about her horns":
        t "She frowns and looks away from you. For a moment, the two of you sit in uncomfortable silence."
        v "I hope you actually came here for a date. I'm a person, not a zoo animal for you to stare at."
        jump negativeF


label positiveF:
    t "Time flies by as you two chat away. Soon the sunlight outside fades, and its time to leave."
    v "This was really lovely! If you want, would you like to meet up again?"
    jump velvetquestion

#Make the dialouge and general interections longer IF we dont fix the time issue.

label velvetquestion:
menu:
    "I'd love to!":
        jump velvetdate
    "...Nah.":
        jump start

label negativeF:
    t "Her expression turns sour and her tone loses its warmth."
    v "I don't mind awkward dates, but I don't put up with a rude ones."
    jump start

return