# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("June", color="#E86F23")
define k = Character("Kai", color="#48586F")
define mw = Character("Marlow", color="#A38970")
define mei = Character("Mei", color="#FFD1DC")

define g_agents = Character("Dusanian Agents", color="#ff0000")

# The game starts here.

label start:
    menu: #TODO / Already at final decision for now
        
        "I'll start the transmission. Alone.":
            jump selfish
        "Marlow, you search for food.":
            jump save_kai
        "Kai. Mei can't survive here. They'll find us.": # Saving marlow
            jump save_marlow
        "Marlow, Kai. Please, search <city> for food.":
            jump save_mei
        
    return

label selfish: 
    #TODO # Trying to save only yourself
    j "Why don't you three look for food? We need more to survive here."

    # Thoughts
    j "{i}(I can survive alone.){\i}"
    j "{i}(What good are friends anyways?){\i}"
    j "{i}(Useless trash.){\i}"

    scene bg city # kai, mei, marlow are here

    # Gets jumped by government officers

    # Mei dies, Marlow escapes with Kai and then dips

    # Kai returns to confront June
    # June acts like a douche

    python:
        # Minigame here idk what to do yet
        pass

    # June leaves

    # scene bg ... # Shelter, june returns

    # Gov. comes back, June is cooked

    return

    

label save_kai:
    #TODO
    mw "No. You need protection."
    j "We need food, and you're the strongest."
    j "Kai, Mei and I will get this transmission working."

    # Marlow & Mei go city where discovered by gov. agents (idk this would be better if it was different)

    # Marlow holds them off and dies

    # Mei (injured) returns to the shelter, but its full bc no resources & cannot get more because the  gov. is already at the place where they can scavenge

    # Kai wants to die
    # I wanna make the reader become Kai for a bit, show all the suicidal thoughts  (can put cool effects to symbolise his spiral or wtv)

    # June (potentially) talks him out of it
    menu:
        "Opt 1":
            "death"
        "Opt 2":
            "death"
        "Opt 3": 
            "Lives"
        "Opt 4":
            "death"

    return



label save_marlow:
    #TODO

    # scene bg ...

    show kai serious
    j "Take her and escape to Ommasia. "
    j "It's her only hope."
    show kai serious talk
    k "JUNE. We stay together."
    k "If I escape, you're coming with me."
    hide kai
    show marlow neutral talk at right
    j "Someone needs to transmit the message."(multiple=2)
    mw "I'll protect June."(multiple=2)

    # scene bg ... # This will be the ending scene for this choice
    
    # Denied entry, gov. discovers, Mei kidnapped, Kai manages to pass msg to June

    # Marlow learns of Mei, gets sad
    menu: # Attempt a rescue or not?
        "Opt 1":
            $ rescue_mei = True

        "Opt 2":
            $ rescue_mei = False
    
    if rescue_mei:
        # Marlow dies
        mw "Dead"
    else:
        # Marlow survives but spirals
        mw "What's the point in living?"

    return


label save_mei:
    #TODO
    k "Why"
    # other stuff 
    j "We can't survive without it!"

    # While searching for supplies they stumble into big radiation place

    # Marlow ides — kai realises hes going to die; returns to the shelter
    
    # Kai pleads for them to end it
    
    menu:
        "Opt 1":
            "Mei kills"
            $ mei_innocent = False
        "Opt 2":
            "June kills"
            $ mei_innocent = True

    if not mei_innocent: # Bad stuff happens
        # scene bg shelter
        mei "WHAT HAVE I DONE?" # (I wanna figure out a way to make this like be big on screen i'll do that tmrw)
        # ...
    else:
        # Thoughts
        j "{i}Guilty thoughts {\i}"

    return
    