#This file follows the route of William After

#William's timer
screen william_timer:
    timer 0.01 repeat True action If(williamtimed > 0, true=SetVariable('williamtimed', williamtimed - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #^This is a timer I peeled directly off of a video
    #It's supposed to send the player to the next description of a building when the timer runs out

label william_after:
    stop music fadeout 3.0
    queue music "sounds/WilliamBgMusic.mp3" volume 0.1
    scene streetside
    "You click on the finely aged man's profile"
    "*Bzzzt bzzzt*"
    t "Hm? It seems you've recieved a text from somebody."
    t "Oh wow, the gentlemen you've chosen has already responded!"
    play sound "sounds/William_Hello.mp3"
    show william_happy with dissolve:
        xalign 0.5
        yalign 0.0
    w "'Do you want to meet at the Ritz?'"
    menu:
        "Absolutely!":
            pass
        "No thank you...":
            t "Maybe another time William..."
            jump start
            hide william_happy
    hide william_happy

    #The timer shows up here now that the player knows how much time they have
    show screen time_meter

    t "Alright!! You have... only [time] minutes to get there..."
    t "Let's see what we can do in the time you have!"
    t "Now, what is the Ritz? Never heard of it either? No matter, Oogle Maps has all the knowledge we need!"
    t "Here we are! It says the Ritz is approximately 15 minutes away if you chose to walk. That is, if there are minimal disruptions."
    t "On the other hand, there is the choice of getting a ride, but it seems the most readily available option is a limo."
    t "You would have a better chance of getting there if you took the limo, but it's more expensive and it doesn't realy seem like... you?"
    t "Unless that's how you want to appear."
    t "What do you think?"
    jump choosing_for_william

    # Deciding how to get to William

    label choosing_for_william:
        if thinkingalot == True:
            t "So, what'll it be? Did you come up with something truly ingenious??"
        else:
            pass
        menu:
            "I'll walk!":
                $ time = time - 1
                t "Right! It says more about your character."
                jump on_foot
            "Limo it is!":
                $ time = time - 1
                t "Are you sure?"
                menu:
                    "Pester me no longer! I am sure of my choice!":
                        t "Alright, cool your jets."
                        jump williamlimo
                    "Errr, actually on second thought...":
                        $ time = time - 1
                        t "I think this will work out in the end!"
                        t "Don't forget about how much time you have though!"
                        pass
            "Think about it" if thinkingalot == False:
                $ time = time - 2
                t "Riiight, I see. Hm, I guess I can see that something like this would require lots of consideration."
                t "Don't forget how much time you have though..."
                jump brain_cramp

    # Thinking too much

    label brain_cramp:
        $ thinkingalot = True
        menu:
            "Think eeeeeven more!":
                $ time = time - 2
                t "Haha, okay right. You're THINKING."
                t "I really, truly, am shocked. Honest."
                t "Now, please, let us do something productive, like getting to your DATE."
                pass
            "Fine, I'll do something else.":
                $ time = time - 1
                t "Wow, you're being compliant? Thank you! I mean it!"
                t "I'm sure William will appreciate it too."
                jump choosing_for_william
        menu:    
            "Think think think thinking thinker":
                $ time = time - 2
                t "You're just on a roll today! Woohoo! You're thinking, you're-"
                t "Oh... what's wrong with your face?"
                t "It looks all scrunched like you're in pain and-"
                show black with dissolve
                t "Omg, are you dying?!"
                "Your brain feels like it's about to explode... btw"
                t "I don't even- just like- uhhhh"
                t "I think you need to lay down for sometime..."
                t "Like... maybe 8 minutes..."
                $ time = time - 8
                "You lay down for a while..."
                hide black with dissolve
                t "Welcome back! Let's not... think... too much again?"
                jump choosing_for_william
            "I'm done with this bit.":
                $ time = time - 1
                t "Just so you know, it was NOT funny."
                t "NOooobody is laughing."
                jump choosing_for_william

    # Choosing how to get to William, but on foot

    label on_foot:
        t "So you're walking, do even you have 15 minutes to spare for walking?"
        t "Or do you want to do anything other than walking?"
        menu:
            "I'm juuust gonna walk...":
                t "Okay! Solid! Works, it works for sure."
                t "Are you sure?"
                menu:
                    "Yes, let me walk":
                        $ time = time - 1
                        t "Okayy fine. Only because you said so."
                        jump walking_along
                    "Noo, maybe not":
                        $ time = time - 1
                        t "Cool! Don't forget, the choice is yours!"
                        t "But also time is ticking!!"
                        jump on_foot
            "I wanna skip my way there!":
                $ time = time - 1
                $ skippedto_william = True
                t "Alright! I like that enthusiasm! Could save you some time too."
                jump skipping_along

    label walking_along:
        "You begin walking"
        t "So... walking, eh?"
        t "Pretty... interesting I must say."
        t "Don't forget not to step on the cracks! Or whatever..."
        menu:
            "Step on a crack":
                $ time = time - 1
                t "You're very spiteful"
                "An icy cold chill runs down your spine"
                t "Woah, you look scared? What- did the crack do that?"
                "The fear of what heinous consequences your act of definace may have brought upon your maternal figure staggers your progress-"
                $ time = time - 4
                show black with dissolve
                "You become immobile for 5 minutes"
                t "Hello? Hello? Heello??"
                hide black with dissolve
                t "Oh, your face is moving again, what was that? Are you okay?"
                t "Nevermind, we don't have the time to ask the questions, you need to get moving!"
                t "And avoid any further... complications...?"
            "Don't step on a crack":
                $ time = time - 1
                t "Soo, you're still walking!"
                t "And not stepping on any cracks, I see!"
                t "Who knows what could've happened if you did..."
        show dollar_bill with dissolve:
            xalign 0.5
            xzoom 0.8
            yzoom 0.8
        t "Hey look, there's a dollar bill hanging in the air!"
        menu:
            "Grab the dollar bill":
                $ time = time - 2
                "You slowly reach for the dollar bill, getting very very very close-"
                hide dollar_bill with dissolve
                "But the dollar bill is pulled away"
                t "You actually believed that?! Now you just look stupid and wasted some time."
            "Pass up on the dollar bill":
                $ time = time - 1
                hide dollar_bill with dissolve
                "You stride confidently past the dollar bill"
                t "I'll give you credit for that, I totally thought you were going to fall for that!"
        scene crosswalk_white:    
            xzoom 0.85
            yzoom 0.85
        t "Hey, look, a crosswalk!"
        scene crosswalk_red:
            xzoom 0.85
            yzoom 0.85
        t "Oh no, the hand appeared on the sign! Do you go now or wait, like a respectful citizen?"
        menu:
            "Go now!":
                $ time = time - 1
                scene streetside
                "You rush across swiftly"
                t "Phew! You made it-"
                play sound "sounds/CarsRushing1.mp3"
                "The sound of rushing cars fills the space behind you"
                t "With not-so much time to spare..."
                t "It's best not to dwell on it!"
            "Wait respectfully":
                $ time = time - 1
                t "Alright, I can see why you'd wait!"
                $ time = time - 1
                t "Though it kind of seems that you might've had some time..."
                $ time = time - 1
                t "And could've gone, maybe about right now..."
                $ time = time - 1
                t "Maybe it's not too late to try?"
                menu:
                    "Step forward":
                        $ time = time - 1
                        scene crosswalk_busy:
                            xzoom 0.85
                            yzoom 0.85
                        play sound "sounds/CarsRushing1.mp3"
                        "As you begin to step forward, cars rush forward and fill the street"
                        t "Oh... wow!"
                    "Wait some more":
                        $ time = time - 1
                        t "Are you sure, maybe it'd be better to-"
                        scene crosswalk_busy:
                            xzoom 0.85
                            yzoom 0.85
                        play sound "sounds/CarsRushing1.mp3"
                        "Cars rush forward, and fill the street before you"
                        t "Oh... wow!"
                t "Well, now we have to wait for these to pass..."
                $ time = time - 4
                scene crosswalk_white with dissolve:         
                    xzoom 0.85
                    yzoom 0.85
                "The cars take 4 minutes to pass"
                t "Alright, at least you can cross safely now!"
        scene streetside
        t "Oh what the, is that a homeless person?"
        show gun_happy at left with dissolve
        t "They kind of look like they're struggling, should you help?"
        menu:
            "Help the homeless person":
                $ time = time - 1
                t "Sure, I think you need some good karma right about now."
                $ time - 2
                "You help the homeless person up"
                if datedgunwick == True:
                    jump gunwick_conversation
                else:
                    pass
                g "Your aid is greatly appreciated, random stranger!"
                t "Oh look at that, I can see the Cafe!"
                jump predate_william
            "Disregard the homeless person":
                hide gun_happy with dissolve
                $ time = time - 1
                t "It's not our fault the economy is collapsing!"
                t "Well, it's not mine- I don't know about you..."
                g "Hey, you!"
                $ time = time - 2
                "The homeless person's shouting from behind you scares you and you trip over yourself"
                g "Actually, I rescind my previous statement, I no longer covet your aid..."
                t "Okay then..."
                t "Oh look at that, I can see the Ritz!"
                jump predate_william

    label gunwick_conversation:
        g "Your aid is greatly appreciated-"
        g "Wait-"
        g "I have reason to suspect we may have interacted in the past..."
        g "Oh by golly, it's you!"
        g "I am very glad to see that you're still as kind as you were on the day we met!"
        g "Good luck on your journey!!"
        $ time = time + 5
        "You become inspired, gain some time (5 minutes), and continue on walking"
        t "Oh look at that, I can see the Ritz!"
        jump predate_william
    
    label skipping_along:
        "You begin skipping"
        t "Alright, I could get behind this! Skipping! Yea!"
        show dollar_bill:
            xalign 0.5
            xzoom 0.8
            yzoom 0.8
        $ timed = 3
        $ timer_range = 3
        $ timer_jump = 'dollarbill_accident'
        show screen countdown
        menu:
            "Watch out for that floating dollar bill!":
                $ time = time - 1
                hide screen countdown
                hide dollar_bill
                t "Woah nice dodge!"
                hide screen countdown
                jump skipping_along2
            "Wait, what's going on? I have reason to believe there is an action I should take to prevent a catastrophe, but I'm entirely unaware of the consequences of my inability to perceive the danger at hand!":
                jump dollarbill_accident

    label dollarbill_accident:
        $ time = time - 8
        hide dollar_bill
        show black
        "The dollar bill hits you in your face, causing you to lose your vision and fall over at the same time"
        hide black with dissolve
        t "Ouchh, what even was that?"
        t "Oh, it looks like somebody was hanging up a dollar bill as a prank- hoping somebody would fall for it??"
        t "That is just so dumb, would anyone fall for that? I don't think I can even fathom someone who-"
        t "Well, you know there may be some exceptions..."
        t "... like you."
        jump skipping_along2

    label skipping_along2:
        t "Let's keep an eye out for more obstacles like that!"
        t "Skipping at a speed like this, you'll never know when something is going to come at you next!"
        scene crosswalk_white:
            xzoom 0.85
            yzoom 0.85
        t "Oh, a crosswalk-"
        scene crosswalk_red:
            xzoom 0.85
            yzoom 0.85
        t "But the window to cross is closing!"
        t "What do you do?"
        $ timed = 3
        $ timer_range = 3
        $ timer_jump = 'crosswalk_accident'
        show screen countdown
        menu:
            "Cross now!":
                hide screen countdown
                $ time = time - 1
                "You fly through the crosswalk, making it to the other side unscathed"
                t "Oh whew! That could've been bad-"
                play sound "sounds/CarsRushing1.mp3"
                "The sound of rushing cars fills the space behind you"
                t "But it wasn't! Just think about that... only that..."
                jump skipping_along3
            "Wait, wait, wait!":
                $ time = time - 1
                hide screen countdown
                jump crosswalk_accident

    label crosswalk_accident:
        scene crosswalk_busy:
            xzoom 0.85
            yzoom 0.85
        "As you attempt to stop before the crosswalk, your momentum causes you to trip, launching you into the road as cars are pulling up"
        t "Oh what-"
        play sound "sounds/CarsRushing1.mp3"
        show black
        t "You're gonna have to wait to date William until you're out of the hospital..."
        t "Sorry!"
        hide black
        jump start

    label skipping_along3:
        t "That could've been bad!"
        t "Like was saying, it's always best to watch out for these things."
        show gun_happy
        $ timed = 3
        $ timer_range = 3
        $ timer_jump = 'homeless_accident'
        show screen countdown
        menu:
            "Is there something in the way?":
                hide screen countdown
                jump homeless_accident
            "There is an impediment in the way and I must avoid it! It is necessary to my current objective to employ my utmost of effort in order to circumvent this incredibly pressing issue!":
                $ time = time - 1
                hide screen countdown
                hide gun_happy with dissolve
                t "Whew, that was super close!"
                jump skipping_along4

    label homeless_accident:
        hide gun_happy
        $ time = time - 8
        show black
        "You collide directly with the homeless person, knocking you both to the ground"
        hide black with dissolve
        show gun_shocked with dissolve
        g "Oh my- have you no need to observe what lays before you?"
        t "It's best we go while we still can!"
        "You get up quickly and rush off"
        hide gun_shocked
        jump skipping_along4

    label skipping_along4:
        t "Oh look at that, I think I see the Ritz!"
        jump predate_william

#This is like a precursor stage to dating William

label predate_william:
    scene fancydiner_outside
    t "You made it! Let's see how much time you have."
    t "You have about [time] minute(s) left."
    if time <= 0:
        t "Oh no... it seems you're out of time."
        t "I'm sorry, you'll have to try again."
        jump start
    else:
        pass
    t "Nice, then William shouuuld be here!"
    t "Wow, this place is... stunning! Maybe the limo would've made for a more appropriate entrance."
    t "Hopefully Sir William reeaaally appreciates your character! Hopefully..."
    t "Now, speaking of Mr. After, where is he?"
    "*Bzzzt bzzzt*"
    t "I wonder if it's William..."
    play sound "sounds/William_Happy1.mp3"
    show william_happy with dissolve:
        xalign 0.5
        yalign 0.0
    w "'If you're wondering where to go, just head on into the V.I.P area!'"
    hide william_happy
    t "Alright! Into the... V.I.P. lounge?!"
    menu:
        "Meet William in the V.I.P. lounge":
            t "Here goes nothing!"
            jump williamdate
        "Ghost William":
            t "Are you sure?"
            menu:
                "Yes...":
                    t "Maybe it's for the best..."
                    jump start
                "No! I won't give up now!":
                    t "That's the spirit!"
                    jump williamdate

# LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO

label williamlimo:
    t "Alright 'Mr. High and Mighty', the limo should be here in about 5 minutes."
    $ time = time - 5
    t "Great, the limo is here! Those 5 minutes went by inexplicably fast!"
    scene incar
    "The limo driver begins driving as soon as you are seated"
    t "Awesome, this limo driver knows what's up!"
    t "Wait, you never told the driver what the building looks like!!"
    t "Look at your phone, we'll have to remember what it looks like and tell the driver when to stop!!"
    "You look at your phone, the Ritz is a tall, red building with gold accents and-"
    t "Oh no!! Your phone died! Why are you so bad at preparing for dates?"
    t "We'll just have to guess which is the right building before the driver passes it."
    jump limominigame

#Trying to make a timed minigame here that is meant to waste the player's time

label limominigame:

    #The if-statement here ensures that the player only gets the tutorial once- and that is when they start the minigame

    if firsttimewithtimer is True:
        "You will have five seconds to determine if the driver is passing the correct building --> clicking will begin the minigame sequence"
        $ firsttimewithtimer = False
    else:
        t "The driver moved on to the next building!"
        pass
    $ timed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame2'
    show screen countdown
    menu:
        "Stop at this red building with gold accents that's... short?":
            hide screen countdown
            $ time = time - 5
            t "Noo, that's wrong!"
            jump limominigame2
        "Next building please!":
            hide screen countdown
            $ time = time - 1
            jump limominigame2
    
label limominigame2:
    t "The driver moved on to the next building!"
    $ timed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame3'
    show screen countdown
    menu:
        "Stop at this red building with gold accents that's... tall?":
            hide screen countdown
            t "Yes! You've found it!"
            jump williamlimo2
        "Next building please!":
            hide screen countdown
            $ time = time - 1
            jump limominigame3

label limominigame3:
    t "The driver moved on to the next building!"
    $ timed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame'
    show screen countdown
    menu:
        "Stop at this blue building with gold accents that's... tall!":
            hide screen countdown
            $ time = time - 5
            t "Noo, that's wrong!"
            jump limominigame
        "Next building please!":
            hide screen countdown
            $ time = time - 1
            t "Guess that means we'll have to circle the block..."
            jump limominigame

label williamlimo2:
    scene fancydiner_outside
    t "You made it!"
    "*Bzzzt bzzzt*"
    t "A text, now?"
    play sound "sounds/William_Neutral.mp3"
    show william_neutral:
        xalign 0.5
        yalign 0.0
    w "'I see a limo has pulled up, one of my limos...'"
    t "One of HIS limos??"
    w "'And the person who got out is looking at their phone-'"
    hide william_neutral
    play sound "sounds/William_Angry1.mp3"
    show william_angry:
        xalign 0.5
        yalign 0.0
    w "'As I'm texting you...'"
    w "'I'm sorry, I don't really see this working out. I don't want to date another superficial person.'"
    t "Wow, the limo was really a terrible idea. Why would you ever even think that would be smart?? Geez..."
    t "Just be yourself..."
    jump start

# LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO LIMO

#This is the actual date with William

label williamdate:
    scene fancydinertable
    play music "sounds/BgMusic.mp3" fadein 2.0
    show bouncer at center:
        xzoom 0.54 yzoom 0.54
    "You walk to the beautiful flower arch, guarded by a fierce bouncer."
    menu:
        "Let me through NOW!!" if williamdemand is False:
            $ williamdemand = True
            "The bouncer slaps you and you snap back into reality"
            t "I think you needed that."
            jump williamdate
        "Uhm, I think Mr. After is expecting someone... me?":
            "The bouncer examines you carefully"
            t "This is making me anxious..."
            "Then, a voice shouts from behind the bouncer..."
            play sound "sounds/William_Shocked2.mp3"
            w "Let them through!"
            hide bouncer with dissolve
            show bouncer at right with dissolve:
                xzoom 0.54 yzoom 0.54
            b "Good luck. Don't dissapoint."
            hide bouncer
            pass
        "I believe Mr. After is expecting me!":
            t "Confidence is key!"
            "The bouncer examines you carefully"
            t "This is making me anxious..."
            "Then, a voice shouts from behind the bouncer..."
            play sound "sounds/William_Shocked2.mp3"
            w "Let them through!"
            hide bouncer with dissolve
            show bouncer at right with dissolve:
                xzoom 0.54 yzoom 0.54
            b "Good luck. Don't dissapoint."
            hide bouncer with dissolve
            pass
    play sound "sounds/William_Happy2.mp3"
    show william_happy with dissolve:
        xalign 0.5
        yalign 0.0
    w "Welcome, welcome! I'm so glad to see you!"
    $ datedwilliamafter = True
    hide william_happy
    t "You've dated William!"
    stop music
    jump start

return