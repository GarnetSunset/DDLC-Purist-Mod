label resetDefaults:
    $ persistent.playername = ""
    $ player = persistent.playername
    $ persistent.playthrough = 0
    $ persistent.yuri_kill = 0
    $ persistent.seen_eyes = None
    $ persistent.seen_sticker = None
    $ persistent.ghost_menu = None
    $ persistent.seen_ghost_menu = None
    $ seen_eyes_this_chapter = False
    $ persistent.anticheat = 0
    $ persistent.clear = [False, False, False, False, False, False, False, False, False, False]
    $ persistent.special_poems = None
    $ persistent.clearall = None
    $ persistent.menu_bg_m = None
    $ persistent.first_load = None
    # Boolean for the opening cutscene
    $ persistent.opening_scene = False
    # Boolean for Monika route unlock
    $ persistent.monika_unlock = False
    # Boolean for if you got the bad end
    $ persistent.got_monika_bad_end = False
    # non persientnt but helps with call stack
    $ monika_route_lock = False
    $ monika_route_position = 1 # choice 1
    # trackers for routing
    $ sayoriRoutePoints = 0
    $ natsukiRoutePoints = 0
    $ yuriRoutePoints = 0
    $ firstWeekendPick = True
    $ natsukiRoute = False
    $ yuriRoute = False
    $ sayoriRoute = True
    $ makeComplex = False
    $ askAboutdate = False
    $ confrontDad = False
    $ readManga = False
    $ natsukiGoodEnd = True

    $ persistent.natsukiCompletedGood = False
    $ persistent.yuriCompletedGood = False 
    $ persistent.sayoriCompletedGood = False

    $ persistent.natsukiBadInterludeViewed = False
    $ saveLocked = False
    $ persistent.timesTried = 0
    $ persistent.skipped = False

    $ playerNameBackwards = "" # YEAH SCREW YOU TOO NINJA YOUR ROUTE IS SO HIGH MAINTENANCE LOL

    $ sayori_affection = 0
    $ sayori_please_clap = False
    $ sayori_flag_one = False
    $ sayori_flag_two = False # SO MUCH HIGH MAINTENANCE I S2G
    $ sayori_goodEnd = True
    $ sayori_informal = True

    $ persistent.sayoriBadInterludeViewed = False
    $ persistent.sayoriGoodInterludeViewed = False

    $ weekendSayori = False
    $ weekendMonika = False

    $ monika_bad_end = False

    # these are here to facilitate the choices for the festival
    $ monikaFestival_maidCafe = False
    $ monikaFestival_hauntedHouse = False
    $ monikaFestival_food = False
    $ monikaFestival_fortuneTeller = False
    $ saidIt = False

    # these are here to keep track of how many times you've been to Monika
    $ persistent.natsukiRouteCompletions = 0
    $ persistent.sayoriRouteCompletions = 0
    $ persistent.yuriRouteCompletions = 0

    $ persistent.yuriBadInterlude1Viewed = False
    $ persistent.yuriBadInterlude2Viewed = False
    $ persistent.yuriGoodInterludeViewed = False

    $ persistent.natsukiRouteStarted = False
    $ persistent.yuriRouteStarted = False
    $ persistent.sayoriRouteStarted = False
    $ persistent.monikaRouteStarted = False

    $ persistent.autoload = ""
    $ persistent.first_run = False

    #init python:
    #    for savegame in renpy.list_saved_games(fast=True):
    #        renpy.unlink_save(savegame)
    return