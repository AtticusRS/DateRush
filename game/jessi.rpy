#This route follows the route of Jessi

label jessi:

    scene outsidebar
    t "Smoke lingers in the air outside this shabby bar. A bouncer glances your way before going back to scold the familliar woman."
    t "Although while he was looking at you, your date slipped on by and into the sketchy bar."
menu:
    "Talk to the Bouncer":
        t "The...man? looks you up and down. Your semi-formal attire speaks volumes."
        b "This place ain't for you. Ain't for folks pretending to be part of this..group."
        b "Beat it unless you got a way in."
        t "Despite claiming your with the women he just let in, he huffs."
        b "She ain't suppose to be here either."
        jump bouncerconvo
    "Skip out on the date":
        t "Just like that? A whiff of danger and you've left? Well..I suppose this is your choice."
        jump start

label bouncerconvo:
    menu:
        "Think of the edgiest thing you can":
            t "By the face he made, it was hard to tell if him opening the door was out of pity or an attempt for a learning moment."
            t "Regardless of the reason though, you're in."
            jump intobar
        "Bribe":
            b "You have no damn idea who you're talking to. Gangs treat loyalty as gold, and I aint giving that up."
            t "The large man cracks his knuckles and stares you down. Perhaps its better to leave without a hospital bill this time."
            jump start
        "The password is absolutely Worsheshire.":
            $ time - 5
            b "What."
            t "....what?"
            e "HAHA! THATS HILARIOUS"
            t "Who on earth are you?"
            jump distractionE

label distractionE:
    menu:
        "Ignore that. Focus. Date.":
            t "The stranger that had just rudely interuppted us was now annoying the Bouncer. Nows the time- QUIETLY."
            jump intobar
        "Talk to the stranger":
            $ time - 5
            t "Now why waste time like this?"
            e "For the secrects man! the LLLLLOOOREEE ya dig?"
            t "...How can you hear me? This is wrong. Sorry, but this can't happen. We're leaving."
            jump intobar

label intobar:
scene bar

t "The bar is full of criminals, monsters, gangsters. If a building could be sugar and everything nice, then here was all that spice."
t "You can spot Jessi at the bar just a few steps away."

menu:
    "Go up to Jessi":
        t "As you head towards your lovely date, a hand grabs your arm and snatches you aside."
        t "Criminals surround you, the odd one out of this bar. They don't seem friendly either."
        j "Hey! Leave that one alone- Their with me."
        t "Words fall of deaf ears, but the ruckus gets anothers attention. The Bouncer barges in and pulls you away."
        t "One less hospital bill at least."
        jump start
    "Blend in":
        t "Pulling all your previous theater knowledge, you swagger into the bar. Taking a look around before settling in the seat beside your date."
        t "Jessie rolls her eyes at your antics, although a small smile remained on her face."
        jump jessiconvo

label jessiconvo:
scene barsit

t "What now? What way will you woo your date?"
menu:
    "Drinking game.":
        j "A drinking game? You think you can outdo me? Well I won't say no to winning."
        t "Shes right. It doesnt take long until you hardly could remember your name. Let alone function on a date."
        t "Maybe it's time to call an Ewber."
        jump start
    "Strike a coversation":
        t "She snickered at the question."
        j "Benefits a leader gets? You really are out of this 'scene'. How about you tell me why you came all the way out here for a date?"
        jump jessicontinue

label jessicontinue:
    menu:
        "Adventure I guess?":
            j "Well how about I get you to ditch this bar for a real adventure then?"
            jump jessiquestion
        "Are you calling me boring?":
            j "Yes. Exactly actually. How'd you figure that how Sherlock? But sure, lets say you are from here- which you arent- I would know you."
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
            t "She cackles at that answer. It takes a moment for her to regain her breath."
            j "DUDE. OF ALL- Oh my god. Out of EVERYONE you name some rich dude. Wow. Alright poser, its been fun but I aint exactly here for money"
            jump start
        "..Yea..Fine. I'm a normal person on an adventure.":
            jump jessicontinue

return