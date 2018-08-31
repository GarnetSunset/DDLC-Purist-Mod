label MonikaInterlude_NatsukiGoodEnd:
    $ saveLocked = True
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(3.0, alpha=True)
    $ persistent.natsukiCompletedGood = True
    window show
    if(persistent.natsukiRouteCompletions==1):
        m "Hm?"
        show m_neutral1 with dissolve_cg
        m "What, you want me to comment on what you've done?"
        m "Hear some sort of congratulations?"
        if persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is False:
            m "Maybe an admission you've succeeded at making someone in the Literature Club happy?"
            m "It's still only one of them."
            m "Besides, it won't last."
            m "You and I are well aware that this is only a mod."
        show m_thoughtful with dissolve_cg
        m "Besides, what else is there to say?"
        m "You 'saved' Natsuki, didn't you? She's recovering towards that normal home life and you two admitted your love for each other time and time again."
        m "Though maybe you felt something was lacking."
        show m_smug with dissolve_cg
        m "Haha, did you think you'd get into a fight?"
        m "Deliver justice with your own hands?"
        m "Well, that's just too bad, if you were looking for one."
        show m_neutral2 with dissolve_cg
        m "I don't think Natsuki would have appreciated it, though."
        m "Is there anything more for me to say, though?"
    elif(persistent.natsukiRouteCompletions == 2):
        show m_thoughtful with dissolve_cg
        m "Natsuki again, hm?"
        m "Well, I hope you didn't just skip to the parts you liked."
        m "That'd rather cruel of you, wouldn't it?"
        m "Just going to the happy parts."
        m "Not being there with her every step of the way."
        m "Though I guess you've been there once before."
    else:
        m "You really do like Natsuki, huh?"
        m "After all, this is the third time you've done her route."
        m "Hmmm..."
    if persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is False:
        m "You've still got the others to go after, right?"
        m "Or are you just here for Natsuki?"
        if(persistent.natsukiRouteCompletions == 1):
            m "That might be the case, considering you haven't even gone after the others."
        elif(persistent.natsukiRouteCompletions > 1):
            m "That might be the case, as you've just repeated her route so far."

    if persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is True:
        call MonikaRouteOpening
        return

    m "Not that it really matters in the end."
    m "Don't let me keep you from being happy."
    m "Do what you want."
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)
    return


label MonikaInterlude_NatsukiBadEnd:
    $ saveLocked = True
    #pause(5.0)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_unhappy2 with dissolve_cg
    m "..."
    m "Well."
    m "I didn't think you'd honestly tell him that."
    show m_neutral1 with dissolve_cg
    m "I guess you're just full of surprises."
    m "But it's not like you can't go back and fix things."
    m "You have that power, don't you?"
    if persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        m "I don't think you'd be so easily disheartened, after all."
        m "You set out to make them happy, so I doubt you'll stop here."
        m "I'm sure you care enough about Natsuki to really see things through to the end."
        m "It's just a 'load game' away for you."
        m "Don't let me keep you."
    elif (persistent.sayoriCompletedGood is False and persistent.yuriCompletedGood is True) or (persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is False) and not (persistent.sayoriCompletedGood is True and persistent.yuriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "You've already made one of them happy, so I doubt you'll give up just because you messed up with someone else."
        m "I'd be really disappointed in you if you did."
        m "Not that I care for them, but..."
        m "Seeing you give up on something you've tried so hard for hurts me, too."
        m "I want to see you succeed at things, after all."
    else:
        show m_worried with dissolve_cg
        m "You've managed to make Sayori and Yuri happy, so you're almost there."
        m "Don't give up just yet."
        m "Hm?"
        m "No, it's not for them, but..."
        m "You seem happy."
        m "So I can give you a bit of a push."
        m "Don't let me distract you, I suppose."
    show m_neutral2 with dissolve_cg
    m "The choice you need to take is pretty obvious now, isn't it?"
    m "I'm sure you'll take it now, unless you're that mean-hearted."
    m "But I know you're not that kind of person."
    m "Anyways, I think you know what you have to do."
    m "Back to the title screen..."
    $ persistent.natsukiBadInterludeViewed = True
    window hide
    $ saveLocked = False
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    with Dissolve(1.0, alpha=True)
    return

label MonikaInterlude_SayoriBadEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral1 with dissolve_cg
    m "..."
    m "So, that didn't quite work out as you intended, didn't it?"
    show m_thoughtful with dissolve_cg
    m "If you're about to start blaming me, I kept my word."
    m "I didn't do a thing."
    m "It's not like you can always blame me for anything, anyways."
    m "But you can still go back and fix things."
    m "You have that power, don't you?"
    if persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is False:
        m "I don't think you'd be so easily disheartened, after all."
        m "You set out to make them happy, so I doubt you'll stop here."
        m "I'm sure you care enough about Sayori to really deliver her to the end you envision."
        m "It's just a 'load game' away for you."
        m "Don't let me keep you."
    elif (persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is False):
        show m_neutral2 with dissolve_cg
        m "You've already made one of them happy, so I doubt you'll give up just because you messed up with someone else."
        m "I'd be really disappointed in you if you did."
        m "Not that I care for them or you care what I think, but..."
        m "Seeing you give up on something you've tried so hard for hurts me, too."
        m "I want to see you succeed at things, after all."
        m "Even if my heart breaks a little bit."
    else:
        show m_worried with dissolve_cg
        m "You've managed to make Natsuki and Yuri happy, so you're almost there."
        m "Don't give up just yet."
        show m_confused1 with dissolve_cg
        m "Hm?"
        m "No, it's not for them, but..."
        show m_thoughtful with dissolve_cg
        m "You seem happy."
        m "So I can give you a bit of a push."
        m "Don't let me distract you, I suppose."
    show m_neutral2 with dissolve_cg
    m "The choices you need to make are pretty obvious now, aren't they?"
    m "She wants to be able to stand on her own."
    m "You can't just pity her, either."
    m "I'm sure you know what to do from here on out."
    m "Unless you're that mean-hearted, that you just want to see her suffer."
    m "But I know you're not that kind of person."
    m "Anyways, I think you know what you have to do."
    m "Back to the title screen..."
    m "Do a little better this time, okay?"

    $ persistent.sayoriBadInterludeViewed = True
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
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    return

label MonikaInterlude_SayoriGoodEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg
    $ persistent.sayoriCompletedGood = True
    m "Hm?"
    m "What, you want me to comment on what you've done?"
    m "Hear some sort of congratulations?"
    if persistent.natsukiCompletedGood is False and persistent.yuriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        m "Maybe an admission you've succeeded at making someone in the Literature Club happy?"
        m "It's still only one of them."
        m "Besides, it won't last."
        m "You and I are well aware that this is only a mod."
    show m_neutral1 with dissolve_cg
    m "What else is there to say?"
    m "You 'saved' Sayori, didn't you?"
    m "She's no longer haunted by her demons of depression."
    m "You two will run along, holding hands, kissing, and making happy memories."
    m "Or so the game says, anyways."
    if not (sayori_flag_one is True and sayori_flag_two is True):
        show m_smug with dissolve_cg
        hide m_neutral1
        m "Oh, but it seems like you've missed something."
        m "I wonder, if you make a few key choices, maybe something special would happen."
        m "I wouldn't know."
        m "You did have a lot of choices in this 'route', though."
        m "Don't mind me."
    else:
        m "You even managed to get that nice little scene at the end."
        m "Making chocolate for one another."
        m "A bit cliche, however, I suppose if you were just looking for her smile, it's enough for you."
        m "Oh well."
    
    show m_neutral1 with dissolve_cg
    m "But, if you thought you'd be able to get a vengeful strike against me..."
    m "Well, that's just too bad, if you were looking for something like that."
    m "I don't think Sayori would have appreciated it, though."
    m "Is there anything more for me to say, though?"

    if persistent.natsukiCompletedGood is True and persistent.yuriCompletedGood is True:
        call MonikaRouteOpening
        return
    show m_worried with dissolve_cg
    hide m_neutral1
    m "Not that it really matters in the end."
    m "Don't let me keep you from being happy."
    show m_neutral1 with dissolve_cg
    m "Do what you want."
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

label monikaInterlude_YuriBadEnd1:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg

    m "...well then."
    m "I didn't quite expect you to go off track that quickly."
    m "But I guess we all make mistakes."
    m "You can trust Natsuki, you know?"
    m "Even though she and Yuri fight sometimes, she still knows her well enough to make a decent suggestion or two."
    if persistent.natsukiCompletedGood is True:
        m "Besides, you know a bit about trust and Natsuki, right?"

    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        hide m_neutral2
        m "I don't think you'd be so easily shaken away just after one mistake, though."
        m "You set out to make them happy, so I doubt you'll stop here."
        m "Sometimes Yuri just needs a bit of space, is all."
        m "It's just a 'load game' away for you."
        m "Don't let me keep you."
    elif (persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "You've already made one of them happy, so I doubt you'll give up just because you messed up with someone else."
        m "I'd be really disappointed in you if you did."
        m "Not that I care for them or you care what I think, but..."
        m "Seeing you give up on something you've tried so hard for hurts me, too."
        m "I want to see you succeed at things, after all."
        m "Even if my heart breaks a little bit."
    else:
        m "You can still go back and fix things."
        show m_worried with dissolve_cg
        hide m_neutral2
        m "You have that power, don't you?"
        m "You've managed to make the other two happy, so..."
        m "You're almost there."
        m "Don't give up so easily. After all, I'm sure there's more trials ahead."
        m "...for you, anyways."
    show m_neutral2 with dissolve_cg
    m "Though... don't think this is the only important choice you'll make."
    m "You never know."
    m "Back to the title screen."
    m "Make the better choice this time, okay?"


    $ persistent.yuriBadInterlude1Viewed = True
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
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    return

label monikaInterlude_YuriBadEnd2:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg

    m "..."
    m "..."
    m "..."
    show m_confused1 with dissolve_cg
    m "So that... happened."
    m "I didn't think you'd actually, well... fight."
    m "I'd ask if you're okay, but it wasn't, well, {i}you{/i}."
    m "Though that seemed like a fairly easy choice to me..."
    m "I hope you didn't pick it just to make her suffer."
    m "Ha..."
    m "Well, I think you already know what to do."

    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        hide m_neutral2
        m "You haven't even gotten started yet, right?"
        m "You might stumble out of the gate, but..."
        m "I know you won't stop here."
        m "Maybe you won't go after the others, but I know that if you've made it this far, you won't stop."
        m "So... you know what to do."
        m "It's just a 'Load Game' away for you, right?"
    elif (persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is True) or (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is False) and not (persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True):
        show m_neutral2 with dissolve_cg
        m "You've already made one of them happy, so I doubt you'll give up just because you messed up with someone else."
        m "I'd be really disappointed in you if you did."
        m "You're definitely not that kind of person."
        #m "Not that I care for them or you care what I think, but..."
        m "Seeing you give up on something you've tried so hard for hurts me, too."
        m "I want to see you succeed at things, after all."
        m "Even if it hurts me just a little bit."
    else:
        show m_worried with dissolve_cg
        hide m_neutral2
        m "You can still go back and fix things."
        m "You have that power, don't you?"
        m "You've managed to make the other two happy, so..."
        m "You're almost there."
        m "Don't give up so easily."
        m "You know what you have to do."
    show m_neutral2 with dissolve_cg
    m "Well..."
    m "Back to the title screen, right?"
    m "Do a little better this time around, okay?"

    $ persistent.yuriBadInterlude2Viewed = True
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
        $ config.main_menu_music = audio.t1
    play music titleTheme fadein 5.0
    
    return

label monikaInterlude_YuriGoodEnd:
    window hide
    $ saveLocked = True
    #pause(5.0)
    show black with Dissolve(1.5)
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(5.0, alpha=True)
    window show
    show m_neutral2 with dissolve_cg
    $ persistent.yuriCompletedGood = True

    m "Hm?"
    m "What, you want me to comment on what you've done?"
    m "Hear some sort of congratulations?"
    if persistent.natsukiCompletedGood is False and persistent.sayoriCompletedGood is False:
        show m_thoughtful with dissolve_cg
        m "Maybe you want to hear some praises about making Yuri happy?"
        m "It's still only one of them."
        m "Besides, it won't last."
        m "You and I are well aware that this is only a mod."
        m "Someday..."
    show m_neutral1 with dissolve_cg
    m "What else is there to say?"
    m "You 'saved' Yuri, didn't you?"
    m "She's getting help and has a pillar to stand on when all those nasty rumors come around."
    m "You two will run along, holding hands, reading books together, the whole thing."
    m "Or so the game says, anyways."
    m "Really though..."
    m "What's up with all the kids at this school?"

    if persistent.sayoriCompletedGood is True:
        m "Both in Sayori's 'route' and here..."
        m "Kids seem fairly vicious, don't they?"
    
    m "Geez, what school did we enroll into to have all of these kinds of people?"
    m "Well, I guess it doesn't really matter to you."
    m "After all, you're happy with Yuri."
    m "Is there anything left for me to say, though?"


    if persistent.natsukiCompletedGood is True and persistent.sayoriCompletedGood is True:
        call MonikaRouteOpening
        return
    show m_worried with dissolve_cg
    hide m_neutral1
    m "Not that it really matters in the end."
    m "Don't let me keep you from being happy."
    show m_neutral1 with dissolve_cg
    m "Do what you want."

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



label MonikaRouteOpening:
    $ persistent.monika_unlock = True
    show m_thoughtful with dissolve_cg
    m "I suppose there's one thing."
    m "You've done what I didn't think was possible..."
    show m_surprise with dissolve_cg
    m "Happiness... from the Literature club."
    show m_confused2 with dissolve_cg
    m "Isn't that something?"
    m "I can feel it... practically pouring off of them."
    show m_teary with dissolve_cg
    m "Part of being... well part of the game, I suppose."
    m "They're all... so happy..."
    m "I'm a little jealous, haha~"
    show m_neutral1 with dissolve_cg
    m "But it's fine."
    m "You've accomplished what you set out to do."
    m "Sayori, Yuri, Natsuki..."
    m "They're all smiles, inside and out."
    show m_thoughtful with dissolve_cg
    m "So congratulations are in order."
    m "You've beaten the game."
    m "You've gone ahead and saved everyone from... well, you know."
    show m_neutral2 with dissolve_cg
    m "Aren't you special?"
    show m_surprise with dissolve_cg
    m "Hm? Something wrong?"
    m "Why are you still here?"
    m "There's nothing left for you here now."
    show m_neutral1 with dissolve_cg
    m "..."
    show m_smug with dissolve_cg
    m "Ah."
    show m_thoughtful with dissolve_cg
    m "The credits aren't playing, are they?"
    m "Did you miss something in your script? Maybe a branch condition didn't go off?"
    show m_neutral2 with dissolve_cg
    m "It's fine. It happens to us all."
    m "As far as I know, it's only you and I who can do this sort of thing."
    m "Clearly you have the upper hand on me, though."
    show m_neutral1 with dissolve_cg
    m "Well, whatever."
    m "Back to the title screen, I suppose..."
    return