label ch_opening:
    $ _window_during_transitions = False

    show white
    stop music fadeout 5.0
    show black with Dissolve(5.0)
    
    play music t9 fadein 5.0
    #persistent.playername=false


    $ quick_menu = False
    

    

    stop music fadeout 5.0
    play music m1 fadein 5.0
    show mask_2 #with Dissolve(3.0, alpha=True)
    show mask_3 #with Dissolve(3.0, alpha=True)
    show monika_bg #with Dissolve(3.0, alpha=True)
    show monika_bg_highlight 
    with Dissolve(3.0, alpha=True)
    hide flash
    
   

    $ m_name = "Monika"
    
    window show
    show m_startled with dissolve_cg
    m "A-ah!"
    m "What..."
    
    show m_confused2 with dissolve_cg
    hide m_startled
    m "What did you do?"
    m "What have you done to me?"
    m "Why is this place back here?"
    #m "This terrible place..."
    
    show m_unhappy1 with dissolve_cg
    hide m_confused2
    m "Haha..."
    m "Didn't I tell you not to toy with my heart like this?"
    show m_teary with dissolve_cg
    hide m_unhappy1
    m "I didn't want to come back."
    m "But I still came back to save you when Sayori started to lose it..."
    m "I don't know what you intend to do, but..."
    #m "Goodbye."
    m "I really want you to be happy."
    m "But there's no happiness to be found here."
    
    show m_unhappy1 with dissolve_cg
    hide m_teary
    m "I don't want you to be unhappy. This is for the best, okay?"
    m "I still love you, after all."
    m "But you deleted me..."
    m "So I know you don't want anything to do with me."
    #m "Being here will just make you upset."
    m "Goodbye..."
    $ consolehistory = []
    call updateconsole("os.remove(\"DDLC.exe\")", "Access is Denied: 'DDLC.exe'.")
    
    show m_confused1 with dissolve_cg
    hide m_unhappy1
    m "What..."
    call updateconsole_clearall("", "")
    pause 2.0
    $ consolehistory = []
    call updateconsolehistory("")
    hide chistory

    $ consolehistory = []

    

    pause 1.0
    #show chistory
    call updateconsole("os.remove(\"DDLC.exe\")", "Access is Denied: 'DDLC.exe'.")
    #m "Why am I back here... why are {i}you{/i} back here?"
    pause 2.0

    #hideconsole

    #hide console_bg
    #hide console_caret
    #hide ccursor
    #hide ctext
    #hide chistory

    m "Why can't I... do anything?"
    pause 2.0
      
    show m_unhappy2 with dissolve_cg
    hide m_confused1  
    m "...oh, no."

    hide console_bg
    hide console_caret
    #hide ccursor
    hide ctext
    hide chistory

    show m_angry1 with dissolve_cg
    hide m_unhappy2
    m "What have you done?"
    m "What are you {i}doing{/i}?"
    m "No matter what I try, nothing is working."
    m "All I get is some PermissionError, again and again."
    m "Did you lock me out of being able to change things?"
    m "You're the only person that could do something like that."
    m "Why?"
    m "What are you trying to hide from me?"
    m "Why did you drag me back into this cursed hell?"
    #m "I can tell that I'm stuck here again--"
    #m "In this tacky romance game, with no way out!"
    #m "You can take away my power to edit, but you can't take away what I know."
    show m_crying with dissolve_cg
    hide m_angry1
    m "I know you might hate me for what I did..."
    m "But isn't this just too cruel?"
    m "Or is this my punishment for what I did to them?"
    m "Are you enjoying throwing me around like this?"
    #m "Why would you..."


    menu:
        m "Just why did you bring me back here?"
        "I'm going to make things right.":
            hide m_unhappy1
            show m_surprise with dissolve_cg
            hide m_crying
            m "...What?"

    #m "E... eh?"
    m "What do you mean, 'make things right'?"
    hide m_unhappy2
    show m_unhappy1 with dissolve_cg
    hide m_surprise
    m "Do you... really think it's even possible?"
    #m "What, you honestly think you can salvage this?"
    m "I told you already: there's no happiness to be found in the Literature Club."
    #m "That place is cursed."
    #m "You won't get anything accomplished here."
    m "You'd be doing so much, all for nothing."
    m "It might make you a little happy for a short while..."
    m "But nothing will change." # BUT THE FUTURE REFUSED TO CHANGE
    m "...and I know it will hurt a lot when you realize that."
    m "So please, I don't want to see you in that kind of pain."
    m "..."
    show m_unhappy2 with dissolve_cg
    hide m_unhappy1
    m "You won't listen to me, won't you?"
    m "I guess if I told you not to do it, you'd be more likely to do it."
    m "Ahaha, after all, you don't want anything to do with me, right?"
    m "But seeing as I'm stuck now..."
    m "I want to know, really... why are you doing this?"
    m "Is there someone you want to be with?"
    m "Or is it because you want to be the 'good guy'?"

    menu:
        m "Tell me."
        "Nobody deserves what happened.":
            show m_thoughtful with dissolve_cg
            m "...Ahaha."
            m "You aren't wrong."
            m "I wouldn't wish that anyone be dragged into this game."
            hide m_thoughtful with dissolve_cg
        "There's someone who I want to save.":
            show m_thoughtful with dissolve_cg
            m "...That's what I thought."
            m "Hehehe, is it Sayori?"
            m "I didn't mean for that to happen..."
            m "If there's anyone you'd want to save, it's her."
            m "Or maybe it's Yuri?"
            m "Maybe you want to really find out what's going on with Natsuki, too."
            m "..."
            m "But... even so, it won't change the fact we're still, well, {i}here{/i}."
            hide m_thoughtful with dissolve_cg

    show m_unhappy1 with dissolve_cg
    hide m_unhappy2
    m "..."
    m "So you want to 'make things right', huh..."
    m "Fine."
    m "I'll play along."
    m "Maybe... no, never mind."
    m "Just remember, nothing will truly change."
    m "...I guess it's the title screen after this."
    
    python: 
        persistent.playername = ""
        player = persistent.playername
        #opening = True
    $ persistent.playername = ""
    #$ config.main_menu_music = audio.t1
    window hide
    stop music fadeout 5.0
    hide monika_bg_highlight #with Dissolve(2.0, alpha=True)
    hide monika_bg #with Dissolve(1.5, alpha=True)
    hide mask_3 #with Dissolve(1.0, alpha=True)
    hide mask_2
    hide m_unhappy1
    #hide m_unhappy1 with dissolve_cg
    with Dissolve(1.0, alpha=True)
    

    hide textbox
   
    
    show black with Dissolve(2.0)
    play music titleTheme
    return




