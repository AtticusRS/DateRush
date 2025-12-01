#This file follows the route of the Cat and the Rat

#Probably should show the Rat here once we get the image (on the left)

label catrat:
    $ time = time - 2
    show rat at left
    t "Well, would you look at that!"
    t "It's a rat in an alley way... how queer!"
    t "Oh? It seems that the rat has a visitor... that is a cat?"
    hide rat
    show ratsee at left with dissolve
    show catsneaky at right with dissolve:
        yalign 1
    
    t "Perhaps we should turn our attention elsewhere? I'm sure we can infer how this altercation will end."
    menu:
        "Return to your original date plans":
            $ time = time - 2
            jump crimealley
        "Just wait a little longer...":
            t "I see... you're going to waste precious time... again."

            hide catsneaky with dissolve
            show catsneaky at center with dissolve:
                yalign 1

            t "The cat is sneaking up on the rat, surely you don't want to see the next part where-"

            hide catsneaky
            show catflowers at center with dissolve:
                yalign 1

            hide ratsee
            show ratwow at left with dissolve

            t "The cat pulls out flowers for the rat??"

            hide ratwow
            show ratlove at left with dissolve

            c "Meow meow!!"
            r "Sqeuak squeak!!!"
            t "This, I can't help but admire! It is truly adorable."
            t "Doesn't their love remind you of something? Perhaps your own pursuit of a love interest? Hm?"
            $ time + 10
            "You feel empowered on your quest to meet Norman! Almost like you suddenly, and somehow, have more time! (plus 10 minutes)"
            jump crimealley

return