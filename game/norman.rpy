#This file follows the route of Norman

label norman:
    scene streetside
    menu:
        "Walk into the bar" if goneintobar == False:
            t "A bar, why?"
            jump normanbar
        "Continue down the street":
            t "The obvious choice."
            jump continuestreet
        "Get a taxi":
            t "The timely choice. You pull out your phone and call a Ewber, although the one in your price range is...defiently full of character."
            jump normantaxi
        "Investigate the nearby alley way":
            t "You don't see anything exactly remarkable. Cars rush down the road as you stand on the cracked pavement. You really should get moving now."
            jump crimealley

#This is where the transition from Norman's route to Gun Wick's route begins

label crimealley:
    scene crimealley
    menu:
        "Investigate the alley even further":
            t "Sure. Look at the alley way. The alley next to the bar that's covered in graffiti. Do you know what they call this alley?"
            t "CRIME Alley. Its called Crime Alley. Happy?"
            t "Now it's time to stop looking over there, there's nothing else to see."
            jump gun_wick

        #The if statement here means the player can only witness the Cat and Rat date once

        "Investiagte the small creature that scampered behind the dumpster" if witnesscatrat == False:
            $ witnesscatrat = True
            t "Why do you concern yourself with such trivial matters?"
            jump catrat
        
        #The if statement here means that the player can only flirt with the narrator once. 
        #If they give up on flirting with the narrator, they have missed their chance!
        
        "Flirt with the narrator" if flirtwithnarrator == False:
            $ flirtwithnarrator = True
            t "You- what?! Hello?? Are you insane?"
            jump narrator
        "Return to the street":
            t "Smart fellow! Let's get you back to Norman."
            jump norman

#This is the route where you go into the bar

label normanbar:
    $ goneintobar = True
    $ time - 25
    t "So, you're in the bar."
    t "You might as well have a drink"
    menu:
        "Okay":
            t "Now that you've had a drink, do you want to try and meet up with Norman?"
        "Might as well...":
            t "Now that you've had a drink, do you want to try and meet up with Norman?"
    menu:
        "I guess":
            jump norman
        "MORE DRINKS!!":
            t "That's... an option too."
            "You then drank yourself into oblivion. Hopefully you're of drinking age."
            jump start

#This is the route where you take the taxi

label normantaxi:


#This is the route where you continue down the street

label continuestreet:
    t "Good thinking! We'll get there in no time if you continue like thi-"
    "SPLASH!!"
    $ wetclothes = True
    t "Oh heavens!! It seems a passing car has plowed through a puddle, splashing the water all over you!"
    t "Your clothes are irreperably drenched!!!"
    t "What will you do?"
    menu:
        "Go home and change":
            t "Oh boy... you're already running low on time."
            $ wetclothes = False
            "You go home and change... it takes a while."
            menu:
                t "Do you think you can make it in time? Or do you want to drown your sorrows out with an ice-cold drink?"
                "Go to the bar...":
                    t "How dreary. Truly dissapointing. But, there's no arguing with the fat chance you're going to be incredibly late."
                    jump bar
                "I'm not giving up yet!":
                    t "That's the spirit! You might have a chance afterall, old chum."
        "Continue on... in wet clothes":
            t "Your determination is admirable! It seems you understand how little time you have to spare."
            t "Let us continue then!"
    
    #Each time you reach the destination of your date, the narrator will check your time and see if you made it on time or not.

    menu:
        "Head into the cafe and meet Norman":
            t "Alright! Let's check the time first, to see if Norman is going to be there or not."
            t "You have [time] minutes left."
        "Wait! I'm too nervous!":
            t "Now is not the time to second guess yourself! There's no going back from here!"
            t "Let's check the time first, to see if Norman is going to be there or not."
            t "You have [time] minutes left."
            if time <= 0:
                t "Oh no... it seems you're out of time."
                t "I'm sorry, you'll have to try again."
                jump start
            else:
                pass
            t "Amazing! It seems you have managed to make it on time, beating the odds!"
            t "Let's meet Norman, the man of the hour!"
            jump normandate

#This is the date with Norman!

label normandate:
    $ datednorman = True
    "Congrats, you dated Norman!"
    jump start

return