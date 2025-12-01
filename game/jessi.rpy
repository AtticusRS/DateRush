#This route follows the route of Jessi

#add interupptions

label jessi:
    $ time = 20

    scene outsidebar
    t "Smoke lingers in the air outside this shabby bar. Theres some other people walking by, but nothing of note. Distantly you could hear an arguement in a nearby alleyway."
    t "An oddly formal bouncer glances your way before going back to scold the familiar woman."
    show bouncer at left:
        xzoom 0.54 yzoom 0.54
    show jessi_happy at right:
        yalign - 0.3
        yzoom 0.4
        xzoom 0.4
    b "Not again Jessi. I let you in before and you just had to cause prblems."
    j "Whaaat? Nooo I'd neverrrrrrrr!"
    t "By the tone of her voice and her expression, she had must have caused problems before."

    t "The Bouncer looked toward you to speak, just as you see that your date slipped on by into the sketchy bar."
    hide jessi_happy

menu:
    "Talk to the Bouncer":
        t "The...man? Thats..thats a dog.That is absoulutely a dog."
        t "Either way he looks you up and down. Your semi-formal attire speaks volumes."
        b "This place is not for you. The rougher customers here will not take kindly to your presence."
        b "I'm sorry but its best if you leave."
        t "Despite claiming you're with the woman whom he'd just let in, he huffs."
        b "Humph! She is NOT supposed to be here either."
        jump bouncerconvo
    "Walk right past the dog man":
        t "His nose wrinkles up in annoyance as you step closer to the door."
        b "I think not."
        jump bouncertime
    "Skip out on the date":
        t "Just like that? A whiff of danger and you left? Well, I guess not all of us can be brave."
        jump start

#Bouncer waisting more time!
label bouncertime:
    t "The Bouncer blocks your way."
    menu:
        "FIGHT":
            t "Seeing the formal dog blocking you're quest for LOVE, you are filled with DETERMINATION."
            t "You hold yourself confidently, ready your fists and-"
            t "Fail to avoid the Bouncer's fist collide with your head."
            hide bouncer
            scene black
            $ time = time - 10
            t "You're unconcious before you even hit the floor."
            $ blackeye = True
            jump wakeup
        "Flirt":
            t "He stares at you for an awkwardly long period, expression unchanged."
            b "Flattering, but I'm married."
            $ time = time - 3
            b "It's really best you leave now."
            jump bouncerconvo
        "Bribe":
            t "The man shakes his head, frowning."
            b "Moderatly insulting for you to believe a man in this expensive of a suit would need money."
            $ time = time - 3
            b "It's really best you leave now."
            jump bouncerconvo

#knocked out route :D 

label wakeup:
scene crimealley
hide bouncer
t "As you come to, you find yourself in a sketchy alleyway just outside the bar."
t "So much for any kindness, that dog dragged you into a alley. Not just any alley either."
t "CRIME alley."
t "This is why I'm personally a cat person."
menu:
    "Investigate the alley":
        jump gun_wick
    "Shamefully walk back":
        t "Now don't let that black eye stop you on this quest for love"
        jump Eenter

#Talking to the bouncer
label bouncerconvo:
    show bouncer at left
    menu:
        "Think of the edgiest thing you can":
            t "By the face he made, it was hard to tell if him opening the door was out of pity or an attempt for a learning moment."
            t "Regardless of the reason though, you're let in."
            jump intobar
        "Bribe":
            b "You have no damn idea who you're talking to. Gangs treat loyalty as gold-- I ain't giving this shit up."
            t "The large man cracks his knuckles and stares you down. Perhaps its better to leave without a hospital bill this time."
            jump start
        "The password is absolutely Worsheshire.":
            $ time = time - 5
            b "What."
            t "....what?"
            e "HAHA! THATS HILARIOUS."
            t "Who on earth are you?"
            jump distractionE

label Eenter:
    scene streetside
    t "As you near, you see that dog man again."
    t "Theres no way past him, and he sure won't let you in now."
    menu:
        "Give up":
            t "..Well I suppose I can't blame you."
            jump start
        "Think of another way in":
            t "You stand beside the bar, thinking of your"
            e "HELLO?"
            t "..What."
            e "HELLO! You want in there right? Of course you do! See I know a"
            t "Oh great heavens not again. Sorry. This may be new for you, but this nuisance is hardly new to me. Lets just..there."
            jump intobar

label distractionE:
    menu:
        "Ignore that. Focus. Date.":
            t "The stranger that had just rudely interupted us was now annoying the Bouncer. Nows the time- QUIETLY."
            jump intobar
        "Talk to the stranger":
            $ time = time - 5
            t "Now why waste time like this?"
            e "For the secrects man! the LLLLLOOOREEE ya dig?"
            t "...How can you hear me? This is wrong. Sorry, but this can't happen. We're leaving."
            jump intobar

label intobar:
scene bar
show jessi_happy with dissolve:
    yalign - 0.3
    yzoom 0.4
    xzoom 0.4
t "The bar is full of criminals, monsters, gangsters. If a building could be sugar and everything nice, then here was all that spice."
t "You can spot Jessi at the bar just a few steps away."

menu:
    "Go up to Jessi":
        t "As you walk toward your date, doubts fill your mind. Afterall, what about you should she even be impressed with? ..Maybe its best to do this another day."
        jump start
    "Blend in":
        t "Pulling all your previous theater knowledge, you swagger into the bar. Taking a look around before settling in the seat beside your date."
        t "Jessie rolls her eyes at your antics, although a small smile remained on her face."
        jump jessiconvo

label jessiconvo:
scene barsit
show jessi_happy:
        yalign - 0.3
        yzoom 0.4
        xzoom 0.4
t "What now? What way will you woo your date?"
menu:
    "Drinking game.":
        j "A drinking game? You think you can outdo me? Well I won't say no to winning."
        t "She's right. It doesnt take long until you hardly could remember your name. Let alone function on a date."
        t "Maybe it's time to call an Ewber."
        jump start
    "Strike a coversation":
        t "She snickered at the question."
        j "Benefits a leader gets? You really are out of this 'scene'. How about you tell me why you came all the way out here for a date?"
        hide jessi_happy
        show jessi_neutral:
            yalign - 0.3
            yzoom 0.4
            xzoom 0.4
        jump jessicontinue

label jessicontinue:
    menu:
        "Adventure I guess?":
            hide jessi_neutral
            hide jessi_angry
            show jessi_happy:
                yalign - 0.3
                yzoom 0.4
                xzoom 0.4
            j "Well how about I get you to ditch this bar for a real adventure then?"
            jump jessiquestion
        "Are you calling me boring?":
            hide jessi_neutral
            show jessi_angry:
                yalign - 0.3
                yzoom 0.4
                xzoom 0.4
            j "Yes. Exactly actually. How'd you figure that how Sherlock? But sure, let's say you are from here- which you arent- I would know you."
            j "So."
            j "Whats the name?"
            jump jname

label jessiquestion:

    menu:
            "Absolutely.":
                $ datedjessi = True
                jump start
            "I'll pass.":
                j "Suit yourself."
                jump start


label jname:
    menu:
        "William After.":
            hide jessi_angry
            show jessi_shocked:
                yalign - 0.3
                yzoom 0.4
                xzoom 0.4
            t "She cackles at that answer. It takes a moment for her to regain her breath."
            j "DUDE. OUT OF ALL- Oh my GAWD. Out of EVERYONE you name some rich dude! Wow. Alright poser, it's been fun, but I ain't exactly here for money."
            jump start
        "..Yeah... Fine. I'm a normal person on an adventure.":
            jump jessicontinue

return