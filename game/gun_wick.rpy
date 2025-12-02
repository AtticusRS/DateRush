#This file follows the route of Gun Wick

label gun_wick:
    scene crimealley
    menu:
        "Look just a liiiittle further":
            $ time = time - 2
            t "Why are you still looking?? Did you not hear what I said?"
            t "Are you forgetting what's at stake?"
            jump crimealley2
        "Return to the street":
            $ time = time - 1
            t "Smart fellow! Let's get you back to Norman."
            jump norman


label crimealley2:
    scene crimealley
    show gun_neutral with dissolve
    t "Oh, would you look at that, there's a sentient gun here..."
    t "In Crime Alley..."
    t "The alley way that is... reknown for its concerning rates of crime. Hence the name." 
    t "I'm starting to question whether or not you made that inference earlier..."
    t "Surely you do not intend to stay in such a precarious location?"
    g "What is up with you, kid? State your business immediately!"
    menu:
        "I think I love you":
            hide gun_neutral
            show gun_shocked with dissolve
            t "..."
            pass
        "Apologies good sir, I believe my gps had led me astray!":
            $ time = time - 2
            t "Yeea, that'll fool him..."
            jump crimealley

    g "Uh, wow, kid. That's considerably, er, audacious of you."
    g "Are you a cop? I don't think I can fathom another individual who may perform as, er... uh, eccentric."
    menu:
        "No I'm not a cop, I just know a beauty when I see it!":
            hide gun_shocked
            show gun_happy with dissolve
            pass
        "Yea sorry, I'm going to have to arrest you for... something...":
            hide gun_shocked
            show gun_shocked2 with dissolve
            g "You're worrying me... I must inqure of your angle-"
            g "What are you getting at?"
            t "What ARE you getting at?"
            menu:
                "Put your hands up!":
                    hide gun_shocked2
                    show gun_angry with dissolve
                    g "I have ascertained the necessary action to handle your unfavorable presence!"
                    t "What have you done?!"
                    g "Behold, my innate power!"
                    scene black
                    hide gun_angry with dissolve
                    "A loud bang rings out and your vision fades"
                    hide scene black
                    jump start

    g "Well... a 'beauty' you say? That's quite delightful of you!"
    g "I'm quite enamored by your lovely choice of words."
    $ datedgunwick = True
    g "You've spoken your way to my heart!"
    jump start

#I'm not yet sure where to take this
        
return