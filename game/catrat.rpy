#This file follows the route of the Cat and the Rat

#Probably should show the Rat here once we get the image (on the left)

label catrat:
    $ time - 2
    t "Well, would you look at that!"
    t "It's a rat in an alley way... how queer!"
    t "Oh? It seems that the rat has a visitor... that is a cat?"

    #Show Cat here once we get the image (on the right)
    
    t "Perhaps we should turn our attention elsewhere? I'm sure we can infer how this altercation will end."
    menu:
        "Return to your original date plans":
            jump crimealley
        "Just wait a little longer...":
            t "I see... you're going to waste precious time... again."

            #Perhaps we'll have the Cat come from the right and slowly go center here

            t "The cat is sneaking up on the rat, surely you don't want to see the next part where-"

            #Show Cat with flowers? Show shocked Rat as well?

            t "The cat pulls out flowers for the rat??"

            #Cat and Rat hugging sprite here?

            c "Meow meow!!"
            r "Sqeuak squeak!!!"
            t "This, I can't help but admire! It is truly adorable."
            t "Doesn't their love remind you of something? Perhaps your own pursuit of a love interest? Hm?"
            $ time + 10
            "You feel empowered on your quest to meet Norman! Almost like you suddenly have more time! (plus 10 minutes)"
            jump crimealley

return