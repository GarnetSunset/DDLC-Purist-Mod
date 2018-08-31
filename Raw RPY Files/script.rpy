# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    #    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    #if persistent.playthrough == 0:
    if True is True:
        # Intro
        $ chapter = 0
        call ch0_main

        if persistent.skipped is True:
            $ persistent.skipped = False # prevent a second triggering
            return

        if monika_route_lock is True:
            call monika_start # throws us to the next one
            # now we are in the monika route
            call monikaRoute_opening # good to go from here

            if(monika_bad_end is False):
                #python:
                #    for savegame in renpy.list_saved_games(fast=True):
                #        renpy.unlink_save(savegame)
                call credits2
            else:
                pass

            #call credits2
            return

        else:

        # Poem minigame 1
            call poem

        # Day 1
            $ chapter = 1
            call ch1_main
            call poemresponse_start
            call ch1_end

        # Poem minigame 2
            call poem

        # Day 2
            $ chapter = 2
            call ch2_main
            call poemresponse_start
            call ch2_end

        # Poem minigame 3
            call poem

        # Day 3
            $ chapter = 3
            call ch3_main
            call poemresponse_start
            call ch3_end

            $ chapter = 4
            call ch4_main

        #python:
        #    try: renpy.file(config.basedir + "/hxppy thxughts.png")
        #    except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        # ROUTE TIME
            if sayoriRoute is True:
                call sayoriRoute_start
                if sayori_goodEnd is True:
                    if persistent.sayoriGoodInterludeViewed is False:
                        $ persistent.sayoriGoodInterludeViewed = True
                        call MonikaInterlude_SayoriGoodEnd
                else:
                    if persistent.sayoriBadInterludeViewed is False:
                        $ persistent.sayoriBadInterludeViewed = True
                        call MonikaInterlude_SayoriBadEnd

            if natsukiRoute is True:
                call natsukiRoute_FestivalDays
                if natsukiGoodEnd is True:
                    $ persistent.natsukiRouteCompletions = persistent.natsukiRouteCompletions + 1
                    if(persistent.natsukiRouteCompletions < 4):
                        call MonikaInterlude_NatsukiGoodEnd
                else:
                    if persistent.natsukiBadInterludeViewed is False:
                        call MonikaInterlude_NatsukiBadEnd
            
            if yuriRoute is True:
                call yuriRoute_theFestival
                if yuri_badEnd1 is True:
                    if persistent.yuriBadInterlude1Viewed is False:
                        call monikaInterlude_YuriBadEnd1
                    $ persistent.yuriBadInterlude1Viewed = True
                if yuri_badEnd2 is True:
                    if persistent.yuriBadInterlude2Viewed is False:
                        call monikaInterlude_YuriBadEnd2
                    $ persistent.yuriBadInterlude2Viewed = True
                if yuri_badEnd1 is False and yuri_badEnd2 is False:
                    if persistent.yuriGoodInterludeViewed is False:
                        call monikaInterlude_YuriGoodEnd
                    $ persistent.yuriGoodInterludeViewed = True

            

            return

label autoload_yurikill:
    jump credits2

label monika_start: # you will only jump here if you pick a choice that locks you to the Monika route
    if monika_route_position == 1:
        call mon_ch0_1

    #s "[player], are you proud of me?" # the line Sayori says, have to do this for nice script flow/call return

    if monika_route_position <= 2: # 1 or 2
        call mon_ch0_2

    # will always hit 3rd choice anyways
    call mon_ch0_3

    return





label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
