#This file follows the route of William After

label william_after:
    "You click on the finely aged man's profile"
    "*Bzzzt bzzzt*"
    t "Hm? It seems you've recieved a text from somebody."
    t "Oh wow, the gentlemen you've chosen has already responded!"
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
    t "Alright!! You have... only [time] minutes to get there..."

    #The timer shows up here now that the player knows how much time they have
    show screen time_meter

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
                t "Right! It says more about your character."
                jump on_foot
            "Limo it is!":
                t "Are you sure?"
                menu:
                    "Pester me no longer! I am sure of my choice!":
                        t "Alright, cool your jets."
                        jump williamlimo
                    "Errr, actually on second thought...":
                        t "I think this will work out in the end!"
                        pass
            "Think about it" if thinkingalot == False:
                $ time = time - 2
                t "Riiight, I see. Hm, I guess I can see that something like this would require lots of consideration."
                t "Don't forget how much time you have though..."
                jump brain_cramp

    # Choosing how to get to William, but on foot

    label on_foot:
        t "So you're walking, do you have 15 minutes to spare by walking?"
        t "Or do you want to do anything other than walking?"
        menu:
            "I'm juuust gonna walk...":
                t "Okay! Solid! Works, it works for sure."
                t "Are you sure?"
                menu:
                    "Yes, let me walk":
                        t "Okayy fine. Only because you said so."
                        jump walking_along
                    "Noo, maybe not":
                        t "Cool! Don't forget, the choice is yours!"
                        jump on_foot
            "I wanna skip my way there!":
                $ skippedto_william = True
                t "Alright! I like that enthusiasm!"
                t "Could save you some time too."
                jump skipping_along

    label walking_along:
        "Walking walking walking"
        jump predate_william
    
    label skipping_along:
        "Skipping skipping skipping"
        jump predate_william

    
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
                t "Omg, are you dying?!"
                "Your brain feels like it's about to explode... btw"
                t "I don't even- just like- uhhhh"
                t "I think you need to lay down for sometime..."
                t "Like... maybe 8 minutes..."
                $ time = time - 8
                "You lay down for a while..."
                t "Welcome back! Let's not... think... too much again?"
                jump choosing_for_william
            "I'm done with this bit.":
                $ time = time - 1
                t "Just so you know, it was NOT funny."
                t "NOooobody is laughing."
                jump choosing_for_william

#This is like a precursor stage to dating William

label predate_william:
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
    show william_happy with dissolve:
        xalign 0.5
        yalign 0.0
    w "'If you're wondering where to go, I'm up the stairs! It's impossible to miss.'"
    hide william_happy
    t "Alright! Up the stairs, into the... V.I.P. lounge?! If only we could go back in time..."
    t "The rest is up to you. I mean, though, you're already here..."
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
    "The limo driver begins driving as soon as you are seated"
    t "Awesome, this limo driver knows what's up!"
    t "Wait, you never told the driver what the building looks like!!"
    t "Look at your phone, we'll have to remember what it looks like and tell the driver when to stop!!"
    "You look at your phone, the Ritz is a tall, red building with gold accents and-"
    t "Oh no!! Your phone died! Why are you so bad at preparing for dates?"
    t "We'll just have to guess which is the right building before the driver passes it."
    jump limominigame

#Trying to make a timed minigame here that is meant to waste the player's time

screen william_timer:
    timer 0.01 repeat True action If(williamtimed > 0, true=SetVariable('williamtimed', williamtimed - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #^This is a timer I peeled directly off of a video
    #It's supposed to send the player to the next description of a building when the timer runs out


label limominigame:

    #The if-statement here ensures that the player only gets the tutorial once- and that is when they start the minigame

    $ time = time - 1
    if firsttimewithtimer is True:
        "You will have five seconds to determine if the driver is passing the correct building- clicking will begin the minigame sequence"
        $ firsttimewithtimer = False
    else:
        t "The driver moved on to the next building!"
        pass
    $ williamtimed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame2'
    menu:
        "Stop at this red building with gold accents that's... short?":
            $ time - 5
            t "Noo, that's wrong!"
            jump limominigame2
        "Next building please!":
            $ time - 1
            jump limominigame2
    
label limominigame2:
    t "The driver moved on to the next building!"
    $ time = time - 1
    $ williamtimed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame3'
    menu:
        "Stop at this red building with gold accents that's... tall?":
            t "Yes! You've found it!"
            jump williamlimo2
        "Next building please!":
            $ time - 1
            jump limominigame3

label limominigame3:
    t "The driver moved on to the next building!"
    $ time = time - 1
    $ williamtimed = 5
    $ timer_range = 5
    $ timer_jump = 'limominigame'
    menu:
        "Stop at this blue building with gold accents that's... tall!":
            $ time = time - 5
            t "Noo, that's wrong!"
            jump limominigame
        "Next building please!":
            $ time = time - 1
            t "Guess that means we'll have to circle the block..."
            jump limominigame

label williamlimo2:
    t "You made it!"
    "*Bzzzt bzzzt*"
    t "A text, now?"
    show william_neutral:
        xalign 0.5
        yalign 0.0
    w "'I see a limo has pulled up, one of my limos...'"
    t "One of HIS limos??"
    w "'And the person who got out is looking at their phone-'"
    hide william_neutral
    show william_angry with dissolve:
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
    show bouncer at center:
        xzoom 0.54 yzoom 0.54
    "You walk to the bottom of the stairs, guarded by a gorgerous velvet rope and a fierce bouncer."
    menu:
        "Let me through NOW!!" if williamdemand is False:
            $ williamdemand = True
            "The bouncer slaps you and you snap back into reality"
            t "I think you needed that."
            jump williamdate
        "Uhm, I think Mr. After is expecting someone... me?":
            "The bouncer examines you carefully"
            t "This is making me anxious..."
            "Then, a voice shouts from atop the stairs..."
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
            "Then, a voice shouts from atop the stairs..."
            w "Let them through!"
            hide bouncer with dissolve
            show bouncer at right with dissolve:
                xzoom 0.54 yzoom 0.54
            b "Good luck. Don't dissapoint."
            hide bouncer
            pass
    show william_happy with dissolve:
        xalign 0.5
        yalign 0.0
    w "Welcome, welcome! I'm so glad to see you!"
    $ datedwilliamafter = True
    hide william_happy
    t "You've dated William!"
    jump start

return