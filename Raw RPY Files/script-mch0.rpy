label mon_ch0_1:
    "I always used to tell myself that it’s about time I go out and meet some girls or something like that."
    "Well, there’s already one girl here."
    show sayori 1a at t11
    "That girl is Sayori, my neighbor and good friend since we were children."
    "We used to walk to school together on days like this."
    "Recently, we've picked up that habit once again."
    $ s_name = "Sayori" 
    s "[player], are you proud of me?"
    return

label mon_ch0_2:
    mc "Eh? For what?"
    s 1c "You know…"
    s "For waking up on time!"
    mc "Well, you’ve been doing that for a while now."
    s "Uh-huh!"
    s "But you never even said anything about it!"
    show sayori at s11
    s "Even though we walk to school together every day…"
    mc "Well, yeah…"
    mc "I always thought it was implied."
    mc "It’s embarrassing to say out loud."
    s 1d "C’mon, please?"
    s "It’s good motivation."
    mc "Fine, fine…"
    mc "I’m proud of you, Sayori."
    show sayori at t11
    s 1q "Ehehe~"
    "We cross the street together and make our way to school."
    "As we get closer to the school, the streets become increasingly crowded."
    s 3a "By the way, [player]."
    s "Have you decided on a club to join yet?"
    mc "I have."
    s 4m "Ooooh, tell me!"
    return

label mon_ch0_3: # this is the last one
    mc "It’s a secret."
    s 2f "Aww…"
    mc "I’ll tell you when we go back home."
    s 1q "Okay, but that’s a promise!"
    "It’s a bit embarrassing to say, really."
    "That feeling of wanting to meet other girls?"
    "I’ve been feeling a little differently, lately."
    "As if my destined meeting was just around the corner."
    "It all started when I saw a flier for the Literature Club."
    "I didn’t really have a lot of interest in literature, but I felt some kind of pull."
    "It’s really strange."
    "There’s going to be a lot of club recruiting today, so I’ve been working up the nerve to go."
    scene bg class_day with wipeleft_scene
    "The school day is as ordinary than ever and it’s over before I even know it."
    "I tried to focus today, but the thought of going to the Literature Club made me nervous for some reason."
    "Maybe I should just rest for a bit and calm myself down."
    return
