#This file follows the route of the Narrator

label narrator:
    scene crimealley
    menu:
        "Some could say, I'm crazy for you...":
            $ time - 2
            t "No, no no no. This is not going to work. Especially not with lines as corny as those."
            t "Do you even hear yourself? Not in a million days."
        "Nobody said anything!":
            $ time - 1
            t "That's right."
            t "*Scoff*"
            t "You weirdo."
            jump crimealley

    menu:
        "But I only have eyes for you":
            $ time - 2
            t "Me? ME?? You can't even SEE me!?"
        "*Sigh*, you're right...":
            $ time - 1
            t "Now now, don't give me that. The answer should've been obvious from the start."
            t "Upon settling that, let's get back to what we came here for? Hm?"
            jump crimealley

    menu:
        "My love for you reaches beyond the confines of visual perception":
            $ time - 2
            t "Well, when you put it like that... it sounds..."
            t "Terrible! No, I cannot even begin to imagine a relationship that exists between the dimensions of reality!!"
            t "Though it does sound like a quite ethereal experience..."
        "Drats, I feared you'd respond this way...":
            $ time - 1
            t "Your judgement is questionable at times, but at least we can agree here."
            t "It seems partially rationale to assume you posess... some intelligence."
            jump crimealley
    menu:
        "YOU are an etheral experience":
            $ time - 2
            t "Oh... you! I can't deny it much longer..."
            t "Your presence does invoke some semblance of a sensation within me..."
            t "But... how? How will WE exist?"
        "YOU are worth reaching beyond the confines of logic":
            $ time - 2
            t "Oh... you! I can't deny it much longer..."
            t "Your presence does invoke some semblance of a sensation within me..."
            t "But... how? How will WE exist?"
    menu:
        "Just like this!":
            $ datednarrator = True
            t "Your answer provides me reassurance through truth. This is enough for me too."
            t "Here's my number :)"
            jump start

    #I think I'm losing it. No... I'm sure I'm losing it