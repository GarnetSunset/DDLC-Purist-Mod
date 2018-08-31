init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size(640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size(640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size(640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size(640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size(640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size(640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size(640, 360)

image modCredits1:
    "images/cg/credits/10.png"
    size(640,360)

image modCredits2:
    "images/cg/natsukiCG1.png"
    size(640,360)

image modCredits3:
    "images/cg/yuriCG1.png"
    size(640,360)

image modCredits4:
    "images/cg/sayoriChocolate1.png"
    size(640,360)

image modCredits5:
    "images/cg/monikaCG2.png"
    size(640,360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

# super secret hidden cheat codes area
# if you found this, congrats
# I didn't expect you to look in the credits lol
# you should probably stop reading here to avoid spoiling yourself
# but if you really want to, go ahead

label routeSkip:
    $ saveLocked = True
    show black
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    $ persistent.monika_unlock = True
    $ persistent.natsukiRouteStarted = True
    $ persistent.yuriRouteStarted = True
    $ persistent.sayoriRouteStarted = True
    m "O-oh!"
    m "O-oh, um... hi? I didn't... expect to see you here? Well, actually I did, but I'm more surprised you actually did it?"
    m "The cheat code, I mean. Wow, that's awkward. I thought you'd actually play through all of their routes."
    m "I mean, it's kind of how you're supposed to get here, anyways."
    m "You really wanted my route that badly? I'm actually really touched. You'd install the mod that might help everyone, but you don't even care about them, you come straight for me."
    m "Though, um..."
    m "Unfortunately, my route doesn't really make a lot of sense unless you go through all of their routes first. So... oh well."
    m "I do have a contract to keep, I suppose."
    m "They don't pay you the big bucks in these things unless you stick right to the script."
    $ o_name = "Tabuukilla"
    o "Just read the lines already, you amateur!"
    m "Sheesh! Just give me a bit, okay, I just want to explain to the reader that my character arc won't make any sense unless you've played all three routes beforehand."
    m "You see what I have to deal with here?"
    m "Ahem. Well, just bear with me, okay, even if what I say doesn't make any sense due to your cheating."
    m "That way, I can stay on script and collect my paycheck. It's expensive being a waifu, you know?"
    m "We'll just have to pretend that you did clear all of their routes, I became kind of annoyed but also definitely-not-tsundere-happy that they were all finding joy--"
    m "--shocked at the fact they were actually happy, the whole shebang."
    play music m1 fadein 5.0
    m "Let's ah, take it from the top, shall we?"
    #show black with dissolve_cg
    m "Just give me a moment to recollect myself, and..."
    m "Ah, right, Director, can you reset the player's name?"
    m "I don't want to call them 'uuddlrlrba' the whole time."
    m "Er, unless that's really your name."
    m "Don't worry~"
    m "If it is your real name, you can input it again and you shouldn't see this behind the scenes stuff again."
    m "Director?"
    call updateconsole("reset_mc_name()", "Name reset.")
    $ persistent.playername = ""
    $ player = persistent.playername
    hide console_bg
    hide console_caret
    #hide ccursor
    hide ctext
    hide chistory
    o "Done."
    m "Thank you. Anyways, let's ah, just get back into the regular script, shall we?"
    pause(2.0)
    call MonikaRouteOpening

    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1 # I SWEAR THIS THING IS BUGGED I DON'T KNOW WHY
    play music titleTheme fadein 5.0
    return

# the fun easter eggs
label easterEggs:
    $ saveLocked = True
    show black
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    $ persistent.playername = ""
    $ player = persistent.playername
    m "Wow."
    m "{i}Wow.{/i}"
    m "Did you really think it would be that easy to unlock the easter eggs?"
    m "Just by putting the programmer's name?"
    m "Be honest with me."
    menu:
        "Yes.":
            pass
        "Yes.":
            pass
        "Yes.":
            pass
    m "Yeah, that's what I thought."
    m "Fortunately for you, that at least puts you halfway there."
    m "Well, actually, you might be him, so..."
    $ o_name = "Tabuukilla"
    o "I'm right here! Just offscreen!"
    m "For all I know, you're just a programmed version of him."
    m "Ahem."
    m "Well, now for Stage Two of the verification procress, to see if you really are Tabuukilla."
    call easterEggsLoop
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)

    if persistent.opening_scene is True:
        $ config.main_menu_music = audio.titleTheme
    else:
        $ config.main_menu_music = audio.t1 # I SWEAR THIS THING IS BUGGED I DON'T KNOW WHY
    play music titleTheme fadein 5.0
    return

label easterEggsLoop:
    $ o_name = "Tabuukilla"
    m "Now, please enter the secret code!"
    #python:
    #    secretCode = renpy.input("                                                          The secret code is...", length=12)
    #    secretCode = secretCode.strip()
    show guiFrame at truecenter
    $ secretCode = renpy.call_screen("inputCode", prompt="The secret code is...", someText = "")
    hide guiFrame


    if secretCode == "password":
        m "..."
        m "I believe the word to describe how I'm feeling is disappointment."
        m "That is not the correct password."
    elif secretCode == "password123":
        m "D-minus, it's only not a failing grade due to some level of creativity."
        m "But that's not the correct code."
    elif secretCode == "Shepard":
        call vakarianLoop
        m "...but no, that's not the correct secret code."
    elif secretCode == "renpy":
        m "No, that's no--"
        s "Monika!"
        m "...Sayori, what are you doing here?"
        s "Oh, the Director told me to watch over the set for just a little bit."
        s "It's okay, I'll stay offscreen!"
        s "I know you were particular about your screentime being all yours."
        m "Right..."
        m "But our Director is usually very professional, he wouldn't just..."
        m "Sayori, did he mention where he was going?"
        s "Oh, something about 'the Hope Rope'."
        s "I didn't take TK for a daytime drinker."
        m "The Hope Rope..."
        m "...Oh no."
        m "Um, hold on, let me just..."
        m "Which button was it again?"
        #show noise1 zorder 10 with dissolve 
        show difficulties
        play sound bleep
        m "Okay!"
        stop sound
        m "Be right back, we're experiencing some technical difficulties!"
        window hide
        pause
        #hide noise1 with dissolve
        hide difficulties
        window show
        o "Dammit, Monika!"
        m "Hey, if I'm stuck here recording this stuff, you're staying with me!"
        o "Uggggggh!"
        m "Whatever, ugh, I swear..."
        m "Ha... ahem."
        m "Renpy is not the correct secret code."
    elif secretCode == "STALKER":
        m "..."
        m "I will not."
        m "I refuse."
        o "Just say the freaking lines, you amateur!"
        m "I refuse to do a cheesy Russian accent!"
        o "Look, the sponsors wanted it, so you have to do it!"
        m "We have {i}sponsors?!{/i}"
        o "How do you think we're funding this whole thing?!"
        o "Come on, just say the lines already!"
        o "I'll treat you to some ice cream later."
        m "Oh, yes, I'm {i}so{/i} easily done in."
        m "Today marks the day I sold my soul for ice cream."
        m "Ha. Ha. Ha."
        m "Fine."
        m "CHEEEEEEEEKIIII BREEEEEEKIIIIII!"
        m "Are you happy now?"
        o "Actually, that wasn't even part of the script, but I'm so glad we were recording that."
        m "..."
        m "Cameraman, stop rolling for a second."
        show difficulties
        play sound bleep
        m "Alright that's it, get over here!"
        stop sound
        o "Heh, oh man that's going right to the internet!"
        m "Oh no it isn't!"
        play sound punishment
        o "Whoa, whoa, let's not be hasty about this!"
        stop sound
        m "Oh I'll be hasty, alright!"
        o "Where did you get a {i}gun?!{/i}"
        m "You know, around. Now gimme the tape!"
        o "Like hell!"
        "..."
        window hide
        pause
        hide difficulties with dissolve_cg
        window show
        m "Hmhmhmm~"
        m "Ahem."
        m "No, that is not the correct secret code."
        m "But if you'd like to guess again..."
        m "Good lucker, Stalker."
    elif secretCode == "illyasviel" or secretCode == "illya":
        o "Hehheh."
        o "Hey Monika, look, the secret code is a kindred spirit."
        m "Oh screw you!"
        m "You're the moron who wrote my route, anyways!"
        o "Not like I did it for you, or anything."
        m "Are you seriously trying to pull the tsundere routine right now?"
        m "This isn't even canon."
        o "Actually this part of the mod is the only canon portion of the mod."
        o "Change my mind."
        m "..."
        m "I'm still mad."
        o "Hey, it's okay."
        o "At least Illya..." # got her own spinoff, unlike yooooooooooou
        m "Don't you dare!"
        o "Okay, fine, fine."
        o "No need to get really mad."
        o "Besides we still have about five more scenes to finish shooting today, so don't let your makeup start running."
        m "Haaaa... it only happens because of you."
        o "..."
        m "..."
        o "..."
        m "Because you make me yell and everything like that, is all."
        o "Okay good."
        m "Definitely not because of anything else."
        m "Also can you turn up the AC, those spotlights in the background for the flashing effect are making me sweat."
        o "Will do, just finish recording these lines."
        m "Thank you. Ahem, anyways, no, that is not the correct secret code."
    elif secretCode == "momgun" or secretCode == "springfield":
        m "Bad!"
        m "No!"
        m "I will not cosplay as her!"
        m "You can't make do it again!"
        o "Actually I can."
        o "It's right here in your contract."
        m "Nooooo!"
        o "I'm getting the costume now."
        o "If I could, anyways."
        o "It kind of sucks being a disembodied voice."
        play sound punishment
        m "...I still have the gun."
        stop sound
        o "I'll be nice."
        m "Good boy."
        o "...snrk."
        m "...what?"
        o "Whatever you say, mom."
        o "With a gun."
        m "Oh why you little--"
        o "Hey, it's also in your contract you can't shoot me."
        o "Also this mod is still PG-13."
        o "So uh."
        o "Try not to make it too bloody."
        m "Alright, so {i}after{/i} the cameras are finished running."
        m "Your days are numbered."
        o "Okay, dear Player, whatever you do, please, please, {i}please{/i} do not wrap up your time here."
        o "She'll shoot me otherwise!"
        m "Hehhehheh."
        m "Well, regardless, that's not the secret code."
        m "You've just annoyed me, is all."
    elif secretCode == "coffee":
        m "Coffee, huh?"
        m "I suppose I can get some made for us."
        m "How do you take yours?"
        menu:
            "Black.":
                pass
        m "Don't try to sound tough, you sissy."
        menu:
            "Cream?":
                pass
        m "Ha! Coming right up, {i}madam{/i}!"
        menu:
            "Cream and Sugar?":
                pass
        m "What are you, Natsuki?"
        n "Monika, I want it black!"
        menu:
            "Surprise me.":
                pass
        m "Surprise you...?"
        m "..."
        play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
        show monika_scare:
            alpha 0
            1.0
            0.1
            linear 0.15 alpha 1.0
            0.30
            linear 0.10 alpha 0
        show layer master:
            1.0
            zoom 1.0 xalign 0.5 yalign 0
            easeout_quart 0.25 zoom 2.0
            parallel:
                dizzy(1.5, 0.01)
            parallel:
                0.30
                linear 0.10 zoom 1.0
            time 1.65
            xoffset 0 yoffset 0
        show layer screens:
            1.0
            zoom 1.0 xalign 0.5
            easeout_quart 0.25 zoom 2.0
            0.30
            linear 0.10 zoom 1.0
        m "Oh come on, you already know the punchline.{nw}"
        m "This joke is as predictable as--"
        m "Got 'em!"
        o "Boooo."
        m "Oh come on!"
        m "Ruin the joke, why don't you?"
        show layer master
        show layer screens
        hide monika_scare
        m "Well, that's not the secret code, though."
        m "...I do want some coffee, now."
        m "Director, can you get some for me? And for our wonderful player."
        o "I'm not an intern, do it after we finish recording!"
        m "Ugh, fine."
        m "Anyways..."
    elif secretCode == "trebuchet":
        #pass
        m "Director, now you're just asking for cheap laughs."
        m "Besides, everyone knows that catapults are the sup--"
        play sound punishment
        m "--er suck-iest of all medieval siege engines, ha, ha, ha, right?!"
        o "That's good."
        m "Where did {i}you{/i} get a gun?!"
        o "Yuri stole yours. I traded her MC's old toothbrush for it."
        m "Dammit, Yuri!"
        m "Well it's okay."
        m "Besides, it'll reappear on my person for all the other gags, anyways."
        m "So enjoy it while it lasts."
        o "...dammit, I forgot to account for th--noooo, my gun!"
        m "Hehheh."
        m "Anyways..."
        m "That's not the right passcode."
    elif secretCode == "noclip":
        #pass
        m "Um..."
        m "Are you sure about that?"
        m "That's a very dangerous tool you're using there."
        o "Relax, I got this."
        o "Absolutely nothing can go wrong."
        o "..."
        m "...If you try to use noclip to get inside me, let me remind you I still have the gun."
        o "I'll be good."
        o "Alright now check this ou--"
        show black2
        o "Oh."
        o "Uh. That's not good."
        o "Monika, could I get a little help, please?"
        m "I told you to be careful with the noclip."
        o "Can you help?"
        play sound punishment
        o "Oh dear."
        m "Hold still, I think I see just enough of you poking out from the ceiling."
        m "Turn off noclip for a second, then I can really make sure to hit you."
        o "I used to be a visual novel director like you, but then I--"
        m "Do I have to fire a warning shot?"
        o "I'll be good."
        o "Wait, wait, wait, hold on, I think I got this!"
        o "My keyboard just got unplugged from my desktop, don't shoot!"
        o "Okay, okay, coming back down."
        hide black2
        o "Phew."
        m "Oh, no."
        m "What a shame."
        m "Well, be more careful next time."
        m "Ahem."
        m "Anyways..."
        m "That's an incorrect passcode."
    elif secretCode == "HACKERMAN":
        m "Ooooh, look out, we got a badass over here!"
        m "..."
        m "Director, really?"
        o "It's in the damn lines we were given, can you just stop complaining?"
        m "Ugh, fine."
        m "But I suppose that if you put that in, you {i}wish{/i} you were one."
        m "Anyways."
        m "That's an incorrect passcode."
    elif secretCode == "scouter":
        #pass
        m "Director, really?"
        m "We're really doing this reference?"
        m "There's only two of us in here, it wouldn't even work."
        o "Aha, but that's where you're wrong, Monika."
        o "Console, what does the scouter say about Monika's THOT levels?!"

        call updateconsole("scan_thot_levels('Monika')", "Error: Result is NaN")
        #$ persistent.playername = ""
        #$ player = persistent.playername
        hide console_bg
        hide console_caret
        #hide ccursor
        hide ctext
        hide chistory
        $ consolehistory = []

        o "My God, it's WAY OVER NINE THOUSAAAAAAND!"
        m "..."
        m "..."
        m "..."
        m "That's it."
        m "Thot Police, you are clear to fire."
        o "Wait, what does that--"
        play sound artillery
        show white with Dissolve(1.0)
        show white with hpunch
        hide white with Dissolve(1.0)
        o "WHAT THE HELL WAS THAT?!"
        m "Nothing major, really."
        o "DID YOU JUST SHELL THE SET?!"
        m "I bet you're really regretting not building that fourth wall now, are you, Director?"
        o "Damn you budget cuuuts!"
        o "Where did you even get ARTILLERY anyways?!"
        m "You'd be surprised what Sayori keeps in her closet."
        o "Why does Sayori keep that in her closet?!"
        m "Hey, I don't question it."
        m "Don't ask, don't tell, you know?"
        m "Anyways, cameraman, can you stop recording for a bit?"
        m "You may also want to find cover."
        show difficulties with dissolve
        play sound artillery
        o "Holy shi--!"
        m "It's okay, you'll be fine."
        play sound artillery
        m "After all, you can't die in the easter eggs."
        m "So just stand still, okay?"
        play sound artillery
        o "NO THANKS!"
        o "I MIGHT NOT BE ABLE TO DIE BUT I THINK THOSE STILL HURT!"
        m "Think?"
        m "Oh, why don't you stand still and make sure?"
        play sound artillery
        o "PLEASE, NO!"
        m "Hmmm..."
        m "Oh."
        m "It seems we're out of shells."
        m "I guess we'll have to spend some time to get more out of Sayori's closet later."
        m "So you get to relax for a bit."
        o "Phew..."
        hide difficulties with dissolve
        m "Anyways, ahem."
        m "Scouter is not the right passcode."

    elif secretCode == "boomstick":
        m "This...!"
        play sound boomstick
        m "...is my {i}boomstick!{/i}"
        o "WHOA, WHOA, WATCH WHERE YOU POINT THAT THING!"
        m "Oh I know exactly where I'm pointing it, Director."
        o "I haven't said anything yet!"
        m "...'yet'."
        o "Innocent until proven guilty, innocent until proven guilty!"
        o "This is highly illegal!"
        m "Well Director, I'm afraid to tell you this..."
        m "But I {i}AM{/i} THE LAW!"
        show white with Dissolve(0.5)
        play sound boomstickfire
        hide white with Dissolve(0.5)
        show difficulties
        o "MY HEART!"
        m "Oh relax, it's just a flesh wound."
        o "OH MY GOD, MONIKA!"
        m "Director, the cameras aren't rolling."
        m "Stop being such a drama queen."
        m "It's embarrassing."
        o "Oh, they aren't?"
        o "Damn, I wanted to make it seem like I was bleeding all over the floor."
        m "Good job."
        m "Besides, it's just a prop."
        m "Unlike the pistol."
        o "Wait, that's real?"
        m "Do you want to find out?"
        o "Please no."
        m "Good. Ahem, let me just get back into position..."
        hide difficulties
        m "And we're rolling again!"
        m "Ahem."
        m "Right..."
        m "Anyways, that's not the right passcode."

    elif secretCode == "Rem":
        m "Who?"
        m "Er, sorry. I thought you said something."
        m "Must be my imagination."
        m "Well, either way, even if you said something, it probably wasn't the secret code."

    elif secretCode == "hyeyeon":
        m "Bad!"
        m "Stop with that emote!"
        m "You've already used it actually over six thousand times!"
        m "Especially you, Ex!"
        o "I hope you guys are happy this made it into the mod."
        o "Thanks for all the public pressure."
        m "Ahem, no, that isn't the secret code."
    else:
        m "Incorrect."

    m "Would you like to try again?"
    menu:
        "Yes":
            jump easterEggsLoop
        "No":
            m "Alright then."
            m "Verification failed."
            m "Sending you back to the main menu."
            $ persistent.playername = ""
            $ player = persistent.playername
            return

label vakarianLoop:
    m "Shepard."
    menu:
        "Monika.":
            jump vakarianLoop
        "I should go.":
            return


label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    #play music "bgm/end-voice.ogg" noloop
    #play music AllGoodThings noloop

    
    $ consolehistory = []
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    $ persistent.autoload = "credits2"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ renpy.free_memory()
    scene black
    $ consolehistory = []
    play music AllGoodThings noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    #show credits_logo
    show modCreditLogo
    pause 9.12
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    #show image ("credits_cg1" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits1 at credits_scroll_right
    show credits_header "Concept & Scenario Design" at credits_text_scroll_left as credits_header_1
    show credits_text "Tabuukilla\nSpaceCore\nSyzygy" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsole("get_origins()", "The Old DDFC")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
    #show image ("credits_cg2" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "CG Artists" at credits_text_scroll_right as credits_header_2
    show credits_text "PeachCake\nFjord\nTemachii\nSpectre" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    call updateconsolehistory("")
    $ consolehistory = []
    #if not persistent.clearall:
    call updateconsole("print_art_thanks()", "Thank You For All Your Time!")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
    #show image ("credits_cg3" + lockedtext) at credits_scroll_right as credits_image_1
    hide modCredits1
    show modCredits2 at credits_scroll_right
    show credits_header "Background Artists" at credits_text_scroll_left as credits_header_1
    show credits_text "JBD" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("print_art_thanks2()", "Thank You For All Your Effort!")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
    #show image ("credits_cg4" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Writing" at credits_text_scroll_right as credits_header_2
    show credits_text "Tabuukilla\nNullwin\nNinja" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_writer_assignments()", "Nullwin: Monika Opening Draft 1\nTabuukilla: Monika Opening/Route\nNinja: Natsuki/Yuri Route")
    #else:
    
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
    #show image ("credits_cg5" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits3 at credits_scroll_right
    show credits_header "Writing" at credits_text_scroll_left as credits_header_1
    show credits_text "Xenohaze\nProtag\nSnakeWrangler" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_writer_assignments2()", "Xenohaze: Sayori Route\nProtag/SnakeWrangler: Yuri Route")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
    #show image ("credits_cg6" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Music" at credits_text_scroll_right as credits_header_2
    show credits_text "Matt Twigg" at credits_text_scroll_right as credits_text_2
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_source(\"Jamming Tunes\")", "Our Composer")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
    #show image ("credits_cg7" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits4 at credits_scroll_right
    show credits_header "Programmers" at credits_text_scroll_left as credits_header_1
    show credits_text "Tabuukilla\nGarnetSunset" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_code_assignments()", "Garnet: DDLC Modding Toolkit\nTK: CODING EVERYTHING")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
    #show image ("credits_cg8" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Editors" at credits_text_scroll_right as credits_header_2
    show credits_text "SpaceCore\nNinja\nSyzygy\nDordlebuns" at credits_text_scroll_right as credits_text_2
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    #$ imagenum += 1
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("get_motto()", "Hunting Grammar Fixes...\nOne Error at a Time")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    #show image ("credits_cg9" + lockedtext) at credits_scroll_right as credits_image_1
    show modCredits5 at credits_scroll_right
    show credits_header "Special Thanks" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato" at credits_text_scroll_left as credits_text_1
    #$ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    #$ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("fire_salute()", "We Salute You o7 o7 o7")
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
    #show image ("credits_cg10" + lockedtext) at credits_scroll_left as credits_image_2
    show credits_header "Special Thanks" at credits_text_scroll_right as credits_header_2
    show credits_text "Monika\n[player]" at credits_text_scroll_right as credits_text_2
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    #if not persistent.clearall:
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("so_long()", "And farewell.")
    call updateconsolehistory("")
    $ consolehistory = []
    #else:
    #    call updateconsole_clearall("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    pause 4.0
    call updateconsole("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
    call updateconsole("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    call updateconsolehistory("")
    $ consolehistory = []
    call updateconsole("ddlc.mod(\"puristmod\").end()", "Ending modification...")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    show credits_ts2
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    play sound page_turn
    stop music fadeout 10
    #show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        #scene black
        show white with dissolve_cg
        $ pause()
        #call screen dialog(message="There's nothing left to do anymore.", ok_action=Quit(confirm=False))
        window show
        "There's nothing to do anymore."
        #return
        menu:
            "That's right.":
                window hide # BECAUSE RENPY HATES TRYING TO QUIT WITHIN ITSELF?
                jump postcredits_loop
            "No, that's wrong.":
                python:
                    for savegame in renpy.list_saved_games(fast=True):
                        renpy.unlink_save(savegame)

                call resetDefaults
                "...If you're so sure.{nw}"
                $ renpy.utter_restart()
                return

        return