#This file follows the route of Gun Wick

label gun_wick:
    scene crimealley
    menu:
        "Look just a liiiittle further":
            t "Why are you still looking?? Did you not hear what I said?"
            jump crimealley2
        "Return to the street":
            t "Smart fellow! Let's get you back to Norman."
            jump norman
    
#Something with the gun will happen here, probably
#Perhaps Gun Wick should appear here (with a 'show' command), but we don't have his image files yet, so we cannot perform this action
#I believe a slow dissolve transition here would be phenomenal and perfect for comedic effect

label crimealley2:
    scene crimealley
    t "Oh, would you look at that, there's a sentient gun here..."
    t "In Crime Alley..."
    t "The alley way that is... reknown for its concerning rates of crime. Hence the name." 
    t "I'm starting to question whether or not you made that inference earlier..."
    t "Surely you do not intend to stay in such a precarious location?"
    g "What is up with you, kid? State your business immediately!"
    menu:
        "I think I love you":
            t "..."
        "Apologies good sir, I believe my gps had led me astray!":
            t "Yeea, that'll fool him..."
            jump crimealley

    g "Uh, wow, kid. That's considerably, er, audacious of you."
    g "Are you a cop? I don't think I can fathom another individual who may perform as, er... uh, eccentric."

    jump crimealley

#I'm not yet sure where to take this, take the regins Addison!
        
return