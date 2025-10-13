# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random as rand
    import time
    
    
    def click_game(timer, num_clicks):
        if timer >= 0:
            if num_clicks >= 10:
                return bool(rand.randint(0, 1))


define j = Character("June", color="#E86F23", image="june")
define k = Character("Kai", color="#48586F")
define mw = Character("Marlow", color="#A38970")
define mei = Character("Mei", color="#FFD1DC")

define config.mouse = { }
define config.mouse["button"] = [ ("gui/pointer.svg", 0, 0 )]
define config.mouse["default"] = [ ("gui/default@0.5.svg", 0, 0) ]


image bg shack = "bg shack.jpg"
image bg shack gray = im.Grayscale("bg shack.jpg")
image gray kai neutral = im.Grayscale("kai neutral@2.25.png")

define g_agents = Character("Dusanian Agents", color="#ff0000")
define omm = Character("Ommasion Border Control", color="#ff0000")


# The game starts here.     
label DoSearchComplete:
    "You find a hidden trapdoor under the rug..."
    return

# Minigames
screen search_game():
    text "Look for supplies! (Click things)":
        at top
        at transform:
            alpha 0.0
            linear 0.5 alpha 0.8

    button:
        xpos 660
        ypos 775
        xsize 600
        ysize 100
        action Call("DoSearchComplete")

screen clicker_game():
    default timer = 3
    default num_clicks = 0
    frame:
        xalign 1.0
        text "Click!" size 100:
            at top, right
            at transform:
                alpha 1.0
                linear 0.5 alpha 0.8


    button:
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        action [SetLocalVariable("num_clicks", num_clicks + 1), SetLocalVariable("timer", timer - 0.2), Function(click_game, timer=timer, num_clicks=num_clicks)]
    

label start:
    scene bg shack
    j "{i}(It's over… We're finally safe.){/i}"

    "The house — a shack, more like — is empty."
    "It looks like it has been long abandoned, old and decrepit and buried deep into the forest."
    "Likely one of the few remaining pre-war structures, It probably only survived because of its distance from the blast."
    
    show kai neutral talk
    k "Jeez, this place has seen better days. I don't think we're gonna get much outta this…."
    show kai neutral

    j "Well, it's worth a shot anyway. We should get searching."

    hide kai neutral
    call screen search_game
    

    show mei neutral talk
    mei "Hey, Juneeee, look at th—"
    hide mei neutral talk

    show marlow neutral
    "Marlow uncharacteristically cuts off Mei, much to her dismay - pouting as he makes a “shush” gesture with his finger."
    
    show marlow neutral talk
    mw "There's something out there."
    hide marlow neutral talk
    
    show kai serious talk
    k "...what?"

    "It was unmistakable. Distant chatter with no levity in their voice and footsteps of purpose."
    "We duck down by a window and peer over the wood through the glass in bated breath."
    "They had found us."

    k "…Shit. How the hell did they find us out here?"
    show kai serious

    j "Shh- We gotta hide."

    hide kai serious
    show mei neutral talk
    mei "Where?! There's nowhere to hide!"

    j "{i}(…Mai's right. This building has nothing. Except…){/i}"
    j "{i}(…! That hidden room…){/i}"

    "I meet eyes with the group."

    j "{i}(But it can only fit two people.){/i}"

    hide mei neutral talk

    menu:
        "Tell them about it":
            pass # Just proceed to who we save
        
        "Hide it from them. I'm the only one who needs to survive.":
            jump selfish

    menu: #TODO / Already at final decision for now
        "Marlow, you search for food.":
            jump save_kai
        # "Kai. Mei can't survive here. They'll find us.": # Saving marlow
        #     jump save_marlow
        # "Marlow, Kai. Please, search <city> for food.":
        #     jump save_mei
        
    return

label selfish: 
    # Trying to save only yourself
    j "Why don't you three look for food? We need more to survive."
    j "I'll start the transmission. Alone."

    # Thoughts
    j "{i}(I can survive alone.){/i}"
    j "{i}(What good are friends anyways?){/i}"
    j "{i}(Useless trash.){/i}"

    scene bg city # kai, mei, marlow are here

    show kai neutral at left
    show mei neutral at right
    show marlow neutral at center

    g_agents "There!"
    g_agents "Get them!"

    k "MEI!"

    mw "KAI! We need to go! There's no helping her now. She's gone."

    scene bg shack # Escaped

    show kai serious at left
    show marlow sad at right

    hide marlow sad    
    show marlow sad talk at right
    mw "I can't do this anymore."
    mw "The endless running, hiding, the constant fear."
    mw "I'm going back to avenge her."

    hide marlow sad talk
    hide kai serious
    
    show kai serious talk at left
    show marlow sad at right
    k "You can't!"
    k "She wouldn't want it!"

    hide kai serious talk
    show kai serious at left

    hide marlow sad
    show marlow sad talk at right
    mw "They're still on our trail. It won't ever end."
    mw " June... Did he know this would happen?"
    mw "I'm going alone, Kai. Don't follow me."
    mw "Go back and survive with June."

    hide marlow sad talk
    hide kai serious
    show kai serious talk at left
    k "No..."
    k "It all makes sense now."

    scene bg shack
    show kai abt to beat up june
    
    # Kai stuff
    k "You're a fucking bastard, you know that?"
    
    j "What? What are you talking about?"
    
    # Kai returns to confront June
    # June acts like a douche

    scene kai abt to beat up june
    with hpunch
    
    k "Don't you dare play dumb."
    k "This is all your fault. They're all dead because of you."
    k "You left us behind."

    j "K-Kai! Calm down, what the hell are you talking about? I didn't do anything!"

    k "You left us. You could've saved us."
    k "You lied."

    scene kai abt to beat up june
    with hpunch
    
    k "I thought we were friends! How could you do this to us?"
    k "To all of us?"
    k "To me?"
    k "You left us all to die, you left me behind."
    k "You need me."

    j  "I was doing what's right! I have to live!"
    j "I have to save everyone!"

    k "How do you expect to save anyone when you can't even save me?"
    k "You could've helped us, any of us!"
    k "But you didn't say a thing."
    k "You're going to die just like the rest of us."


    default win = False
    $ win = renpy.call_screen("clicker_game")   
    pause 1.0 # Otherwise theyd just click off
    if win:
        scene black
        with hpunch

        scene fight cg

        j "I've helped you your entire life."
        j "How dare you?"

        k "You monster!"
        k "I thought we were friends, I didn't expect you to leave me - leave us behind."
        k "I can't stand you."

        g_agents "Come out with your hands raised!"

        j "Yo- you!"
        j "{i}(It's over, isn't it?){/i}"
        j "{i}(I can't take them all.){/i}"

        scene black

        "I've failed."
        "(You died.)"

        return

    else:
        scene black
        with hpunch
        j "...!"
        
        # scene death cg

        j "Ka-Kai. Why?"

        k "It's all your fault."

        j "{i}Is it over?{/i}"
        
        scene black

        "I've failed."
        "(You died.)"

        return
    

label save_kai:
    mw "No. You need protection."
    j "We need food, and you're the strongest."
    j "Kai, Mei and I will get this transmission working."

    # Marlow & Mei go city where discovered by gov. agents (idk this would be better if it was different)
    scene bg city #  mei, marlow are here

    show mei neutral at left
    show marlow neutral at right

    g_agents "There!"
    g_agents "Get them!"

    hide marlow neutral
    show marlow neutral talk at right
    mw "MEI!"
    mw "Run! I'll stop them here. Get back to June!"
    
    hide marlow neutral talk
    show marlow neutral at right

    hide mei neutral
    show mei worry talk at left
    mei "B-but... No! I can't leave you here!"
    hide mei worry talk
    show mei worry at left

    hide marlow neutral
    show marlow neutral talk 

    mw "Go!"

    scene kai staring body
    k "{i}(Finally... He's gone!){/i}"
    k "{i}(She's all mine now.){/i}"
    k "{i}(All mine...){/i}"

    scene bg shack
    show mei neutral talk at left
    show kai serious at right
    mei "K-kai!"
    mei "Marlow, he's dead!"
    mei "I can't do this anymore..."
    
    hide mei neutral talk 
    show mei neutral at left
    show kai serious talk at right 
    k "{i}(Marlow... Even in death, he's useless){/i}"
    k "{i}(He couldn't even protect her. She has burns everywhere...){/i}"
    k "Mei. What happened?"

    j "Mei!"
    j "Kai. You know we can't save her."

    # Mei collapses, maybe death scene?

    k "NO!"
    
    scene bg shack gray
    show gray kai neutral 
    k "{i}(I can't live like this...){/i}"
    k "{i}(Why should I even live without her?){/i}"
    k "{i}(It's over.){/i}"

    scene black

    "I've failed."
    "(You died.)"

    return



label save_marlow:
    #TODO

    scene bg shack

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
    scene bg city
    
    

    # Denied entry, gov. discovers, Mei kidnapped, Kai manages to pass msg to June


    # Marlow learns of Mei, gets sad
    menu: # Attempt a rescue or not?
        "We can't just leave her, Marlow. ":
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
        scene bg shack
        mei "WHAT HAVE I DONE?" # (I wanna figure out a way to make this like be big on screen i'll do that tmrw)
        # ...
    else:
        # Thoughts
        j "{i}Guilty thoughts {/i}"

    return
    