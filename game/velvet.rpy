#The file follows the route of Velvet

#This timeline is dialouge heavy, SO for the time mechanic we'd prbably need to figure out things here 

#add illusion of random- roll more dice
#dnd actions! NOT DND
#use up more timeee


label velvet:
    scene gamerbasement
    menu:
        "Roll the dice":
            t "a perfect D20. Your dnd person flawlessly swoons the teifling! She offers a hand to you, stepping to toward the dancing crowd...."
            t "..something off. She's upset?"
            jump intoDNDsuccess
        
        "Roll the dice WITH LUCK!":
            t "Its a natural all right. A natural one."
            jump intoDNDfail

label intoDNDsuccess:
scene tavern

t "Immeditly engaged with the action, the world itself leaks into reality until you find yourself sitting in the tavern."
t "The tiefling, Velvet, listening to your flawlessly executed pick-up line, doesnt seem particallaurly engaged."
v "I havent heard that one before- but if you don't mind being less... Well could we get to know eachother instead of just 'diving right in'?"
menu:
    "Flirt":
        t "Her brows furrow as she stares at you, irratated"
        v "Are you kidding? Could you just listen to me?"
        jump datefailV
    "Ask about her":
        t "She leans to a side, thinking over the question."
        v "Hm.. Well I like Squeaker, but they wander too much for me. My friend Willaim is the same as me in that homebody personaliy."
        t "Velvet pauses to look at your puzzled expression. When the realization hits her, you notice the teiflings ears perk up."
        v "Oh! Squeaker is a mouse that hangs around. Sweet thing."
        jump postive



label datefailV:
    v "Y'know what? I'll just go actually. No point in a conversation if you'd just ignore me."
    jump start

label postive:
menu:
    "Will? That one rich dude?":
        v "Yes! He's a delight!"
        t "Time flies as you two converse. Your chatter goes until the day fades away. She seems delighted with how the date has turned out."
        jump velvetdate

    "Mouse? You...like rodents?":
        v "Sorry if thats an issue. I can just go you uh..look a little green in the face. Sorry."
        jump start

label velvetdate:
    $ datedvelvet = True
    
    t "And so you and this tiefling agree to meet up another time, in another land."

    jump start

label intoDNDfail:
scene tavern
t "As the real world fades away, a fantasy one makes itself known."
t  "Words fumbled out of your mouth as you try to woo the lady. Something about your awkward stumbling made her smile."
menu:
    "Apologise":
        t "The woman waves her hands."
        v "Nono its alright! Its cute-really!"
        jump positiveF
    "Ask about horns":
        t "She frowns and looks away from you. For a moment, the two of you sit in uncomfortable silence"
        v "I hope you actually came here for the date instead of a zoo exhibit."
        jump negativeF


label positiveF:
    t "Time flies by as you two chat away. Soon the sunlight outside fades, and its time to leave."
    v "This was really lovely- if you want we can meet up again?"
    jump velvetquestion

#Make the dialouge and general interections longer IF we dont fix the time issue.

label velvetquestion:
menu:
    "I'd love to!":
        jump velvetdate
    "..nah.":
        jump start

label negativeF:
    t "Her expression turns sour and her tone loses its warmth."
    v "I don't mind a awkward encounter, but I don't put up with a rude one."
    jump start

return