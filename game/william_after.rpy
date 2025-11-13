#This file follows the route of William After

label william_after:
    "You click on the finely aged man's profile"
    "Bzzzt bzzzt"
    t "Hm? It seems you've recieved a text from somebody."
    t "Oh wow, the gentlemen you've chosen has already responded!"
    w "'Do you want to meet at the Ritz?'"
    menu:
        "Absolutely!":
            pass
        "No thank you...":
            t "Maybe another time William..."
            jump start
    t "The Ritz? Never heard of it either? No matter, Oogle Maps has all the knowledge we need!"
    t "Here we are! It says the Ritz is approximately 15 minutes away if you chose to walk. That is, if there are minimal disruptions."
    t "On the other hand, there is the choice of getting a ride, but it seems the most readily available option is a limo."
    t "You would have a better chance of getting there if you took the limo, but it's more expensive and it doesn't realy seem like... you?"
    t "Unless that's how you want to appear."
    t "What do you think?"
    menu:
        "I'll walk!":
            t "Right! It says more about your character."
            pass
        "Limo it is!":
            t "Are you sure?"
            menu:
                "Pester me no longer! I am sure of my choice!":
                    t "Alright, cool your jets."
                    jump williamlimo
                "Errr, actually on second thought...":
                    t "I think this will work out in the end!"
                    pass
    
    #I think we should add obstacles here in the future, but this is the prototype as of now

    t "You made it! With [time] minutes to spare!"
    t "Wow, this place is... stunning! Maybe the limo would've made for a more appropriate entrance."
    t "Hopefully Sir William reeaaally appreciates your character! Hopefully..."
    t "Now, speaking of Mr. After, where is he?"
    "Bzzzt bzzzt"
    t "I wonder if it's William..."
    w "'If you're wondering where to go, I'm up the stairs! It's impossible to miss.'"
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

#This follows the route of taking the limo
label williamlimo:
    t "Alright 'Mr. High and Mighty', the limo should be here in about 5 minutes."
    $ time - 5
    t "Great, the limo is here! Those 5 minutes went by inexplicably fast!"

    #I wonder if we can add any obstacles to the limo too, even if it doesn't matter in the end

    t "You made it! With lots of time to spare too!"
    "Bzzzt bzzzt"
    t "A text, now?"
    w "'I see a limo has pulled up, one of my limos...'"
    t "One of HIS limos??"
    w "'And the person who got out is looking at their phone-'"
    w "'As I'm texting you...'"
    w "'I'm sorry, I don't really see this working out. I don't want to date another superficial person.'"
    t "Wow, the limo was really a terrible idea. Why would you ever even think that would be smart?? Geez..."
    t "Just be yourself..."
    jump start


#This is the actual date with William
label williamdate:
    "You walk to the bottom of the stairs, guarded by a gorgerous velvet rope and a fierce bouncer."
    menu:
        "Let me through NOW!" if williamdemand is False:
            $ williamdemand = True
            "The bouncer slaps you and you snap back into reality"
            t "I think you needed that."
            jump williamdate
        "Uhm, I think Mr. After is expecting someone... me?":
            "The bouncer examines you carefully"
            t "This is making me anxious..."
            "Then, a voice shouts from atop the stairs..."
            w "Let them through!"
            pass
        "I believe Mr. After is expecting me!":
            t "Confidence is key!"
            "The bouncer examines you carefully"
            t "This is making me anxious..."
            "Then, a voice shouts from atop the stairs..."
            w "Let them through!"
            pass
    w "Welcome, welcome! I'm so glad to see you!"
    $ datedwilliamafter = True
    t "You've dated William!"
    jump start

return