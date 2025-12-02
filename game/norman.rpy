#This file follows the route of Norman

label norman:
    scene streetside
    t "Alright! Let's get to Norman!"
    
    show screen time_meter
    
    t "You have [time] minutes to get to him, what do you suggest?"
    menu:
        "Walk into the bar" if goneintobar == False:
            t "A bar, why?"
            t "Are you sure?"
            menu:
                "Yes! Drinks, drinks, drinks!":
                    t "I think you actually have a problem..."
                    jump normanbar
                "No actually":
                    t "You had me worried for a moment there!"
                    jump norman
        "Continue down the street":
            $ time = time - 2
            t "The obvious choice."
            jump continuestreet
        "Get a taxi" if calledtaxi == False:
            t "The timely choice. You pull out your phone and call a Ewber, although the closest one is... definitely full of character."
            jump normantaxi
        "Investigate the nearby alley way":
            $ time = time - 2
            t "You don't see anything exactly remarkable. Cars rush down the road as you stand on the cracked pavement. You really should get moving now."
            t "Especially because you don't have all of the time in the world..."
            jump crimealley

#This is where the transition from Norman's route to Gun Wick's route begins

label crimealley:
    scene crimealley
    menu:
        "Investigate the alley even further":
            $ time = time - 2
            t "Sure. Look at the alley way. The alley next to the bar that's covered in graffiti. Do you know what they call this alley?"
            t "CRIME Alley. Its called Crime Alley. Happy?"
            t "Now it's time to stop looking over there, there's nothing else to see."
            jump gun_wick

        #The if statement here means the player can only witness the Cat and Rat date once

        "Investiagte the small creature that scampered behind the dumpster" if witnesscatrat == False:
            $ time = time - 2
            $ witnesscatrat = True
            t "Why do you concern yourself with such trivial matters?"
            jump catrat
        
        #The if statement here means that the player can only flirt with the narrator once. 
        #If they give up on flirting with the narrator, they have missed their chance!
        
        "Flirt with the narrator" if flirtwithnarrator == False:
            $ time = time - 2
            $ flirtwithnarrator = True
            t "You- what?! Hello?? Are you insane?"
            jump narrator
        "Return to the street":
            $ time = time - 1
            t "Smart fellow! Let's get you back to Norman."
            jump norman

#This is the route where you go into the bar

label normanbar:
    $ goneintobar = True
    
    #This immediately results in a failure

    $ time = time - 25
    t "So, you're in the bar."
    t "You might as well have a drink"
    menu:
        "Don't mind if I do!":
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
    $ time = time - 5
    $ calledtaxi = True
    "The taxi finally arrives"
    t "Thank goodness, how long was that? Were you counting? I would say 5 minutes but I don't really have any way to be sure."
    t "Forget it, forget it. The taxi is here now, that's what matters."
    "You get into the taxi and the taxi driver grunts as to acknowledge your presence."
    menu:
        "I'd like to go to the Nondiscript Cafe please?":
            "The taxi driver grunts"
            t "I guess that means 'okay'."
            pass
        "I'm in a bit of a rush, I need to go to the Nondiscript Cafe!":
            "The taxi driver grunts"
            t "I don't think they share the same sense of urgency..."
            pass
    menu:
        "How much will the fare be?":
            "The taxi driver seems to perk up at the word 'fare', but alas no verbal response is given"
            t "This is going to take a minute. Or multiple minutes."
            jump normantaxifare
        "I will NOT be paying by the way":
            t "You imbecile!"
            "In a flash, the driver kicks you out of the car"
            t "That was impressive... and hopefully that taught you a lesson!"
            t "Now we have to live with the consequences, and find some other way to get to Norman on time!"
            jump norman
    
label normantaxifare:
    menu:
        "Will it be $5?" if norman5ask == False:
            $ time = time - 2
            $ norman5ask = True
            "No response"
            t "The air is exceptionally cold, I can just feel that they didn't like to hear you ask that."
            t "While lowballing can sometimes be effective, you need to be more reasonable, we don't have a lot of time!"
            jump normantaxifare
        "Will if be $7?" if norman7ask == False:
            $ time = time - 2
            $ norman7ask = True
            "No response"
            t "I don't think that was the right answer..."
            t "Don't forget to be reasonable! Time is wasting."
            jump normantaxifare
        "Will it be $10?":
            $ time = time - 2
            "There is a pause, but then the driver grunts in agreement"
            t "Whew, I'm pretty sure you only have $10."
            t "I would say that's uh... pretty reasonable."
            jump normantaxi2
        "Will it be $15?":
            $ time = time - 3
            "The driver grunts in agreeance immediately"
            t "Uhm... do you even have $15?"
            "A fly buzzes out of your wallet"
            t "That's NOT reasonable."
            "In a flash, the driver kicks you out of the car"
            t "That was impressive, but very unfortunate. Now how will we get to Norman on time?"
            jump norman

label normantaxi2:
    "The driver accepts your money and begins driving"
    t "Alright! Now we're making progress."
    t "But, it seems the driver is going kind of slow..."
    t "Maybe you can prompt him to go faster?"
    menu:
        "Excuse me, can you go faster?":
            $ time = time - 1
            "The driver grunts and ever so slightly picks up the pace"
            t "That... is somewhat better..."
        "Say nothing":
            $ time = time - 5


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
            $ time = time - 5
            t "Oh boy... you're already running low on time."
            $ wetclothes = False
            "You go home and change... it takes a while."
            menu:
                t "Do you think you can make it in time? Or, do you want to give up and drown your sorrows out with an ice-cold drink?"
                "Go to the bar...":
                    t "How dreary. Truly dissapointing. But, there's no arguing with the fat chance you're going to be incredibly late."
                    jump normanbar
                "I'm not giving up yet!":
                    t "That's the spirit! You might have a chance afterall, old chum."
        "Continue on... in wet clothes":
            $ time = time - 2
            t "Your determination is admirable! It seems you understand how little time you have to spare."
            t "Let us continue then!"
    
    #Each time you reach the destination of your date, the narrator will check your time and see if you made it on time or not.

    menu:
        "Head into the cafe and meet Norman":
            t "Alright! Let's check the time first, to see if Norman is going to be there or not."
            t "You have [time] minute(s) left."
        "Wait! I'm too nervous!":
            t "Now is not the time to second guess yourself! There's no going back from here!"
            t "Let's check the time first, to see if Norman is going to be there or not."
            t "You have [time] minute(s) left."
            if time <= 0:
                t "Oh no... it seems you're out of time."
                if goneintobar == True:
                    t "Maybe you would've made it if you didn't go into the bar."
                else:
                    pass
                t "I'm sorry, you'll have to try again."
                jump start
            else:
                pass
            t "Amazing! It seems you have managed to make it on time, beating the odds!"
            t "Let's meet Norman, the man of the hour!"
            if wetclothes == True:
                jump normandate_wetclothes
            else:
                jump normandate_normal

#This is the date with Norman!

label normandate_normal:
    $ datednorman = True
    show norman_happy:
        xalign 0.5
        yalign 0.0
        xzoom 1.1
        yzoom 1.1
    n "Oh, hello!"
    n "It's so great to see you! I love your outfit!"
    n "I hope my apparel isn't too underwhelming..."
    menu:
        "Not at all!":
            n "I appreciate that. Your reassurance means a lot to me!"
            pass
        "Uhm yea, actually... your outfit kind of sucks":
            hide norman_happy
            show norman_neutral:
                xalign 0.5
                yalign 0.0
                xzoom 1.1
                yzoom 1.1
            n "Oh..."
            hide norman_neutral
            show norman_happy with dissolve
            n "Oh! Haha, you got me! That's surely an abrasive joke though..."
            menu:
                "I'm not joking, your wardrobe needs work.":
                    hide norman_happy
                    show norman_shocked with dissolve:
                        xalign 0.5
                        yalign 0.0
                        xzoom 1.1
                        yzoom 1.1
                    n "Uhh, well maybe you could help me with that or something??"
                    n "Like going on a thrifting trip or...."
                    menu:
                        "I don't think I can be seen in public with you...":
                            hide norman_shocked
                            show norman_angry with dissolve:
                                xalign 0.5
                                yalign 0.0
                                xzoom 1.1
                                yzoom 1.1
                            n "Alright well this is obviously not working out."
                            n "Goodbye! No, not 'good'-bye, just bye!"
                            t "Who are you??"
                            jump start
                        "I don't think I can afford the amount of clothes you'd need to fix your style...":
                            hide norman_shocked
                            show norman_angry with dissolve:
                                xalign 0.5
                                yalign 0.0
                                xzoom 1.1
                                yzoom 1.1
                            n "Alright well this is obviously not working out."
                            n "Goodbye! No no, not 'good'-bye, just bye!"
                            t "Who are you??"
                            hide norman_angry
                            jump start
                "You're right, sorry! Joke was a little out of hand there...":
                    n "That's alright! The first step to being a better person is acknowledging your mistakes!"
                    n "Seeing that you are aware of a small slip-up, I foresee maturity within you!"
    jump start

label normandate_wetclothes:
    $ datednorman = True
    n "Oh, hello!"
    n "It's so great to see you! Your attire is... stunningly unique!"
    menu:
        "Oh yea... lol, about that...":
            pass
        "Long story short...":
            pass
    n "No worries! I totally understand!"
    n "You know, I actually find it really endearing that you cared more about getting here than your appearance."
    n "I believe that says a lot of positive things about yourself."
    menu:
        "Thank you so much!":
            n "Of course!"
            pass
        "Well you charmer!!":
            n "Oh gosh! I'm just being polite you know!"
            pass
    jump start

return