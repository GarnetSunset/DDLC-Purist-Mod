label monikaRoute_sayoriInteract:
    $ s_interact = True
    show sayori 1a at t11
    s "Hi, [player]!"
    "Hearing Sayori's voice, I raise a hand and wave."
    show sayori 1c at f11
    s "Ehehe, you look tired~"
    mc "I was up late."
    mc "Couldn't get to sleep in class, either."
    mc "I'm probably going to take a nap."
    "I look around the room and find no one else is here yet."
    mc "Huh, that's pretty strange. No one's here."
    s "Mhm. They're all running kinda late."
    "I walk over to a seat next to the wall and put my things down, taking said seat."
    s 2r "Ehehe, you must be really tired."
    mc "Yeah."
    show black with close_eyes
    "I fold my arms for a makeshift pillow and put my head down in it, closing my eyes and letting rest overtake me."
    "Or at least, I try."
    "It's difficult since I can feel Sayori sharing the desk with me as pillow space."
    hide black with open_eyes
    mc "Um, Sayori."
    s 1b "Hm?"
    mc "...why are you on the same desk?"
    s 5b "Well..."
    s 1a "We haven't gotten to spend much time together, so I thought that if you were going to take a nap, I would too~"
    "I don't know how to respond to that, so I decide to let it happen without further resistance."
    "It's not like I am actually bothered by it."
    mc "Alright, well... good night, for a bit."
    s "Good night~"
    show black with close_eyes
    hide sayori
    "With that, I decide to close my eyes and try to go to sleep."
    "When I wake up, I take a look at the clock and see that ten minutes have gone by."
    mc "Ha..."
    hide black with open_eyes
    "I take a look around the room, finding the others slipped in. I start poking Sayori on the shoulder."
    mc "Sayori, wake up, everyone's here now."
    show monika 1k at t44
    m "Haha, sorry, did we disturb you?"
    mc "N-no, not really, we were just waiting for everyone to show up, anyway."
    hide monika with dissolve
    s "Mmmmmhhh..."
    show sayori 1a at f11
    "Sayori perks up, rubbing her eyes."
    s "Ehehe, that was a good nap!"
    s 4m "Oh!"
    s 1r "Monika, hi!"
    "Sayori gives a smile to our club president as she stands up."
    show monika 1n at t44
    m "It's fine..."
    m "A-anyway, we can begin club activities."
    "Part of me is surprised to hear what sounded like a stammer coming from Monika, as she usually has it so together."
    m 4l "Er, well, if you aren't done with your song, anyway."
    m 5a "Ahaha, unless we'd all like to do something else to take a brief break from songwriting?"
    show monika at thide 
    hide monika 
    "No one seems to have any ideas for something we could do instead, so we end up lounging around."
    "I try to keep working on my song. Sayori pulls up a desk so we can sit next together as she works on hers."
    show sayori at thide 
    hide sayori
    "The day quietly goes by, the sounds of pencils scribbling on paper and the occasional grumble of frustration at words not going together breaking the silence."
    "All in all, it's a fairly calm day."
    show sayori 1a at t11
    s 1c "Hey, [player]."
    mc "Hm? What is it, Sayori?"
    s "Could you look over what I have?"
    s "I want a second opinion on it."
    mc "Alright."
    show sayori 1a at f11
    "Sayori slides me a single sheet of paper."
    s 2k "Um, well, it's actually only the second verse, but I'm having some trouble with it."
    mc "I see."
    mc "Well..."
    "I give it a quick read through, trying to imagine how it would be sung."
    mc "Here, this third line."
    mc "I think there's too many syllables."
    mc "It doesn't flow as nicely."
    s 1c "Is there anything else?"
    mc "Hmm..."
    mc "I don't know if it's intentional, but you use the word 'sun' a lot in this verse alone."
    mc "I mean, if there's no other way to do it, I guess it's fine, but it kind of stands out."
    s 1q "Ehehe, you're really helpful, [player]."
    s 1r "Are you sure you didn't write songs before, either?"
    s "Your poems were pretty good..."
    mc "Well, I did use to watch a lot of anime, so they had fun openings..."
    s "Ehehe, maybe."
    s "Thanks for helping, [player]!"
    mc "No problem, Sayori."
    show sayori at thide
    hide sayori 
    "After that, Sayori goes across the room, sitting down at a desk and continuing her work from there. Or at least, that's what I assume she's doing."
    "The silence of the room from before when Sayori came over returns. I take another look at my song. I still have to do the second verse."
    "Maybe writing it here would be a bad idea. It is kind of embarrassing to think about it, writing about how I found friends here."
    "Then again, I'm going to have to share it anyway, so they're all going to see it in the end."
    "The time goes by quickly. My worries about the others seeing what I wrote down so far seems to have been off the mark since everyone is kind of secretive, keeping to themselves."
    "I guess even if we have shared poems with each other, a song is kind of a step up."
    "We might be fine showing one or two poems to each other, but there's things like the genre of a song that differ from a poem."
    return


#[Natsuki]
label monikaRoute_natsukiInteract:
    $ n_interact = True
    stop music fadeout 3.0
    play music NatTheme fadein 3.0
    show natsuki 2b at t44
    n "He--"
    show natsuki 4q at t43
    show sayori 1c at t44
    s "Oh, hi [player]!"
    "My attention is grabbed by Natsuki, who turned her head away the instant Sayori called out to me."
    mc "Um, did I walk in at a bad time?"
    n 5w "Hmph."
    s 1r "Ehehe~"
    "Natsuki's reaction seems to make Sayori giggle, causing Natsuki to get even more annoyed."
    mc "I can leave if you want."
    s 2x "It's not that, [player]."
    n 1p "A-ahh!"

    #show natsuki 1r at t43 zorder 2
    #show sayori 4q at t44 behind natsuki
    #"Sayori gets up from her seat and puts her hands on Natsuki's shoulders."
    #s "Your cupcakes, your poems, even the manga you read..."
    #s "It's all just as cute as you are~"
    show sayori at t22 behind natsuki # TK lazily copy pastes reused code
    show natsuki at h43

    "Natsuki lets out a yelp as Sayori goes behind her and then wraps her arms around Natsuki."
    s 1c "She's just embarrassed, is all."
    s "Come on, Natsuki~"
    n 5q "S-shut up..."
    show natsuki at thide
    show sayori at thide
    hide natsuki
    hide sayori 
    "I go to my usual desk and put my things down."
    mc "What's going on?"
    show natsuki 1q at t11
    n "... en... ng... rls..."
    show sayori 4q at t44
    s "[player] won't be able to hear you, you know?"
    show sayori at thide 
    hide sayori
    n "I... I just wanted to know..."
    mc "Know what?"
    n "J-just be quiet!"
    "Natsuki takes another breath."
    n 5w "I... I wanted to know if you saw Parfait Girls this past weekend."
    n 4q "S-sayori said you used to watch a lot of anime and you seemed to know about songs, so I..."
    n "I wanted to know if you watched it and what you thought about the opening."
    "Parfait Girls..."
    mc "It was good. I think the animation was fine and pretty smooth."
    mc "The music itself was pretty catchy. I'll probably have to preorder the full single. Next week's show should have the ending theme, right? They did close out this episode with the opening."
    n 1c "Yeah. Hopefully it'll be just as good."
    mc "Were you planning on using it for your song?"
    n 5g "W-what?! No!"
    mc "Oh, my bad. I didn't word that very well."
    n 4q "N-no, I got what you meant, dummy."
    n "W-well, if it fits what I want the song to be about, I might use it for inspiration."
    show sayori 1c at t44
    s "Ehehe, Natsuki's so cute when she's honest~"
    n 1i "S-shut up, Sayori!"
    s 4q "But it's true!"
    s "Don't you think so, [player]?"
    mc "U-um..."
    "This is a landmine filled question."
    menu:
        "I think so.":
            s 1x "Come on, tell usssss!"
        "I don't think so.":# (doesn't matter)
            s 1x "Come on, tell usssss!"
    #s "Come on, tell usssss!"
    n "S-sayori!"
    show natsuki 1i at t43 zorder 2
    show sayori 1q at t22 zorder 1
    "Before I can open my mouth, Sayori pushes Natsuki forward, probably a little harder than she had to."
    mc "I got'cha!"
    hide sayori with dissolve
    show natsuki 1i at f11
    "I manage to catch Natsuki before she can stumble over into me and into the desks."
    mc "Sorry about that."
    n 1r "I... I'll forgive you this time."
    show sayori 1q at t44
    s "Ehehe~"
    n 4e "Don't think I haven't forgotten about you!"
    s 4q "Oh no, Natsuki's ma~ad~"
    "Sayori only laughs as Natsuki pouts more."
    show monika 1b at l41
    m "It's quite lively here--"
    mc "U-um..."
    n 1i "R-right!"
    show natsuki 1i at t11
    "I quickly step away from Natsuki, letting go of her."
    n 5g "Sayori shoved me."
    m 3c "Sayori, please don't push everyone around."
    s 5b "Ehehe, sorry~"
    s 1q "I'll stick to hugging from now on!"
    m 2c "Right..."
    "Monika then pauses before putting on a smile."
    m 3a "But it seemed quite energetic in here. What was going on?"
    mc "We were just talking about Parfait Girls."
    "I quickly shove my comment in before Sayori can say anything."
    mc "It aired this weekend, so Natsuki and I were talking about how we thought the first episode went."
    mc "Sayori thought to play with Natsuki and ended up pushing her a little harder than anticipated."
    m 2c "I see..."
    m 3c "Well, make sure to be careful."
    y "Hm?"
    mc "Oh, hi Yuri."
    show yuri 2b at l41
    show monika 2c at t42
    show natsuki 4c at t43
    show sayori 1q at t44
    y "Sorry for being late, someone asked me to take over their clean-up duties today. What are we being careful of?"
    m 2b "Things like playing around in here."
    s 5b "Ehehehe..."
    m 3b "As I was saying, since we sometimes have tea in here, it probably would be best to keep calm and not play around."
    y "Yes, having hot tea spill around wouldn't be for the best."
    s 1x "Don't worry, I'll behave~"
    "Sayori gives me a knowing smile, as if to say we're not finished yet."
    m 3j "Anyway, I guess today's the same as yesterday. If you want help, then we're here for you, but other than that you're free to do what you want."
    show yuri at thide
    show monika at thide 
    show natsuki at thide
    show sayori at thide
    hide yuri 
    hide monika 
    hide natsuki 
    hide sayori 
    "Everyone seems fine with this and goes about their normal business."
    "Well, I'm glad I grabbed some manga this morning."
    "I start reading the first of the volumes I brought with me."
    n "Hey."
    show natsuki 2s at t11
    "I look up, finding Natsuki standing next to my desk."
    mc "Did you need something?"
    n "No, just..."
    n 4w "I thought we could talk about Parfait Girls."
    "I notice Natsuki has volume one and two in her hands."
    "Ah, right, those are the ones that got adapted this last weekend."
    mc "Well, I think they did okay."
    mc "My only concern is that they'll rush through the first few volumes since the beginning isn't exactly the strongest."
    n 1c "Yeah. It is a little generic at the start."
    mc "But hopefully they'll find ways to make it exciting or gather attention, since the beginning might be generic but it lays out all the groundwork."
    n "Mhm."
    n 2q "W-well, hey. If you aren't doing anything this weekend..."
    mc "Hm?"
    n "We could maybe watch the episode."
    n "It'll be nice to watch it with someone who read the manga, at least."
    show sayori 1a at t44
    s "Ehehe~"
    show sayori 1q at t44
    "Sayori gets a pretty harsh look from Natsuki, but it only makes her laugh more."
    show sayori at thide 
    hide sayori 
    n 5s "N-never mind."
    n "Let's just talk about it next week."
    mc "Alright."
    show natsuki at thide 
    hide natsuki
    show monika 1c at t41
    "I notice out of the corner of my eye that Monika was watching us, her eyes darting back to the paper in front of her as the conversation ends."
    show monika at thide
    hide monika 
    "The rest of the day goes off without much incident, though Natsuki seems to avoid talking to me afterwards."
    "Maybe I should've taken her invitation."
    "Either way, eventually we all have to leave."
    return

label monikaRoute_yuriInteract:
    $ y_interact = True
    scene bg club_day with wipeleft_scene
    play music aNewDay fadein 3.0
    show yuri 1b at t11
    y "Good afternoon, [player]."
    mc "Oh, hey Yuri."
    y "It seems I got here a little earlier than the others."
    mc "Yeah. Well, they'll show up soon enough, right?"
    y 1d "They should."
    "I nod, going over to my usual seat and sitting down."
    show sayori 1r at t41
    s "Yahallo!"
    "Is that supposed to be some new trendy greeting or something?"
    y "Hello, Sayori."
    show sayori 1a at t21
    show yuri 1c at t22
    s "Hi, both of you! Come on you two, hurry up!"
    n "Geez, someone's energetic."
    show yuri 1c at t44
    show sayori 1a at t43
    show natsuki 4c at t42
    show monika 1a at t41
    "Shortly after Sayori enters the room, Monika and Natsuki come in as well, saying their hellos."
    y 1f "Are we doing anything special today?"
    m 3b "Nope, it's the same deal as usual. Maybe we should plan for something, though. It's been a while since we did anything as a club."
    y 1b "That's true."
    s 1c "Well, maybe next week. I think it's fine like this for now, ehehe~"
    s "Maybe we can take a break from writing songs and try writing a poem again."
    m 2a "That's true."
    s "Well, maybe we should do that next week. I'm still in the mood for songs."
    m "Mhm. After all, it's only been about a week or so. Let's try to keep the song-writing for a little longer before switching gears."
    m "Is that fine with everyone?"
    n 4b "I don't see a problem with it."
    y 2b "Neither do I."
    mc "I'm fine with that, too."
    m 3a "Alright, it's settled then. We'll wait until next week to try something new."
    m "But until then, I guess we'll just go as we have been for this week. Make sure to let anyone know if you want help with your song~"
    show monika at thide 
    show natsuki at thide 
    show sayori at thide 
    show yuri at thide
    hide monika 
    hide natsuki 
    hide sayori 
    hide yuri
    stop music fadeout 2.0
    "With that, everyone goes back to their activities."    
    "The time begins to crawl by as I read a book I grabbed from my shelf this morning."
    "Mgh... probably should have read the description. Where did I even get this book again...? Probably bought it on a sale. It's hard to read, too."
    "I'm brought out of my thoughts by the sound of glass clinking in front of me."
    play music YurTheme fadein 3.0
    mc "Hm?"
    show yuri 2c at f11
    y "You looked like you could use some tea."
    mc "Oh. Thanks Yuri."
    y 2f "Is that a hard book?" # // the book isn't the only thing that's hard
    mc "I guess? Maybe I'm not smart enough to understand it."
    "I hear some more glass being put down, seeing that Yuri put another glass down before she pulls a chair over."
    show yuri 1a at s11
    y "Well, maybe I can help."
    mc "Oh, alright. Though, why the sudden interest?"
    y 3j "Y-you brought a new book in today, so I was curious about it is all."
    "I seem to have put Yuri on the defensive."
    mc "Oh, that's nice of you. But I am struggling to get through it."
    y "Can I see the book?"
    mc "Sure."
    "I close the book and turn it over to Yuri, who looks at the cover and then the first few pages."
    show yuri 1a
    "Her eyes seem to light up as she looks through the pages."
    mc "Um, Yuri?"
    y 3j "O-oh, sorry. I can see why you might have difficulty with it, though."
    y 3b "It's definitely not an easy read."
    y "But if you reread several pages, you should be able to get it."
    mc "Okay."
    y 3e "You could also try something easier, as well. While it's good to push yourself, if you push yourself too much, you'll only end up making no progress and getting frustrated about it."
    mc "That's true."
    y 2b "Hmm..."
    y "[player], did you ever finish reading Portrait of Markov?"
    mc "I did, it was an interesting read. Thanks for the warnings about the horror, though."
    y 1a "Hmm, okay."
    "Yuri gets up from her seat."
    y "Excuse me for a bit."
    show yuri at lhide
    hide yuri
    "I watch Yuri go over to her bag and fish something out of it, quickly turning away when she turns around to come back."
    show yuri 1a at f11
    y "Here."
    "I receive a book from Yuri titled \'Shadow of the Meadow\'."
    y 2b "This one is of lower difficulty. Since you've read the book Portrait of Markov, it's about the same difficulty--if not slightly easier."
    mc "Ah, I see..."
    mc "I guess I can give it a shot."
    mc "Aren't you reading it, though?"
    y 1a "I actually finished it today, so you can borrow it."
    mc "Thanks, Yuri. I guess you can borrow that book as well."
    y 1d "Thank you, [player]."
    "I start reading the book Yuri gave to me, finding it much, much easier to read."
    y 2d "Oh, let me know if there's anything confusing."
    y "I should be able to clarify things."
    mc "Alright, thanks again, Yuri."
    scene bg club_day with wipeleft_scene
    "The time goes by quickly, much faster than normal."    
    "The two of us quietly read together, occasionally breaking the silence when I ask Yuri about something that happened, making sure I understood it properly."
    show yuri 1a at t11
    y "You're pretty good at reading, though."
    mc "Well, I guess I read visual novels all the time."
    mc "It's like books, in a way."
    y 2f "I see. I'm not very familiar with that medium."
    mc "It can be kind of hard to get into..."
    y "Would you happen to know any good beginner ones?"
    mc "Er, I'll have to think about that one."
    mc "Sorry."
    y 1d "It's fine. It'd be hard for me to suggest a good beginner for thriller books, so I understand."
    mc "I'll try to think of one for you, though."
    y "Thank you."
    "Yuri smiles at me. I give a small smile back before we go back to our books."
    "With that, the time passes by quickly, and soon enough it's time to head home."
    return
