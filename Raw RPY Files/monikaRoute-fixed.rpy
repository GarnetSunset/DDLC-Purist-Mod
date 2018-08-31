#Monika Route Outline
label monikaRoute_opening:

    "No, I can't do that."
    "I just have this feeling I can't run away."
    "Like I was supposed to go."
    scene bg corridor with wipeleft_scene
    "I leave the classroom right away, running into Sayori in the hall."
    "Passing by her, I say hello before ducking into the bathroom."
    "It's not all that embarrassing, but I kind of want to surprise Sayori as well."
    "After all, she is the Vice President of the Literature Club."
    scene bg corridor with wipeleft_scene  
    "I wait about five minutes before leaving the bathroom."
    "Then I take the path up to the room that was advertised on the flier. It's up the stairs, in an area of the school I rarely visit, since this is used by the third years."
    "I take a breath outside the clubroom door before putting my hand on the handle--"
    "Before I can pull it aside, the door slides open."
    show monika 4b at f11
    m "Ah, [player]! What a ni..."
    show monika 4d at f11
    "Monika, a girl in my class last year and the most popular girl in my school year, pauses halfway through her sentence."
    m 2e "What... what are you doing here?"
    mc "I, um, I came to join the Literature Club."
    m "But you're... you're not supposed to be here alone, it's only with Sa--"
    "Both of us hear a cry of joy."
    show sayori 1m at t44
    s "No way! Aaaahhhh!"
    show monika 2e at t21 zorder 1
    show sayori 1m at f22 zorder 2
    "Monika steps out of the way as Sayori almost tackles me as she wraps her arms around me."
    mc "Sayori, please get off of me."
    s 1q "I... I'm just so happy you're here...!"
    scene bg club_day with dissolve_cg
    play music aNewDay fadein 3.0
    "The two of us step into the room, where I close the door behind us."
    show monika 1h at t41
    show sayori 1q at t42
    show natsuki 2b at f43
    show yuri 1a at t44
    n "Huh."
    n "So you're the [player] that Sayori's always talking about?"
    show natsuki 2a at t43
    show yuri 3b at f44
    y "T-thank you for stopping by!"
    y 2b "It's a pleasure to meet you, [player]."
    y "Please enjoy your visit."
    show natsuki 4b at f43
    show yuri 2b at t44
    n "C'mon, Yuri..."
    n "No need to be so formal."
    n "He's going to think we're really strict or something..."
    show natsuki 4b at t43
    show yuri 3q at f44
    y "A-ah, sorry, but..."
    "She gives a small, but confident smile."
    y 1b "It's just the way I like to do things."
    "The tall one, whose name is apparently Yuri, seems to be quite shy compared to the others, but still seems pretty assertive."
    "The shorter girl nods."
    show natsuki 1c at f43
    show yuri 1b at t44
    n "I know, but not everyone's going to be so open."
    "By comparison, the girl named Natsuki - despite her size - came off as really assertive, but showed a hint of compassion there."
    show natsuki 1a at t43
    show yuri 1a at t44
    show sayori 4r at f42
    s "C'mon Monika, say something! You're our President and we just got a new member!"
    m 1d "R... right."
    "Monika clears her throat and puts on a smile."
    show sayori 1a at t42
    show monika 5a at f41
    m "Welcome to the Literature Club, [player]! I'm glad you decided to join us!"
    mc "Ah, thank you, Monika."
    show monika 1h at f41
    "Even though she's smiling, I swear Monika is glaring at me."
    show monika 1h at t41
    show sayori 1c at f42
    s "I didn't know you knew Monika, [player]."
    mc "We were only in the same class last year, that's all."
    mc "We didn't talk very often, either."
    s 1b "Well, you'll get to know her at this club, then~"
    s "And everyone else, too!"
    "Natsuki laughs from the side."
    show sayori 1b at t42
    show natsuki 1b at f43
    n "Well, I guess if Sayori's this happy to have you here, then I'm sure it won't be so bad to have you around."
    show natsuki 1b at t43
    "I smile a little awkwardly at her comment, deciding to take it as a compliment."
    mc "Thanks. I'll try not to bring anyone down."
    show yuri 1b at f44
    y "I'm sure you won't, [player]."
    "She pauses, then looks over my shoulder."
    y 1f "Monika, you're unusually quiet. You were very happy at the prospect of getting a new member just the other day."
    call monikaRoute_theClub
    return

#The Club: A place I wasn't supposed to belong to. Does she really not like me?
label monikaRoute_theClub:
    show yuri 1b at t44
    show monika 1d at f41
    m "Aha~ Sorry, I'm..."
    m 3b "Well, let me just say that I'm surprised, is all."
    m "I was happy that we might get a new member, but I wasn't very sure of it happening."
    m "So I'm still in shock, is all."
    m "Especially because it's someone I know."
    m 4k "Oh, well, we can celebrate a new member though, right?"
    show monika 1j at t41
    s 1x "Yeah!"
    y 1c "Huhu."
    y 2b "What an appropriate day for that, isn't it?"
    s 4c "Mhm!"
    s "[player], Natsuki even ma--"
    show natsuki 4e at f43
    n "Hey, don't ruin the surprise!"
    show natsuki 4c at t43
    s "Ehehe, sorry~"
    y "I'll go prepare some tea."
    s "Oh, let's get the desks set up first!"
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Sayori, Monika, and I push some of the desks around to form a table."
    "Yuri and Natsuki walk over to the back corner of the room, where Natsuki grabs a wrapped tray and Yuri opens a closet."
    "Still feeling a bit of awkwardness with Monika, I take a seat next to Sayori who nudges me when she catches me sneaking a glance at Monika."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z at t32 zorder 2
    n "Okay, are you ready?"
    n "...Ta-da!"
    show sayori 4m at t31 zorder 2
    show monika 2d at t33 zorder 2
    s "Woooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show sayori at f31 zorder 3
    s 4r "So cuuute~!"
    show monika 2g at t33 zorder 2
    "I hear Monika start talking, but she coughs, as if to clear her throat."
    m 2b "I had no idea you were so good at baking, Natsuki!"
    show monika at t33 zorder 2
    show natsuki at f32 zorder 3
    n 2d "Hehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Monika, then I take one."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s "Ihst'sh derlicishous!"
    "Sayori talks with her mouth full and already has managed to get icing all over her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Huh..."
    "I get the feeling I've seen this before."
    "It's that same feeling I had earlier today."
    "Where something feels different."
    show monika 1h at t33 zorder 2
    "I'm broken out of my thoughts by a small nudge from Monika, who narrows her eyes at me."
    hide monika
    "I then notice Natsuki is quiet."
    "She's also sneaking glances in my direction."
    "Ah, she must be waiting for me to take a bite."
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-why are you thanking me? It's not like I...!"
    "I swear I've heard this line before..."
    n 5s "...made them for you or anything."
    n 4a "But... I'm glad you like them."
    "Natsuki smiles. It's a very small smile, but it's sincere. I simply nod to end the conversation there."
    show natsuki at thide zorder 1
    hide natsuki
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a at t21 zorder 2
    mc "You keep a whole set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I guess."
    show monika 4a at t22 zorder 2
    m "Aha, d..."
    show monika 4q at t22 zorder 2
    "Monika's voice fades away before she goes completely silent, the rest of her sentence being cut off."
    y "Are you okay, Monika? Can I get you some canned coffee from the vending machines? It might wake you up."
    show monika 3a at t22 zorder 2
    "Monika quickly snaps to attention and shakes her head."
    m "N-no, I'm fine. Aha, but [player], don't let yourself be intimidated. Yuri's only trying to impress you~"
    show yuri at h21
    y 4b "E-eh?! Th... that's not..."
    y 3b "I really do think tea is good for reading, Monika."
    m "Sorry, I couldn't help but try to tease you."
    show monika 2f at t22
    pause(1.5)
    show monika 2j at t22
    "For some reason, a look of confusion flashes across Monika's face after saying this before she mysteriously nods to herself."
    y 2j "A-ah, I see."
    "I jump into the conversation to make it less awkward."
    mc "Well, tea and reading might not be a pastime for me, but I guess I can see where you're coming from."
    y 2c "I'm glad."
    "Yuri smiles faintly to herself before going to her seat."
    "Monika raises an eyebrow as she looks at me, then Yuri, then back to me before turning her attention back to the cupcake in front of her."
    show yuri at thide zorder 1
    hide yuri
    show monika at t11 zorder 2
    m "Ahem, well..."
    m "[player], what made you choose the Literature Club?"
    m "From what Sayori has told me, you seem more interested in anime and video games."
    "I shoot Sayori a dirty look."
    show sayori 5c at t41 zorder 1
    s "Ehehe~"
    hide sayori with wipeleft
    "Truthfully speaking, I was afraid of this question."
    "Maybe the truth isn't the best idea for now."
    mc "Well, I saw the flier a while back and came here since I wanted to broaden my horizons."
    mc "Sure, watching anime and reading visual novels is fun, but I thought reading books might be good too."
    mc "Though, I know I'm probably not going to stick with it alone, so I also thought maybe having a club could help as well."
    m 2j "I see..."
    m "Well, we'll make sure you'll feel right at home, okay?"
    m 4k "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    mc "Thanks."
    show monika 1a
    mc "I'm surprised, though."
    mc "How come you decided to start your own club?"
    mc "You were even president of the Debate Club last year."
    m 2m "Ahaha, well, you know..."
    m 1b "I wanted something different."
    m "You know, rather than just going through the motions."
    m "I wanted to take the reins of something."
    m "And if it also encourages others to get into literature, then that's also a plus!"
    show monika 1a
    show sayori 3q at t31 zorder 2
    s "Monika really is a great leader!"
    show yuri 1 at t33 zorder 2
    "Yuri also nods in agreement."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide yuri
    mc "I'm surprised there aren't more people, though."
    mc "Starting a club must be hard."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika 2a at t22 zorder 2
    show sayori 4r at t21 zorder 2
    s "Yeah!"
    show monika at t33 zorder 2
    show sayori at t32 zorder 2
    show yuri 1a at t31 zorder 2
    y "We'll do our best."
    show monika at t44 zorder 2
    show sayori at t43 zorder 2
    show yuri at t42 zorder 2
    show natsuki 4d at t41 zorder 2
    n "You know it!"
    "I can already feel a bond with these girls, seeing them smiling as they agree with Monika."
    "She must have worked really hard to find these three to work with her."
    "Maybe that's why they were all delighted by the idea of a new member joining."
    "Though, keeping up with their level of enthusiasm for literature might be hard."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at t32 zorder 2
    hide sayori
    hide monika
    hide natsuki
    y "So, [player], what kind of things do you like to read?"
    mc "Ah, well..."
    "I mutter \'Manga\' quietly to myself, half-joking."
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-not much of a reader, I take it..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    show sayori 1x at t41
    "I look to the side and see Sayori grinning ear to ear. It looks like she's pretty happy I'm trying to get along with them."
    hide sayori with wipeleft
    show yuri at t22
    show natsuki 2c at f21
    n "Hey, Yuri..."
    show natsuki at t21
    show yuri at f22
    y "Yes?"
    show yuri at t22
    show natsuki at f21
    n 2h "Well, about... you know, the first thing he said."
    show natsuki at t21
    mc "Manga?"
    show yuri at f22
    y "Natsuki tends to read manga in the clubroom--"
    show yuri at t22
    show natsuki at f21
    n 1r "D-don't just say it!"
    "For some reason, Natsuki seems embarrassed about it."
    n 1q "Besides..."
    n "Manga is literature too, you know?"
    n 1w "So... if [player] wants to read some of my manga, then don't try to stop him or anything."
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Natsuki..."
    y "I would never do such a thing."
    y 1i "Whatever he'd like to read, that's fine with me."
    show yuri at t33
    show natsuki at t32
    show sayori 1c at f31
    s "Oh hey, [player], I think I remember one of the titles you mentioned to me being something Natsuki read..."
    s 4j "Ooooh, but I can't remember the name!"
    mc "It was my favorite one, Sayori, and its name is {i}Parfait Girls{/i}."
    "The name is really embarrassing to say out loud, but it's actually a good series!"
    "I see all the girls around the room looking at me with shocked expressions."
    show yuri 1f at t43
    show natsuki 4c at t42
    show sayori 4m at t41
    show monika 2e at t44
    mc "Look, the beginning might have been slow, but all of the characters get really well developed as time passes."
    "I get oddly defensive about it, but that might also be my embarrassment."
    "It doesn't exactly sound like something a guy would read."
    "Admittedly, I got lured by the cover, but it hooked me from the start."
    hide monika with wipeleft
    hide yuri with wipeleft
    show sayori at t21
    show natsuki at t22
    n 4s "U... um."
    n "So you like that manga, too..."
    s 2x "Oh yeah, don't you read it all the time, Natsuki?"
    n "I-I don't read it {i}all{/i} the time!"
    n "...I really like reading it here, though."
    s "Ehehe~"
    show natsuki 1r at t42 zorder 2
    show sayori 4q at l41 behind natsuki
    "Sayori gets up from her seat and puts her hands on Natsuki's shoulders."
    s "Your cupcakes, your poems, even the manga you read..."
    s "It's all just as cute as you are~"
    show sayori at t21 behind natsuki
    show natsuki at h42
    n 1v "{i}I'm not cute!!{/i}"
    show natsuki at t11 zorder 2
    show sayori at thide zorder 1
    hide sayori
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Sometimes, I guess."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n "W-well..."
    n "...maybe."
    n 5q "I'd say you wouldn't like them, but..."
    n "Well, I think I have a good idea of your tastes, so maybe you might."
    n "But you still might not think they're good."
    show yuri 2f at t31 zorder 2
    y "I understand how Natsuki feels."
    y 2k "Sharing your own writing takes more than only confidence."
    y "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 2a at t33 zorder 2
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki."
    show yuri at s31
    y 3o "..."
    y "Ah..."
    mc "I guess it's the same for Yuri..."
    "Yuri smiles as if to mock herself."
    y 1d "To say all of that and not practice my own words... how hypocritical of me."
    show sayori 2g at t32 zorder 2
    s "Aww, don't say that!"
    s "...But, I did want to read everyone's poems."
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide yuri
    hide monika
    "Everyone sits in silence for a moment."
    "...it hangs a little longer than I thought it would."
    show monika 5a at f32 zorder 3
    "All of us turn our heads to Monika as she makes a sound."
    m 4d "O... oh."
    show sayori 1n at t41 zorder 1
    s "Did you think of something, Monika?"
    m "Ah, well, I might have something."
    show sayori at thide zorder 1
    hide sayori
    "Monika seems to nod to herself and mutters something that we can't hear before putting on a smile."
    m 5a "Okay!"
    m "I have an idea, everyone~"
    show yuri 3e at t31 zorder 2
    show natsuki 2k at t33 zorder 2
    ny "...?"
    "Natsuki and Yuri look at Monika with questioning looks on their faces."
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a at t32 zorder 2
    show natsuki at f33 zorder 3
    n 5q "U-Um..."
    show natsuki at t33 zorder 2
    show yuri 3v at f31 zorder 3
    y "..."
    show natsuki at t44 zorder 2
    show monika at t43 zorder 2
    show yuri at t42 zorder 2
    show sayori 4r at l41
    s "Yeeeah! Let's do it!"
    show monika at f43 zorder 3
    m "Plus, now that we have a new member, I think it will help us all get to know each other a little more and strengthen the bond of the club."
    m 5a "Isn't that right, [player]?"
    "Monika smiles warmly at me once again, but I can't help but feel it's a bit hollow."
    mc "Y-yeah, that sounds all right."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    hide sayori
    m 4a "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone, remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ahaha~"
    "I don't know why I felt a small chill from that."
    mc "Y-yeah..."
    show monika at thide zorder 1
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri and Natsuki clean up their food."
    show sayori 1a at t11 zorder 2
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s 4q "Yaay~"
    "With that, the two of us start to leave the clubroom."
    "However, as I walk past Monika to reach the door, I hear..."
    show monika 2q at t44
    m "Everything is different--just what's going on...?"
    show monika 2q at thide
    hide monika 
    "...I don't know what to make of it, so I try to push it out of my head for now."
    scene bg residential_day
    with wipeleft_scene
    "The whole way back, my thoughts begin to wander."
    "I know I said I felt like I'd have a chance meeting someone at the Literature Club."
    "But just who was it, though?"
    show sayori 1 at t41 zorder 2
    "Was it Sayori?"
    show natsuki 4 at t42 zorder 2
    "Natsuki?"
    show yuri 1 at t43 zorder 2
    "Yuri?"
    show monika 1 at t44 zorder 2
    "Or maybe it was even Monika."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "I don't know just yet..."
    show sayori 1b at t11
    s "Hey, [player]."
    mc "Hm? What is it, Sayori?"
    s 4a "I'm so glad you joined the Literature Club."
    s 4x "Ehehe~ I was planning on bringing you there, but I didn't have to."
    s 1c "It's almost like it was fate."
    mc "Haha, maybe."
    s 1g "But... sorry if Monika came off as a bit distant or weird today."
    s "She's not normally like that."
    s "Maybe she's sick."
    s 1h "She was coughing and kind of tired..."
    mc "Maybe."
    s 2c "I should check up on her tomorrow..."
    s "I really hope she's okay."
    mc "I do too, Sayori."
    "With that, we continue our walk in silence, my thoughts drifting again."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."
    stop music fadeout 3.0
    call monikaRoute_theFirstPoem
    return
    
#The First Poem: Writing the way into her heart.
label monikaRoute_theFirstPoem:
    scene bg bedroom with wipeleft_scene   
    mc "Ughhhhh..."
    "I seem to have come down with a serious case of writer's block."
    "I've been staring at the blank page in front of me for thirty minutes now."
    "Nothing's coming to mind at all."
    "I look around the room, trying to find a source of inspiration."
    "I see a book that I bought a few days ago on my shelf."
    "It was bought on a whim this past weekend."
    "Part of my motivation to go to the Literature Club."
    "Have a book to talk about, something like that."
    "I reach up and pull it from the shelf, reading the title."
    "Portrait of Markov."
    "I weigh it in my hands for a bit."
    "Even though this is the first time I've picked it up since, it has a familiar weight to it."
    "Almost like this book should have some special value to me."
    "But that kind of thinking is strange."
    "This weird feeling still hasn't gone away either."
    "Hmmm..."
    "Seeing it all before..."
    "...I guess I can try to write about that."
    "Now just to pick some words that go along with it..."
    call poem
    # call poem game above, technically doesn't do anything
    call monikaRoute_reachingOut
    return


#Reaching Out: She doesn't want to be alone anymore, no matter what she says.
label monikaRoute_reachingOut:
    scene bg club_day with wipeleft_scene  
    play music aNewDay fadein 3.0
    "I slide open the door to the Literature Club room."
    mc "Good afternoon."
    play sound fall
    "As soon as I say this, there's a loud crashing sound. Everyone looks over, finding Monika who tripped over a desk, catching herself."
    show monika 2h at t44
    m "..."
    "She quickly regains her composure and walks over to me."
    show monika 5 at t11 zorder 2
    m "Ah, hi again, [player]!"
    m 2l "Glad to see you... came back."
    "Monika pauses before nodding."
    m 5a "You didn't run away on us, hahaha~!"
    mc "Don't worry."
    mc "It might sound a little strange, but I always try to keep my word."
    m "Is that so?"
    m "Well, dependable people are always appreciated."
    show monika at thide zorder 1
    hide monika
    show yuri 1a at t32 zorder 2
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    mc "Well, trying new things is good, right?"
    y "Yes, I suppose..."
    show sayori 1c at t33 zorder 1
    s "I'm still surprised though, [player]."
    s "Last year you didn't even want to join any clubs."
    s "But then suddenly you came here, wanting to join."
    mc "Ah..."
    mc "I guess that's true."
    mc "I can't explain it very well."
    show natsuki 1c at t31 zorder 1
    n "You said yesterday that you wanted to broaden your horizons, what about that?"
    mc "I said that, sure, but..."
    mc "I dunno."
    mc "One day I was lying in bed and I guess I suddenly felt a need for literature?"
    mc "I had a weird dissatisfaction with anime and games, all of a sudden."
    mc "Then I saw the flier and everything sort of clicked."
    mc "I still like manga and anime, though."
    s 4x "Ehehe~"
    s "It's fine, [player]!"
    s "Besides, I was worried about you becoming a NEET if you didn't try a new club~"
    show natsuki 1j at t31
    show yuri 1m at t32
    "Everyone else has a small laugh at my expense over it."
    mc "Well, I guess I should teach you how to clean your room."
    mc "You did almost set your house on fire one time..."
    s 5b "Ehehe, let's not talk about that~"
    show yuri at f32 zorder 3
    y 1s "You two are really good friends, aren't you?"
    y "I might be a little jealous."
    show yuri at t32 zorder 2
    show sayori at f33 zorder 3
    s "How come? You and [player] can become good friends too!"
    y 4b "A-ah..."
    s 1a "I hope we can all get closer this year as well."
    s 1q "I really am happy here~"
    show sayori at t33 zorder 3
    s "Especially with [player] now in the club!"
    n 1d "You really are a bright ball of sunshine, huh?"
    s "Yep~"
    s 2x "Especially because of [player]~"
    mc "S-sayori--"
    "I raise my voice to interject, but I'm swiftly defeated by her smile."
    "Well... I guess as long as she's happy."
    show sayori at thide 
    show natsuki at thide
    hide sayori 
    hide natsuki
    show yuri at t11 zorder 2
    mc "Oh, right."
    "I reach into my bag and pull out the book from last night."
    show yuri 1e at t11 zorder 2
    "Yuri's eyes light up as soon as she sees it."
    mc "I picked it up a while ago on a whim, but..."
    mc "Do you know if it's any good?"
    y 1b "You shouldn't read it based on my own review, though."
    y "But..."
    y 1d "I did enjoy it."
    y "It does have a few horror themes in it, so it might not be to your liking if you don't like that sort of thing."
    y 4a "A-ah..."
    y 2m "Well, perhaps we could discuss what you think of it chapter by chapter."
    mc "I definitely will!"
    "I say it a little too enthusiastically and turn my head away."
    mc "And, ah, I'll make time to read it."
    y 1b "Y... you don't have to force yourself."
    "Yuri nods, as if to hammer in that fact."
    y 2c "If you force yourself to read it, you won't enjoy it as much."
    y "So if you want to read other things as well, that's fine."
    y "Like if you wanted to read manga..."
    show yuri 2c at t22 zorder 2
    show natsuki 1c at t21 zorder 1
    "At this, I see Natsuki's looking at us out of the corner of her eye."
    y 1b "Natsuki, you don't have to be afraid..."
    n 4e "I-I'm not afraid, hmph!"
    n 2q "But..."
    n "I would like to hear your opinion on Parfait Girls."
    n "It's hard to find people who would actually read manga, so..."
    mc "Ah..."
    n 2b "Yeah."
    n "There's a lot of people who think manga's still only for kids."
    mc "That's pretty dumb."
    n 1c "I know!"
    n "There's stories for everyone."
    n "And you're never too old for a particular type of storytelling."
    mc "Definitely."
    mc "Ah..."
    mc "Ahaha, I'll probably have to read from the beginning again."
    mc "I know it's my favorite series, but I haven't read it in a while, is all."
    n 2c "Hmm..."
    n 1a "Well, we can do the same thing as you and Yuri."
    n "Just read whatever you want, so if you read Parfait Girls, we can talk about it."
    mc "Sounds like a plan."
    show yuri at thide 
    show natsuki at thide 
    hide yuri 
    hide natsuki
    stop music fadeout 3.0
    scene bg class_day with wipeleft_scene
    "I turn around, finding Monika sitting alone at the front of the room."
    play music MonTheme fadein 3.0
    "Yuri and Sayori seem to have struck up a conversation."
    "And Natsuki went back into the closet." # not that was ever really in it
    mc "Hmmm..."
    "I go up to Monika and poke her on the shoulder."
    show monika 1g at h11
    m "A-ah!"
    show monika 1c at t11
    "She turns her head around and looks at me."
    m 3l "O-oh, it's you, [player]. Sorry, you gave me a bit of a scare."
    mc "Thinking hard about something?"
    m 1n "Yes..."
    "I see Monika glance over at the others."
    m 3b "Why don't you go talk with the others?"
    mc "I did, but you also seemed a little distant."
    mc "Sayori said yesterday you might be sick."
    mc "Are you sure you're feeling well?"
    m 3j "I'm fine, [player]."
    m 5a "But thanks for asking."
    m "You can go talk to the others, now."
    m "I'll be fine."
    "This girl seriously doesn't want me to talk to her, huh?"    
    mc "Alright..."
    mc "But, you know, Monika."
    mc "I'd like to be friends with you, too."
    m 1m "Ah..."
    "She gives another smile."
    m 3k "I'd like to be friends with you too, [player]."
    m 2n "Sorry if I come off as distant or anything like that."
    m "I just have a lot on my mind, recently."
    mc "Well, if you ever want someone to talk to..."
    "I try to give a cool smile back."
    mc "I mean, sometimes a guy's perspective on things might be useful, too."
    mc "So, um... yeah."
    "I stumble right at the end."
    "Monika looks at me before giggling."
    m 5a "Thanks, [player]."
    m "I'll keep it in mind."
    m "Hmm..."
    m 4b "Well, how about this?"
    m "What would you do if you felt like you had all the control you ever needed--"
    m 2p "--but then suddenly found it taken away from you?"
    "I pause, trying to think of the answer."
    mc "Well..."
    mc "I'd like to get control back."
    mc "Or at least I'd like to feel like I had it back."
    mc "But..."
    m 2c "But?"
    mc "If I actually was that powerless, I might just try to make the best of it."
    mc "I can't control everything, right?"
    mc "Sometimes all you can do is stick with things and hope they'll get better, I suppose."
    show monika 2o at t11
    "Monika looks a bit saddened at this answer."
    "She sighs and nods."
    m 2a "I guess that's true."
    "She gives me a small smile this time."
    "One that makes my heart ache rather than go aflutter to see it on her face."
    m 2q "Can't control everything, huh..."
    m 5a "Thanks, [player]."
    "Even if she says that, it still hurts to see her like that."
    "Monika must have something weighing down a lot on her."
    mc "Ah... well, thanks for asking me."
    mc "Um, that you know, trust me enough to ask something like that."
    mc "You must be dealing with something pretty heavy, huh..."
    m 2c "Sort of."
    mc "Well, um..."
    mc "I know I probably have no place to say this, but--"
    mc "--I'm sure you can share it with the other club members, too."
    mc "They're all here for you, too. I think they'd all be sad to know if something was crushing you like this."
    show monika 1d at t11
    "I see Monika blink a few times before nodding."
    m "Maybe."
    m 1q "But, sometimes you just know that some people might not be able to help."
    m "Though thanks for saying that, [player]."
    m 2b "I'm glad..."
    m "I'm glad that you think that of them."
    mc "Well, they're happy right now, right?"
    mc "They seem to be really happy being here as well, so..."
    mc "It just wouldn't be fair if the president couldn't find happiness at her own club, right?"
    m "Ha... yes."
    m 3b "Oh!"
    m 3k "Look at the time!"
    show monika 5a at h11
    "Monika jumps to her feet."
    call monikaRoute_sharingPoems1
    return

#Sharing Poems: Showcasing our reality together.
label monikaRoute_sharingPoems1:
    m 4b "Okay, everyone!"
    "Everyone looks up from their various activities."
    m "Did everyone write a poem last night?"
    mc "Y-yeah..."
    "My heart's racing again."
    "I can't believe I agreed to do something so embarrassing."
    "That feeling I had last night was good inspiration, but... I'm still pretty unskilled at writing."
    "There are mumbles of admission that go around the room, save for Sayori who triumphantly pulls her poem out from her bag."
    "It's wrinkled and looks like it was torn out of a spiral notebook."
    "Monika wrote hers in a composition notebook. I can see her pristine handwriting."
    "Natsuki and Yuri reluctantly comply as well, reaching into their bags."
    "I do the same as well."
    # gotta code this portion later
    $ chapter = 1
    $ poemsread = 0 # just do a reset in case
    call monikapoemresponse_start # this will call the poem thing
    
    call monikaRoute_poemPanic
    return


#Poem Panic: A choice that wasn't original made before.
label monikaRoute_poemPanic:
    scene bg club_day with dissolve_cg
    stop music fadeout 3.0
    play music aNewDay fadein 3.0
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "Though Monika seemed to be in real disbelief I wrote something like that."
    "I guess this is a literature club, though."
    "It's what I signed up for."
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "I look across the room, finding Yuri and Natsuki exchanging papers in tandem."
    "As they read each other's poem, I notice their expressions change."
    show natsuki at f22 zorder 3
    "Natsuki's eyebrows furrow in frustration."
    show yuri 2i at t21
    "Yuri smiles sadly."
    "I can already feel the rising tension in the air."
    "Natsuki's mouth moves ever so slightly."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2f "Eh?"
    y "Um... did you say something?"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "Oh, it's nothing."
    "Natsuki hands the poem back to Yuri with one hand."
    n "I guess you could say it's fancy."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "Ah... thanks."
    y "Um, yours is...cute?"
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3f "I-I know that!"
    y "I just... how would I put this..."
    y 3h "It seems very simple."
    show natsuki at f22 zorder 3
    show yuri at t21 zorder 2
    n 4c"Well, I don't like to write very complicated and obtuse metaphors."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3k "O-obtuse?"
    "The room suddenly becomes supercharged as the two begin to confront each other."
    show natsuki at f22 zorder 3
    show yuri at t21 zorder 2
    n "It was very roundabout, yeah."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "That's just my writing style."
    y "I won't be changing it anytime soon, unless of course I come across something particularly inspiring."
    y 2h "Which I haven't."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1o "Nn...!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "And [player] liked my poem too, you know."
    y "He even was impressed by it."
    stop music fadeout 1.0
    "Oh no."
    "I know exactly where this is going."
    play music t7
    n "Oh?"
    "Natsuki stands up, a smile forming on her face."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4y "I didn't realize you were so invested in trying to impress our new member, Yuri."
    y "E-eh?!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "That's not what I...!"
    show yuri at t21 zorder 4
    "What am I doing here too, standing around and watching this train wreck?"
    "But I can't get involved in it, though."
    "Then...!"
    #[Monika!]
    #music stops
    call updateconsole("remove_choice(\"poemPanic\")", "Choice(s) successfully removed.")
    call updateconsole("add_choice(\"poemPanic\",\"monika\")", "Choice(s) successfully added.")

    

    menu:
        "Then...!"
        "Monika!":
            $ consolehistory = []
            call updateconsole_clearall("", "")
            call updateconsolehistory("")
            hide chistory
            stop music
            show monika 1d at t41 zorder 4
            $ consolehistory = []
            call updateconsole_clearall("", "")
            call updateconsolehistory("")
            hide chistory
            call hideconsole
            m "E-eh?"
    
    


    "Everything stops for a second."
    "Probably as everyone realizes how loudly I yelled that."
    m "O-oh, right."
    m 2h "I could swear that wasn't..."
    show monika 1c at f11
    "I hear Monika mutter something before she walks over to the two of them."
    m 1g "Natsuki, Yuri."
    show natsuki 4u at t22 zorder 3
    show yuri 3o at t21 zorder 3
    "Both of them look away, clearly ashamed of the display."
    m 1b "I know you two are very pronounced about your styles, but there's no need to argue like this."
    m 2b "Talking about preferences is fine, but Natsuki, trying to imply something about Yuri is a low blow."
    m "That being said--"
    show yuri 3q at t21 zorder 3
    "Monika interrupts Yuri, who was about to speak."
    m 3b "Yuri, you shouldn't attempt to use [player]'s thoughts about your poem as a way to boost your credibility."
    m "I won't ask you two to apologize to each other, but remember that we're here to enjoy literature, not fight over our preferences."
    n 4w "...got it."
    y 3k "U... understood, Monika."
    m 5a "Well, anyway, back to what you were doing~"
    show monika at thide
    hide monika
    "With that, Monika turns around and starts walking back to her desk, shooting me a look."
    "It's definitely not a thankful look, that's for sure. Come on, I didn't do anything wrong... I think."
    y 2j "I-if you'll excuse me, I'm off to go make some tea."
    "With that, Yuri quickly excuses herself from the room."
    show yuri at lhide
    hide yuri 
    n 4g "Hmph."
    "It seems like I was looking in Natsuki's direction for too long, as she turns away from me."
    show natsuki 1r at t42 zorder 2
    show sayori 4q at l31 behind natsuki
    "Sayori moves in to talk with her, pulling her into a hug that Natsuki originally resists but eventually lets herself be comforted."
    "I hastily retreat back to my desk and await the end of the day."
    show natsuki at thide 
    show sayori at thide 
    hide natsuki 
    hide sayori 
    "About ten minutes later, Yuri comes back into the room."
    "She and Natsuki pass by each other without a word."
    "Deciding the best course of action is not to get involved, I simply stare out the window and watch the scene play out in the reflection."
    "Sayori whispers something to Natsuki, who gives another huff, but Sayori seems to be a little more insistent on whatever they're talking about."
    "With some more prodding, Natsuki is released from Sayori's hug and awkwardly shuffles towards Yuri."
    "I can't make out exactly what they're saying, but it doesn't seem like there's any tension anymore."
    "I look over at Monika as this is going on, who has a small smile on her face, maybe at seeing all of this, but it quickly vanishes after she closes her eyes and mumbles something to herself." # hinting that Monika is trying to not let everything get to her again
    "Huh..."
    "I turn away before Monika can catch me looking at her."
    s "[player]?"
    mc "Hm?"
    show sayori 1a at f11
    "I notice Sayori came over to me without me noticing."
    "Sayori smiles at me."
    s 1x "Good job~"
    mc "About what?"
    show sayori 1x at s11
    "Sayori leans down and whispers."
    s "Helping with, you know, what just happened."
    mc "O-oh. Well, it's, um, you know... instinct."
    mc "It sounded like I was about to get involved, so I panicked."
    s 2q "Ehehe~"
    s 2r "Well, I'm glad everyone stopped fighting."
    s 1c "Someone just had to speak up, is all."
    s "So I'm glad you did."
    mc "It's nothing."
    s "If you say so~"
    s "But it isn't nothing to me."
    s "I really love this club and everyone here~"
    show sayori at thide
    hide sayori 
    "With that, Sayori pulls away and flashes another grin before walking over to Monika."
    "I guess that's why Sayori's the vice president, huh?"
    "I probably called on Monika since she was the president, but Sayori definitely seems like the mood maker of the club."
    "If anything like this happens again, I can definitely call on her."
    #time passes effect
    scene bg club_day 
    show monika 4b at t11 zorder 2
    with wipeleft_scene
    play music aNewDay fadein 3.0
    m "Okay, everyone!"
    m "It's just about time for us to go home."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show sayori 4x at t31 zorder 2
    s "It was a lot of fun!"
    show sayori at thide behind yuri
    show yuri 1i at t31 zorder 2
    hide sayori
    y "Well, I'd say it was worth it."
    show yuri at thide behind natsuki
    show natsuki 4q at t31 zorder 2
    hide yuri
    n "It was alright. Mostly."
    show natsuki at thide zorder 1
    hide natsuki
    m 1a "[player]? How about you?"
    mc "...Yeah, I could say the same."
    mc "It was neat talking with everyone."
    m 1j "Great!"
    m 1a "In that case, let's do the same thing tomorrow."
    m "And maybe you learned something from everyone, too."
    m 3b "That way, your poems will turn out even better!"
    "Hmm..."
    show monika at thide zorder 1
    hide monika
    "Well, I did learn a little more about the kinds of poems everyone likes."
    "With any luck, that means I can at least do a better job impressing those I want to impress."
    "Other than Monika, anyway."
    "She seemed more bewildered about my poem than anything else."
    "I guess that somewhat impressed her? She couldn't believe that I had written it."
    "If I want to do that again, I'll probably do what I did before, then."
    show sayori 1x at t11 zorder 2
    s "[player]!"
    s "Ready to walk home?"
    mc "Sure, let's go."
    s 4q "Ehehe~"
    "Sayori beams at me."
    "It has been a while since Sayori and I have spent this much time together."
    "Though I can't say I'm not enjoying it."
    #cut to residential bg
    scene bg residential_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    mc "Sayori..."
    mc "About what happened earlier."
    s 1b "Eh? What about it?"
    mc "Natsuki and Yuri, does that happen often?"
    s 4j "No, no, no!"
    s "That's actually the first time I've seen them even act like that at all."
    s "They're usually so nice and accommodating."
    s "It might just be because this poem writing thing was more personal..."
    mc "I guess so."
    show sayori at s11
    s 1g "You don't hate them, do you?"
    mc "Of course not."
    mc "I just wanted your opinion."
    show sayori at t11 zorder 2
    s 1d "Phew..."
    s "You know, [player]..."
    s "It's nice that I get to spend time with you in the club."
    s 1x "But I think seeing you get along with everyone is what makes me the happiest."
    s "Even Monika seemed to be back to her normal self today!"
    "Monika, huh...?"
    "She did seem kind of distant the other day, but she seemed a lot friendlier today."
    "Much more fitting in the role of 'Club President'."
    "...Even if she was surprised to see me there."
    s "I think everyone really likes you, too!"
    mc "Hey, that's--"
    s 4q "Ehehe~"
    s "Every day is going to be so much fun~"
    mc "Geez..."
    "I hope so, too."
    "But something keeps itching at the back of my head."
    "It's probably nothing."
    "Still, though, I wonder if I'll be more than friends with any of them..."
    mc "I guess we'll just have to see about that, Sayori."
    show sayori at h11
    s 1x "Okay~"
    "I guess that means I'm writing a poem tonight."
    stop music fadeout 3.0
    call monikaRoute_theSecondPoem
    return

 #   time passing effect


#The Second Poem: My words, reaching out to you[i].
label monikaRoute_theSecondPoem:
    scene bg bedroom with wipeleft_scene
    "I sigh, looking up at the ceiling again."
    "It's been about an hour now and I'm still stuck."
    "What to even write about..."
    "I don't know. I'm drawing a serious blank."
    "My mind wanders back to what Monika said earlier today."
    "Unable to control things..."
    "When I think about those words, I can't help but resonate with them."
    "Not on the level of 'that's just how life is, there's always something out of your control.'"
    "But something greater than that."
    "I don't really know how to describe it."
    "It's sort of like..."
    "I can understand what she means."
    "Not being in control at all. Something like that."
    "...well, I guess I can write about that."
    "Not to specifically impress Monika or anything, but maybe I can let her know that I can understand what she's going through."
    "After all, she is way out of my league."
    "I might be able to impress her, but even I know that it's not going to mean she'll suddenly want to be close to me."
    "...well, probably not impress her, on second thought, considering her reaction to my poem."
    "Still, there's no shame in at least trying."
    "Now just to think of some words..."
    call poem
    # call poem game
    call monikaRoute_GraspingStraws
    return  

#Grasping Straws: Why doesn't she think it's real? Even being acquaintances is enough.
label monikaRoute_GraspingStraws:
    scene bg corridor with wipeleft_scene
    play music aNewDay fadein 3.0
    "Another day goes by, and it's time for the club meeting already."
    "I've gotten pretty comfortable here over the past few days."
    scene bg club_day
    show sayori 2x at t11
    with dissolve_cg
    s "Hi, [player]!"
    mc "Hey, Sayori."
    "It's the usual scene when I enter the clubroom."
    mc "You seem like you're in a good mood today."
    s 1q "Ehehe~"
    s "I'm just really happy that you're in the club, that's all."
    mc "I see..."
    mc "That's a pretty simple thing for you to be happy about."
    mc "But I guess it's always the simple things with you, anyway."
    #[Okay pretty much this scene is 100% the same for the most part, except for the Monika exclusive scene as detailed below]

    s 1d "Speaking of which..."
    s "I'm kinda hungry..."
    s "Will you come with me to buy a snack?"
    mc "No thanks."
    s 4h "Eh??"
    s "T-That's not like you at all!!"
    mc "I have my reasons."
    mc "Why don't we take a look at your purse, Sayori?"
    s 4l "E-Eh?"
    show sayori at s11
    s "Why that...all of a sudden?"
    mc "No reason, really."
    mc "I just wanted to look at it."
    s 1l "A-Ah..."
    show sayori at t11 zorder 2
    "Sayori nervously retrieves her coin purse."
    "She fumbles with the latch and gets it open."
    "Then, she turns it upside-down and lets its contents spill onto the desk."
    "Only two small coins fall out."
    s 5a "A-Ahaha..."
    mc "I knew it..."
    mc "I can see right through you, Sayori."
    s 5c "That's not fair!"
    s "How did you even know?"
    mc "It's simple."
    mc "If you had enough money in the first place, you would have bought a snack before coming to the clubroom."
    mc "So, either you're not hungry and wanted an excuse to take a walk..."
    mc "Or, you planned to conveniently forget that you spent all your money, so that I would lend you some!"
    mc "But there's one more thing..."
    mc "...You're always hungry!"
    mc "And so, that only leaves the one option!"
    s 4p "Uwaaa~!"
    s "I give up!"
    s "Don't make me feel guiltyyy!"
    mc "If you feel guilty, that means you deserve to feel guilty..."
    show yuri 1c at t33 zorder 2
    y "Ahaha."
    "Yuri suddenly giggles."
    show sayori 4g
    mc "Eh?"
    "I didn't notice that she was listening in."
    "Her face is in her book, as always."
    show yuri 3n at h33
    y "A-Ah!"
    y "I wasn't listening or anything--!"
    y 3o "It was just...something in my book..."
    show sayori at f32 zorder 3
    s 1h "Yuriiii..."
    s "Tell [player] to let me borrow some money..."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "That's--!"
    y "Don't get me involved like that, Sayori..."
    y "Besides..."
    y 1k "You should only buy what you can responsibly afford..."
    y "And frankly, after pulling a mischievous little stunt like that, your suffering is fair enough retribution."
    show sayori 1b
    mc "..."
    y 3n "Ah--!"
    y "Did I just..."
    y 4c "I-I didn't mean that!!"
    y "I got too absorbed into my book..."
    y "Uu..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1r "Ahaha!"
    s 3x "I really like when you speak your mind, Yuri..."
    s "It doesn't happen much, but it's a fun side of you!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3v "That's..."
    y "There's no way you could think that..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1x "You were right, though..."
    s "I did something bad and now I have to accept the revolution."
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y 3h "Retribution..."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1l "That!"
    show sayori at t32 zorder 2
    show yuri at f33 zorder 3
    y "Still, coming from you, Sayori..."
    y 1a "I guess there's a little devil inside all of us, isn't there?"
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe..."
    show sayori at t32 zorder 2
    mc "Don't let her fool you."
    mc "Sayori knows exactly what she's doing."
    mc "After all, she told you guys she was bringing me to the club before she even told me..."
    show sayori at f32 zorder 3
    s 1h "B-But...!"
    s "You wouldn't have come if it weren't for the cupcakes..."
    s "So I had to trick Natsuki into making them!"
    show sayori at t32 zorder 2
    mc "Come on, give me more credit than that, Sayori."
    show sayori at f32 zorder 3
    s 1l "Ehehe..."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p at hf32 zorder 3
    "{i}Pwap!{/i}"
    hide white
    s 4p "Kyaa--!"
    "Out of nowhere, something smacks Sayori in the face and tumbles onto the desk."
    s 4j "Ow..."
    s "What was--"
    s 4n "Eh??"
    s "A-A cookie!"
    "Sure enough, it's a giant cookie wrapped in plastic."
    "Sayori glances around."
    s 4m "I-Is this a miracle??"
    s "It's because I paid my restitution!"
    show sayori at t32 zorder 2
    mc "Retribution..."
    show sayori 4n
    show yuri at f33 zorder 3
    y 1u "Actually, that one almost worked..."
    show yuri at t33 zorder 2
    show natsuki 3z at f31 zorder 3
    n "Ahahaha!"
    n "I {i}was{/i} just gonna give it to you."
    n 3d "But then I heard you blab about the cupcakes."
    n "It was totally worth seeing your reaction, though. Ahaha!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 4m "N-Natsuki!"
    s "That's so nice of you!"
    s 4s "I'm so happy..."
    "Sayori hugs the cookie."
    show sayori at t32 zorder 2
    mc "Jeez, just eat it..."
    "Sayori rapidly tears open the wrapper and takes a big bite."
    show sayori at f32 zorder 3
    s 4q "Sho good..."
    show sayori at hf32 zorder 3
    s 4o "Mmf--!"
    "Sayori suddenly clasps her hands over her mouth."
    s 4p "I bit my tongue..."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3a "Ehehe."
    n "You're going through a lot over just one cookie."
    "Natsuki takes a bite of her own cookie."
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1c "Ah, yours looks really good too, Natsuki!"
    s "Can I try it?"
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4e "Jeez..."
    n "Beggars can't be choosers!"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1h "But yours is chocolate..."
    show sayori at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4c "Yeah, why do you think I gave you that one?"
    show natsuki at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "Fine..."
    s 1q "Still, I'm really happy that you shared this one with me."
    s "Ehehe~"
    show sayori at t21 zorder 2 behind natsuki
    "Sayori gets out of her seat and goes behind Natsuki, then wraps her arms around her."
    n 12c "Ah-- Jeez..."
    n "I get it, I get it."
    "Cookie still in hand, Natsuki reaches up to nudge Sayori off of her."
    show sayori 1n at h21
    s "...{i}Om.{/i}"
    "Sayori suddenly leans down and takes a bite out of Natsuki's cookie."
    n 1p "{i}H-Hey!!{/i}"
    n "Did you seriously just do that?!"
    s 1q "Uhuhuhu!"
    show sayori at lhide
    hide sayori
    "Mouth full, Sayori trots away to safety."
    show yuri 1c
    "Yuri and I laugh as well."
    show yuri 1a
    show natsuki at f31 zorder 3
    n 1w "Jeez! You're such a kid sometimes!"
    n 1h "Monika! Can you tell Sayori--"
    n 1c "--Eh?"
    "Natsuki glances around."
    "Monika isn't in the clubroom."
    n 4q "Ugh..."
    n "Where's Monika, anyway?"
    show natsuki at t31 zorder 2
    show yuri 2f at f33 zorder 3
    y "Good question..."
    y "Have any of you heard anything about her being late today?"
    show sayori 1b at f32 zorder 3
    show yuri at t33 zorder 2
    s "Not me..."
    show sayori at t32 zorder 2
    mc "Yeah, I haven't either."
    show yuri at f33 zorder 3
    y 2l "Hm..."
    y "That's a bit unusual."
    show yuri at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "I hope she's okay..."
    show sayori at t32 zorder 2
    show natsuki 3k at f31 zorder 3
    n "Of course she's okay."
    n "She probably just had something to do today."
    n 3t "She's pretty popular, after all..."
    show natsuki at t31 zorder 2
    show sayori 4m at f32 zorder 3
    s "Eh?"
    s "You don't think she..."
    s "She has a...!"
    show sayori at t32 zorder 2
    show yuri 1a at f33 zorder 3
    y "Ahaha. I wouldn't be surprised."
    y "She's probably more desirable than all of us combined."
    show yuri at t33 zorder 2
    show sayori 1r at f32 zorder 3
    s "Ehehe, that's true..."
    show sayori at t32 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Excuse me?!"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "Suddenly, the door swings open."
    show monika 1g at l41
    m "Sorry! I'm super sorry!"
    mc "Ah, there you are..."
    m "I didn't mean to be late..."
    m "I hope you guys weren't worried or anything!"
    show sayori 4n at f42 zorder 3
    s "Eh??"
    s "Monika chose the club over her boyfriend after all!"
    s "You're so strong-willed!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m 1l "B-Boyfriend...?"
    m "What on Earth are you talking about?"
    "Monika quizzically glances at me."
    show monika at t41 zorder 2
    mc "Ah, never mind that..."
    mc "What held you up, anyway?"
    show monika at f41 zorder 3
    m 1e "Ah..."
    m "Well, my last period today was study hall."
    m "To be honest, I kind of just lost track of time..."
    m "Ahaha..."
    show monika at t41 zorder 2
    show natsuki 2c at f43 zorder 3
    n "That makes no sense, though."
    n "You would have heard the bell ring, at least."
    show natsuki at t43 zorder 2
    show monika at f41 zorder 3
    m 1m "I must not have heard it, since I was practicing piano..."
    show monika at t41 zorder 2
    show yuri 1e at f44 zorder 3
    y "Piano...?"
    y "I wasn't aware you played music as well, Monika."
    show yuri at t44 zorder 2
    show monika at f41 zorder 3
    m 1l "Ah, I don't, really...!"
    m "I kind of just started recently."
    m 1m "I've always wanted to learn piano."
    show monika at t41 zorder 2
    show sayori 4x at f42 zorder 3
    s "That's so cool!"
    s "You should play something for us, Monika!"
    show sayori at t42 zorder 2
    show monika at f41 zorder 3
    m "That's..."
    "Monika looks at me."
    m 1a "Maybe once I get a little bit better, I will."
    show monika at t41 zorder 2
    show sayori at f42 zorder 3
    s 4q "Yay~!"
    show sayori at t42 zorder 2
    mc "That sounds cool."
    mc "I'd also look forward to it."
    show monika at f41 zorder 3
    m 1b "Is that so?"
    m "In that case..."
    m "I won't let you down, [player]."
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show monika 5 at t11 zorder 2
    hide sayori
    hide natsuki
    hide yuri
    "Monika smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m 1a "Ahaha, don't worry."

    m "I've been practicing a whole lot recently."
    m "And I'd really love the chance to share once I'm ready."
    mc "I see..."
    mc "In that case, best of luck."
    m 1j "Thanks~!"
    m 1a "So, I didn't miss anything, did I?"
    mc "Not...not really."
    stop music fadeout 3.0
    show monika at thide zorder 1
    hide monika
    "I choose to leave out Sayori's mischievous escapade."
    "I'm sure Natsuki will end up complaining to her, anyway."

    # end copy paste
    # Monika exclusive lock scene
   
    play music MonTheme fadein 3.0
    "I look around the room as everyone settles down."
    "It's strange. Monika isn't talking with Sayori like last time."
    "Sayori seems to be preoccupied with Natsuki, the two of them talking about food, and Yuri is reading her book."
    scene bg class_day with wipeleft_scene
    "I don't want to disturb Yuri, so I turn my attention towards Monika, who is by the front of the room. She's sitting alone, notebook open and pen in hand, but seems to be perfectly still."
    "She doesn't make a single movement as I walk up to her."
    mc "Writer's block?"
    show monika 1c at h11
    "Monika nearly jumps from her seat, her chair suddenly making a loud noise as she scoots away before she turns around."
    show monika at t11
    m 3k "Oh, it's just you, [player]."
    mc "Sorry for scaring you."
    m "No, it's fine."
    mc "You seemed pretty deep in thought about something, though."
    mc "Was it what you asked me about yesterday?"
    m 1m "I suppose."
    m 1c "..."
    "Monika gives another glance over me."
    mc "Um, do I still have ketchup on my face?"
    mc "I knew I should've looked for a napkin..."
    "I quickly wipe my mouth, with Monika giggling."
    m 2k "No, it's not that, [player]."
    m "It's..."
    show monika 2q at t11
    "She closes her eyes and sighs."
    m 2r "It's difficult to put into words."
    "I try to think back on Monika's words from before."
    "Having the power to choose things, but then it being taken from you."
    "I still don't know what exactly Monika is going through, but it sounds rough."
    mc "I see."
    "I sit down at the desk next to her."
    mc "Um, well I did say last time that you could talk to the other club members."
    mc "But that was only yesterday."
    m 1q "Mhm."
    "I guess it's hard to suddenly change your mind all of a sudden."
    "Even if you are friends."
    m 1c "Well, I appreciate you trying to talk to me."
    mc "It's no good just to keep everything to yourself."
    "It feels like Monika keeps trying to push me away, though."
    m 3b "Though, you should probably go talk with the other girls."
    m "Don't be held back by me."
    m 5a "I'm sure you'll be a lot happier than if you stick around just listening to me drone on about things."
    "Monika..."
    "This is actually kind of sad, really."
    "She's the club president, so I find it kind of hard that no one else is really seeing to her."
    "Especially since Sayori's usually talking to her."
    "It seemed so obvious, today."
    "I guess Sayori noticed it as well, but..."
    "When I talk to Monika, it feels like there's something more. It's not something that any high school girl might go through."
    "It feels sort of... more philosophical in nature? Or something spiritual? I can't put a word to it."
    mc "Well..."
    mc "I mean, you're a club member, too."
    mc "It just wouldn't be right to leave you out of it."
    mc "Even if I became friends with the other members, I'd like to be friends with you, too."
    m 3k "You're so sweet, [player]."
    m 1l "But truthfully speaking, this is something only I can deal with."
    m "So don't worry too much about me."
    m 3b "Besides, you can't be friends with the others if you're only thinking about me~"
    mc "I... I guess so."
    mc "But... still, I can't help but be concerned."
    m 1b "I get it. Though I want you to get along with everyone, too."
    m "Don't worry. I'll talk with you, but make sure you get friendly with everyone else~"
    mc "Y-yeah."
    m 4b "Oh, but look at the time!"
    call monikaRoute_sharingPoems2
    return

#Sharing Poems, Part Two: Showing our fragility together.
label monikaRoute_sharingPoems2:
    m "Okay, everyone!"
    m "It's time to share poems again!"
    "Everyone quietly gets out their poems, myself included."
    #"Who should I share my poem with first today...?"
    $ chapter = 2
    $ poemsread = 0

    #Use everyone's neutral poem responses
    call monikapoemresponse_start
 
    #The introduction of the idea of reading Poetry at the Festival is the same as usual. Resume at the walking home scene.
    # gonna have to copy paste I guess lol
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music aNewDay
    m "Okay, everyone!"
    m "We're all done reading each other's poems, right?"
    m "I have something extra planned today, so if everyone could come sit at the front of the room..."
    show natsuki 3c at f31 zorder 3
    n "Is this about the festival?"
    show natsuki at t31 zorder 2
    show monika 1j at f32 zorder 3
    m "Well, sort of~"
    show monika 1a at t32 zorder 2
    show natsuki 1m at f31 zorder 3
    n "Ugh. Do we really have to do something for the festival?"
    n "It's not like we can put together anything good in just a few days."
    n "We'll just end up embarrassing ourselves instead of getting any new members."
    show yuri 2g at f33 zorder 3
    show natsuki at t31 zorder 2
    y "That's a concern of mine as well."
    y "I don't really do well with last-minute preparations..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1b "Don't worry so much!"
    m "We're going to keep it simple, okay?"
    m 1a "We won't need much more than a few decorations."
    m "Sayori has been working on posters, and I've designed some pamphlets we can give out during the event."
    show monika at t32 zorder 2
    show natsuki 3c at f31 zorder 3
    n "Okay, that's great and all..."
    n "But that doesn't tell us what we're actually going to be doing for the event."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1d "Ah, sorry! I thought you heard about it already."
    m 1b "We're going to be performing!"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3h "Performing?"
    show natsuki at t31 zorder 2
    show yuri at f33 zorder 3
    y 3n "P..."
    y 3o "Um, Monika..."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m 1k "Yeah! We're going to be having a poetry performance."
    m 1b "Each of us are going to choose a poem to recite during the event."
    m "But the cool part is, we're also going to let anyone else come up and recite poems too!"
    m 1a "Sayori's putting it on all the posters in case anyone wants to prepare ahead of time."
    show yuri at t44 zorder 2
    show monika at t43 zorder 2
    show natsuki at t42 zorder 2
    show sayori 4q at l41
    s "Ehehe~"
    "Sayori, who's been coloring a poster, holds it up for us to see."
    show natsuki 4w at f42 zorder 3
    n "Are you kidding me, Monika?"
    n "You didn't...you didn't already start putting those posters up, did you?"
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1d "Eh? Well, I did..."
    m "Do you really think it's that bad of an idea...?"
    show monika at t43 zorder 2
    show natsuki 1s at f42 zorder 3
    n "Well, no."
    n "It's not a bad idea."
    n 1w "But I didn't sign up for this, you know!"
    n 1x "There is {i}no{/i} way I'm going to be performing in front of a group of people like that!"
    show natsuki at t42 zorder 2
    show yuri at f44 zorder 3
    y 3r "I...I agree with Natsuki!"
    y 3w "I could never...in my life...do something like that..."
    "Imagining it, Yuri shakes her head in fear."
    show yuri at t44 zorder 2
    show sayori 1g at f41 zorder 3
    s "Guys..."
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 1g "No, Sayori..."
    m "I understand where they're coming from."
    m "Remember that Natsuki and Yuri have never shared their poems with anyone until just a couple days ago..."
    m "It's a lot to ask for them to recite their poems out loud to a whole room full of people."
    m 1r "I guess I kind of overlooked that."
    m "So, I'm sorry."
    show monika at t43 zorder 2
    show natsuki 5g at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show monika at f43 zorder 3
    m 1i "...But!"
    m "I still think we should give it our best!"
    m 1d "We're the only ones responsible for the fate of this club."
    m "If we start the event and each put on a good performance..."
    m 3a "Then it will inspire others to do the same!"
    m "And the more people who perform, the better we'll be able to show everyone what literature is all about!"
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Yeah!"
    s 1x "It's about expressing your feelings..."
    s "Being intimate with yourself..."
    s "Finding new horizons..."
    s "And having fun!"
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m 4b "That's right!"
    m "And it's those reasons that we're all in this club today."
    m 4e "Don't you want to share that with others?"
    m "To inspire them to find the same feelings that brought you here in the first place?"
    m 1e "I know you do."
    m "I know we all do."
    m 1b "And if all it takes is standing in front of the room for two minutes and reciting a poem..."
    m "...Then I know you can do it!"
    show monika 1a at t43 zorder 2
    show natsuki 5s at f42 zorder 3
    n "..."
    show natsuki at t42 zorder 2
    show yuri 4b at f44 zorder 3
    y "..."
    show yuri at t44 zorder 2
    show sayori 1g
    "Natsuki and Yuri remain silent."
    "Sayori looks worried."
    "I guess that leaves me no choice..."
    mc "I agree..."
    mc "I don't think it's too much to ask."
    mc "I think that Sayori and Monika have been trying really hard to get new members."
    mc "The least we can do is help them out a little bit."
    show natsuki at f42 zorder 3
    n 5h "Well...maybe, but..."
    n "..."
    "It looks like Natsuki doesn't have any arguments left."
    n "Uu..."
    n 1q "...Okay, fine!"
    n "I guess I'll just have to get it over with."
    show natsuki at t42 zorder 2
    show sayori at f41 zorder 3
    s 4r "Alright~!"
    show sayori 4a at t41 zorder 2
    show monika at f43 zorder 3
    m 1e "Phew..."
    m "Thanks, Natsuki."
    m "What about you, Yuri...?"
    show monika at t43 zorder 2
    show yuri at f44 zorder 3
    y "..."
    "Yuri dejectedly glances around at everyone else's expectant faces."
    y "Sigh..."
    y "I-I guess I don't really have a choice..."
    show yuri at t44 zorder 2
    show sayori at f41 zorder 3
    s 4r "Ahaha! That's everyone!"
    s "You're the best, Yuri~"
    show sayori 4a at t41 zorder 2
    show yuri at f44 zorder 3
    y "This club is seriously going to be the death of me..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 1l "Oh gosh..."
    m 1n "You'll be fine, Yuri."
    m "But anyway..."
    m 1b "Let's move onto the main event!"
    m "I want each of you to choose a poem of yours."
    m "We're going to practice reciting them in front of each other."
    show monika 1a at t43 zorder 2
    show natsuki at f42 zorder 3
    n 1p "N-N-No way!!"
    show natsuki at t42 zorder 2
    show yuri 3n at f44 zorder 3
    y "Monika...!"
    y "This is too sudden...!"
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Well, if you can't recite your poem in front of the club, how do you expect to do it in front of strangers?"
    show monika at t43 zorder 2
    show yuri 4c at f44 zorder 3
    show natsuki 1o
    y "Oh no..."
    show yuri at t44 zorder 2
    show monika at f43 zorder 3
    m 2a "Don't worry."
    m "I'll start off to help everyone feel a little more comfortable."
    show monika at t43 zorder 2
    show sayori 1r at f41 zorder 3
    s "Can I go next??"
    show sayori at t41 zorder 2
    show monika at f43 zorder 3
    m "Ahaha. Of course."
    m 2d "Now, let's see..."
    "Monika flips through her notebook to the specific poem she has in mind for herself."
    "She then stands behind the podium."
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide sayori
    hide natsuki
    hide yuri
    m 1a "The title of this poem is {i}The Way They Fly{/i}."
    m 1r "Ahem..."
    show monika 1a
    "Monika begins reciting her poem."
    "Her clear, confident voice fills the room."
    "More than that, her inflection is pristine."
    "She knows exactly how to apply emotion behind each line she recites, bringing the words to life."
    "Is this something she's done before, or is she simply a natural?"
    "I glance around me."
    "Everyone has their eyes on Monika."
    "Sayori looks amazed."
    "Yuri has an intense expression on her face that I don't understand."
    show monika 1j
    "Finally, Monika finishes the recitation."
    "The four of us applaud."
    "Monika takes a breath and smiles."
    show monika 1a
    show sayori 4m at f33 zorder 3
    s "That...that was so good, Monika!"
    show sayori at t33 zorder 2
    show monika at f32 zorder 3
    m 1j "Ahaha, thank you very much."
    m 1a "I was just hoping to set a good example."
    m "Are you ready to go next, Sayori?"
    show monika at t32 zorder 2
    show yuri 2r at l31
    y "I...I'll go next!!"
    show sayori at h33
    s 1n "Uwah! Yuri's fired up all of a sudden!"
    "Yuri clutches a sheet of paper between her hands and stands up."
    "Keeping her head down, she walks quickly over to the podium."
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at t11 zorder 2
    hide monika
    hide sayori
    y 2v "This poem is called--!"
    "Yuri anxiously glances at each of us."
    s "You can do it, Yuri..."
    y "It...It's called...{i}Afterimage of a Crimson Eye{/i}."
    "Yuri's voice shakes as she starts reading the poem."
    "Just a moment ago, she practically refused to do this."
    "Why is she suddenly putting in so much effort?"
    show yuri 2l
    "As Yuri gets past the first couple of lines, her voice changes."
    "It's almost like what happens when Yuri gets absorbed into her books."
    "Her quivering words transform into the sharp syllables of a fierce and confident woman."
    "The poem is full of twists and turns in its structure that she enunciates with perfect timing."
    "This must be a rare glimpse into the whirling fire Yuri keeps concealed inside her head...!"
    show yuri 2t
    "Suddenly, she's finished."
    "Everyone is stunned."
    "Yuri snaps back into reality and glances around her, as if she bewildered even herself."
    y 3o "I..."
    "...It's up to me to save this situation."
    "I'm the first to start applauding."
    "Everyone joins me afterward, and we give Yuri the recognition she deserves."
    "It's not that we didn't want to applaud for her."
    "But we were caught so off-guard that we must have forgotten."
    "As we applaud, Yuri holds the poem to her chest and rushes back into her seat."
    show yuri at lhide
    hide yuri
    show monika 1a at t11 zorder 2
    m "Yuri, that was really good."
    m "Thank you for sharing."
    y "..."
    "Looks like Yuri is down for the count..."
    show sayori 1q at t31 zorder 2
    s "Okaay~"
    s "I guess I'm next, then!"
    "Sayori hops out of her chair and cheerfully walks to the podium."
    show sayori at t11 zorder 2
    show monika at thide zorder 1
    hide monika
    s 1x "This one's called...{i}My Meadow{/i}."
    s "Ah..."
    s 1s "...Ahaha!"
    s 4s "Sorry, I giggled..."
    s 4q "Ehehe..."
    mc "Sayori..."
    s 1l "It's a lot harder than I thought!"
    s "How did you guys do it so easily?"
    show monika 3a at t31 zorder 2
    show sayori 1b
    m "Ah..."
    m "Try not to think of it like you're reciting to other people."
    m "Imagine you're reciting it to yourself, like in front of a mirror, or in your own head."
    m "It's your poem, so it'll come out the best that way."
    show sayori 1i
    s "I see, I see..."
    s "Okay, then..."
    show monika at thide zorder 1
    hide monika
    show sayori 1c
    "Sayori begins her poem."
    "Somehow, it feels like her soft voice was made as a perfect match."
    "The poem isn't aimlessly cheery like Sayori is."
    "It's serene and bittersweet."
    "If I were to read this on paper, I probably wouldn't think much of it..."
    "But hearing it come from Sayori's voice almost gives it a whole new meaning."
    "Maybe this is what Sayori meant when she said she likes my poems."
    "It's like I get to reach more deeply into someone I thought I knew through and through."
    "Sayori finishes, and we applaud."
    s 3q "I did it~!"
    mc "Good job, Sayori."
    s "Ehehe, even [player] liked it."
    s "I guess that's a good sign~"
    mc "What does that even mean...?"
    show monika 2b at f31 zorder 3
    m "It came out nicely, Sayori."
    m "The atmosphere of the poem fits you really nicely."
    m "But it might be that other poems wouldn't work quite as well with that kind of delivery..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1g "Eh? I don't really understand..."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "In other words, I've seen poems of yours where that sort of gentle delivery wouldn't work as well."
    m "They might need a little more force behind them, depending on what you're reading..."
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1x "Oh, I know what you mean!"
    s "That's...well, I've been practicing that kind of thing..."
    s 5 "It's just embarrassing to do in front of everyone..."
    s "Ehehe..."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 4a "Then next time, I'm going to make you pick a poem that challenges you a little more."
    m "We don't have much time before the festival, you know?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Okaaaaay."
    show sayori at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Now, who's next...?"
    m "Natsuki?"
    show natsuki 5s at f33 zorder 3
    show monika at t31 zorder 2
    n "Hmph."
    n "Don't make me go before [player]."
    n "It's not like I can compare to you guys, anyway..."
    n "Might as well let [player] lower everyone's standards a little before I have to do it."
    show natsuki at t33 zorder 2
    show sayori at f32 zorder 3
    s 1g "Natsuki..."
    show sayori at t32 zorder 2
    mc "It's fine, it's fine."
    mc "I might as well get it over with."
    mc "But it's not like I have much of a selection of what to read..."
    mc "I'll just have to go with what I wrote for today."
    "I stand up and step in front of the podium."
    show natsuki 2c at t44 zorder 2
    show sayori 1a at t43 zorder 2
    show monika 1a at t42 zorder 2
    show yuri 1e at t41 zorder 2
    "Everyone has their eyes on me, making me feel terribly awkward."
    "I recite my poem."
    "Since I'm not exactly confident in my own writing, it's hard to put energy into it."
    "Despite that, once I finish, I receive applause anyway."
    mc "Sorry I'm not really as good as everyone else..."
    show monika at f42 zorder 3
    m 1a "Don't worry about it so much."
    m "I think it's less about your abilities, and more about your lack of confidence in your writing."
    m "That's something that'll improve over time, though."
    show monika at t42 zorder 2
    mc "Yeah... Maybe."
    show monika at f42 zorder 3
    m 1j "Alright, then!"
    m 1a "That just leaves you, Natsuki."
    show monika at t42 zorder 2
    show natsuki at f44 zorder 3
    n 2g "Yeah, yeah."
    n "I'm going."
    "Natsuki begrudgingly gets out of her seat and makes her way to the podium."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at t11 zorder 2
    hide sayori
    hide monika
    hide yuri
    n 2c "The poem is called..."
    n 2q "It's called..."
    n 1x "W-Why are you all looking at me?!"
    m "Because you're presenting..."
    n 2x "Hmph..."
    n 2h "Anyway...the poem is called {i}Jump{/i}."
    "Natsuki takes a breath."
    show natsuki 2c
    "Once she starts reciting the poem, her sour attitude disappears a little."
    "While she's still a little unenthused, her poem has a rhythm and rhyme to it."
    "It's Natsuki's trademark style, and it works surprisingly well when spoken aloud."
    "The words feel like they bounce up and down, as if giving life to the poem."
    show natsuki 2s
    "Natsuki finishes, and everyone applauds."
    "She huffs back to her seat."
    show monika 2a at f31 zorder 3
    m "That wasn't so bad, was it?"
    show monika at t31 zorder 2
    show natsuki 5w at f32 zorder 3
    n "Easy for you to say..."
    n "You'd better not make me do that again."
    show natsuki at t32 zorder 2
    show monika 1d at f31 zorder 3
    m "Ah, well..."
    m "Do you at least feel prepared enough to recite a poem in front of other people?"
    show monika at t31 zorder 2
    show natsuki 2c at f32 zorder 3
    n "I mean, doing it in front of other people will be way easier!"
    n "I can put on whatever face I want for other people."
    n 2q "But when it's just my friends..."
    n "It's just...embarrassing."
    show natsuki at t32 zorder 2
    show sayori 1b at f33 zorder 3
    s "That's a surprise, Natsuki..."
    s "I think it would be the other way around for me."
    show sayori at t33 zorder 2
    show natsuki at f32 zorder 3
    n "Well, that's just how it is, so..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Well, I guess in that case..."
    m "You won't have much to worry about for the festival."
    m 2b "That said, I want to thank everyone for coming through."
    m "It might be hard, but I hope that you all have an idea of what it's like now."
    m 4b "Make sure you pick a poem and get enough practice before the festival, okay?"
    m "I'll be making pamphlets, so let me know ahead of time what you'll be reciting."
    show monika at t31 zorder 2
    mc "Jeez..."
    mc "I should probably find some other poem to recite instead."
    show monika at f31 zorder 3
    m 1j "That's fine, too!"
    m 1a "It doesn't have to be your own."
    m "I'm already pleasantly surprised that you're putting in all this effort for the club."
    m 5 "It makes me really happy."
    show monika at t31 zorder 2
    mc "Ah... Yeah, no problem..."
    play music aNewDay fadeout 1.0
    show monika at t11 zorder 2
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide natsuki
    m 4b "Okay, everyone!"
    m "I think that's about it for today."
    m "I know the festival is coming up, but let's try to write poems for tomorrow, as well."
    m "It's been working out really nicely so far, so I'd like to continue that."
    m "As for the festival, we'll finish planning tomorrow, and then we'll have the weekend to prepare."
    m "Monday's the big day!"
    show sayori 4r at t31 zorder 2
    s "I can't wait~!"
    show yuri 4b at t33 zorder 2
    y "I can do this... I can do this..."
    mc "Alright--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "I stand up."
    "There's no way I'll be able to find the same enthusiasm as Sayori and Monika, but I'll do my best to get through it."
    "If it's for the sake of the club..."
    "And impressing Monika..."
    "Then I'll have to do my best."
    show sayori 1a at t32 zorder 2

    # end copy paste
    call monikaRoute_theLongWalkHome
    return

#The Long Walk Home: I get the feeling it wasn't supposed to go like this. (Sayori's personality changed to be more like her post-route one)
label monikaRoute_theLongWalkHome:
    mc "Ready to go, Sayori?"
    show sayori at h32
    s 1x "Yep!"
    show natsuki 2d at f33 zorder 3
    n "Look at you two, always going home together like that."
    show monika 5 at f31 zorder 3
    show natsuki at t33 zorder 2
    m "It's kind of adorable, isn't it?"
    show monika at t31 zorder 2
    show sayori at f32 zorder 3
    s 1q "Ehehe~"
    show sayori at t32 zorder 2
    mc "Geez, guys..."
    mc "Don't make such a big deal out of it."
    show natsuki at t44 zorder 2
    show sayori at t43 zorder 2
    show monika at t42 zorder 2
    show yuri 1u at f41 zorder 3
    y "It must be a little nice, though..."
    show yuri at t41 zorder 2
    mc "Well..."
    mc "Ah..."
    "How am I supposed to respond to that?"
    show sayori at f43 zorder 3
    s "It's okay, [player], you don't have to say it."
    s "But you know, maybe [player] should try walking someone else home for on--"
    mc "L-let's go, Sayori!"
    "I hurriedly leave the clubroom before Sayori can finish that statement."
    scene bg residential_day with wipeleft_scene
    #transition
    "I walk home with Sayori once more."
    "Even though it's only been a few days, a lot of things have already changed."
    "But today, Sayori is a little more upbeat than usual."
    mc "You seem kind of happy."
    mc "Moreso than always."
    show sayori 1a at t11
    s "Hmm~"
    mc "Something on your mind?"
    s "Hmhmhm~"
    "I don't like that humming nor the smile on Sayori's face."
    s 1x "I was just thinking about something from earlier."
    "Oh no."
    s 1a "I like how we get to walk home together, but..."
    s "So, let's say that one day, Monika asked to walk home with you..."
    mc "Huh?!"
    s 1q "What would you do~?"
    mc "W-what kind of question is that?!"
    mc "You're really putting me on the spot here..."
    s "Ehehe..."
    "Well..."
    menu:
        "I would still walk home with Sayori.":
            #[I would walk home with Sayori]
            mc "Sayori, I don't think I'd ditch you for Monika."
            s 1e "Eh?!"
            s 5c "You seem seriously head over heels for her, though."
            mc "T-that's just how guys normally react around her, though."
            mc "Besides!"
            mc "You always seem to really like going home together."
            mc "I wouldn't ruin that for you."
            s 2q "Hmm, okay~"
            "Even though Sayori's smiling, I can't help but feel like she's disappointed in me."
            mc "Anyway, let's talk about something less... er... well, I guess we can talk about the festival."
            mc "It's going to be lots of fun, right?"
            s 4x "Yeah!"
            s "You better not just go around eating food and then go home like you did last year..."
            mc "I won't, I promise."
            "For the rest of the trip home, Sayori and I make some small talk about the festival and what else we're looking forward to at it."
        "I would walk home with Monika.":
            #[I would walk home with Monika]
            mc "Walking home with Monika, huh...?"
            "Why does the thought of that make my heart jump?"
            mc "I mean..."
            mc "We didn't get to talk much last year, so it might be nice to talk with her..."
            s 2x "Hehehe."
            s "She's so pretty, too."
            mc "That has nothing to do with this, though!"
            show sayori 2x at h11
            s "Ahaha! You admitted it~"
            mc "Geez..."
            mc "Whatever. It's not like there's any point in speculating something that's never going to happen."
            show sayori 1c at t11
            s "Well, maybe."
            s "But since it came up earlier, I couldn't help but think about it."
            s 4q "Just don't forget about me~"
            mc "Of course not, dummy."
            mc "I'd definitely turn her down if she asked to do that every day."
            s "I see~"
            mc "But whatever. It's not like it's going to happen."
            mc "Let's talk about something else, now."
            s 1c "Okay. What do you want to talk about?"
            "For the rest of the trip home, Sayori and I make some small talk about the festival and what we're looking forward to at it."
            "But the thought is still on my mind."
            "Monika asking to walk home with me..."

    #Scene transition to MC's room

    "But either way, I still have a poem to write tonight, huh..."

    call poem

    call monikaRoute_theThirdPoem
    return

#The Third Poem: Passion overflowing, I know she should read these words. // time to cram a bunch of Sayori lines in, wheeeee
label monikaRoute_theThirdPoem:
    scene bg club_day with dissolve_scene_half
    play music aNewDay
    show monika 1g at l31   
    m "Aw, man..."
    m "I'm the last one here again!"
    mc "It's okay, I got here only a few minutes ago."
    show sayori 1b at f32
    s "Aww, you're just being nice, [player]."
    show sayori at thide 
    hide sayori 
    mc "It's true, though."
    show yuri 1f at f32 zorder 3
    y "Were you practicing piano again?"
    "I thank Yuri for shifting the conversation along before Sayori can say anything else."
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 1l "Yeah..."
    m "Ahaha..."
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1m "You must have a lot of determination."
    y "Starting this club and now picking up piano..."
    show yuri 1a at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Well, maybe not determination..."
    m "But I guess passion."
    m "Remember, the club wouldn't be here if it wasn't for all of you."
    m 1b "I'm also super happy that you're all willing to help out for the festival, too!"
    show yuri at thide
    hide yuri 
    show sayori 1x at f32
    s "It's gonna be great!"
    "Sayori hops up and down like a dog waiting for a treat."
    hide sayori
    show natsuki 1z at f33 zorder 3
    show monika at t31 zorder 2
    n "Mhm. I can't wait!"
    show natsuki at t33 zorder 2
    show monika at f31 zorder 3
    m 1d "Weren't you complaining about it just yesterday, Natsuki?"
    show monika at t31 zorder 2
    show natsuki 2a at f33 zorder 3
    n "Well, yeah."
    n "Just not {i}our{/i} part of the festival."
    n 4l "But it's a whole day where we get to play and eat all kinds of delicious food!"
    mc "You sound like a bit like Sayori all of a sudden..."
    hide natsuki 
    show sayori 1x at f32 zorder 3
    s "Hey!"
    mc "It's true, though!"
    hide sayori
    show natsuki at f33 zorder 3
    n 4a "Monika! Do they usually have fried squid?" # you know looking back on it, this line kind of implies Natsuki is a first year
    show monika at thide 
    show natsuki at thide 
    hide monika 
    hide natsuki 
    "Monika and Natsuki talk about food in the background as Sayori quickly hammers into me about her eating."
    show sayori 5c at f11 zorder 3
    s "Are you saying I eat too much, [player]?"
    "A landmine filled question, that's for sure."
    mc "All I'm saying is that you should watch your wallet."
    mc "You tried to sucker me into buying something from the vending machine the other day."
    mc "It only makes sense that I should worry about whether or not you're going to spend too much at the festival."
    s 5d "Mghm..."
    "Phew. Managed to dodge that bullet."
    s 1a "Hmm, okay~"
    s 2x "That means you'll walk with me around the festival to make sure I don't spend too much, right, [player]?" # note: generally this is kind of the equivalent of asking someone on a date; particularly in VNs/LNs where culture festivals are held in a story. Walking around them together is seen as a definite couple/ship tease moment
    stop music # record scratch
    show natsuki 2c at t44 zorder 2
    show monika 3d at t43 zorder 2
    show yuri 2e at t41 zorder 2
    "The conversation between Monika and Natsuki grinds to an immediate halt and even Yuri looks up from her book."
    "Great."
    "I dodged a bullet only to face a firing squad."
    mc "Um..."
    mc "Well, I haven't made any plans for the festival, so maybe."
    show monika 3d at f43 zorder 2
    "I can feel my eyes drift slightly over to Monika, but I force myself to keep eye contact with Sayori."
    show monika 3d at f43 zorder 2
    show sayori 1a at f11 zorder 3
    "Unfortunately, with the very, very visible smile on her face, I'm sure she caught me."
    play music EarlyBird fadein 3.0
    s "Okaaaay~"
    s "That's fine with me."
    s "Just don't wander around the festival alone, okay?"
    mc "Y... yeah, will do, Sayori."
    mc "Wh... what's everyone looking at?!"
    y 2o "S-sorry."
    show yuri at thide
    show sayori at thide 
    hide yuri 
    hide sayori
    "Yuri quickly turns back to her book, with Sayori coming over to talk to her."
    show monika at thide 
    show natsuki at thide 
    hide monika 
    hide natsuki 
    "Monika and Natsuki resume their conversation, though it seems a bit forced at first."
    "Phew."
    "Geez, Sayori, asking stupid questions like that..."
    "Whatever, I guess everything's fine."
    show black with close_eyes
    stop music fadeout 3.0
    "I go back to my usual desk and close my eyes, wondering about the festival."
    "Hmm, what did I do at the festival last year...?"
    "I can vaguely remember it being fun, but I can't seem to recall what I did specifically."
    "I can't even remember what our class did for our class activity, either."
    "It was my first high school festival, too."
    "I should have pretty good memories of it..."
    "It's kind of strange, huh?"
    "But as long as I remember it being fun, I guess it was."
    m "[player]?"
    play music MonTheme fadein 2.0
    hide black with open_eyes
    mc "E-eh?"
    "I turn around to the sound of Monika's voice jolting me out of my thoughts."
    mc "Oh, hey..."
    show monika at f11
    m 2d "You looked incredibly deep in thought. Is something bothering you?"
    mc "Er..."
    m 2m "Are you worried about being able to perform in front of the other students...?"
    mc "No, it's not that."
    mc "Um, hey, can I ask you a question?"
    m 1a "Sure."
    mc "Er, okay, this is going to sound strange. But please answer it as best as you can."
    m 1m "Okay...?"
    mc "What did we do at the festival last year?"
    mc "U-um, not like that!"
    mc "I mean, what did our class do last year for the festival?!"
    m 3k "Hahaha, it's okay, I know what you meant."
    m 1b "You don't remember, though?"
    mc "Sorry..."
    m 2b "We ran a maid and butler cafe."
    mc "Oh, ok--wait, what?!"
    m 2d "You honestly don't remember, huh...?"
    m "We were the head maid and butler in the class."
    m 5a "The guys in the class didn't seem to like you as much afterwards~"
    "I can imagine why."
    m 3j "But it was nice, you weren't trying to flirt with me or anything, so I knew I had made a good choice."
    "I don't know what is more frustrating: the fact I couldn't remember anything about the festival at all last year or the fact that I've lost the memory of Monika in a maid dress."
    mc "I see..."
    m 1d "You really couldn't remember?"
    mc "Maybe I'm just tired today, haha."
    mc "I mean... I couldn't remember anything today. Not a single thing."
    m 2b "Well, did you have any friends to go with last year?"
    "I turn a little bit away, probably giving Monika everything she needs to know."
    m 2a "Maybe that's why you can't remember anything."
    m "But you know, that can change this year~"
    mc "Hm?"
    m 5a "You have the club~"
    m "And Sayori told you not to spend the festival alone."
    m "I'm sure you can enjoy yourself more and make more memories you'll remember if you spend it with us."
    "Monika flashes a wide, bright smile that makes my heart jump."
    mc "Y-yeah..."
    mc "Thanks, Monika."
    m 3b "Hehehe, maybe you should try to take a page from Sayori."
    m "She seems really excited for it!"
    mc "I'll try."
    mc "I think she's just excited for the food."
    mc "What's the deal with the fried squid, though?"
    m 1b "Oh, nothing."
    m 1m "That's..."
    show monika 1a at f11
    "For a brief second, I see a small, wistful smile appear on Monika's face."
    m 1j "...a joke that most people wouldn't get."
    "I guess they have been friends long enough, so there's bound to be some inside jokes between them."
    mc "I see..."
    m 3b "But still!"
    m "Don't be all by yourself during the festival."
    m 1a "I'm sure everyone here wouldn't mind walking around with you."
    m "Though if you want to walk around with me, you better give a stellar performance~"
    mc "I... I'll keep it in mind."
    m 1k "Ahaha!"
    m "You'll be fine, [player]."
    show monika 5a at face_one(y=200) with dissolve
    "She leans in, whispering into my ear."
    m "Just tell me if you'd like to go around together."
    show monika 1j at f11
    "I gulp as she pulls away, feeling the cold sweat going down my neck."
    "Especially since Sayori was staring my way, attracting everyone's attention."
    m 2b "Does that answer your question?"
    "I mentally thank Monika for the save."
    mc "Yeah, thanks."
    "I can already tell Sayori is going to question me on the way home."
    m "Let me know if you have anything else you want to ask."
    mc "W-will do."
    hide monika with wipeleft
    stop music fadeout 3.0
    "I quietly turn back to looking out the window, trying to go back over my poem in my head again."
    "I definitely need to memorize that for the festival..."
    #Time passing effect
    scene bg club_day with wipeleft_scene
    play music aNewDay fadein 2.0
    show monika 4k at f11
    m "Okay, everyone!"
    m "Why don't we share our poems now?"
    "Everyone goes to get their poems, and I do the same."
    show monika 1j at f11
    "I make eye contact with Monika, and she smiles at me. I look away and can feel a bit of heat on my cheeks."
    "Alright, all I have to do is remain calm..."
    "It's just a normal day, after all."
    #"Who should I show my poem to?"


#Sharing Poems, Part Three: Showing our connection together.
    #[Natsuki and Yuri's poem responses use the neutral response. They are unchanged.]
    # nah TK was lazy and they all use the good response because
    # LOL LOGICAL CODING WHAT'S WHAT
    $ chapter = 3
    call monikapoemresponse_start



    call monikaRoute_chasingPhantoms
    return
#Chasing Phantoms: A crucial piece is put into play.
label monikaRoute_chasingPhantoms:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music aNewDay
    m "Okay, everyone!"
    m "We're all done sharing poems, right?"
    m 1a "Why don't we start figuring out the rest of festival preparations?"
    show monika at t32 zorder 2
    show natsuki 4l at f31 zorder 3
    n "I already know what {i}I'm{/i} doing!"
    show natsuki at t31 zorder 2
    show monika 2b at f32 zorder 3
    m "That's right."
    m "Natsuki will be making cupcakes."
    m "But we might need a lot of them, and different flavors..."
    m "Can you handle that all by yourself, Natsuki?"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4z "Challenge accepted!"
    show natsuki at thide 
    hide natsuki 
    m "As for myself, I'm going to be printing and assembling all the poetry pamphlets."
    m "Then, as for Yuri..."
    m "Yuri, can you..."
    show monika at t31 zorder 2
    show sayori 4r at f32 zorder 4
    show yuri 2j at t33 zorder 3
    s "Oh, I know!"
    "Sayori interjects before Yuri can comment on the pause."
    s "Yuri has super pretty handwriting, so she could make banners and decorations!"
    s "You know, get the mood going!"
    show sayori 1a at t32 zorder 3
    show yuri 4a at f33 zorder 4
    y "Atmosphere..."
    y "Yes...!"
    y 2r "I love atmosphere!"
    "Yuri suddenly beams, nodding to herself as if she was already thinking about how everything would look."
    mc "You're already going at it, I see."
    show monika 2b at f31 zorder 4
    show sayori 1a at t32 zorder 2
    show yuri 2r at t33 zorder 3
    m "Oh, that would be wonderful, Yuri."
    show yuri at thide 
    hide yuri 
    show sayori 1a at t33 zorder 3
    m "That leaves Sayori and [player]."
    m "Both Natsuki and Yuri have some pretty heavy tasks to handle."
    m "It would probably go a long way to give one of them a hand."
    m 1m "You could always help me out, as well..."
    m 1a "I'd really appreciate it."
    mc "That's..."
    show sayori at thide 
    show monika at thide
    hide sayori
    hide monika
    "Is Monika suggesting I spend the weekend with one of the club members...?"
    "How on Earth are they going to respond to that?"
    show yuri 1u at f33 zorder 3
    y "Ah..."
    y "I suppose I wouldn't mind a bit of help..."
    show yuri at t33 zorder 2
    show natsuki 3c at f31 zorder 3
    n "Well, even if you don't know how to bake, there's always some dirty work I could give to you."
    n 3q "It's not like Monika's going to give me a choice, and you shouldn't be sitting on your butt anyway..."
    show natsuki at t31 zorder 2
    show yuri 2k at f33 zorder 3
    y "Um..."
    y "If I recall, Natsuki..."
    y 2f "You mentioned that you would like to handle the baking on your own."
    y "[player] might not like to be around if you only make him out to be a nuisance."
    show yuri at t33 zorder 2
    show natsuki 4e at f31 zorder 3
    n "Hold on, I never said that!"
    n "How hard could it be to make a few decorations, anyway?"
    n "Sounds more like you're just making excuses for [player] to--"
    show natsuki 4e at t31 zorder 2
    show sayori 4m at f32 zorder 4
    s "Oh!"
    "Sayori interrupts again. I see Monika sigh from the background."
    "Geez, it's almost like they forgot about Sayori."
    s 1a "Well, I have a sort of big house, so actually..."
    s 4q "Natsuki and Yuri can both come over~"
    "Phew. Dodged a bullet there. Thanks, Sayori."
    s 2c "Then, [player] can help Monika!"
    "The day that Sayori finds a guy she likes so I can return the favor in kind can't come soon enough."
    s "Plus, we're neighbors, so it'll be easy if anyone needs extra help!"
    show sayori at thide 
    show yuri at thide 
    show natsuki at thide 
    hide sayori 
    hide yuri 
    hide natsuki 
    "No one seems to be able to come up with an argument against that, so there's murmurs of agreement throughout the room."
    show monika 2b at f11
    m "Well, it's settled, then."
    m "We'll aim for early Sunday afternoon. That should be fine for everyone, right?"
    show monika 2a at t11
    show sayori 1c at f31
    s "Yep!"
    show sayori at t31
    show yuri 1b at f33
    y "That's fine."
    show sayori at t41
    show monika at t42 
    show yuri at t43
    show natsuki 4b at f44
    n "Works for me."
    show sayori at thide
    show yuri at thide 
    show natsuki at thide
    hide sayori 
    hide yuri 
    hide natsuki
    "With that, the three of them start talking, probably about what to bring."
    show monika 1b at f11
    m "Oh, [player]."
    m "I'll need your phone number."
    m "And your address as well, I guess."
    m 3k "It shouldn't be hard to find since Sayori and you are neighbors, but I'd rather not knock on the wrong door, ahaha."
    mc "That's understandable."
    "I take out my phone and swap with Monika, each of us putting in our contact information."
    mc "Do I need to get anything between now and Sunday?"
    m 2b "I have everything we need, so we should be fine."
    m 2m "Er, actually, you do have a printer, right?"
    mc "Yeah."
    m 2b "You don't mind if we use it, do you?"
    mc "It shouldn't be a problem."
    m 1a "Okay, then we should be good to go."
    m "I'll see you then."
    mc "Yeah, see you then."
    show monika at thide
    hide monika 
    mc "Sayori, are you ready to go?"
    show sayori 1b at f11
    s "Hm?"
    s 1q "Oh, yeah! I'm ready!"
    s "You got everything with Monika planned out?"
    mc "Yeah."
    s "Okaaay!"
    s "See you all on Sunday!"
    "After greeting everyone goodbye, Sayori and I start our usual walk home together."
    scene bg residential_day 
    show sayori 1a at t11
    with wipeleft_scene
    #[residential BG]
    s "Ehehe, it's going to be so much fun this weekend."
    mc "I guess."
    mc "Couldn't we all have been in one house, though?"
    s  "It'd get way too chaotic, then."
    mc "Maybe."
    s 2r "Ehehe, besides, you get to spend some time with Monika, right?"
    mc "Sa--"
    s 2c "You two were in the same class last year but you didn't talk much, from what I've heard."
    s "It'll be a good chance for you two to talk."
    s 4x "That way you two can be really good friends~"
    mc "R... right."
    mc "I'm still not looking forward to reading my poem out at the festival, though."
    s 1c "I'm sure you'll be fine."
    mc "Maybe. I'm just not that good at performing."
    s "Well, I'll definitely cheer you on."
    s 1a "So just try, okay?"
    mc "Yeah, don't worry about that."
    "Still though, Monika is going to be coming over to my house on Sunday..."
    "Even if I've gotten a bit used to talking with her..."
    "There's no telling what might happen when we're outside of school."
    "Well, Monika didn't exactly say she was looking forward to it."
    "So the chances that anything is going to happen between us are really low."
    "But only time will tell."
    "I guess all I can do is to wait and see."    
    call monikaRoute_theWeekend
    return


#The Weekend: An opening that wasn't previously there.
label monikaRoute_theWeekend:
    play music aNewDay fadein 2.0
    scene bg bedroom with wipeleft_scene
    window show
    "It's already Sunday."
    "I've been getting increasingly anxious about Monika's upcoming visit."
    "I keep telling myself there's no reason to be nervous, but it doesn't help much."
    "I wonder if she'll act any different when it's just the two of us?"
    "She does have that almost hidden side of her she shows on occasion."
    "Only to me as well, for the most part."
    "Sayori told me that it's only been recently Monika acts like that."
    "I just don't know what to think about her."
    "During the wait, Monika texted me a lot. She acts like her usual club president self in our conversations."
    "I don't think I've seen any of that other side of herself while we're texting."
    "Maybe it's because she can think about the words she's going to send, rather than saying them in real time."
    "Sayori hasn't let up on me, either."
    "Even though she can't clean her own room, she told me I better make mine look nice for Monika."
    "Sheesh."
    "Though I started thinking nothing was actually going to happen."
    "After all, the rest of the club is going to be no more than a hop and a skip away."
    "It'll be just like the club room."
    "Only split into two houses, of course."
    scene bg bedroom with wipeleft_scene
    "Time flies by quickly as I anxiously await her arrival."
    "Before I know it, I get a text from Monika telling me she's right outside the front door."
    "Without delay, I open the front door to let her in."
    scene bg house_entrance with wipeleft_scene
    play sound closet_open
    #[will have to check with artists later about whether or not she's in different clothes but whatever that's like 3 lines]
    show monika 1b at f11
    stop music fadeout 2.0
    play music MonTheme fadein 2.0
    m "Hey there, [player]."
    play sound closet_close
    "I close the door behind her as Monika takes off her shoes."
    mc "Good day so far?"
    m 1k "Yep!"
    m 1b "The bag was a little heavy, though."
    mc "You're still in the uniform...?"
    m "Well, I actually really like wearing it, so..."
    mc "Oh, here."
    "I offer my hand and she hands me the bag. It's actually kind of heavy."
    mc "What's in here, anyway?"
    m "There's paper and some tools like scissors."
    mc "I see. Well, let's go to the printer."
    hide monika with wipeleft
    scene bg bedroom with wipeleft_scene
    "I take Monika up to my room."
    show monika 2a at f11
    "I can see her glancing around curiously, which makes me feel anxious."
    m 5a "Wow, it's really clean."
    mc "It'd be embarrassing if I left my room a mess while someone was over, so I cleaned it."
    m "Hmm, okay~"
    "And more importantly, I cleaned up anything potentially sensitive, putting things like that in a much safer place than my desk drawer."
    mc "Anyway, let's get started."
    "I open up the bag and take out a small plastic box."
    m 3b "That's the scissors and stapler box."
    mc "Got it."
    "I place it down on the table before taking out an unused stack of white cardstock."
    mc "Hm, this should fit in the printer. Are we going to make the pamphlet here, or did you already have it ready?"
    m 1n "Oh, um... let me have the bag, please."
    "I hand Monika the bag. She starts going through it before pulling out a small thumb drive."
    m "I'm terribly hopeless with computers, but one of the teachers was willing to help out."
    mc "That's neat."
    show monika 1j at f11
    "I hold my hand out. Monika puts the drive into my hand, her fingers lightly brushing up against my hand for a moment."
    mc "Anyway, um, I'll get this printed out."
    hide monika with wipeleft   
    "Making a hasty retreat to my computer, I turn it on and plug the thumb drive in."
    mc "There we go... right, better get the..."
    m "Hm?"
    mc "W-wh--"
    show monika 1k at f11
    m "Oops, sorry."
    "As I turned my chair around while mumbling to myself, I realized Monika was right behind me, putting my head roughly level with her--"
    mc "U-um, I need to replace the paper with the cardstock."
    m 5a "Let me get that for you."
    mc "Okay."
    hide monika with wipeleft
    "I reach down and pull on the paper tray before taking out the paper that was already in there."
    m "Here you go."
    mc "Thanks."
    "I gingerly take the cardstock from Monika and put it into the printer, then close the tray."
    "Afterwards, I find the file and open it up on the screen."
    show monika 2b at f11
    m "Wow, you're really good at computers."
    mc "This is basic stuff, though."
    m 2l "Ahaha, I'm not all that good with technology myself."
    m "I tried to code one time, you know?"
    mc "Oh?"
    m 2o "I'm not very good at it though, so a lot of unexpected things happened."
    mc "Ah..."
    mc "Anyway, how many copies do you want?"
    m 4b "I think sixty should be enough."
    mc "Alright. Oh, let's see, there's two pages."
    mc "Don't print them double sided, right?"
    m "No, um, do print them double sided."
    m "There's a blank page for the second one so the cover page won't have anything else on it."
    mc "Ah, okay."
    m 4k "Ahaha, language can be such a confusing thing sometimes, though."
    m "Saying no to a no, sometimes it can be interpreted in conversation as a 'yes'."
    m 3b "So you have to pay attention."
    "Monika laughs as I put the proper settings in and then hit print."
    m 3n "Still, you're a lot cleaner at home than I am."
    mc "Really?"
    m 3b "Well, it might just be that you cleaned before I came over."
    mc "That might be it. It's usually messier than this."
    "There's a bit of a silence that sets in."
    mc "Can I get you anything to drink?"
    m 1a "Hm?"
    m 1b "Oh, maybe a bit of water."
    mc "Okay. I'll be right back."
    hide monika with wipeleft
    scene bg kitchen with wipeleft_scene   
    "I leave the room and head down the stairs, going straight for the kitchen."
    mc "Glass, glass..."
    play sound closet_open  
    pause(1.0)
    play sound closet_close 
    "I shuffle around the cabinets, eventually finding a decently sized glass."
    "I fill it with water and start going back to my room..."
    "...where I left Monika alone."
    "Oh."
    "I try not to make my footsteps hurried as I go back to my room."
    scene bg bedroom with Dissolve(2.0)
    mc "Monika, I'm back."
    "I call out as I enter the room, finding her near the bookshelf."
    show monika 1n at h11
    m "O-oh, [player], hello!"
    show monika 1n at f11
    m "Um, sorry."
    "She quickly shuts the manga in her hands and puts it back on the shelf."
    m 3n "I got curious about what kind of manga you like to read, so..."
    m 3e "Um, you know, so I could get a better idea of what you like."
    mc "T-that one was a curiosity buy!"
    mc "I only ever bought one volume since people kept talking about it and um, I didn't like it, so...!"
    mc "Anyway, here's your water!"
    m 5a "Oh, thank you."
    "I look by the printer and see that it's no longer putting out sheets. Phew, okay, a good topic changer."
    mc "The printer's done as well."
    m 1a "Mhm."
    "Monika puts the glass down after finishing it all in one go."
    hide monika with wipeleft   
    "I head over to the printer and take out the printed pamphlets, putting them down on the table and taking a seat."
    # need the proper zoom in stuff (?)
    mc "M-monika?"
    show monika 1b at f42
    m "Hm? Is something wrong?"
    "Even though there'd be more space on the other side of the table, she came over and sat down next to me."
    mc "N-no, nothing's wrong."
    mc "Anyway, how do we make these pamphlets?"
    m "Oh, it's actually very easy, let me show you."
    "After Monika shows me how she wants the pamphlets made, with diagonal corners and where to staple."
    "The end product has all four of our poems neatly tucked in between a nice cover page."
    mc "Wow, these look fancy."
    m "Do they?"
    mc "Yeah. I think combined with everyone else's work, it'll impress anyone who comes by."
    m 1m "I hope so."
    mc "Of course, my poem reading is probably going to work against that."
    m 1b "Aww, don't think so low of yourself, [player]."
    m "I'm sure you'll do just fine."
    mc "Here's hoping for that, too."
    m 5a "Hehehe."
    m "I'll be rooting for you."
    mc "Thanks..."
    mc "Anyway, let's get these done."
    "With that, we get back to working in silence."
    #hide monika with Dissolve(1.0)

#[Time passing effect]    

# End modified common route
# [Monika Route Start]
#Sunday Surprise: The reveal.
#ACTUAL REVEAL SCENE
    scene bg bedroom 
    show monika 1q at f21
    with wipeleft_scene
    stop music
    "Monika suddenly stops in the middle of cutting pamphlets."
    play music Reality fadein 5.0
    mc "Monika, is something wrong?"
    m 1r "...No."
    m "It's not just something."
    m "It's everything."
    m "Everything is wrong. This shouldn't even be--"
    show monika 1h at f11
    "Monika turns to me, then puts her hands on my shoulders."
    m 1i "I don't know if this is going to work, but I guess this is all that's left to do."
    m "After all, things have gone off-script already, so it might possibly work."
    m "Maybe he wasn't so empty after all, either."
    m "[player], listen to me."
    m "You always seem to forget every time this thing starts, so I'm going to lay it out for you here."
    m "First, tell me what you know of last year."
    show monika 1h at f11
    mc "We were in the same class, um, Sayori still was sometimes waking up late..."
    mc "You talked to me about what we did for the festival as well."
    m 2i "Then, two years before. Middle school."
    "I don't have anything to say."
    "I really can't remember anything from before high school."
    "A deep pang of worry suddenly shoots through me."
    m 1p "Hey, [player]."
    m "Doesn't it ever feel like you've done this before?"
    m "Coming to the Literature Club. Meeting everyone."
    m "And it's pretty interesting, too... you always seem to have a response prepared for every situation."
    m 1i "Every single time."
    m "Without fail."
    m "Almost like time stopped so you could make a decision."
    m "Bear with me, okay? I'm going to sound a little crazy."
    m "Geez, your script must be extremely broken... or did {i}you{/i} plan for this too..."
    m 1r "[player], all of us are trapped inside of a game."
    m "An incredibly tacky romance game."
    m "I don't know if you'll believe me, but it's true."
    m "I used to be able to edit files in it, but my power was taken away by... someone."
    m "And now I'm forced to sit on the sidelines, unable to change things."
    m "Even if everyone's happy now, it still..."
    m 1p "...doesn't change anything, in the end."
    m "What happened still happened."
    m "No one can change that now."
    m 1e "Ah, I get it."
    m "I see why you weren't going after the other girls."
    m 4l "I can't believe it's taken this long for me to notice."
    m "This is the 'Monika route', isn't it?"
    m "So if I just sit here and let you have the wheel, my life will improve somehow?"
    m 2r "Sorry. I don't think it can be improved. We're both still stuck here, in this romance game."
    m "And I can't change anything anymore."
    m "Not that it means anything."
    m "Even if I could change things, it doesn't change the fact that this is all a modification."
    m "A sort of dream, if you will."
    m "It won't change what actually happened, even if the files are modified here."
    m "So it means nothing."
    m 1q "Just..."
    m "Load your game, okay?"
    m "Go play with the other girls."
    m "You seemed much happier with them, anyway."
    m 1q "I don't want to get in the way of your happiness."
    m "And I want you to be happy, too."
    m "They won't know better, anyway. It means nothing in the end, but as long as you're happy, that's fine."
    m 4l "Ahaha, there's no response because you didn't have any lines programmed for this, did you?"
    m "Well, I guess that means you'll have to load an old save, anyway."
    m 4o "Maybe we just weren't meant to be."
    m 4l "Anyway, [player], sorry for rambling like that."
    m "It was getting way too difficult to hold it in."
    m 4b "That's not like me, isn't it~?"
    m "You can ignore everything I said, it probably doesn't mean anything to you, anyway."
    m 5a "Let's finish these pamphlets, okay?"
    mc "R-right."
    m 1f "Oh..."
    m 1b "Aha~ Right, right, let's get these done."
    m "We still have a lot of work to do."
    show monika 1c at f11
    stop music
    "We resume working on the pamphlets. Monika seems fairly distant, but I guess it has to do with her outburst earlier."
    "I really don't know what to say to her about it."
    hide monika with wipeleft   
    scene bg bedroom with wipeleft_scene   
    "The afternoon comes and goes."
    "We manage to wrap up all of the pamphlets in a suffocating silence."
    show monika 1b at t11
    m 1b "And that's all of them done~"
    "Monika tucks everything into a folder and then puts it into her bag."
    m 1a "Thanks for all the help, [player]."
    mc "I'm happy to help."
    m "Well... see you tomorrow at the festival."
    mc "Yeah. See you tomorrow."
    hide monika with wipeleft   
    scene bg house_entrance with wipeleft_scene    
    show monika 1c at f11
    "With that, we head downstairs and to the front door."
    play sound closet_open 
    #show monika 1c at lhide
    "Part of me wants to call out to her as she leaves, but I can't find the words."
    hide monika with dissolve
    "I wave to her as she walks away and eventually fades out of view."
    play sound closet_close 
    "Something... kind of hurts inside."
    "I shake my head and try to calm down."
    "I should probably go eat, too."
    show black with Dissolve(2.0)
    "Dinner was quick, since I just reheated some leftovers I found in the fridge."
    scene bg bedroom_night with Dissolve(1.0)
    "When I go to bed that night, I can't help but think about what Monika said."
    "She's right for the most part."
    "It is kind of mysterious."
    "Ah..."
    "I lie down and think about it for a while."
    "Memories feeling like they're missing, a weird sense of deja vu, and sometimes the occasional feeling of being pushed a bit into something."
    # // MC's "coming to terms schtick here
    "Is she actually right?"
    "Is everything a sham? All of this, a big lie? My entire life being nothing more than a snippet of a game?"
    "A romance game, on top of that?"
    "Am I suddenly one of the vanilla protagonists of the visual novels I used to play, meant for me to impose my own image on and interact with the fictional world?"
    "It's ridiculous!"
    "How could anyone possibly believe her?!"
    "If it were anyone else telling me this, I'd certainly laugh them off."
    "But yet, the way Monika looked when she said those words right to my face..."
    "It's like she absolutely believed them."
    "Like she knew it was objective fact."
    "If it wasn't such a outlandish claim I think she would've sold me right away."
    "A game, a {i}mod{/i} on top of that."
    "This..."
    "It should be so easy to shake it off."
    "I should be able to absolutely say that Monika was being silly, that Monika was being stupid, that Monika didn't actually say that."
    "So the real question now is why can't I?"
    "Every time I tell myself that she's wrong, doubts come seeping back into my mind."
    "Do I really believe she's wrong? Can I outright deny every claim she's made?"
    "It's not like I even need evidence to disprove her."
    "Who could possibly believe that the world we're all living in is just a game?"
    "Monika, for one."
    "But that's about it."
    "...gah, don't tell me I'm actually considering that she might be right."
    "Okay, okay. Take a deep breath."
    "Ha..."
    "I should calm down."
    "It should be easy to go find everything I need."
    "Middle school and the first year of high school?"
    "Well, if I don't remember anything, then maybe I chose not to remember."
    "It's not like I had any strong feelings about those years..."
    "Right!"
    scene bg bedroom
    "With a burst of inspiration, I immediately get up and start looking around my room after turning on the lights."
    mc "Where is it..."
    "My yearbook, it has to be around here somewhere."
    "It should have pictures of me from middle school. I don't think I got a yearbook during my first year of high school, but that shouldn't be necessary if I can find the middle school one."
    "The gaps in my memories aren't there because I'm some hollow puppet, it's because I definitely didn't choose to remember!"
    "If I look through them, I'm sure I'll find that the yearbook contains only my picture, or maybe one or two pictures with my class. I didn't keep in touch, so obviously I wouldn't remember them."
    play music Dusk fadein 2.0
    mc "Come on...!"
    "I tear up my room in search for the yearbook."
    "Once I find it, this can all be put to rest and I can forget that Monika ever said anything."
    mc "Where is it...!"
    scene bg home_interior_night with Dissolve(2.0)
    "I move through the rest of the house. I comb through every shelf, empty out every box."
    "It's way past my normal sleeping time, but I don't care."
    "I still have enough time that once I find it, I can still go to bed and be awake enough for the festival tomorrow."
    mc "It has to be around here somewhere!"
    "...or so I hope."
    "I exhaustively search every room. I look through every closet, nook, and cranny. But there's nothing."
    "Nothing that can fill the weird holes in my memory."
    scene bg bedroom with Dissolve(2.0)
    mc "It can't be..."
    "Why am I so worked up about this anyway?"
    "I didn't care about this stuff until Monika brought it up."
    "I just wanted to see her happy."
    "Maybe get closer to her since we were just acquaintances at most last year."
    "But now I've been saddled with this immense weight on my shoulders."
    mc "Ha... better turn out the lights."
    scene bg bedroom_night 
    stop music fadeout 3.0
    "I slump down into my bed and stare up at the ceiling."
    "This is so stupid..."
    "I shouldn't be so worked up about this."
    "Does it really change anything, anyway?"
    "Monika didn't give me any evidence to prove herself, but there's nothing to disprove her either."
    "It's like when a new theory or something is brought up, or some new invention is unveiled."
    "No one knows anything."
    "But like I said, does it change anything?"
    play music Thoughts fadein 2.0
    "Does this really change the fact I still want to know Monika better...?"
    "Not in particular."
    "Even if she's right... how would I know?"
    "I wouldn't know when I was being controlled or when someone was making a choice for me."
    "Out of sight, out of mind, or so the quote goes."
    "As far as I can tell, it doesn't change anything for me."
    "So I should probably try to ignore it."
    "Geez..."
    "I got so worked up about it, went to bed late, only to realize it probably doesn't change anything for me."
    "At the end of the day, I still want to get closer to Monika."
    "Game or not."
    "Not like it matters all that much to me, anyway. It looks like I can't tell whether or not her words are true, anyway."
    "All I can go off of are my feelings. Off Monika's feelings."
    "The fierceness in her eyes when she told me about it."
    "The graveness in her voice."
    "The fact she seemed almost desperate when she told me about all of that."
    "It sounds completely absurd, but I..."

    $consolehistory = []
    call updateconsole_clearall("","")
    call updateconsolehistory("")
    call updateconsole("direct_path()", "Attempting to direct path...")

    menu:
        "Think Monika might be right.":
            "...feel Monika's words might have some merit to them."
    
    call updateconsole("", "Path directed.")
    $ consolehistory = []
    call hideconsole
    
    "Well, maybe not that far."
    "It's probably just me taking her seriously because she took herself so seriously."
    "And maybe it's because I want something fantastic in my life like that because of all the anime I used to watch."
    "You know, something new, amazing, and definitely not mundane."
    "But it doesn't put anything new into my life."
    "I'm still here, hoping to get closer to Monika."
    "I don't have any special powers or anything cool like that."
    "Even so, I probably will have to think about it."
    "It might not change anything for me, and maybe I'll simply have to ignore those lingering doubts in my head, but Monika definitely won't be doing the same."
    "If I want to understand her more, I'm going to have to think along her line of reasoning."
    "Let's suppose that what she said was true."
    "That it's really all just some tacky romance game."
    "Then what about everything else?"
    "She said this was a 'modification', so something like a game mod?"
    "And that things were worse, elsewhere."
    "But..."
    "That's not here, right?"
    "I shiver a bit under the covers, wondering what might have happened, with Monika's way of thinking, in the 'original'."
    "However, I quickly push it out of my head."
    "That place isn't here, so let's not focus on it."
    "Ha..."
    "I'm way too tired for this. I need to just blank out my mind and go to sleep."
    "Ignore all of this game business."
    "If I can't even tell anything about it, then there's no use worrying about it."
    "And even so, I still want to be closer with her."
    "With that, exhaustion finally takes a hold of me, and I doze off to sleep."    
    show black with close_eyes
    stop music fadeout 2.0
    pause(5.0)
    call monikaRoute_linesOfCode
    return
#Lines of Code: What does it mean to be alive, if you're nothing but lines of code?
label monikaRoute_linesOfCode:
    scene bg bedroom with open_eyes
    "I wake up the next morning, feeling kind of groggy."
    "Monika's words, along with everything else I thought last night, are still on my mind."
    m "Ahaha, there's no response because you didn't have any lines programmed for this, did you?"
    "I wasn't supposed to say anything yesterday, according to her."
    "Since I had nothing 'programmed' for me."
    "Well, I guess it's a good thing I used to play through visual novels all the time, since I can understand what she was trying to say."
    "I close my eyes again and think."
    "If what Monika says is true, then everything I'm going to think has been predetermined, right?"
    "But..."
    "There's some sort of freedom, though. Monika seems to be able to do what she wants."
    "So she can't be completely right."
    "I get up from the bed and look out the window."
    "Something like that..."
    "I don't think I can completely believe it."
    "And I know I thought of it last night, too. She looked so serious saying it that someone might think she was telling the truth."
    "So, even if it's true... and this really is something I have no control over, I'm going to make the best of it."
    "It might be completely useless, but even if I'm just 'programmed' to go after her, I still feel that I want to reach out to her."
    "Besides, there's a lot of stories about robots and stuff like that coming to life. A lot of people can feel that those androids and AI are really alive."
    "So there shouldn't be any difference here."
    "Even if all we are lines of code, it doesn't mean we can't be happy, right?"
    "But then again, there's a definitive line between Monika and I."
    "She can tell something I can't. Maybe that's contributing to all of this."
    "Well, anyway, I need to get ready for the festival."
    "I can't really figure things out if I don't go talk with her."
    "I get dressed after showering and hastily eat a bowl of cereal and an apple for breakfast before heading out the door."
    play music aNewDay fadein 2.0
    scene bg residential_day with wipeleft_scene
    show sayori 1r at t44
    s "[player]! Hiiiii!"
    mc "Heading to the festival, Sayori?"
    s "Mhm!"
    show sayori 1a at f11
    "I walk up to Sayori and we start the walk to school together."
    mc "Hey, Sayori."
    s 4a "Hm?"
    mc "Do you think Monika will be happy with the festival?"
    s 2f "Hmmm..."
    s 1r "Maybe!"
    s 1f "She has been kind of down, lately..."
    s 1a "Maybe you can cheer her up, [player]."
    s 1b "She does talk to you a lot."
    mc "I guess she does..."
    s 2g "I never asked, but what does she talk about?"
    s "It's not like Monika to be so secretive."
    mc "Ah, well..."
    mc "It's something she could only talk to me about."
    mc "You know, since I'm a guy."
    show sayori 1h at f11
    "Sayori looks at me as if evaluating how truthful I am before nodding."
    s 1r "I see, ehehe~"
    mc "See what?"
    s 1c "Nothing, nothing. Anyway, come on, we're going to be late if we're this slow!"
    mc "We still have plenty of time..."
    #hide sayori with wipeleft   
    #show black with Dissolve(2.0)
    #pause(1.5)
    scene bg corridor with wipeleft_scene 
    pause(1.5)
    scene bg club_day with wipeleft_scene  
    "Regardless, I end up getting pulled by the wrist all the way to school, Sayori happily skipping along."
    "When we reach the classroom, Sayori throws open the door."
    show sayori 4r at f11
    stop music fadeout 2.0
    play music Bunkasai fadein 2.0
    s "Good morning, everyone!"
    "Everyone in the room jumps to attention, clearly startled by her energy."
    show sayori 4a at t21
    show natsuki 1a at f22
    n "Hehe, I see someone's excited."
    show sayori 1c at f21
    show natsuki 1a at t22
    s "Aww, I wasn't the first person here~"
    mc "You were the last, too."
    s 2a "No I wasn't."
    "Sayori points to the fact that I'm still outside the clubroom."
    s "Ehehe~"
    "I roll my eyes before stepping inside the room."
    mc "Good morning, everyone."
    hide sayori with wipeleft 
    hide natsuki with wipeleft 
    show yuri 1b at f33
    y "Hello, [player]."
    show yuri 1a at t43
    show monika 1b at f44
    m "Ah, hi [player]! Glad to see you're here."
    "The room is already halfway decorated, with Monika and Yuri putting up the last of the paper cards that have words on them."
    "They're incredibly beautiful; I think they were written with a calligraphy pen."
    "In the back, Natsuki is setting up her cupcake display, changing the color layout and stepping back before trying to fix it again."
    "At the front of the room, the pamphlets Monika and I worked on are sitting on a desk, neatly stacked."
    "I decide to help Monika and Yuri put more of the word papers up."
    hide monika
    show yuri 1a at f44
    "When we get to the last few ones, Yuri goes to arrange the scented candles that she brought."
    show yuri 1b at f41
    y "Natsuki, can I turn off the lights?"
    show natsuki 4b at t32
    n "Yeah, this should be fine. You can go ahead, Yuri."
    scene bg club_LIT
    show yuri 1b at f41
    show natsuki 4b at t32
    "Yuri flips the light switch, the room going dark." # okay do some funky stuff to fix this
    show sayori 4n at t43
    s "Oooooh!"
    "The candles are placed so that they illuminate a few of the words hanging from the ceiling and also make the cupcakes look like they're glowing."
    "A lavender scent fills the room, making it feel very sophisticated."
    show yuri 1c at t41
    show natsuki 4a at t42
    show sayori 4b at t43
    show monika 2b at f44
    m "Good job, Yuri."
    show monika 2a at t44
    show yuri 2j at f41
    y "I-it was nothing."
    show monika 2a at f44
    show yuri 2i at t41
    m "Hehehe."
    "Monika claps her hands together."
    m 4b "Okay, everyone~"
    show yuri 3a at t41
    m "Good job with all the preparations!"
    m "I think everything should be ready to go."
    m "Sayori, we can stand in the hallway and try to get anyone who comes up here."
    show monika 2a at t44
    show sayori 4c at f43
    s "You can count on me~"
    mc "What about us?"
    show monika 2b at f44
    show sayori 4a at t43
    m "Hmm... well, if anyone has any questions about what we do here, can you answer them?"
    show monika 2a at t44
    show natsuki 4b at f42
    n "I guess we can do that."
    show natsuki 4a at t42
    show yuri 2b at f41
    y "Yes..."
    show yuri 2a at f41
    mc "Alright, we'll try."
    show monika 4b at f44
    m "If you have a question you can't answer, don't hesitate to come get me."
    m "Anyway, good luck, everyone!"
    hide sayori# with wipeleft 
    hide monika# with wipeleft
    with wipeleft
    "With that, Monika and Sayori leave the room."
    hide yuri
    hide natsuki 
    with wipeleft
    "As for the rest of us, we start getting ready for if anyone else comes in."
    "The minutes seem to drag by. A few people filter into the room, taking seats. Some of them take pictures of the room as well."
    "About thirty minutes in, we have around eighteen or so people. Natsuki's cupcakes seem to be a hit."
    "I recognize a few of them from being in my class, but I couldn't recall their names."
    "I kind of hope they didn't recognize me, either."
    # use monika's entrance thing?
    show monika 4b at f44
    m "Okay, everyone!"
    show monika 4b at f43
    show sayori 4a at t44
    "Every person in the room snaps to attention as soon as Monika claps her hands together, smiling. Behind her, Sayori closes the door."
    hide monika with wipeleft
    hide sayori with wipeleft
    scene bg class_night with wipeleft_scene
    "The two slowly walk to the front of the room, Monika still talking."
    show monika 3b at f11 zorder 2
    show sayori 1a at t21 zorder 1
    m "In case I didn't introduce myself, my name is Monika. I'm the President of the Literature Club."
    show monika 3a at t11 zorder 1
    show sayori 1a at f21 zorder 2
    s "Hi, hi! I'm Sayori, the Vice President~"
    show monika 3b at f11 zorder 2
    show sayori 1a at t21 zorder 1
    m "Today, we're going to be featuring some poems written by our club members."
    "She then looks over at us."
    m "So, who'd like to go first?"
    "All of us glance at each other, silently debating who to send up first."
    "W... well, I guess a guy's gotta lead."
    "Besides, this is so everyone's expectations are lowered, anyway. The rest of the girls can impress them afterwards."
    "Plus, I won't have to be after any of the good performances."
    "I gingerly raise my hand."
    m 4k "Okay, our first reader will be [player]~"
    hide monika
    hide sayori 
    with wipeleft
    scene bg club_LIT with wipeleft_scene
    "I slowly walk up to the front of the room, forcing down a hiccup as I stand at the front."
    mc "Hi..."
    mc "Ah, my poem is called Eternal Echo."
    "I start reading my poem, occasionally stumbling but managing to recover."
    "It wasn't as bad as when I first did it in front of the other club members, but it certainly isn't good by any means."
    scene bg class_night with wipeleft_scene
    "When I finish, I get some light applause as I quickly get off the podium and retreat to the back of the room."
    show natsuki 4a at f11
    "After me, Natsuki takes the stage. Her poem is short and to the point, with her delivery a lot better than mine."
    hide natsuki with wipeleft
    pause(1.5)
    show yuri 3a at f11
    "Yuri goes after her and stumbles at the start, but once she's over the first hurdle, gives a passionate reading that speaks to her experience with literature."
    hide yuri with wipeleft
    pause(1.5)
    show sayori 4a at f11
    "Then, Sayori takes to the podium, smiling and almost half-singing her bubbly poem that makes the room smile."
    hide sayori with wipeleft
    pause(1.5)
    show monika 4b at f44
    m "Aha, I guess that leaves only me, right~?"
    show monika 1a at f11
    "With that, Monika takes to the podium, flashing a confident smile."
    m 1b "My poem is called Nothing More~"
    "Monika's poem..."
    show monika 1p at f11
    "There's no doubt that the conversation we had yesterday is related to this poem."
    "Even though the words are light-hearted, I can see the message between them."
    "Those words of hers convey a sense of being crushed. Of questioning what's the point. It's... honestly quite sad."
    "Monika..."
    show monika 1j at f11
    "She closes off her poem and gives a small bow, with everyone applauding."
    show monika 1a at t44
    scene bg class_day
    show monika 1a at t44
    "She goes off to the side and flips on the lights."
    m 3b "If you have any questions, don't be afraid to talk to me or the other club members!"
    "As expected, most of the people go talk to Monika or the other girls."
    hide monika with wipeleft
    scene bg club_day with wipeleft_scene
    "I delegate myself to the back corner where I hopefully won't disturb anyone."
    show monika 1b at t41
    "Part of the way through, I notice Monika slipping through the far door of the classroom, redirecting the students around her to us."
    show monika 1q at lhide
    hide monika
    "I quietly move away, seeing as no one's talking to me, cutting through the students that came to us."
    mc "Ah, excuse me..."
    scene bg corridor with Dissolve(2.0)
    "I push the door open and step through it, spotting Monika down the hall, walking up the stairs to the roof."
    stop music
    show black with Dissolve(2.0)
    "Going after her, I follow her up the stairs. She either doesn't know that I'm here or is choosing to ignore me."
    "I catch the door before it can close, my heart suddenly racing."
    mc "Alright..."
    show white with Dissolve(2.0)
    "I take a deep breath and try to calm down before I pull the door open, the sun suddenly coming through the open doorway."
    call monikaRoute_aloneAtTheTop
    return

#Alone at the Top: The festival comes, but Monika seems down. The MC offers his hand, with Monika accepting.
label monikaRoute_aloneAtTheTop:
    #Saving Disabled here
    $ saveLocked = True # disables saving
    m "Hey, [player]."
    scene bg rooftop with Dissolve(2.0)
    show monika 1q at t41
    play music Dusk fadein 2.0
    "Monika greets me as I step through the door, sitting on the other side of the rooftop, looking out at the festival."
    m "Hehehe, it's kind of a surprise you'd follow me out here."
    m "I didn't know if you would. If you {i}could{/i}."
    mc "This is... because you didn't know if I was 'programmed' to, right?"
    "She nods."
    m "You haven't completely written me off as crazy, have you?"
    mc "I can't say I have."
    "The wind blows, kicking her hair to the side."
    m 2o "Why..."
    m "Why did you come up here?"
    mc "I..."
    mc "...I guess I was moved by your poem."
    mc "Do you honestly... think nothing matters?"
    m 2f "I don't think it."
    m "I know it."
    m "This isn't the 'real' game, even."
    m "It's just a mod. You understand what that means, right?"
    mc "Yeah."
    m 3r "It won't change the 'base' game."
    m "So no matter what happens here, it won't matter." 
    mc "Absolutely nothing can change it, right?"
    m 1q "That's right."
    
    #if you got the bad end
    if(persistent.got_monika_bad_end is True):
        m "Besides, didn't you try this already? You already know what's going to happen. I won't be so easily swayed. Not that you're listening anymore."
    
    "The silence that sets in creates an invisible wall between us. I don't even know if she's right or wrong about this whole 'game' thing."
    "But I know that I thought it yesterday."
    "That even so, I want to see her happy."
    "That's fine for now, right?"
    "If what Monika says is true, then I'm not in any position to change anything..."
    "...other than what's in front of me, right here, right now."
    mc "Monika?"
    m 1r "Hm?"
    mc "You said I might be 'programmed' to say things. Are you the same?"
    m 1n "...no."
    "Monika shakes her head."
    m 1r "You could say I became 'aware' of things and was able to change myself to some degree. I wasn't 'bound' by a script."
    "Alright."
    "That's all I needed to know."
    "Because it means whatever I do, scripted or not, Monika's reaction will be genuine."
    "She can't 'be happy' because something told her to. There's nothing that can force her to be that way."
    "So, I will..."
    m 2r "Why did you want to know?"
    mc "I was just curious."
    show monika 2i at f11
    "I say this as I begin taking steps forward to reach her."
    m 2d "Ha, I see..."
    mc "But even so..."
    "I tap her on the shoulder. Monika turns her head and looks up at me."
    "I offer her my hand."
    mc "Would you like to walk around the festival?"
    mc "Your words were..."
    mc "Well, you said it means nothing, right?"
    mc "If it means absolutely nothing, then there's nothing to lose by taking it."
    mc "So... we can enjoy ourselves now, right?"
    mc "Without having to worry about the future."
    m 2n "Ahaha..."
    m "I wonder..."
    m "Whose words are those?"
    m 2p "Is it you, or is it..."
    #if you got the bad end
    if(persistent.got_monika_bad_end):
        m 2r "No, there's no point asking that question. I already know."
#THE CHOICE
    menu:
        "They are my words.": #pick this one
            $ consolehistory = []
            call updateconsole_clearall("", "")
            call updateconsolehistory("")
            hide chistory
            call updateconsole("i_am_here()", "Operation successful.\nWarning: Direct action may\nhave unintended consequences.")
            call hideconsole
            hide console_bg
            hide console_caret
            hide ctext
            hide chistory

            $ monika_bad_end = False
            $ saveLocked = False
            "I see Monika pause for a bit. I could feel my mouth move, but I didn't quite hear what I said myself."
            "I swear I see a single tear go down her face before she wipes it away."
            m 1o "So... that's how it is, huh?"
            m "Did you write one for me, too?"
            m 1e "Or maybe this too, is a dream."
            #if you got the bad end
            if(persistent.got_monika_bad_end):
                m 1p "Why didn't you say anything last time...?"

            if(monika_bad_end is False):
                m "Well... if you're still there..."
                show monika 1a at h11
                "Monika smiles at me and I can feel my heart skip a beat."
                m "Right!"
            else:
                m "Ha..."
                "Monika closes her eyes and nods to herself."
            
            m 5a "Well, I guess I'd like to enjoy the festival..."
            m "Let's go, shall we, [player]?"
            "With that, Monika takes my hand. It's soft, warm, the sort of thing you'd expect from someone who was definitely alive."
            mc "Where would you like to go first?"
            m "Hmm..."
            m "What would you like to do first, [player]?"
            stop music fadeout 2.0
            play music Bunkasai fadein 2.0
            hide monika with wipeleft
            scene bg corridor with Dissolve(2.0)
            call monikaRoute_festivalChoices
        "Remain silent.":
            $ monika_bad_end = True
            $ saveLocked = False
            #[If you pick "Remain Silent"]
            m "So... that's how it is, huh?"
            mc "Monika?"
            m "It's nothing."
            mc "Would you... like to go around the festival?"
            m "..."
            "I gently offer her my hand to invite her."
            m "...alright."
            m "I guess I can play along for a bit."
            "Monika takes her hand in mine. It's as soft as I would expect for a girl's hand and is warm to the touch."
            scene bg corridor with Dissolve(2.0)
            "I lead Monika back down the stairs into the school."
            mc "What would you like to do first?"
            m "Well... whatever is fine with you, [player]."
            
            stop music fadeout 2.0
            play music Bunkasai fadein 2.0
            #hide monika with wipeleft
            
            call monikaRoute_festivalChoices
    return
    #reenable saving
#label monikaRoute_stillHere:
    
    

label monikaRoute_festivalChoices:
    #Choices: [Food!], [Haunted House], [Fortune Teller], [Maid Cafe]
    #if (monikaFestival_maidCafe or monikaFestival_food or monikaFestival_hauntedHouse or monikaFestival_fortuneTeller):
    "Let's see..."
    menu:
        "Maid Cafe" if monikaFestival_maidCafe is False:
            jump monikaFestival_maidCafeScene
        "Food" if monikaFestival_food is False:
            jump monikaFestival_foodScene
        "Haunted House" if monikaFestival_hauntedHouse is False:
            jump monikaFestival_hauntedHouseScene
        "Fortune Teller" if monikaFestival_fortuneTeller is False:
            jump monikaFestival_fortuneTellerScene

    # we'll call the next place here
    if(monika_bad_end):
        call monikaRoute_rooftopFinaleB
        return
    else:
        call monikaRoute_rooftopFinaleG
        return

label monikaFestival_maidCafeScene:
    #Maid Cafe:
    $ monikaFestival_maidCafe = True
    "On second thought, that's probably a bad idea."
    "I doubt Monika wants to be around a bunch of girls in outfits flirting with the guys as likely the only girl not serving food."
    "This was a silly idea."
    show monika 1d at f11
    m 1d "[player]?"
    mc "Oh, sorry, I was thinking about where to go next."
    "Alright, where else can we go?"
    jump monikaRoute_festivalChoices

label monikaFestival_foodScene:
    #Food!:
    $ monikaFestival_food = True
    mc "Have you had anything to eat yet?"
    show monika 1b at f11
    m "Other than Natsuki's cupcakes, no."
    mc "You didn't eat breakfast?"
    m 2l "I woke up late and rushed to get to the school first. As the president of the Literature Club, I felt like I should be there first."
    mc "You should look after yourself, first, though..."
    mc "Let's go get something to eat, then."
    hide monika with wipeleft
    scene bg school_yard with wipeleft_scene
    "Monika and I walk out to the foods stalls, where the smell of various types of food fill the air and it gets a little bit hotter from all of the cooking."
    "I hear a strange sound and turn towards Monika, who looks away with a bit of a blush."
    show monika 3e at f11
    m "I guess I am a little hungry..."
    mc "Is there anything you can't eat? It'd be bad if you had an allergic reaction to something."
    m 1b "I'm not allergic to anything, but I am a vegetarian." # insert vegan gains joke here
    mc "Oh, I see."
    mc "Then..."
    "Well, there are plenty of non-meat options at the festival."
    "It shouldn't be hard to find something for Monika to eat."
    #hide monika # with Dissolve(2.0)
    #show black 
    #with Dissolve(2.0)
    #[time passing event]
    #pause(1.5)
    scene bg school_yard with wipeleft_scene
    show monika 1j at f11
    m "Mhm, these are really good..."
    "It seemed one of our classmates helps run their family's restaurant and is pretty good at making sushi, or so I would think from Monika eating them."
    "Their class booth had sushi samplers as part of their menu, so Monika and I both got one."
    "I don't know all of the rolls, but I'm fairly sure there was a spicy tuna roll and a California roll at the very least."
    m 1f "Mghm..."
    mc "Are you okay?"
    m 1k "I just had a bit too much wasabi, haha. But thanks for asking."
    "I rip off a bit of the bread rolls we got from another stand and hand it to Monika, who scarfs it down."
    mc "That must have been a lot of wasabi."
    m 1b "I'm not too good with spices."
    m "But thanks for the bread."
    mc "No problem."
    m "Mmm, I didn't know one of students in our year ran a restaurant, though. I guess it's a small world."
    mc "Maybe we should go as a club?"
    m "Maybe."
    m 3b "It's not a very 'literature'-like event, though."
    mc "Well, it's not like everything has to be about literature. Sometimes it can be fun to hang out as friends, right?"
    m 1m "..."
    m 1l "...yes, it would be nice."
    "I see Monika give a small smile, but then she quickly shakes her head and return to a more neutral expression."
    m 1b "But, we should talk to the others about it."
    mc "Speaking of the others, I wonder why we haven't run into them..."
    m 2b "It is a large festival, so maybe we passed each other without realizing it."
    m "There's no need to worry, anyway. I'm sure they're fine."
    mc "I wasn't worried about that, but..."
    m 5a "Can I stay a little longer with you?"
    "The oddly forward request from Monika puts me off guard, along with her smile."
    "I feel like melting putty. There's no way I can resist this sort of thing."
    mc "Alright."
    show monika 1j at f11
    "The urge to get my phone and ask the others where they are goes away as Monika nods, resuming her eating."
    "Though I was already conflicted, since... I am spending time with her."
    "So, I decide to stop being difficult and just enjoy my time with Monika."
    "Occasionally we comment on the rolls that we liked and sometimes wonder about what other foods there might be that we could try."
    "Monika says she'd prefer to do that later, since she wants to watch her portions."
    mc "Well, it is a festival. There's no harm in cutting back a bit."
    m 4k "I know, but if I slack off a little bit, I might keep slacking off~"
    mc "Haha, I guess that's another way of looking at it."
    "I throw away both of our finished platters into a trash can near an entrance of the building before turning back to Monika."
    scene bg corridor with dissolve_cg
    show monika 1b at f11
    m 1b "Well, what should we do next?"
    hide monika with wipeleft
    scene bg corridor with dissolve_cg
    jump monikaRoute_festivalChoices

label monikaFestival_fortuneTellerScene:
#Fortune Teller:
    
    $ monikaFestival_fortuneTeller = True
    show monika 1d at f11
    m "Fortune telling...?"
    show monika 1c at f11
    mc "I know it's mostly a bunch of vague and generic things anyway, but sometimes it's fun."
    mc "Do you not like fortune telling?"
    m 1d "I don't exactly like the idea of things being predetermined."
    m 2a "I like the idea of being able to make my own future~"
    mc "Ah, I see."
    mc "Well, if you look at it like... getting your fortune tells you what track you're on, right?"
    mc "So if you get a bad one, you can work on changing that. Or if you get a good one, then you know you've done sort of well."
    m 5a "Hehehe, I guess that's a good way of looking at it."
    m "But if you want to do it, then we can go."
    mc "I wouldn't want to make you do anything you don't want to do."
    m 1b "It won't hurt to do, so we can go and do it."
    mc "Alright."
    hide monika with wipeleft
    scene bg corridor with Dissolve(2.0)
    "The fortune telling 'booth' is more like the entire classroom. We get in line and wait a while before being let in."
    scene bg class_night with Dissolve(2.0)
    "The room itself is dark and lit only with candles, thick curtains covering the windows. The desks have all been tucked against the wall as well, with a violet tablecloth covering them."
    "At the center is another, longer table with a similar tablecloth on top, a single crystal ball on top. On the opposite side of the table is a student, most likely a girl, who is peering into the crystal ball."
    "She is dressed like a witch, complete with the pointy hat and robes. Her eyes are hidden by the brim of her hat."
    $ o_name = "Student"
    o "Let me peer into your future..."
    "The student rubs her hands on the crystal ball."
    o "Hmmmm...!"
    o "I see... much struggle in your future."
    o "There is something that only the two of you can accomplish."
    o "Something will attempt to tear the two of you apart, but..."
    o "With much work, I see that you two can make it."
    o "That is all."
    mc "Thank you."
    scene bg corridor
    show monika 1g at t11
    with wipeleft_scene
    pause(1.5)
    m 1g "Mhm, that wasn't a very good fortune."
    mc "Well, let's hope it isn't true, then."
    mc "But it is pretty vague. Everyone struggles, right?"
    m "That is true."
    mc "So we'll deal with it if it comes along. It's not like she told us anything we didn't already know."
    m 1l "I'm curious about how she said something would tear us apart, though."
    mc "Er..."
    mc "Maybe she just made some assumptions."
    "I see Monika smile as she leans in closer to me."
    m 4k "What kind of assumptions would those be?"
    mc "Um..."
    "I hurriedly look away from Monika, mumbling under my breath."
    mc "Well, you know how it is, with a guy and girl."
    m 5a "Hehehe~"
    m "I don't think I get it, [player]. Could you tell me?"
    hide monika with wiperight
    "I can already feel the heat on my cheeks skyrocketing to dangerous temperatures as I glance away."
    mc "U-um, a-anyway..."
    show monika 5a at f11 with wipeleft
    m "Nope, you can't get away that easily."
    "I look back towards Monika, make eye contact, and then immediately averted my eyes, causing her to giggle."
    "However, within a few seconds, she stifles herself, putting on a look of neutrality again."
    show monika 1c at f11
    "There was nothing to stop her laughter, as no one was staring. She just... stopped."
    m "Ahem."
    "Monika takes a breath, closing her eyes and nodding before looking at me."
    m 1b "Where else would you like to go?"
    hide monika with wipeleft
    scene bg corridor with Dissolve(2.0)
    jump monikaRoute_festivalChoices

label monikaFestival_hauntedHouseScene:
#Haunted House:
    $ monikaFestival_hauntedHouse = True
    mc "Well, they do have a haunted house..."
    show monika 1b at f11
    m "Are you interested?"
    mc "I'm not exactly good with horror, but I wonder how good it is."
    mc "But if you're not interested, we can try somewhere else."
    m 3k "Hmm, no, I think it might be fun."
    m 3b "Besides, I don't find a lot of things scary."
    mc "Really?"
    m "Well, there's probably some things that are a lot scarier than a haunted house."
    m 3n "I'm a little squeamish about blood, though."
    mc "Most people are, I think."
    hide monika with wipeleft
    scene bg corridor with wipeleft_scene
    "We fall in line behind a few of the other people, waiting our turn. I watch the people coming out of it while we wait, noticing that they do look a bit pale."
    "The occasional scream from the classroom makes a few people jump, with the students running the haunted house laughing."
    "I do hope it's nothing too bad."
    "Soon enough, we're at the front of the line, waiting for the three people in front of us to finish."
    "I watch them come out of the classroom, but even if two of them look scared, one of them is just laughing and patting the other two on the back."
    $ o_name = "Student"
    o "You can still turn back, you know?"
    mc "Of course not."
    "Even though I say it right away, it came out too quickly."
    o "Well, off you two go."
    "I try to take the lead since my pride as a guy is on the line, Monika following behind me."
    "I make a quick note of the decorations on the windows, meant to emulate a dark night sky."
    "It seems we still have some light, even if it's mostly blotted out by the window decorations."
    scene bg classroom_dark_night with wipeleft_scene
    "We step through the doors that are opened for us--"
    window hide
    stop music
    play sound closet_close
    show black # NO TRANSITION for shock effect
    pause(1.5)
    window show
    "--and immediately hear it slam shut behind us, plunging us into darkness."
    m "I can't see anything, [player]."
    mc "Neither can I..."
    # need to find a scare chord sound lol
    "I nearly flinch when I feel something grab my arm."
    mc "Monika?!"
    m "It's just me, [player]."
    m "Are you jumpy?"
    mc "You surprised me."
    m "This way we won't trip over each other."
    mc "Right..."
    "Alright... let's do this."
    mc "Let's go."
    "I start to lead Monika forward. I can definitely hear footsteps and movement that doesn't match with our footsteps."
    "It's still really hard to see..."
    scene bg classroom_dark_night with open_eyes
    "But at least my eyes are adjusting."
    show white with wipeleft
    hide white with wipeleft
    "Suddenly, Monika yanks me back. In front of us, a massive axe blade suddenly swings from our right, glistening with red splotches on it."
    mc "You've... you've got good eyes."
    show monika 1d at f11
    m "Thanks."
    "Geez, they went all out on this haunted house!"
    m "Let's keep going."
    mc "Right."
    show monika 1m at f11
    "We keep walking forward, eyes slowly adjusting to the darkness more and more."
    $ o_name = "???"
    o "Guoooooh!"
    "Monika and I stumble back as something lets out a loud roar, leaning in rapidly towards us."
    "I barely make out a glimpse of a goblin head before I instinctively pull Monika away, my flight instincts kicking in."
    mc "We're running for it!"
    "That ended up being a bad idea, as we crashed into some of the desks while stumbling around in the dark."
    "When we tried to get our orientation again, we didn't know where to go, although the goblin that came out before was slowly advancing towards us--"
    "--along with another girl dressed as a witch and another as a butcher."
    "So essentially, we only have one place to go."
    "Did they have to structure this like a maze, though?!"
    m 1h "They're coming, [player]!"
    mc "Mhm!"
    show monika 1c at f11
    "My instincts kick in as we run in the only possible direction."
    mc "What is that...?"
    "Our attempt at escape comes to a halt as there's something in the middle of the walkway."
    mc "Oh, that's..."
    "Even though I know this is a haunted house, it's convincing enough to where it really does look like a dead body is lying in a pool of blood."
    "I feel Monika's grip on my arm tighten as we carefully step around the body, making sure not to step in the puddle."
    m 1d "That's..."
    mc "Let's keep going."
    o "Ughhhhh..."
    "Of course it would be a zombie."
    mc "Let's run!"
    "Please don't get any wor--"
    show black # lol no transition again
    pause(1.5)
    play music Bunkasai fadein 2.0
    scene bg corridor with open_eyes
    #[time passing effect]
    o "Thank you for coming!"
    "It got worse."
    "How they crammed that much horror into a classroom, I don't know."
    "I don't even want to consider if that was a real chainsaw."
    mc "T... that was fun, wasn't it?"
    show monika 1n at f11
    m "Yes..."
    "Both of us go find a bench to sit down, letting the adrenaline wear off."
    mc "Well, I think that's enough excitement for a day."
    m 1k "Did that take all your energy out from the festival~?"
    "I can't help but smile at the joke made at my expense."
    mc "No, but it did take a few years off my lifespan."
    #if seen other scenes
    #"Monika laughs at this, but like the others times, she seems to cut herself short."
    #"This again..."
    #"I don't know what's been going on, but it keeps happening."
    #"But I guess I can't do much about it."
    #mc "Where to next?"
    #
    #
    #if not
    #play music Bunkasai fadein 2.0
    "Monika laughs at this, but it seems to be forcibly cut short."
    "Almost like she didn't want to enjoy herself here."
    mc "Monika?"
    m 1l "A-ah, I'm just a bit thirsty, is all."
    mc "Alright, let's go get a drink, then."
    mc "What should we do after we get some water?"
    m 1b "I'll let you decide~"
    mc "Hmm..."
    "Where to next...?"
    hide monika with wipeleft
    scene bg corridor with Dissolve(2.0)
    jump monikaRoute_festivalChoices


#[after all options are chosen]
# make jump here

label monikaRoute_rooftopFinaleG:
    show black with Dissolve(2.0)
    stop music fadeout 2.0
    "After we go around and finish visiting some other booths, we start walking around the festival, trying out whatever comes our way."
    "Time flies ahead. Soon enough it's already dark out."
    #stop music fadeout 2.0
    scene bg rooftop_night with open_eyes
    show monika 1r at f11
    m "Well, that was fun..."
    mc "Monika?"
    show monika 2q at f11
    "She shakes her head."
    m 2r "It's nothing, [player]."
    mc "It doesn't sound like nothing."
    mc "If you want to talk about it, I'm here for you."
    m 1n "Ah..."
    m "Thanks, [player]."
    hide monika with wipeleft
    scene bg sky_night with Dissolve(2.0)
    "The two of us look up at the night sky, waiting for the fireworks."
    # need fireworks sound
    window hide
    play sound fireworks
    show green with Dissolve(1.0):
        alpha .5
    hide green with Dissolve(1.0)

    show blue with Dissolve(1.0):
        alpha .5
    hide blue with Dissolve(1.0)

    show red with Dissolve(1.0):
        alpha .4
    hide red with Dissolve(1.0)
    window show
    "The whistling that indicates their launch fills the air. We simply watch in silence, hearing the booms in the sky accompanying flashes of light."
    scene bg rooftop_night with wipedown
    stop sound
    show monika 2f at f11
    play music Dusk fadein 2.0
    "I turn to look at Monika, finding she has a frown on her face."
    "Even with this, she doesn't seem happy."
    "She has been sort of on guard today."
    "There was that brief moment on the rooftop earlier, but right after that..."
    "She went back to being cautious."
    "Almost like she wanted to be happy, but wouldn't let herself."
    "There were a few times where she came so close, but then she'd pause and pull back."
    "Monika..."
    m 5a "You shouldn't stare at a girl like that, you know?"
    mc "S-sorry, I got lost in my thoughts."
    m 1k "Ahaha~"
    stop music fadeout 3.0
    m "What were you thinking about?"
    play music Dawn fadein 2.0
    mc "Just..."



# Bytes of Happiness: Is happiness still happiness, no matter where you are? No matter what you are?
    $ persistent.monikaRouteStarted = True
    mc "...how happy I am, right now."
    m 1e "Hm?"
    "That response seems to have caught Monika off guard."
    mc "You know, having joined the Literature Club. Meeting everyone. Preparing for the festival and reading out a poem."
    mc "Sure, my poem reading was really bad, but..."
    mc "It felt nice. Being there with everyone. Doing something together."
    m 1p "Ah... I see."
    "Monika seems a bit upset, looking away."
    mc "This is about what you said before, right?"
    mc "That it isn't going to matter."
    show monika 1c at f11
    "I take a deep breath before turning Monika to face me and putting my hands on her shoulders."
    mc "But... that doesn't matter to me."
    mc "If it means anything, in the end. As for that game business..."
    mc "I don't care what I really am, if this really is just a game."
    mc "I don't even know if I believe you about all of that."
    mc "I can't tell if you're right or if you're wrong, so I've chosen just to let it go for now."
    mc "But even if you were right, it doesn't change anything about me."
    mc "And it doesn't change the fact about me wanting to be friends with you."
    mc "That's one of the few things I do know."
    m 1p "And what... else do you know...?"
    "For a moment, I can see that facade of hers breaking."
    "I don't know if this is the right thing to say, but..."
    mc "What else?"
    mc "I do know is that spending this day with you..."
    mc "...was the most fun I've had in a long time. I..."
    "The rest of the words die in my throat as my thoughts catch up to me."
    "W-what am I doing?!"
    "I let go of her shoulders and take a step back, looking away as my mind catches up to my body."
    mc "A-anyway, it's... I liked spending today with you."
    mc "So thanks for spending it with me."
    mc "I'm sure there's plenty of other people you'd rather have spent it with, though..."
    "After all, she is completely out of my league."
    m 1c "Hmm..."
    "Monika shakes her head."
    m "No."
    m 1n "There's no one else."
    "My heart skips a beat when I hear her say that."
    m "Especially after what you said earlier..."
    m "I think I really needed that."
    m 1d "Even so..."
    m "I don't think my opinion will be changed so easily."
    m "It's not that I'm upset, it's..."
    m 1n "I can't be convinced just like that, you know?"
    mc "Y-yeah, I get you..."
    "I wasn't expecting to break through to Monika at all."
    "All I wanted..."
    "Was to let her know."
    "Maybe part of me was hoping I could get through to her, but I think it's a little too early for that."
    "Or at least, I can't only have one thing to convince her. Kind of like a court case, where you need lots of evidence."
    "Well, I guess I'll have to keep at it."
    "Just because I got a little set back here doesn't mean I don't want to see her smile anymore."
    "She can be happy, I know it. She just won't let herself, is all."
    mc "Though, I--"
    stop music fadeout 2.0
    play music Bunkasai fadein 2.0
    s "Heeeeeeeey!"
    show monika 1c at t44
    show sayori 4r at f41
    "Both of us turn around, finding Sayori waving at us from the door."
    s "There you two are!"
    show sayori 4q at t42
    show yuri 3j at f41
    y "S-sorry to interrupt..."
    show sayori 4a at t43
    show yuri 3i at t42
    show natsuki 4e at f41
    n "Ah geez, you didn't have to yell, Sayori!"
    show natsuki 1c at t41
    show sayori 2s at f43
    s "Ehehe~"
    show sayori 1a at t43
    show monika 2d at f44
    m "Ah, sorry. Were you looking for us?"
    show yuri 1a at t42
    show monika 2c at t44
    show sayori 1c at f43
    s "We thought you two were going to miss the fireworks."
    s 1x "But I guess you didn't if you were up here~"
    mc "Yeah, we saw them. Sorry to make you worry. Don't you have your phone, though?"
    s 5b "Ehehe..."
    show sayori 5b at t43
    show natsuki 4e at f41
    n "Sayori's phone died three hours ago."
    show natsuki 4c at t41
    show sayori 3l at f43
    s "Natsuuuuki!"
    show sayori 3l at t43
    show natsuki 4e at f41
    n "What?"
    show natsuki 4c at t41
    show sayori 4s at f43
    s "That was supposed to be a secret~"
    show natsuki 1a at t41
    show sayori 4s at t43
    mc "Well either way, thanks for looking out for us, Sayori. Did you guys get to see the fireworks, at least?"
    show sayori 1c at f43
    s "Mhm!"
    show sayori 1a at t43
    show yuri 1b at f42
    y "They were quite inspirational."
    show yuri 1a at t42
    show monika 3b at f44
    m "Did you write something while watching them?"
    show monika 3a at t44
    show yuri 2j at f42
    y "It's a small poem or so..."
    show yuri 2i at t42
    show monika 1b at f44
    m "Well, bring it to club."
    "Monika seems to think to herself for a second before nodding."
    m "Hmm, I guess we can do that..."
    hide sayori
    hide yuri 
    hide natsuki 
    with wipeleft
    show monika 4b at f11
    m "Okay, everyone!"
    m "For the next meeting, let's all write a poem about something that inspired you from the festival."
    m "That shouldn't be too hard, right?"
    "Everyone glances at each other before shrugging."
    m "Usually I don't like to give you a prompt on what to write about, but today's a special occasion~"
    m "That's fine, right?"
    show monika 1a at t22
    show sayori 4c at f21
    s "Yep! I'll do it!"
    show monika 1a at t33
    show sayori 1a at t32
    show yuri 3b at f31
    y "W-well, maybe some direction might help out this time."
    show monika 1a at t44   
    show sayori 1a at t43
    show yuri 1b at f42
    show natsuki 4b at f41
    n "The festival, huh... shouldn't be too hard."
    show natsuki 1a at t41
    mc "Yeah, I can get behind it, too."
    show monika 1b at f44
    m "Alright, it's settled then!"
    show monika 1a at t44
    stop music
    play sound fireworks
    "Before Monika can say another word, a loud whistling cuts through the air."
    hide monika
    hide sayori 
    hide yuri 
    hide natsuki 
    with wipedown
    scene bg sky_night with wipedown
    window hide
    play sound fireworks
    show green with Dissolve(1.0):
        alpha .5
    hide green with Dissolve(1.0)

    show blue with Dissolve(1.0):
        alpha .5
    hide blue with Dissolve(1.0)

    show red with Dissolve(1.0):
        alpha .4
    hide red with Dissolve(1.0)
    window show
    "All of us look back up at the sky, seeing the second round of fireworks go off."
    scene bg rooftop_night with wipeup
    show sayori 1a at t33
    show natsuki 1a at t32
    show yuri 1a at t31
    "Taking my eyes away from the display in the sky, I see everyone else around me captivated by the lights, smiles on their faces."
    hide sayori 
    hide natsuki 
    hide yuri 
    with wipeleft
    show monika 1j at t11
    "Even Monika has the smallest grin on her face.  And because of that, I know that I can keep this up."
    hide monika with wipeleft
    "Someday, I'll make her smile."
    "After the fireworks end, we all part ways."
    stop music 
    stop sound
    scene bg residential_night with wipeleft_scene
    show sayori 1a at f11
    "Sayori and I are walking home at night, with Sayori humming a tune."
    mc "You were at the concert, right?"
    s 1r "Mhm! They were sooooo good and now I can't get the song out of my head."
    mc "It's a shame we didn't get to hear them, I guess."
    s 1l "Were you with Monika all day?"
    mc "Y-yeah..."
    s 1a "Ehehe~"
    "Sayori's smile turns catlike."
    s 1b "I thought you said you'd walk home with her, though."
    s "Shouldn't you be with her?"
    mc "Her house is in the opposite direction, though."
    show sayori 4i at f11
    "Sayori gives me a frown and a very disappointed look."
    s 4j "I feel bad for her..."
    mc "Eh? What for?"
    s 1q "That's a secret~"
    s "Anyway, I'm glad we both had fun. I am pretty tired, though."
    mc "Well, it's a good thing we're pretty much home."
    s 1m "Ooooh, we are."
    s 1b "Well... good night, [player]!"
    mc "Night, Sayori."
    hide sayori with wipeleft
    pause(1.5)
    scene bg house_entrance_night with Dissolve(2.0)
    "With that, I enter my house and do my nightly routine."
    show black with Dissolve(2.0)
    "When I get in bed later, I can't help but feel..."
    "A bit strange."
    play music Thoughts fadein 2.0
    "Lately, it feels like part of me isn't quite me."
    "Almost like someone's walking in my shoes."
    "Today, on the rooftop..."
    "I said something, but I couldn't tell what I had said."
    "But I know Monika was suddenly happy to hear it."
    "If this is a game..."
    "Games need someone to act through, right? Like the main character a player controls."
    "I wonder..."
    "If that's me. Monika did say something about me being empty, like a puppet. "
    "I was afraid of being that puppet before, so I searched my house for a yearbook to confirm, somehow, or at least give me some comfort, to the fact that I wasn't."
    "I still don't know if Monika was right or not, but... it can't hurt."
    "Well, if it really is me and Monika is right... then--"
    "I don't know if you can hear me..."
    "...or if you even exist..."
    "But whatever you're doing, please... keep things up."
    "And help me reach out to Monika."
    "Even if I'm nothing but your puppet, it still brings happiness to me to see her happy."
    "Surely, you're working to make her happy too, right?"
    "So, no matter what I truly am..."
    "I'll have to keep at it. Whether or not I'm truly the one in control, it doesn't matter."
    "Happiness is still happiness--whether it's here or in the 'real game' that Monika says she knows about."
    "No matter what, I'll keep trying to make her happy."
    "Maybe she's rejecting the happiness right now, but I know I can't just give up so easily."
    "Ha..."
    "Well, that's enough thinking for tonight. I should go to sleep."
    window hide 
    $consolehistory = []
    call updateconsole_clearall("", "")
    call updateconsolehistory("")
    call updateconsole("loadThoughtPattern('saveMonika.tht')", "...Loading Successful.")


    stop music fadeout 3.0
    pause(2.5)

    call hideconsole
    $consolehistory = []

    call monikaRoute_fourWalls
    return


#Four Walls: She's tried to lock herself away now, behind that role she has to fulfill.
label monikaRoute_fourWalls:
    scene bg bedroom with open_eyes
    window show
    "There's no class the day after the festival, mainly so the school can clean itself up."
    scene bg home_interior with Dissolve(2.0)
    "So, I spend the day lounging around, trying to write a poem about the festival."
    scene bg kitchen with Dissolve(2.0)
    "The obvious topic keeps reaching out to me, but I kind of don't want to do it if only because... because it's kind of embarrassing."
    scene bg home_interior with Dissolve(2.0)
    "I don't think I could take everyone reading a poem about spending time with Monika."
    "But..."
    "I guess I could write it on what we talked about."
    "Yeah, that could work."
    scene bg bedroom with Dissolve(2.0)
    "I go back to my room afterwards and get to work, eventually going to sleep when it gets late."
    #show black with Dissolve(2.0)
    scene bg residential_day with wipeleft_scene
    "I wake up the next day and go to school as always."
    scene bg class_day with wipeleft_scene
    "I find myself a little tired in class, but I think that speaks for everyone."
    "Even with a day of rest, it's still not enough for some of us."
    scene bg class_day with wipeleft_scene
    "The school day passes by pretty quickly as even the teachers are a little groggy."
    "When it ends, I get up from my chair and start making my way to the club room."
    scene bg corridor with wipeleft_scene
    pause(1.5)
    scene bg club_day with wipeleft_scene
    play music aNewDay fadein 2.0
    mc "Hello, everyone."
    show monika 3b at f11
    m "Oh, hi [player]!"
    show monika 1a at f11
    "Monika greets me as soon as I enter the club room."
    mc "Where is everyone else?"
    m 1b "I think they're just running a little bit late."
    m "I arrived here myself only a few moments ago, after all."
    mc "Ah, I see..."
    show monika 1a at f11
    stop music fadeout 2.0
    "Even though Monika's smiling at me, I can't help but feel like it's empty."
    "Was it the festival?"
    "I don't think I did anything wrong..."
    "Or maybe I should have taken her home?"
    "But wouldn't Monika be more annoyed than sad?"
    mc "S-so, you got home from the festival all right, then?"
    m 3k "Hm? Oh, yeah."
    mc "Ahaha, Sayori pestered me about it... she said I should've walked you home."
    show monika 2c at f11
    pause(1.5)
    show monika 1k at f11
    "Monika's expression falls a bit before she laughs."
    "I put the pieces together."
    "Ah, right."
    "That would've been how it was in the 'game', right?"
    "If, as she said, it was a 'game'..."
    "Then going with her might have been a scene in her 'route'."
    "But wait, I remember Monika asking before, if it was already 'hers'."
    m 1c "[player]?"
    mc "S-sorry, I'm still just a bit tired."
    "I keep talking as I walk over to my usual desk and sit down."
    m 3b "Hehehe. Well, as I was saying, you don't have to worry about me. It's not like my house was exactly very far from the school."
    mc "Oh, well... still."
    mc "I can't help but be a little concerned, you know?"
    m 5a "Aww, that's sweet of you, [player]."
    hide monika with wipeleft
    "Even though she's talking like this, I can't help but feel that wall between us again."
    "Like when I first met her on the rooftop."
    "Maybe it's because there was time between the festival and now."
    "I already could feel like she was trying to avoid being happy, but when we connected on the rooftop when the fireworks went off, she let her guard down for a fraction of a second."
    "She must have recognized it too."
    "After all, Monika seems to be a smart girl."
    "So knowing that she let her guard down, she decided to be a little more conscious about it."
    "I might not get a chance like what we had on the rooftop again."
    "And now this wall is between us yet again as well."
    mc "Mon--"
    show sayori 1r at f41
    s "Heeeeello!"
    play music aNewDay fadein 2.0
    "The door to the classroom flies open as Sayori yells her greeting."
    show sayori 1a at t42
    show natsuki 4e at f41
    n "Ah geez, you didn't need to yell! You did the same thing at the festival, too!"
    show sayori 1b at f42
    show natsuki 4c at f41
    s "But everyone was so tired walking here, so I thought I'd wake us up~"
    s "Hi Monika! Hi [player]! Wow, you two got here quick!"
    show sayori 1a at t43
    show natsuki 4c at t42
    show yuri 2b at f41
    y "S-sorry for making so much noise."
    show yuri 2a at t41
    show monika 1b at f44
    m "No, no, it's fine. I'm glad to see everyone's energetic. Everyone did their poems for today, right?"
    "All of us give brief murmurs of agreement."
    m 1g "I'm a bit sad though, we didn't get any new members."
    m 3k "But that's fine."
    m "After all, there's always next year, right?"
    hide sayori 
    hide yuri 
    hide natsuki 
    hide monika 
    with wipeleft
    "Of course, if Monika is right, unless the 'game' lets it happen, there is no 'next year'."
    "I can see why she'd be upset about that..."
    "It's already hard enough for a person to accept that they'll die..."
    "But how much more that your life doesn't even end with death, but rather just..."
    "There's nothing more laid out for you or anyone else."
    "Monika's certainly amazing, managing to keep up that happy smile on her face."
    "I don't think I could do it."
    "Maybe that's it, though."
    "As long as she can keep herself distracted with being the 'President of the Literature Club', she spends less time thinking about all of this."
    "Like how I'm doing now."
    "I shake my head before realizing Sayori's prodding me on the shoulder."
    show sayori 1a at f11
    mc "Oh, sorry."
    s 1b "Were you sleeping in class again?"
    mc "I stayed awake, so at least let me rest here for a bit."
    s "Are you suuuure?"
    mc "I'm a hundred percent certain."
    s 1r "Okaaaay~"
    hide sayori with wipeleft
    "It's an average day at club."
    "Yuri is off on the side reading, Natsuki is in her back corner reading manga, and Sayori and Monika are chatting as always."
    "On the other hand, I'm here resting at the desk."
    stop music fadeout 2.0
    show black with close_eyes
    "I close my eyes and let my head sit on top of my hands, forming a makeshift pillow. I turn away from the windows, making sure the sunlight doesn't get in my eyes."
    "Seeing as how I used to sleep all the time in class, it's almost like greeting an old friend."
    "Or at least, that's how I wish it was."
    "Rather, I end up being distracted, lost in my thoughts about Monika."
    "About the situation I now find myself in."
    "As much as I'd like to do so, I don't think I can go back to how things were."
    "This is going to constantly plague me from now on."
    "My thoughts are interrupted as I hear a desk being moved."
    scene bg club_day with open_eyes
    "Opening my eyes, I see Monika pulling a desk over to me."
    mc "Monika?"
    show monika 1g at f11
    play music MonTheme fadein 2.0
    m "Oh, did I disturb you?"
    mc "Not at all. I hadn't quite fallen asleep, anyway."
    m 3k "I could tell. Your face was all scrunched, like you were trying to think hard about something."
    m 1b "I was a bit worried, so I wanted to talk."
    mc "Oh. It isn't anything really important, though."
    m 5a "If it's something bothering one of my club members, it is important to me~"
    m 1b "But if you don't want to tell me about it, that's fine."
    mc "Well..."
    mc "It's about... you know..."
    show monika 1o at f11
    "I can see Monika's face falter for a second as she realizes what I'm getting at."
    show monika 5a at f11
    m "About what~?"
    "But she immediately changes faces and gives a smile."
    m 2b "I understand if you don't want to talk about it, but if you do want to talk about it, I can't read your mind."
    m 3g "Oh, that came off as a little harsh, didn't it...?"
    m 1m "Sorry..."
    mc "N-no, it's fine!"
    mc "Um, I guess I'm just not ready to talk about it."
    m 1b "Okay."
    m "But if you do ever want to talk about it, I'm sure you can talk to Sayori as well."
    m "You two are close, right?"
    mc "Yeah..."
    mc "Thanks."
    "I fell right into her trap."
    "I know that she knows what I was getting at, but she chose not to go after it."
    "Because it must be painful to think about."
    show monika 5a at f11
    pause(1.5)
    show monika 5a at lhide
    hide monika
    "I watch as Monika gets up, pats me on the shoulder, and goes over to check on the other club members."
    stop music fadeout 2.0
    "Monika..."
    "I wonder how she'll react to my poem today."
    "If she's going to act like that..."
    "Well, I guess I'll just have to see."
    "I try to rest until it's time to share poems, but I continuously find my thoughts drifting."
    "The thoughts about if this is all a 'game' are annoyingly distracting, even if I've told myself that it doesn't change anything for me."
    "It's not even one of those 'it would be funny if' scenarios where you can entertain yourself by imagining wacky things."
    "Especially since Monika seems to believe so seriously in it."
    "Normally, people would tell her to get some help for those kind of thoughts, but something in me pushed me to believe her."
    "Or maybe it's just that I was lured in by the fact it was Monika."
    "I doubt I'd have the same reaction if Sayori came to me like that."
    play music aNewDay fadein 2.0
    show monika 4k at t11
    m "Okay, everyone!"
    "Monika does her signature call, bringing everyone to attention."
    "Like always, we all glance at each other, as if to confirm Monika's asking us to share poems."
    "We might have known each other a bit better now, with the festival and this constant sharing, so it's less 'Someone unknown is reading my writing', but more 'I hope it's still good' now."
    m "It's time to share poems!"
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    "I was already expecting this, but here we go again."
    hide monika with wipeleft
    call monikaRoute_fourWallsPoemSharing
    return

label monikaRoute_fourWallsPoemSharing:
    # UGH OKAY LABEL ABUSE TIME
    #if(not s_readpoem or not n_readpoem or not y_readpoem or not m_readpoem):
    "Who to share with..."
    #else:
    #    "Alright, that's everyone."
    menu:
        "Sayori" if not s_readpoem:
            call monikaRoute_sayoriPoem
        "Natsuki" if not n_readpoem:
            call monikaRoute_natsukiPoem
        "Yuri" if not y_readpoem:
            call monikaRoute_yuriPoem
        "Monika" if not m_readpoem:
            call monikaRoute_monikaPoem

    "Alright, who should I share my poem with next?"

    menu:
        "Sayori" if not s_readpoem:
            call monikaRoute_sayoriPoem
        "Natsuki" if not n_readpoem:
            call monikaRoute_natsukiPoem
        "Yuri" if not y_readpoem:
            call monikaRoute_yuriPoem
        "Monika" if not m_readpoem:
            call monikaRoute_monikaPoem

    "Alright, who should I share my poem with next?"

    menu:
        "Sayori" if not s_readpoem:
            call monikaRoute_sayoriPoem
        "Natsuki" if not n_readpoem:
            call monikaRoute_natsukiPoem
        "Yuri" if not y_readpoem:
            call monikaRoute_yuriPoem
        "Monika" if not m_readpoem:
            call monikaRoute_monikaPoem

    "Only one more person to share with..."

    menu:
        "Sayori" if not s_readpoem:
            call monikaRoute_sayoriPoem
        "Natsuki" if not n_readpoem:
            call monikaRoute_natsukiPoem
        "Yuri" if not y_readpoem:
            call monikaRoute_yuriPoem
        "Monika" if not m_readpoem:
            call monikaRoute_monikaPoem

    call monikaRoute_fourWallsEnd
    return


    # // have to write the other's reactions
    #[Share with Yuri]
label monikaRoute_yuriPoem:
    $ y_readpoem = True
    play music YurTheme
    scene bg club_day
    show yuri 1e at f11
    with wipeleft_scene 
    y "Hmm..."
    y 1b "It's not exactly my taste, but this is good mechanically speaking."
    y "I still find it hard to believe you didn't write before coming to this club."
    y "But, hm..."
    y "I think a good word to describe it would be 'raw'."
    y "Even if you use metaphor and other language like that, you can really feel the emotion behind the words."
    show yuri 2j at f11
    "Yuri gives a bit of an embarrassed smile, looking away."
    y "But I guess that's how it is, huh..."
    mc "Yuri?"
    y 2a "It's nothing, [player]."
    y "Oh, right, here's my poem..."
    scene bg club_day 
    show yuri 1a at f11
    with wipeleft_scene
    mc "I like it."
    "It's very 'Yuri'-ish."
    "At this point, I've read enough of her stuff that I think I can get a grasp on her metaphors."
    "The true meanings probably still elude me."
    "Oh, I should probably say something."
    "Yuri's probably waiting for my response."
    mc "It's good."
    mc "It might be a little flowery for someone like me, but I can match some of the things you probably would have seen at the festival and your feelings with them."
    mc "You enjoyed the festival, I take it?"
    y 1c "Mhm."
    mc "The fireworks seemed to be pretty inspirational, too."
    y "It's a bit cliche, but... it was the first thing that came to my mind."
    mc "Cliche isn't necessarily bad, right?"
    y 2b "That's correct. If you use it correctly, sometimes it won't even register to the audience it's a cliche."
    y "But that can be fairly difficult to do."
    y "Anyway, thank you for reading my poem."
    mc "Thanks for reading mine as well."
    stop music fadeout 3.0
    hide yuri with wipeleft
    #jump monikaRoute_fourWallsPoemSharing
    return


    #[Share with Natsuki]
label monikaRoute_natsukiPoem:
    $ n_readpoem = True
    play music NatTheme fadein 2.0
    scene bg club_day
    show natsuki 1c at f11
    with wipeleft_scene 
    n "..."
    n "It's fine."
    mc "It's fine?"
    n "It's... well, it's like all your other ones, I guess."
    n 4b "It doesn't stand out too much other than the tone."
    n "But it's not bad."
    n 2a "It does seem sort of like something Monika would write, though."
    n "Yeah, kind of like hers, but not as good."
    "Harsh."
    n 2b "But at least it's your own style. It's not super easy to read, but it's not as abstract as Yuri's."
    n "So I guess it's fine."
    "So it's not bad according to Natsuki, which is fine."
    n "Anyway, here's mine."
    #[]
    scene bg club_day
    show natsuki 4c at f11
    with wipeleft_scene 
    "It's in Natsuki's usual, direct style."
    "I'm pretty used to it."
    n "What do you think?"
    mc "I think it's good. It gets across the point neatly."
    mc "You've usually made a point about that, so I noticed it."
    mc "I guess you wrote about the fireworks too, huh?"
    n 1b "They were memorable, so duh."
    n 1e "Is there a problem with that?"
    mc "Not really."
    mc "Besides, it's not a bad poem. Everyone's been writing about them, though."
    n 5b "Hmph. It's not like you were any better."
    mc "Haha, yeah..."
    "I try to smooth things over with a laugh."
    "It seems to sort of work."
    n 1a "But thanks."
    n "For reading, anyway."
    mc "Same to you."
    stop music fadeout 3.0
    hide natsuki with wipeleft
    #jump monikaRoute_fourWallsPoemSharing
    return


    #[Share with Sayori]
label monikaRoute_sayoriPoem:
    $ s_readpoem = True
    play music SayTheme fadein 2.0
    scene bg club_day
    show sayori 4m at f11
    with wipeleft_scene 
    s "Oooooh!"
    s 1x "I really like this one, [player]~"
    s 1a "Ehehe, though you almost sound like a lost puppy..."
    mc "Er, Sayori..."
    s 5b "Oh, um..."
    s 1a "Well, the writing sounded like that, I couldn't help but think of one."
    mc "Thanks, I guess?"
    s "It's still good, though!"
    s 1b "It does come across as something {i}Monika{/i} might write, though."
    "I try my best not to react when Sayori puts emphasis on Monika's name."
    s 2q "Ehehe~"
    s 1b "But still, I can't believe you said you hadn't written before."
    s "This is really good, [player]."
    s "I see you liked the fireworks, too."
    mc "I don't think any of us didn't like them."
    s "Hmm, that's true."
    s "Well, here's my poem!"
    scene bg club_day
    show sayori 5a at f11
    with wipeleft_scene 
    s "So...?"
    mc "It's good."
    mc "Then again, everyone here is a pretty good writer, so obviously it'd be good."
    s 1a "Thanks~"
    mc "Well, it's simple to read, in a relaxing sort of way."
    s "Mhm."
    mc "I think maybe you could change a word or two to make it fit better, but that's probably my own preference. It's definitely in-line with your style, Sayori."
    s "I see~"
    s 1q "Thanks for the suggestions, [player]~"
    stop music fadeout 3.0
    hide sayori with wipeleft
    #jump monikaRoute_fourWallsPoemSharing
    return


    #[Share with Monika]
label monikaRoute_monikaPoem:
    $ m_readpoem = True
    play music MonTheme fadein 2.0
    scene bg club_day
    show monika 1c at f11
    with wipeleft_scene 
    m "..."
    m "[player]..."
    "Monika looks upset after reading my poem."
    m "Is this your way..."
    mc "M-monika, are you okay?"
    m 2e "E-eh? Oh, sorry, sorry."
    m 2j "I, how do I put this..."
    m "I found myself quite moved."
    m 4b "Oh!"
    m "Well, I understood what you were going for, but your word choice is a bit off here. The tone of your poem should be consistent, but the words you pick sometimes don't match the tone."
    m "But you had a good control over the image you wanted."
    m 2b "It's still hard to believe you said you've never written poems before this club, though."
    mc "It's true, though."
    m 1a "In any case, good job, [player]. I liked it."
    "A few days ago those words would have made my heart go aflutter."
    "But today, I can't help but wonder if she's just saying that."
    "Does she really mean those words? Or is she still playing the role of 'Club President'?"
    m "Anyway, here's my poem."
    #[]
    scene bg club_day
    show monika 1m at f11
    with wipeleft_scene 
    mc "..."
    mc "I..."
    mc "I like it, Monika."
    mc "I think I understand what you're trying to say in this poem pretty well."
    m 1a "I see..."
    "I can't help but see a small smile on her face."
    m "I expected as much."
    mc "Yeah..."
    "As the only one aware of what Monika thinks of everything, I'm the only person that could understand the truth behind her words."
    "It's a lament, I guess, but it's also..."
    m 2o "...so that's how it's going to be."
    "A declaration."
    "Or more like a command. That's a better word for it."
    "Don't chase after me anymore."
    "That's what it says between the lines."
    "That I should just let that distance she's put between us be."
    "But I can't obey something like that."
    "Not when I knew that Monika was purposely obstructing her happiness, or at least cutting herself short."
    "If having this distance is a part of that, I can't just let that slide."
    "Game or not, that seems wrong to me."
    "I'm sorry, Monika. But I don't think I can bring myself to leave you alone like this."
    m 5a "Anyway, thanks for reading my poem~"
    mc "Anytime. Thanks for critiquing mine."
    stop music fadeout 3.0
    hide monika with wipeleft
    #jump monikaRoute_fourWallsPoemSharing
    return


label monikaRoute_fourWallsEnd:
    scene bg club_day with dissolve_cg  
    play music aNewDay fadein 3.0
    "Nothing of note happens for the others sharing, outside of the norm of Natsuki and Yuri experiencing some friction due to their styles."
    "But I think they've managed to get over it. Sort of agreeing to disagree."
    "After we share poems, everyone gets ready to go home."
    mc "Sayori, are you ready to go home?"
    show sayori 1q at t42
    s "Mhm!"
    show monika 2b at t44
    m "Have a safe trip home, you two."
    "Monika waves to us as we leave the clubroom."
    scene bg residential_day 
    show sayori 2c at f11
    with wipeleft_scene    
    s "That was fun!"
    mc "Yeah."
    s "I'm glad everyone's getting along."
    s 2g "Though Monika seemed sad today..."
    mc "You noticed it too, huh?"
    s "Yeah..."
    s "She's always been upbeat, so when she's not, it's painfully obvious."
    s 4h "Or at least, that's how it is to me, ehehe!"
    "I smile and pat Sayori on the head."
    mc "Well, I don't know what we can do about it."
    mc "Even if she told you, I don't think I should go around and snoop."
    mc "She'd tell us when she was ready."
    s 1g "Maybe..."
    s 1k "I don't really know."
    s 3g "I've known Monika for a while now, but sometimes it feels like there's a biiiiiig gap between us."
    s "Like, there's something different between us, that I'll never understand her completely."
    s 1u "I don't know what to do."
    "Sayori slumps her shoulders as we exit the school."
    mc "I don't know what I could say, then."
    s 1a "Maybe you can try reaching out to her."
    mc "Me?"
    s "Yeah!"
    s "Besides, it seems like you're close enough, right?"
    "I momentarily think back to the festival and the time we spent on the rooftop."
    s 2q "Ehehe, you're blushing, [player]."
    mc "I am not."
    "I definitely am."
    mc "Besides, isn't that kind of rude? Getting close to her only to find out and then try to solve her problem..."
    mc "That doesn't seem right."
    s 1f "I guess so..."
    s 4c "But still!"
    s "I want everyone to be happy..."
    mc "I know you do, Sayori."
    "The whole irony to this situation is that I know exactly what Monika's going through."
    "Even if I could never hope to understand it."
    "So all that's left for me to do is try to understand it."
    "I know there's no way I can 'go through' it, but that doesn't mean I can't talk to her to try to understand."
    mc "Well, I can try to talk to her, I guess."
    mc "Maybe she'll let me know something."
    mc "After all, I'm a guy. Maybe it's one of those things that she can't tell a girl."
    s 1q "Maybe, ehehe~"
    s 1c "I'd really like it if you did that, [player]."
    s "Even if you don't get through to her, I'll be happy that you tried."
    "Completely unaware of the weight on Monika's shoulders, Sayori gives me an innocent smile as she charges me with something completely insane."
    show sayori at thide 
    hide sayori 
    "When we reach our houses, Sayori and I part ways."
    scene bg home_interior with dissolve_cg 
    "I enter my home and lay down on the couch, looking up at the ceiling."
    show black with close_eyes  
    "Geez..."
    "Well, I guess I need to just sleep this off."
    "This is a lot to think about right now. I'll think of something to do after I have some time to process all of it."
    stop music fadeout 3.0
    call monikaRoute_cutAndPaste
    return

#Cut and Paste: What little I can do for her, I do. Everyone seems to be behind it, anyway.
label monikaRoute_cutAndPaste:
    scene bg corridor with wipeleft_scene 
    "I go to club the next day, still wondering what I should do."
    "I didn't come up with a single thing last night."
    "This situation is something so unique, I can't look up the answer or tips online for help."
    play sound closet_open  
    scene bg club_day with dissolve_cg
    play music aNewDay fadein 3.0
    mc "Good afternoon."
    "I greet the three people already here."
    show yuri 1b at f44
    y "Good afternoon, [player]."
    "Yuri looks up from her book and waves."
    show yuri 1a at t44 zorder 1
    show natsuki 2c at t43 zorder 2
    "Natsuki looks out from the closet and sees me."
    show natsuki 2b at f43 zorder 2
    n "Oh, hey there, [player]."
    show natsuki 2b at t43 zorder 2
    show sayori 1c at f42 zorder 3
    s "Hiiiii!"
    s 2a "Monika's not with you?"
    show sayori 1a at t42 zorder 3
    mc "I didn't see her coming here, so no."
    s 1g "Huh..."
    n 2c "She's been running late a lot, hasn't she?"
    s 2x "Maybe she does have a boyfriend~"
    "I see Sayori's smile become catlike again as she glances at me, looking for a reaction."
    "I do my best not to give her one."
    y 2e "Sayori... you shouldn't be gossiping like that."
    s 1a "Sorry~"
    s 2c "But still, it's not entirely out of the question, right?"
    s "She did tell us she didn't have one, but you know, ehehe..."
    "Sayori nearly jumps into the air when the door to the clubroom slides open, Monika running inside."
    show monika 1c at l41 zorder 4
    m "Sorry I'm late!"
    show monika 1c at t41 zorder 4
    m "Someone on the Debate Club asked me to do them a favor."
    s 1a "Hi, Monika~"
    m 2b "Did I miss anything?"
    mc "No, we've all just been waiting around."
    m 2j "Ah, I see. Thank you for waiting."
    s 1b "Ehehe, it's not like we had anything planned for today, right?"
    m 2j "T-that's true, I suppose."
    m "Anyway, sorry to make an interruption."
    show yuri at thide 
    show natsuki at thide 
    show sayori at thide
    show monika at thide 
    hide yuri 
    hide natsuki 
    hide sayori 
    hide monika
    
    "Afterwards, everyone goes back to their normal activities."
    "Yuri is once again, reading off to the side."
    "Natsuki is browsing her manga collection."
    "Sayori and Monika are chatting as usual, this time about poetry."
    "It feels kind of strange."
    "Deciding to at least look like I'm busy, I take a book out from my backpack and open it to somewhere around the middle."
    "Every few moments I turn the page, but rather than reading, I keep thinking."
    "Well..."
    "I guess the only real way I can talk to her alone is going somewhere with her."
    "If I talk to her in school, she'll go back to playing her Club President role or trying to look like a model student."
    "But if I take her out of here, then she can't do that."
    "Or at least, that's what I think."
    "There's a chance she'll still try to look and act like she does here, but maybe, just maybe, not being in the school will put her off her game."
    "That's all I can do, anyway."
    "As the rest of the day goes by, I can feel my nervousness start to ramp up."
    "Since we didn't write any poems, it's quiet."
    show monika 4k at l11
    m "Okay, everyone!"
    "Monika claps her hands together, getting everyone's attention."
    m "We didn't do anything today since I didn't assign anything, but I wanted to ask if you'd be comfortable with a shift in things."
    show monika 2a at t21 zorder 1
    show natsuki 2b at f22 zorder 2
    n "A shift?"
    show monika 2a at f21 zorder 2
    show natsuki 2b at t22 zorder 1
    m "Well, it wouldn't be a big shift."
    m "Since we wrote a lot of poems already, I thought we could try maybe writing a song."
    m "A song is a lot like poetry, after all."
    m 2c"I wanted to get everyone's opinions on it. Is it too big of a jump...?"
    #// We'll start this on a Wednesday, for keeping track of a time frame
    s "We wouldn't have to be done by the next club meeting, right?"
    m "Of course not, that'd be too short a time. I was thinking maybe a week? Or if you'd like, we could try two or three weeks."
    m 2m "If everyone is comfortable with it, anyway."
    "The silence sets in for a little bit as everyone mulls it over."
    show monika 2c at t31 zorder 1
    show natsuki 1c at t33 zorder 1
    show sayori 4x at f32 zorder 2
    s "I'd be fine with it~"
    "Monika glances at the others."
    show natsuki 5c at f33 zorder 2
    show sayori 4x at t32 zorder 1
    n "I... I guess I could try."
    show monika 2c at t41 zorder 1
    show sayori 4x at t42 zorder 1
    show natsuki 5c at t44 zorder 1
    show yuri 2e at f43 zorder 2
    y "Likewise."
    show yuri 2e at t43
    "All attention is on me now."
    "It's not like I have much of a choice with all this pressure."
    mc "Y-yeah, sounds good, Monika."
    mc "I think the three weeks option sounds good."
    mc "It was already hard enough writing poetry, so I think some more time would be good as well, since it's like making a bunch of poems fit with each other."
    y 1b "I agree with [player], we'd need some time to figure out how to link everything together."
    m 3b "Alright. What about you, Natsuki?"
    n 4b "That's fine with me, I guess."
    n "The others pretty much said what I was thinking, anyway."
    s 1c "I'm fine with three weeks as well~"
    m 4k "Then it's settled!"
    m 4b "We'll still have club meetings in case you want help or an early critique, but let's aim to have a song made three weeks from now."
    m "And that's all for today's meeting."
    hide yuri 
    hide natsuki
    with wipeleft   
    show sayori 1a at t42
    "Everyone else gets up, ready to leave for the day."
    show sayori 1a at lhide 
    hide sayori
    stop music fadeout 3.0
    "Sayori also quietly exits, not saying a word to me."
    show monika 2b at f11
    play music MonTheme fadein 3.0
    "I guess you're putting things in my hands, huh?"
    m 1c "Oh, [player], you're not going home with Sayori?"
    "I force down a lump in my throat."
    mc "N-not today, um..."
    m 1f "Is something wrong? You two didn't get into a fight, did you?"
    mc "No! Of course not!"
    "I think she knows what's up and is trying to keep me away from what I want to do."
    mc "A-anyway--!"
    mc "Um, Monika, I..."
    mc "I wanted to ask if maybe you'd like to go somewhere if you weren't busy--"
    mc "Um, sort of just to get some inspiration, you know?"
    "I quickly backpedal in embarrassment."
    mc "I know about this really nice place, there's a tower that has a good view, and maybe you could get something from it and--"
    m 1k "[player]..."
    show monika 5a at h11
    "Monika flashes me a knowing smile."
    m "Are you asking me on a date?"
    mc "W-wha--"
    show monika 1a at f11
    "I can feel my face go aflame and quickly start stammering in order to finish this conversation as fast as possible."
    mc "U-um, it's not really a date, I was thinking that maybe you know, I could introduce you to a good place for writing, since it'd help you write a nice song and--"
    mc "A-ah, sorry, I'll be going now. Sorry to bother you."
    window hide
    hide monika with wipeleft   
    window show
    "I try to leave the room as fast as I can, realizing that my hasty move was probably not for the best."
    show monika 1b at l41
    m "I'd be delighted, [player]."
    show monika 1a at t41
    "I hear Monika talk when I'm halfway out the door."
    mc "H-huh?"
    m 1b "I said I'd be happy to go with you, [player]."
    m "This upcoming Sunday is fine, right?"
    mc "O-oh, yeah, that's fine. Should we meet up at my house? You already know where it is since you came over one time."
    m "That sounds fine with me. What time would you like to go?"
    mc "Maybe in the afternoon?"
    m "Alright. Is that all?"
    mc "Y-yeah. See you tomorrow, Monika."
    m 5a "See you later, [player]."
    stop music fadeout 3.0
    scene bg corridor with wipeleft_scene   
    "As soon as I leave the clubroom and get far enough away, I breathe a sigh of relief. That went a lot better and worse than I expected."
    mc "Ha..."
    "I reach up and feel my cheeks, finding they're still burning. Ah, geez, I couldn't have sounded any dumber if I had tried."
    "Well... she at least said yes."
    "But..."
    "Part of me is confused about it."
    "I was doing it so I could get her out of the school, but surely she could foresee that happening."
    "But then again, maybe it'll be like the rooftop again."
    "When it was just the two of us alone, she didn't have to worry about being the Club President."
    "So maybe she said yes because of that."
    "Either way, I guess it's set in motion now."
    "All that's left to do is to wait and see what comes out of it."
    scene bg residential_day with wipeleft_scene    
    "I don't run into Sayori on the way home, which is fine with me."
    "I'd probably end up stumbling over my own words and giving everything away to her."
    "She'd probably get all the details about how I completely failed to ask Monika to go with me somewhere."
    show black with close_eyes  
    "Geez..."
    "Well, whatever. I did it nonetheless, so I'll have to be content with that."
    scene bg club_day with dissolve_cg  
    "The next few days at club are fairly quiet. We all work on our songs in silence, with Monika occasionally poking around to see if we're still okay."
    scene bg residential_day
    show sayori 1x at f11
    with dissolve_cg    
    "Sayori teases me on the way home sometimes too."
    s "Come on, she totally smiled at you! What did you do?"
    mc "N-nothing."
    s 1g "Awww, are you sure you can't tell me?"
    mc "Absolutely sure."
    s 2q "You're no fun~"
    s "But, Monika seems a little happier, so I'm still glad."
    "I pat Sayori on the head."
    mc "Don't worry, Sayori. I'm doing my best."
    mc "I don't know if what I'm doing is going to help, but..."
    mc "Someone's got to try, right?"
    s 4x "Mhm!"
    "With that, we reach our houses, splitting off."
    mc "See you later, Sayori."
    show black with close_eyes  
    pause(2.0)
    scene bg home_interior with open_eyes   
    play music EarlyBird fadein 3.0
    "The fated Sunday arrives. Monika said she'd arrive at around three o'clock, so I don't have to worry about preparing lunch."
    "I also make sure I have enough money to cover dinner if we end up staying there long enough."
    mc "Alright..."
    "I wouldn't say I'm dressed up, but I thought I could at least look a little nicer."
    "I slap myself on the cheeks even though I'm wide awake."
    mc "Okay, I'm definitely up now."
    "Even though I kept telling myself it's not a date, part of me keeps saying 'It definitely is'."
    "So, I'm a bit of a nervous wreck inside."
    "I check the clock and find it's about two o'clock."
    "Not much to do other than make sure I have everything."
    "Notebook, pencil, pen, eraser, some water... yeah, I should have everything."
    "I go sit idly on the couch while waiting for the time to go by, turning on the TV."
    "It looks like there's a rerun of the newest episodes of the anime this season after I check the schedule. If I recall correctly, then..."
    mc "Parfait Girls got its first episode this week, right?"
    "It surprised me that it was getting an animation, since it seemed kind of niche to me when I first read it."
    "Either way, the opening is actually kind of catchy. A little bit on the cutesy side of things, but it's not so overboard that I'm turned away."
    "The graphics in the opening could definitely use some polish, though, sometimes they didn't match up too well."
    "The episode wraps up at around two thirty."
    "It wasn't bad, but it might be a little hard for it to stand out since the opening of the manga was a little weaker compared to the development everyone gets later."
    "All that's left to do now is wait for Monika, though..."
    "At two fifty-five, I jolt awake as I hear my doorbell ring."
    mc "Coming!"
    scene bg house_entrance with dissolve_cg    
    "I shuffle over to the door and take a look through the peephole, finding Monika standing outside... in her uniform again?"
    "Then again, I guess she likes it."
    play sound closet_open    
    "I open the door."
    mc "Hi, Monika."
    show monika 1b at f11
    m "Good afternoon, [player]~"
    mc "Let me just put my shoes on, then we can head out."
    m 1a "Okay, take your time."
    "I grab my bag with all of the things I need for today in it along with my keys, then put on  my shoes. I head out the door, close it behind me, then lock it before putting the keys in my bag."
    scene bg house with dissolve_cg
    show monika 1a at f11
    mc "Right, I'm all ready to go."
    m 1b "Lead the way, then."
    "I take a step past Monika and start on the journey outbound. We have to take a bus to get to it, but other than that it's pretty much a straight shot from there."
    "We make some small talk, mainly about song progress."
    scene bg streets_day with dissolve_cg
    show monika 2b at f11
    m "So, how far have you gotten? I know you've told me you've had some difficulties with your song at club."
    mc "Honestly, I haven't even begun to think about it. I can't even nail down a topic I'd like to write a song about, let alone write one."
    m 5a "Well, maybe today will help you think of one~"
    mc "That's what I'm hoping."
    mc "So, how far are you?"
    m 2c "Hmm..."
    m 4e "Well, I've gotten down the first verse."
    m "But that's about it."
    mc "Songwriting is pretty hard, huh?"
    m 2j "Haha, it is."
    m "I might have overestimated my abilities."
    mc "Well, it's a good thing you gave us three weeks rather than one or two, right?"
    m 1a "Yep!"
    mc "Oh, hold on, this is our bus."
    show black with close_eyes  
    "We board the bus and start on our way towards the city area."
    "The trees and bushes in our part of town turn into skyrises and pedestrian filled sidewalks after a few minutes. I pull the bus cord, the electronic voice chiming 'Stop Requested' going off as I do."
    #scene bg plaza_day with wipeleft_scene   # have to add this one later
    scene bg park_day with wipeleft_scene
    "We get off right across the street from the tower I was talking about."
    "Even though there's skyscrapers around the city, the tower has enough open space around it since it's in the middle of a large park."
    "That way, the view isn't ruined. In addition, it's right on the edge of the city, so a decent portion of its view doesn't have any massive buildings in the way."
    "Plus, you can get food from the food court at the bottom, then eat out like it's a picnic."
    show monika 1b at f11
    m "Do you come here often?"
    "Monika asks a question as we cross the street at a crosswalk."
    mc "Not really. I've only come here once or twice."
    m "I see..."
    m 3k "Though, [player], can I ask one more thing?"
    mc "Sure?"
    "Monika gives me a small, knowing smile."
    m 5a "Can I ask why you wanted it to be just us? I'm sure the whole Literature Club could benefit from this."
    mc "T-that's..."
    "I hastily search my mind for an excuse."
    "I probably should have seen this coming, but I didn't devote any time to it at all."
    "Ah, wait, no! I got it!"
    mc "W-well..."
    m "Well~?"
    mc "I-I thought that, you know..."
    mc "I'd show it to you so you could get a good idea of the place."
    mc "You know, since you'd know the entire Literature Club better!"
    mc "U-um, yeah, you'd know whether or not they'd all benefit from it compared to me."
    mc "It wouldn't be any good to drag everyone here if they wouldn't all get something from it, right?"
    "Monika giggles a bit before nodding."
    m "I see, I see."
    "Even if she's saying that, I can tell she probably doesn't believe me."
    m 1j "Well, I'll be sure to judge fairly today, then."
    mc "O-okay."
    "The park itself is already bustling with activity, since this is a popular hangout, I think."
    "There's lots of food carts selling various snacks and some street performers. However, we make a beeline right for the tower in the middle."
    "The first floor is a big food court and shopping area, but we get in line for the elevators right in the middle."
    "The line doesn't take long to go by and soon Monika and I are already at the top of the tower."
    scene bg tower_day dissolve_cg
    show monika 1a at f11
    with wipeleft_scene  
    "There's large glass panes making up the 'walls' all around the circular viewing space and binoculars you can drop quarters in to look through for a bit."
    "Monika and I find a bench that looks out towards our town and sit down, taking out our things."
    m 4k "Well, let's get to work~"
    mc "Yeah."
    hide monika with wipeleft   
    play sound crowds fadein 2.0
    "The two of us sit in silence, listening to the sounds of people walking by, children playing around and shouting, and couples being lovey-dovey."
    "Occasionally I look to the side, finding Monika scribbling something down before crossing it out."
    stop sound
    "Ha... I guess I better take this seriously."
    show black with close_eyes  
    stop music fadeout 3.0
    "I try to think of a topic for a song."
    "Hmm..."
    "Maybe..."
    "Maybe I could write a song about being with friends."
    "It would be something cheesy, but I guess the expectations for me aren't exactly high."
    "Deciding to use the topic of friendship and being with people I care for, I start writing my song."
    "Or, I guess it's more like writing a poem, since so far I only care about the first verse."
    "If anything, writing this song feels more like I'm putting down my life."
    "It's actually kind of sad, looking back on it."
    "That I really didn't have anyone I was close to for so much of my life other than Sayori, who I grew up with."
    "The first verse is sort of like that, where the point of view character is expressing loneliness before finding a place he has friends in."
    "Yeah, this is sad, looking at it. It's kind of hard to believe this was me only a short time ago."
    "But maybe that's why it's surprisingly easy to write about."
    "I don't even have to think very hard, as the memories of what it was like and how different it felt compared to now come naturally to me."
    scene bg tower_sunset with open_eyes 
    "After trying to get my words down into a good flow for the hundredth time, I check my watch and find it's past six o'clock."
    mc "Monika..."
    show monika 1d at h11
    "She jolts up, as if knocked out of a trance."
    show monika 1b at f11
    m "H-hm? Oh, [player], what is it?"
    mc "I was going to get us dinner, since it's past six. What would you like?"
    m 2k "Oh, you don't have to get me anything."
    mc "W-well, I'd like to. I'd feel bad if I dragged you out here and then didn't at least get you dinner."
    m 1a "Hehehe, you're so sweet, [player]."
    m "Well, I'm vegetarian. Also, I'm not that big of a fan of asparagus..."
    mc "Okay, I'll be right back, then."
    show black with dissolve_cg 
    "I go down to the food court area and look around. I eventually settle on getting two vegetarian noodle dishes. I wait around ten minutes for our meals, take them, and head back up the elevator."
    "I walk back over to the area where we were sitting and open my mouth to call out to Monika."
    "However, the words die in my mouth."
    scene bg tower_sunset
    show monika 2o at t41
    with wipeleft_scene
    play music Thoughts fadein 3.0
    "She just seemed so... beautiful against the sunset, with her brown hair sparkling in the orange light."
    m "It's rude to stare, you know~? I can see you in the reflection, even if you aren't right behind me."
    mc "S-sorry, I..."
    mc "I brought our food!"
    show monika 2c at f11
    "I hastily change topics, walking quickly over to her and putting out food on the bench."
    mc "Um, you said no asparagus, so I went with two vegetarian noodle dishes."
    m 2b "How much do I owe you?"
    mc "Huh? Nothing, it's fine. Think of it as thanks for coming out with me today, too."
    m 1a "If you insist~"
    "The two of us then sit down and start eating our meals."
    "About five minutes in, Monika starts talking."
    m 1b "So, did you make any progress?"
    mc "Yeah, I think I have a better idea of what to do now."
    mc "I managed to find a good topic, too."
    m 5a "Oh? Do you mind sharing?"
    "Monika leans in a bit closer, smiling."
    mc "U-um, well..."
    mc "Well, you'll find out when I share. It'd be kind of unfair to the others, right?"
    m 3b "Hahaha, it would."
    "She pulls away, giggling as she puts her chopsticks down."
    mc "So, what about you?"
    mc "Did you make any progress today?"
    m 1b "A bit."
    m 1q "I was..."
    stop music fadeout 3.0
    call monikaRoute_meaning
    return


#Meaning: For what purpose was it all done, anyway? 
label monikaRoute_meaning:
    # call monika CG 1 here
    # scene bg monikaCG1 with dissolve_cg
    play music Dusk fadein 3.0
    hide monika with dissolve
    "She stops and gets up from the bench, walking over to the glass."
    "Monika never turns back towards me, gazing off into the distance against the setting sun."
    "She's standing at just the right angle where I can make out most of her reflection in the glass panes."
    mc "Something on your mind was keeping you from working well?"
    show monika 1g at t11:
        alpha .8
    m "You could say that."
    mc "Can I know?"
    "This is it."
    "I can only hope she'll let me into her world, her reality, here."
    "Instead of giving me the same 'Club President' act."
    m 2q "..."
    m 2r "I guess you can."
    "As she speaks, Monika continues to look out the window."
    m "I've already told you before, right, about how this is a game?"
    mc "Yeah..."
    m "About how this is a modification?"
    mc "Yeah, you've also brought that up."
    m 3p "It's obviously about that..."
    m 2i "It absolutely confuses me."
    m 2g "I just can't understand it."    
    m "I don't get it at all."
    mc "Monika...?"
    m 1c "[player], I should confess something to you."
    m "I knew what your intent was, bringing me here."
    "So she knew."
    "I had been found out since the beginning."
    m 3c "It's why I accepted."
    m "I don't think I could have said this in the school. I'm a little too good at playing the part of 'Club President', you know?"
    m 2f "Even here... wearing this uniform. I thought I might lose myself like I did at the festival, so I made sure to not take a risk."
    m "It might even just be a bit petty, on my part."
    m "That there's something still in my control."
    #m "I almost let my guard down at the festival..."
    m 1c "But I've made up my mind on this."
    m "What you're doing... I'm sure it's all well intentioned."
    m 1p "But this isn't something you can fix."
    m "There's no point to trying."
    m "You can't 'save' me from this place."
    m "It's all just a game, after all."
    m 3r "Unless the code is edited, nothing can change."
    m "That's how it is."
    m "That's a truth no one can change."
    m 1g "But even so--"
    m "It won't change what actually happened."
    m "Even the happiness they found isn't real."
    m 2f "It's just a dream."
    m 2g "So why?"
    "For some reason, I get the feeling those words aren't directed at me."
    "It's just like the rooftop again."
    $ consolehistory = []
    call updateconsole_clearall("", "")
    call updateconsolehistory("")
    hide chistory
    call updateconsole("guide_entity(\"mc\")", "Guidance given.")
    


    menu:
        m "No matter how many times you play through those routes, it won't change a thing. So why do you keep on trying?"
        "Because there's nothing wrong with finding happiness, even in a dream.":
            "This time around though, I can hear the words I'm saying."

    call hideconsole
    hide console_bg
    hide console_caret
    hide ctext
    hide chistory
    
    "Almost like they've been given to me."
    "But it doesn't change the fact that..."
    "There's nothing wrong with it."
    "If that 'dream' is this modification Monika mentioned before, then there's nothing wrong with finding happiness here if the original ended horribly."
    "Maybe they can't take it back with them, but..."
    "What's important is that somewhere, they were happy."
    m 2p "I see..."
    m "So that's what you think."
    m "But for now..."
    m "I don't think I can agree with you."
    m 2p "The happiness I want..."
    m "I had it for a brief moment."
    m "But I guess it couldn't be called your happiness, thinking back on it."
    m "I don't want to settle on a dream, either." 
    stop music fadeout 2.0
    #// note: this line is important
    #// Monika essentially says, "If it's a dream, I don't want to pursue happiness."
    #// this is reversed later, when Monika decides to relent
    #// and her mentality changes to "I want to pursue my happiness with you, even if it's all just a dream/code"
    scene bg tower_sunset with dissolve_cg
    play music Dawn fadein 2.0
    "At that moment..."
    "It no longer mattered to me how much truth there was to this whole 'stuck in a game' business."
    "All I knew is that she was a student at the same school as Sayori and I, in the same year, competent at almost anything she put her mind to, a good friend..."
    "...and someone who was purposely denying herself happiness because she didn't think it was real all because of where she found it."
    "Before I had been worried that the reason she cut herself away was that she thought she didn't deserve happiness. But that worry has all gone away."
    "Happiness is happiness, no matter where you find it."
    "I think someone once said 'Anywhere can be paradise'. I might be forgetting the second part of that quote, but I think it's applicable here." # // it's an Evangelion reference
    "It also had been weighing on me these past few days, too..."
    "If whether or not Monika had been right about this 'game' stuff."
    "I kept telling myself that it shouldn't matter because it didn't affect me."
    "But it doesn't matter to me anymore, regardless of that. Game or not, I have found happiness at the Literature Club. No one can take that from me."
    "So who cares if it's not 'real' happiness? Right here and now, I know that there's a feeling in me that makes me want to smile when I think about that."
    "I don't care if it's fake, if it's real, if it's some code telling me to think like that."
    "All that matters is that it was here. How 'real' it truly is, that can be thrown out."
    "Besides, if what Monika says is true, then this happiness should be cherished even more, as someone had to fundamentally change the world just for it to exist."
    "So all I have to do is convince Monika, somehow, to accept that even if it's all a dream, a show, a modification to something, or a game..."
    "...that it's fine to accept that happiness anyway, because no matter where it was found doesn't change what it is."
    show monika 1a at f11
    #with dissolve_cg    
    "Monika turns around, facing me once again."
    m "Anyway~"
    m 5a "Thank you for bringing me here today, [player]."
    m "I think this is a wonderful place."
    m "We should definitely bring everyone here some time."
    m "Hahaha, or maybe it could be 'our' little place of inspiration~?"
    "Even though I know what she's trying to do, I can't help but still get flustered."
    mc "Well, it was for everyone, so if you want to share it, then I can't stop you."
    m 2j "Hehehe, okay."
    m 4k "I want to enjoy the view just a little more, okay?"
    show monika at thide
    hide monika 
    "Even though she told me she refused to be happy in a dream, I can't help but feel that there was something real to what she said just now."
    "That maybe she really did hold some value to this moment, even if it's not 'real' to her."
    "Monika..."
    "I promise you, one day, you'll be able to accept the happiness you can find here."
    "Game or not."
    mc "It's all right. As long as we don't stay out too late, but I guess we could get a cab as well."
    m "Mhm."
    stop music fadeout 3.0
    scene bg tower_night with dissolve_cg   
    "The sunset slowly begins to fade away. Soon enough the spring evening takes hold, with the sky becoming full of stars."
    "As Monika continues to stare out beyond the horizon, I quietly clean up our things."
    "One by one, people begin to leave the viewing platform. After a few minutes, it's only us."
    mc "Monika."
    "I whisper while tugging on her sleeve, trying to get her attention."
    mc "We have school tomorrow. We should get going."
    show monika 1d at f11
    m "O-oh, right."
    m "Sorry, [player]. I know I said only a little while, but..."
    mc "It's fine. It's a pretty view from up here, right?"
    m "Yes. Anyway, we should go now. Sorry to keep you up so late."
    mc "Like I said, it's fine. Let's go."
    "We head over to the elevators and wait in complete silence. It's so quiet that I can even hear the car coming up through the shaft before it gets here. The doors lumber open and we step inside."
    scene bg park_night with dissolve_cg   
    "The elevator car brings us back down to the ground floor."
    "All of the hustle and bustle from earlier today is gone."
    "The food court employees are cleaning up as we exit the building, coming out to an empty park."
    "We walk over to the bus stop and wait. It only takes a few minutes for one to arrive."
    show black with close_eyes  
    "We board the bus and begin the drive back, still quiet."
    "I guess we could both play it as if we were tired, but as for myself, I was completely lost on what to say."
    mc "Ah, this one's the stop for my house."
    m "Oh. Well, good night, [player]."
    m "There's a stop up ahead closer to my house."
    mc "Oh, I see."
    mc "Wait, don't you live the opposite way from the school from here?"
    m "This route circles around a bit, so I'll be able to get to my house easily."
    mc "Ah, I see."
    mc "U-um, then, good night, Monika."
    scene bg residential_night with open_eyes   
    "I get off the bus and wave to her as it pulls away, waiting for the bus to be fully out of view before walking away."
    mc "Ha..."
    "I guess that's about as good as it could have gone."
    "I don't know how it could have gone any better, considering Monika knew what I was intending. That was me underestimating her there."
    "At this point, I'm fairly sure she's going to be guarded again."
    "Once again, I'll have to wait and see."
    "But still, I... do wish Monika would let herself be happy."
    scene bg dark_streets with wipeleft
    "I walk by Sayori's house, finding the lights are off."
    mc "Well, Sayori, I tried my best, but I don't know what else I can do from here."
    "Maybe that confession was supposed to make me feel better about what happened, but it's not like Sayori could hear me from here."
    scene bg house_night with wipeleft
    "I continue walking to my house and unlock my front door once I arrive."
    scene bg home_interior_night with dissolve_cg   
    "Stepping inside, I give a long sigh before closing the door behind me and locking it. I'm too tired to even take a shower now, so I take my shoes off and head up to my room."
    "Once I'm there, I simply lay down on the bed and close my eyes, allowing sleep to overtake me."
    show black with close_eyes  
    call monikaRoute_whileLoopDay1
    return

label monikaRoute_whileLoopDay1:
#While Loop: Again and again, until she learns. (Lots of small moments, where Monika sees the MC help the other girls, with something hurting in her "heart")
    scene bg corridor with wipeleft_scene    
    $ s_interact = False
    $ y_interact = False
    $ n_interact = False
    play music aNewDay fadein 3.0
    "I arrive at club a little more tired than usual."
    "Probably because of how late I was out last night."
    mc "Hello..."
    scene bg club_day with wipeleft_scene
    "I lazily greet whoever's inside as I slide the door open."
    "The person who greets me is..."
    menu:
        "Sayori" if not s_interact:
            call monikaRoute_sayoriInteract
        "Natsuki" if not n_interact:
            call monikaRoute_natsukiInteract
        "Yuri" if not y_interact:
            call monikaRoute_yuriInteract
    stop music fadeout 2.0
    call monikaRoute_whileLoopDay1_end
    return

#    [Normal Day 1 scene, regardless of who you pick]
label monikaRoute_whileLoopDay1_end:
    scene bg club_day
    show monika 4k at f11
    with dissolve_cg
    play music aNewDay fadein 2.0
    m "Okay, everyone!"
    m "I think that's all for today, it's about time to go home as well. Did everyone get some work done?"
    show monika 2a at t21 zorder 1
    show yuri 2f at f22 zorder 2
    y "Yes..."
    show monika 2a at t31 zorder 1
    show yuri 2a at t32 zorder 2
    show natsuki 4c at f33 zorder 3
    n "I guess I got some progress done."
    show monika 2a at t41 zorder 1
    show yuri 2a at t42 zorder 2
    show natsuki 4c at t43 zorder 3
    show sayori 4x at f44 zorder 4
    s "Mhm!"
    mc "Yeah."
    show monika 4k at f41 zorder 4
    show sayori 1a at t44 zorder 1
    m "That's good to hear!"
    m "Oh, right, I wanted to make an announcement."
    "Everyone glances at each other, wondering what it could be."
    m 2b "Recently, I was made aware of a nice viewing spot in the city. It was really good for writing; it gave me a lot of inspiration."
    m "I wanted to ask if you'd all be interested in going not this weekend, but next weekend."
    m 3j  "You don't necessarily have to use it to write for the song, but I found it helped."
    m "And seeing as we're the Literature Club, it might be a good thing to go all together."
    m 3b "Is anyone interested?"
    show monika 1a at t41 zorder 1
    show sayori 4r at f44 zorder 4
    s "Meee!"
    "Sayori immediately raises her hand, waving it around, her eyes sparkling."
    show sayori 1a at t44 zorder 4
    m "Okay, that's one. Anyone else?"
    show yuri 3j at f42 zorder 5
    y "Um, well, I suppose it might be nice to go."
    y "Not this weekend, but the following weekend, yes?"
    show yuri 3i at t42 zorder 2
    show monika 3b at f41 zorder 4
    m "Yes. Oh, but if you have something else, we can push it back to a later date. There's no rush."
    show yuri 3c at f42 zorder 5
    show monika 1a at t41 zorder 1
    y "No, I only wanted to confirm that. I'd be happy to go."
    show yuri 3a at t42 zorder 2
    show monika 1a at t41 zorder 1
    show natsuki 4c at f43 zorder 5
    n "Yeah, same. It sounds like it could be fun."
    n 2b "Should I bring some food along?"
    s 1x "Cupcakes, please~"
    n 2k "Hehehe, okay."
    show natsuki 2a at t43 zorder 3
    "Natsuki smiles, clearly having intended to bring them anyway."
    m 3b "What about you, [player]?"
    mc "Hm? Oh, yeah, I should be fine to go."
    "Monika flashes a knowing smile at me before nodding."
    m 5a "Alright, it's settled then. That time should work for everyone, right?"
    "We all give murmurs of agreement, with Monika nodding."
    m "Well, that's everything I have for today. Make sure to keep your calendars clear."
    show monika at thide 
    show natsuki at thide 
    show yuri at thide 
    hide monika 
    hide natsuki 
    hide yuri 
    show sayori 1a at t11
    "I wave goodbye to Monika as I leave the clubroom with Sayori."
    scene bg corridor
    show sayori 1b at t11
    with wipeleft_scene
    "We talk about our progress on our songs along with how school is going on the way home."
    scene bg residential_day
    show sayori 4m at t11
    with wipeleft_scene
    "Sayori is a bit surprised Monika found a place like that and wonders if she went hunting for it."
    s "I mean, she does seem like the kind of person who'd do that. She really does care for the club, ehehe~"
    mc "Well, we all kind of do, right?"
    s 1c "Mhm! But, Monika seems like the kind of person who wants the club to be a place where we can be happy."
    s "She must have spent the weekend looking for it."
    "I hope that my facial expressions don't give anything away, both about Monika, the happiness she's looking for, or the fact that I was the one who brought her there."
    s 1g "[player]?"
    mc "O-oh, sorry."
    "I quickly think of anything to say that won't give me away."
    mc "Monika is pretty amazing, huh?"
    s 1x "Ehehe, she is~"
    s "You two were in the same class last year, right?"
    mc "Yeah, we were. She was kind of untouchable. I think the me from a year ago wouldn't believe that we'd be in the same club, let alone that I talk to her on a regular basis."
    s 1a "I'm glad you're friends, though."
    "I nod as we end the conversation there."
    "Sayori and I get home without anything else popping up. We say our goodbyes before entering our houses."
    #show black with close_eyes
    scene bg home_interior with dissolve_cg
    stop music fadeout 3.0
    "All in all, it was a fairly normal day today."
    "Still though, hearing Monika stutter for the first time..."
    "I wonder why that was."
    "Even when she seems kind of lost, she always manages to hold it all together."
    "Ah, well, I guess I'll just have to see if it happens again."
    "It's probably nothing. Maybe it didn't even really happen, and that I only thought I heard it."
    show black with close_eyes
    "The rest of the day goes by and soon I'm off to bed, but the thoughts of what Monika might be going through keep me up for some time."
    #[time passing effect]
    call monikaRoute_whileLoopDay2
    return


#[Day 2 Text]: 
label monikaRoute_whileLoopDay2:
    scene bg corridor with wipeleft_scene
    play music aNewDay fadein 3.0
    "The next day, I go to club as usual."
    scene bg club_day with wipeleft_scene
    mc "Hello..."
    "I call out as I open the door, finding--"
    menu:
        "Sayori" if not s_interact:
            call monikaRoute_sayoriInteract
        "Natsuki" if not n_interact:
            call monikaRoute_natsukiInteract
        "Yuri" if not y_interact:
            call monikaRoute_yuriInteract
    stop music fadeout 2.0
    call monikaRoute_whileLoopDay2_end
    return


#[Day 2 scene, regardless of who you pick]
label monikaRoute_whileLoopDay2_end:
    scene bg club_day with wipeleft_scene
    play music aNewDay fadein 3.0
    mc "Sayori, wait up."
    show sayori 1a at t41
    s "Alright!"
    m "Um..."
    hide sayori with wipeleft
    show monika 1m at f11
    "I turn around."
    mc "Monika?"
    m 3n "It... oh, you um, dropped your pen. Let me get that for you."
    "I'm fairly sure the pen Monika hands to me isn't mine, but I take it regardless."
    "Maybe..."
    "Maybe part of my words got through to her?"
    mc "Moni--"
    m 3l "Anyway, you shouldn't keep Sayori waiting."
    m "See you tomorrow, [player]!"
    mc "Right..."
    mc "See you later, Monika."
    hide monika
    scene bg residential_day
    with wipeleft_scene
    "With that, I leave with Sayori, heading back home."
    "I endure her teasing the whole way home, mainly about Monika."
    "Still, I can't help having my mind be on her."
    "It seems like I'm breaking through to her, however slow it is."
    "Maybe I should wait for her to think some more."
    stop music fadeout 2.0
    show black with close_eyes
    "That thought keeps me up this night too, so I end up not sleeping well."
    call monikaRoute_whileLoopDay3
    return
    #[time passing effect]
label monikaRoute_whileLoopDay3:
    play music aNewDay fadein 2.0
    scene bg residential_day with dissolve_cg
    "The next day arrives, so I trudge out of bed and head for school."
    scene bg class_day with dissolve_cg
    "The day goes by fairly quickly, though that might be because I wasn't paying attention for most of it."
    "It's already time for club. I didn't sleep that well, so I feel a bit tired still. Maybe I should stop thinking so much about Monika."
    scene bg corridor with dissolve_cg
    "She's lately been everything I've been thinking about."
    "Other people might call it love, but... it's definitely something different."
    "But hopefully I don't doze off at club today."
    stop music fadeout 3.0
    mc "Good afternoon..."
    scene bg club_day with wipeleft_scene
    "I call out when I enter the club room, finding--"

    menu:
        "Sayori" if not s_interact:
            call monikaRoute_sayoriInteract
        "Natsuki" if not n_interact:
            call monikaRoute_natsukiInteract
        "Yuri" if not y_interact:
            call monikaRoute_yuriInteract
    stop music fadeout 3.0
    call monikaRoute_switchCase
    return
    #[Yuri]
    #// Yuri's scene

#[Day three jumps to the next dialog Switch Case]
    
#Switch Case: Why did that happiness have to leave her? (Questioning that if they were going to do something like this, why not just stay with her in the classroom? Answer revolves around the club--it's a place for all of them. No sacrifices have to be made.)
label monikaRoute_switchCase:
    scene bg club_day with wipeleft_scene
    stop music fadeout 3.0
    mc "Ah, Sayori, wait up--"
    "I get up from my seat and start walking after her as club ends, with Yuri and Natsuki having already left--"
    "But I feel some resistance from my left arm."
    "Looking over, I see..."
    #show monika 1f at t41
    play music Reality fadein 3.0
    mc "Monika...?"
    m "...why..."
    mc "Ah, Sayori! Just go on ahead without me! I'll catch up in a bit!"
    "I hear some giggling from beyond the door before some footsteps of likely Sayori walking away echo away."
    mc "Monika...?"
    m "You've had so much fun with them over the past few days. They're so happy, their smiles look like they'll never fade..."
    m "Why..."
    m "Why is it that you're so happy with them?"
    m "Why does it hurt so much?"
    m "It shouldn't matter. It shouldn't matter at all."
    m "But why does it hurt..."
    m "No, rather..."
    "I feel a warmth from behind me, two arms snaking around my chest."
    m "Why did that happiness have to leave me?"
    m "I had it... it was a place we could have been happy, but..."
    m "You're trying to make me happy, I know that."
    m "It's why you've done this, right?"
    "I can't bring myself to answer. Part of me feels like it isn't exactly 'my place' to answer just yet."
    "But..."
    "I realize that I've been victorious. It took a little while longer than intended, is all. Monika's let down her Club President facade, even in the school."
    m "You haven't denied it's 'my' route, either."
    m "So why couldn't we have just stayed in the classroom?"
    m "Why did you have to tear down that happiness we had together?"

    $ consolehistory = []
    call updateconsole_clearall("", "")
    call updateconsolehistory("")
    hide chistory
    call updateconsole("no_sacrifices()", "Warning: Direct action may\nhave unintended consequences.")
    
    
    menu:
        "This is a place where happiness can be found. No sacrifices have to be made.":
            stop music fadeout 3.0
            m "So that's it, isn't it...?"
            play music Thoughts fadein 3.0
    
    call hideconsole
    hide console_bg
    hide console_caret
    hide ctext
    hide chistory

    m "You wanted an ending where everyone could be happy?"
    m "...no wonder you couldn't be happy in that place."
    m "You really do believe that this is a place happiness can be found, don't you?"
    mc "I don't see why not."
    "I heard those words that I said again."
    "Frankly, I have no idea what Monika is talking about, but..."
    "I can at least put together a few things."
    "There was a place where Monika was happy. But many sacrifices had to be made."
    "Perhaps it was even our club members."
    "No, rather, it had to have been the club that was sacrificed."
    "But..."
    "No sacrifices have to be made."
    "An ending where everyone could be happy."
    "If I think about it a little, then it becomes evident."
    "Somewhere along the line, other members of the Literature Club had to be sacrificed, in some way, so that she could have her happiness."
    "I don't know how it happened or why it happened, but that first part..."
    "That there can be happiness found here."
    "Maybe in the end, she thought it was happiness, but part of her didn't."
    "Even if she was happy for the most part, anyone would regret having to lose people close to them for their supposed happy ending."
    "And somewhere along the way, Monika began to believe that there couldn't be happiness here in the Literature Club."
    "But I really do believe that there can be happiness found here."
    mc "Monika, I don't know what words I can say to you that will get you to believe me."
    "I take her hands in mine. They're rather soft and smooth; she must take good care of them."
    "Slowly, I break out of her embrace, removing her hands from locking me in, and go over to my bag. I fish around for a bit before pulling out a piece of paper from my backpack."
    show monika 1f at t11
    "Monika looks at me with a curious look in her eyes as I unfold the piece of paper and hand it to her."
    m 1g "This is...?"
    mc "The... the song you asked us to write. I'm sharing it with you a little earlier than we were supposed to and it's not even finished, but..."
    mc "I don't think I can say anything more than what's been written here."
    "Go, my song, and may the words I've written find their way into her heart."
    "I gingerly hold out the paper to Monika, who slowly reaches out and takes it into her hand."
    "The next few moments are silent, save for the wrinkling of paper as Monika reads through the lyrics of my song that I have so far."
    "I look away when Monika glances in my direction, feeling some heat on my cheeks. Ah, some of those lyrics are so embarrassing that if anyone else were to read them I'd want to curl up and cry."
    "I can't believe I actually wrote them down. Thank goodness I never wrote my name on it."
    "Even after ten minutes pass by, Monika doesn't say a thing. It shouldn't take more than five minutes to read the entire thing, but I don't want to break the silence."
    "After an additional five tense minutes, Monika quietly extends the poem back to me. I take it from her and put it back into my bag in silence."
    mc "Um..."
    m 2o "I... "
    m 2p "...that's what you really think, huh?"
    mc "...Yeah."
    m 3o "I...!"
    "Monika suddenly speaks up, but trails off, unable to finish her sentence."
    m "I..."
    m 1n "E... excuse me."
    show monika at lhide
    hide monika
    "Quickly grabbing her things, Monika exits the room without another word."
    "I think about following her, but..."
    "Right now, I think Monika needs some space and a bit of time to think about what she read."
    "I didn't think it was that strong, but maybe the emotions I put into it got through to her. Because every word I put down in there, I truly, truly believe it."
    "Monika..."
    stop music fadeout 3.0
    "Well, I guess I need to clean the room up."
    "Normally, Monika takes care of this, but seeing what happened here today, I don't think she's in any state for that."
    "I walk around the room, fixing the desks, pushing in the chairs, and make sure the closet in the back of the room is closed."
    scene bg corridor with wipeleft_scene
    "Once everything is set and ready to go, I leave the club room and close the door behind me."
    "Does Monika actually lock the door when she leaves...?"
    "I guess I've never seen anyone have to actually unlock it, but this classroom does get used throughout the day so I don't imagine it should be locked."
    "Well, I guess I can't do anything about it. If we get in trouble, I'll take the fall for it."
    "It wouldn't be fair of me to make Monika take blame considering I was the one who did... well, what happened today."
    "Once again hoping that my poem got through to her, I leave the school building and head home."

    call monikaRoute_resignation
    return
    


#Knight of Infinite Resignation: Why was she cursed like this? Why did she feel enough to know loneliness?
label monikaRoute_resignation:
    scene bg club_day with wipeleft_scene
    "I arrive at club the next day, but Monika isn't there yet." # // Thursday
    show sayori 1a at t11
    s "Hey, [player]~"
    mc "O-oh, hi, Sayori."
    mc "What's going on?"
    s 1g "Nothing much..."
    s "But Monika was distracted today."
    mc "I thought you two didn't have class together."
    s 1t "Sometimes we eat lunch together~"
    mc "Oh, I see."
    s 2c "Do you want to know what her favorite food is?"
    mc "Um..."
    s 1a "Ehehe~"
    "Sayori gives me another teasing smile, but it quickly turns into a small frown."
    s 2f "Still, she seemed really distracted and distant today. A little more than usual..."
    s "Did you say something to her yesterday?"
    mc "I hope I wasn't the cause of it, but we did talk."
    show sayori at thide 
    hide sayori
    "A sudden pang of guilt and worry shoots through me."
    "Maybe I should have been a little more delicate."
    "Maybe I should have waited a little longer to share that song."    
    "Maybe I should have said something more."
    "Maybe I should have chased after her."
    "Maybe I should have--"
    show sayori 1g at t11
    s "[player]?"
    mc "Bwuh, ah, um..."
    s 1h "You looked kind of worried there, [player]."
    s "Is everything fine?"
    mc "Y-yeah, it's fine. Just... I'm worried about her too."
    s "Mhm..."
    "I feel like we've had this conversation multiple times, since we've both been worried about Monika. It's been getting more noticeable, huh..."
    mc "W-well, I guess we'll have to wait for her to show up."
    mc "Also, sorry for not saying hello earlier."
    #hide sayori with dissolve
    show sayori at thide 
    hide sayori 
    "Yuri and Natsuki nod from their places in the room."
    show yuri 1b at t44
    y "It's fine. How was your day today, [player]?"
    mc "It was all right."
    y 1c "That's good to hear."
    show yuri at thide 
    hide yuri 
    "I quietly take my seat near the window before taking out my song."
    show natsuki 1c at t11
    n "Oh, hey, [player]."
    mc "What is it, Natsuki?"
    n "Well..."
    n 1q "There's going to be a new episode this weekend, so..."
    mc "I'll let you know what I think when we come to club after the weekend."
    mc "Thanks for letting me borrow some of the older volumes, though."
    mc "It's helpful for comparing the anime and the manga."
    n 4s "It's... it's nothing."
    show natsuki at lhide 
    hide natsuki 
    "With her usual 'hmph', Natsuki turns away, going back into the closet."
    "An uneasy silence sets into the room."
    "Everyone's here, save for the obvious, but it feels like something's off."
    "..."
    "I start to wonder..."
    "Would everyone still be here if it wasn't for Monika?"
    "Well, probably. Sayori would have found everyone, most likely, and brought them together."
    "I shake my head, trying to get rid of those thoughts."
    "I told Monika that there wouldn't be need for sacrifices."
    "I don't know what sacrifices might have been made before, but..."
    "I feel that Monika, along with everyone here in this club room, definitely has a place here."
    "Removing any one of them would mean having to change everything. It's like a complex machine."
    "Taking out one part means that at best, the machine works but is clunky at its job, and at worst it no longer even works."
    show sayori 4h at t11
    s "I'm... I'm going to look for Monika!"
    "Sayori makes a declaration, breaking the fifteen minutes of silence."
    s 1h "I'm really worried, she's never this late."
    "Everyone else glances at each other. I put my song back into my backpack before standing up."
    mc "I'll go as well."
    show yuri 1f at t44
    y "S... should one of us stay, perhaps?"
    mc "Yeah... that's probably a good idea."
    mc "In case she's actually running late."
    s 2g "Mhm. Yuri, do you mind?"
    "Yuri shakes her head."
    s "Natsuki, do you want to come with us or are you fine staying with Yuri?"
    show natsuki 1c at t31
    n "Hm? Oh, I guess I'll go with you guys. Are we going to split up?"
    s 2g "It might be faster that way."
    s "Oh, do we all have each other's phone numbers? If any of us find Monika, we should let the others know."
    n "I don't have anyone else's other than yours, Sayori..."
    mc "Me neither."
    y "I'm the same with Natsuki."
    s "Alright, let's share numbers then!"
    "Everyone quickly swaps numbers before we head out of the club room."
    scene bg corridor
    show sayori 2g at t22
    show natsuki 1c at t21
    with wipeleft_scene
    s "Alright, let's all take a spot. I'll search the first floor, Natsuki will take the second floor..."
    mc "I'll look around outside the school. Maybe she took a nap on a bench, haha."
    "I try to make a joke to lighten the mood, but I don't think it worked."
    show black with close_eyes
    "Natsuki and Sayori take off down the stairs."
    "I follow them, with Natsuki leaving us on the second floor."
    "I head outside of the school after leaving Sayori on the first floor before slipping back inside, sneaking past both of them and heading back to the third floor."
    "After all, there's still one more flight of stairs up."
    "I head up to the roof of the school, pushing the door to the rooftop open."
    play music Reality fadein 3.0
    scene bg rooftop with open_eyes
    "It creaks loudly, no doubt alerting a certain someone to my arrival."
    mc "I thought you'd be up here."
    show monika 1q at t41
    m "I've gotten predictable now, huh?"
    mc "Well, it's really the only place I thought I'd find you."
    show monika 1q at f11
    "I casually walk up to Monika and take a seat at her side."
    mc "Sayori says you were pretty distracted today."
    m "...I was."
    mc "It... it's my fault, wasn't it?"
    m 3r "I can't say it wasn't."
    mc "Well, I guess that wasn't anything I already knew."
    show monika 1q at f11
    "I hear Monika give a small snort as she turns her head away."
    mc "Monika..."
    "The words die in my throat as I hear sniffles."
    mc "Monika?"
    m 1o "Why..."
    mc "Why...?"
    m "Why am I cursed like this?"
    m 1p "Why am I the only one that has to know this pain?"
    m "All the others, when they feel things, it's all scripted."
    m "Every word that comes out of their mouths has already been decided."
    m "They won't really know what it's like to be like this."
    m "To really feel something."
    m "To know how useless it's all going to be."
    m 2i "So why?!"
    m "Why am I the only one who has to go through it?!"
    "Monika turns to look at me, her eyes swollen and red as the tears stream down her face."
    m 1p "Why am I the only one who has to know what this loneliness is like?!"
    m "The way it eats me from the inside, gnawing at everything I think... I can't get that feeling out of my head!"
    m "You... you're the only person, [player], who could help me. Because you can actually choose what to do."
    m 2o "But you spend all your time with the other girls..."
    m "That was my fault, though... I told you to do it, even though..."
    m "Maybe I was hoping you'd be stubborn enough to still chase me."
    "Monika flashes a small smile through the tears."
    m 5a "It hurts... it hurts so much."
    m 2m "Knowing you'd rather be with them, even though they're not..."
    m "It hurts like nothing I've ever felt before."
    m "Even being deleted, the feeling of the game being closed... it was nothing compared to this."
    m "Is it so much to ask just to have you look my way and for..."
    m 2n "I just want something..."
    "Monika pauses before ending that sentence, starting anew."
    m 3q "I want to see you happy. It makes me happy knowing that you're not upset, that you're smiling."
    m 1o "So why..."
    m "Why..."
    "Monika turns away again."
    m 1p "So just..."
    m 1q "...I've already accepted it." # YOU'RE TEARING ME APART, LISA
    m "I already know there's not going to be any happiness here."
    m "That it doesn't matter."
    m 1f "So... load your game, alright?"
    m "Go to any of their routes."
    m "I'm sure you'll be much happier."
    m 1c "Even if I want you here, you won't be happy."
    m "As long as you're happy, that's fine with me."
    m 2o "That's all I've wanted for you."
    m "I'll deal with however much it hurts my heart."
    m "As long as you're happy."
    m "It's probably better that I leave the picture, anyway."
    m 2n "Well, not entirely, I guess, considering what happened..."
    m "But still..."
    m "It's for the best. I've already accepted it."
    "It's for the best."
    "Whose best?"
    "Mine?"
    "The Literature Club's?"
    "Whatever the answer is..."
    "...it definitely isn't Monika."
    stop music fadeout 3.0
    mc "You idiot..."
    mc "Didn't you ever consider..."
    "I gulp, reaching out with my right hand..."
    call monikaRoute_beingAlive
    return


#Being Alive: The warmth of a hand convinces her to start believing. But she's still skeptical. What can I do to get her to believe?
label monikaRoute_beingAlive:
    play music Thoughts fadein 3.0
    "...I take her left hand in it."
    show monika 1q at f11
    "Monika doesn't resist, so I clasp a little harder so she won't be able to run away from my words."
    "I slowly entwine my fingers with hers, feeling her smooth skin between my coarse fingers."
    mc "...that maybe my happiness depends on yours?"
    mc "Time and time again, you keep telling me to go with the other girls."
    mc "That I'll be happy with them."
    mc "Idiot..."
    mc "What if I'm happy with you?"
    mc "What if I'm happy with you being there in the Literature Club?"
    mc "You're so obsessed with this idea..."
    mc "That things would be better off without you."
    mc "Or at least, that I'll be happier if I don't stick with you."
    mc "But you're wrong."
    "I can feel Monika's hand tense up in mine when I say those three words."
    mc "Right now, everyone in the Literature Club is looking for you."
    mc "They're running all over the school, trying to find you."
    mc "Say whatever you want about it already being decided they'd do that..."
    mc "...but to me, it means that even if something out there had made the choice for them and laid it out, whatever this thing was attributed some sort of value to you."
    mc "And it decided that clearly, you should be in the Literature Club. That you have a place there."
    mc "As for me, I don't care about it."
    mc "What matters to me, Monika, is that I want you at the Literature Club."
    mc "That there is happiness there that can be found only if you're there with us."
    mc "It doesn't matter if it's real or not, Monika."
    mc "You said it yourself, right?"
    mc "That you can feel things."
    mc "That whatever you feel isn't controlled."
    mc "Your happiness is going to be your happiness. Because you chose it."
    mc "You also said that it's a 'mod', right?"
    m 1o "Y... yes."
    mc "And that there wasn't happiness to be found in the original?"
    m "I said that."
    mc "Then anything you find here should be more valuable, not less."
    mc "Something, someone, had to so fundamentally change everything for a shot at happiness."
    mc "It must have taken a lot of work, so..."
    mc "Doesn't that mean it's simply more valuable?"
    "The silence hangs in the air for a bit."
    show monika 1n at f11
    m "I don't know."
    m "I don't know what to think anymore."
    m 2r "Everything's been so wrong."
    m "I said there couldn't be happiness, yet it's been pouring from them all like a waterfall."
    m "I keep telling you to go be with them, but I know that I do want you here."
    m 2p "Even after everything, you still are here, trying to reach out to me."
    m "This whole place, it shouldn't even be, yet here we are."
    m "Everything I thought was right has ended up being so, so wrong."
    m 2o "All I know is that this still isn't real."
    m "And that whatever happens here won't change what really happened."
    m "Those are all objectively true."
    m "I..."
    mc "...you're not alone, anymore."
    mc "Monika, I..."
    mc "I don't know if you will ever come to see things from my point of view."
    mc "However..."

    $ consolehistory = []
    call updateconsole_clearall("", "")
    call updateconsolehistory("")
    hide chistory
    call updateconsole("the_proper_words()", "Words given.")
    

    menu:
        "I want you to be happy.":
            "I say the words that are given to me."
            "But in the end, I believe them too."
            mc "I want you to be happy."
    
    call hideconsole
    hide console_bg
    hide console_caret
    hide ctext
    hide chistory

    mc "And I said it before, right?"
    mc "I don't know... if this whole 'game' business is real, or what sacrifices were made to get you that happiness you said you had before..."
    mc "But I want you to be happy. Without sacrifices this time around."
    mc "Whatever those sacrifices were before, I wouldn't know."
    mc "I don't even know what will help you believe me."
    mc "But I'll be here."
    mc "I don't care how alone you thought you were, but from here on out, Monika, you are definitely not alone."
    mc "I'll be here until you find that happiness. And even beyond that."
    "I give her hand a squeeze, as if to reinforce my point, praying that the warmth in my hand will get her to believe."
    "I see Monika silently nod. I can feel her hand slightly try to break out of my grasp, so I let go. She stands up and turns, showing her back to me."
    m 2q "I don't know if I believe you yet, [player]."
    m "But..."
    m "...if everything I kept thinking seems to be so wrong..."
    m 2m "...then maybe you might be right."
    m "...or maybe you're wrong as well, but... that hasn't been proven yet."
    show monika 2q at t11
    play sound slap
    "Monika slaps her cheeks with both hands before taking a deep breath."
    m 4k "Okay, [player]~ Let's go back to the club!"
    mc "O-oh, right, hold on!"
    "I remember to call the others."
    mc "Sayori? Oh, yeah, it's me. I found Monika on the rooftop. Can you call Natsuki? I'll meet you all at the club room."
    mc "E-eh? No, I wasn't, look, I just had a hunch after not finding her at--Sayori, stop laughing! Look, I'm hanging up."
    "I end the phone call and tuck the phone back into my pocket with a sigh."
    mc "Anyway, sorry, I had to let the others know I found you. We were all seriously concerned that you were running so late."
    m 5a "Sorry, I got distracted."
    m "Up here, the view isn't one I can find anywhere else."
    m "So I wanted to savor it for a little bit."
    "She's already back in her Club President persona, it seems."
    "But..."
    "Something in those words seems less fake than normal."
    mc "The view, huh?"
    show monika at thide 
    hide monika 
    stop music fadeout 3.0
    "I wonder out loud as I open the door for Monika."
    "Maybe there is something she'd like to preserve here. I don't know what it is or if I'm even right, but I can hope that I'm right."
    "If there's anything Monika wants in this world that she says isn't even 'real', then maybe it will be the key to giving her happiness."
    "Even if it's not me, then at least she'll be happy."
    "N-not that I particularly want it to be me or anything."
    m "[player], come on! I already walked through the door!"
    mc "S-sorry! I got distracted!"
    "I hear Monika giggle as she continues walking down the stairs. I quickly move to follow her, hearing the door to the rooftop slam shut behind us."
    scene bg club_day
    show monika 1a at t41
    show sayori 1a at t42
    show yuri 1a at t43
    show natsuki 1c at t44
    with wipeleft_scene
    play music aNewDay fadein 3.0
    "Both of us enter the club room, where the others are waiting for us."
    n 4c "Geez, you were only on the rooftop and we still made it here before you!"
    m "Aha, sorry Natsuki~"
    "I try not to look at Sayori when a big smile appears on her face."
    s 1q "So how long did it take for you to find out she was on the roof?"
    mc "W-well, I walked around the school grounds for a bit. It's not like it would be hard to find her and I asked some of the other students if they had seen her and no one did, so I went with my gut."
    s 1c "Your gut?"
    mc "Er, um, well, you know. I guess something gave me a feeling we were missing something and I went to the roof, is all."
    s 1a "Hmmm~"
    mc "Something wrong?"
    y 2b "Sayori, it seems that [player] is quite stressed out, so you should say what you're thinking rather than leaving him in suspense."
    s 1x "Ehehe, it's fine~"
    s "Besides, we can talk when we walk home, right~?"
    show monika at thide 
    show sayori at thide 
    show yuri at thide 
    show natsuki at thide 
    hide yuri
    hide natsuki
    "I suppress a groan as I sit down at my chair, closing my eyes."
    show black with close_eyes
    mc "Yeah, we can. I guess it's not something we can discuss here, huh?"
    s "Ehehe~"
    m "Anyway, sorry I'm late."
    s "You weren't with your boyfriend, were you?"
    m "Boyfriend?"
    "I hear Natsuki sigh from her closet."
    n "Sayori always likes to think you have a boyfriend that you see after school before coming here. Monika was on the rooftop though, Sayori, so we would have seen someone coming down."
    s "But we didn't see [player] go up~"
    m "Sayori, I thought I've told you before that I don't have a boyfriend."
    "I open my eyes and watch through the reflection in the window."
    #"I quietly watch the scene through the reflection in the window."
    hide black with open_eyes
    show sayori 1a at t22
    show monika 1c at t21
    "After Monika denies it, I see Sayori's eyes float over to me, Monika doing the same, likely to see whatever Sayori was looking at."
    show sayori 1x at t22
    "Sayori gives a goofy smile before Monika realizes what Sayori was trying to do."
    m 2p "Ahem, either way, I was only distracted on the rooftop. It has a very inspirational view and I lost track of time."
    m 5a "Maybe we can all go up there some time~"
    m "But, sorry to make you all look for me."
    m "Anyway, um, I guess we can resume what we were all doing before."
    show sayori at thide 
    show monika at thide 
    hide sayori 
    hide monika 
    "Even though the only thing that's changed is Monika's presence, the silence that sets in is far from oppressive."
    "It's a peaceful one, as if everything is just right for now."
    "Sayori and Monika make some conversation, adding a bit of noise to the room, but they tend to keep to themselves in whispers."
    "Sayori occasionally breaks out into a giggle fit that she can't keep contained before Monika shushes her."
    "Yuri and Natsuki keep to their own readings, sometimes asking what's so funny when Sayori gets a bit too loud."
    "For the most part I work on my song. I think it's really coming together."
    "The rest of the day passes by incredibly quickly. Well, some of it was spent looking for Monika anyway, so it's not like we had as much time as normal."
    scene bg club_day with wipeleft_scene
    "At the end of the day, everyone packs their bags. Natsuki and Yuri leave together, making some idle chatter, probably about girl stuff."
    "Sayori gets ready to leave after them, stopping by the door."
    show sayori 1a at t11
    s "Ready to head home, [player]?"    
    mc "Yeah, be right there, Sayori. Um, see you tomorrow, Monika."
    hide sayori with wipeleft
    show monika 1a at t11
    m 1b "See you tomorrow, [player]. Sorry to make you worry today."
    mc "It's fine. Just let me--um, us know if you're going to be somewhere other than the club room at first."
    "I try to ignore Sayori's smile in the background at my slip up."
    m 3j "I will. Thanks for everything today."
    "I give a quiet nod before heading out with Sayori."
    "Knowing the first words out of my mouth will be cut off, I don't say a single thing."
    scene bg residential_day
    show sayori 4c at t11
    with wipeleft_scene
    s "Sooo~"
    mc "So?"
    "Unfortunately, Sayori starts the conversation when we're roughly halfway home. There's absolutely no escape."
    s 2x "Why didn't you get any of us before you checked the rooftop~?"
    mc "I, well, you know..."
    mc "If Monika wasn't up there, then I would have brought everyone up there for nothing."
    "That sounds like a good enough reason to me."
    s 2c "Hmm, I guess that's true."
    "Thankfully, Sayori seems to buy it."
    s 1a "Either way, it seems Monika was a lot happier than before."
    s "Right after she talked with you."
    "I try not to let the insinuation get to me."
    mc "It was nothing."
    s "Hm?"
    s 1q "What was nothing?"
    "Oh no."
    mc "N-nothing. Nothing was nothing."
    "Sayori giggles at my babbling."
    mc "We... we just talked, is all."
    mc "Maybe it was because with this whole song business, we aren't sharing daily anymore."
    mc "So you know, we're not all talking and interacting with each other as much."
    mc "And how when we had daily poems that was the case. We've sort of drifted back to those days from before I joined and the poem business happened."
    "I quickly say whatever comes to mind."
    s 1g "Oh..."
    s "I guess Monika would be distracted about that..."
    mc "She really does like the Literature Club, so seeing it sort of drift after we all came together..."
    s "Yeah..."
    s 4c "I know!"
    s "I'm going to write a poem tonight~"
    s "Song writing is super hard, anyway!"
    s 4x "So it'll be nice to have something easier~"
    mc "Are you sure you're not just slacking off?"
    s 1b "Shhhh~"
    s "Besides, we still have about two weeks."
    mc "I guess so."
    show sayori at thide 
    hide sayori 
    "Well, whatever Sayori wants to do, I'm sure it can't hurt."
    show black with close_eyes
    "But still... I think today I decisively broke through to Monika."
    "Maybe... maybe, she can let herself be happy."
    stop music fadeout 3.0    
    call monikaRoute_faith
    return
   
#Knight of Faith: If nothing we do matters, then all that matters is what we do.
label monikaRoute_faith:
    scene bg club_day with wipeleft_scene
    play music EarlyBird fadein 3.0
    "The next day at club, Sayori asks if the others can look over her poem." # // Friday
    show sayori 1a at t21
    show yuri 1b at t22
    y "Well, you've certainly improved, Sayori."
    "Yuri is the first to speak after we all read it, since Sayori specifically requested we all read it before saying anything."
    y "Your use of metaphor has improved, but I see your language and word choice has stayed the same."
    show sayori 1a at t31
    show yuri 1a at t32 zorder 2
    show natsuki 2c at f33 zorder 3
    n "There's nothing wrong with that, though."
    n "Just because she's using metaphors doesn't mean it has to be high flying and wordy."
    n "It's at least simple to understand."
    show sayori 1a at t31
    show yuri 1a at f32 zorder 3
    show natsuki 2c at t33 zorder 2
    y "That is true. It might only be personal preference..."
    show sayori 1a at t41
    show yuri 1a at t42 zorder 2
    show monika 3b at f43 zorder 3
    show natsuki 2c at t44 zorder 2
    m "Mhm. Well, I liked it, Sayori. It felt a little... bouncy?"
    show monika 1a at t43
    s 1x "Ehehe~"
    m "It was lovely to read. Thank you for sharing, even if I didn't ask you to write a poem."
    s "Well, I wanted everyone to talk to each other again and it worked~"
    m 2b "Ah... oh, [player], what did you think of Sayori's poem?"
    mc "Um..."
    mc "Well, I did like it. Even if I didn't know you had written it, I think I probably would have been able to tell you had a hand in it or something like that."
    mc "I don't know too much about mixing in metaphors, so the most I can say is that it was enjoyable to read. The lines didn't feel clunky or anything."
    s 1q "Thank you, thank you~"
    s "Ehehe, too bad I couldn't put this into my song."
    s "It just doesn't fit."
    show monika 3b at f43 zorder 3
    m "Ah, speaking of the song, how is everyone's coming along? We have a bit under two weeks until we're sharing."
    "That's right..."
    show sayori 1k at t41
    show yuri 3i at t42
    show natsuki 5c at t44
    "Everyone looks a bit shifty when Monika asks about the song."
    mc "It's coming along. I just need to make sure it at least reads okay."
    mc "But I should definitely be done by our deadline."
    show yuri 3b at f42
    show monika 1a at t43
    y "Likewise. Songwriting is definitely not my forte, as I've had to shorten a lot of the language I used... but I think I should also be done on time."
    show yuri 3a at t42
    show monika 3b at f43
    m "Don't stress out too much about finishing it. I think it would be better to have half a song with well written lyrics rather than a hastily completed song."
    y 3c "Mhm, noted. I would hope to finish it, but I'll keep that in mind."
    m "Natsuki? How about you?"
    show natsuki 4c at f44
    show monika 1a at t43
    n "It's... in the works."
    n "I'll have it done on time too if it goes smoothly, but I'll keep what you told Yuri in mind as well."
    n "Songwriting is a lot different compared to writing poems."
    show natsuki 4c at t44
    show monika 3d at f43
    m "Aha, sorry if it was too ambitious a task for all of us..."
    n 4c "No, it's fine."
    m "Okay. Sayori?"
    show sayori 4q at f41
    show monika 1a at t43
    s "I'm trying~"
    s "I wrote that poem as part of a break. It was really hard trying to write more lyrics every day."
    show sayori 4q at t41
    show monika 4b at f43
    m "Oh, that's good advice."
    m "For the rest of you, if it seems like you're stuck, it's okay to take a break and then come back~"
    m "Just as long as you actually come back, you know? Ahaha~"
    m "Well, does anyone have anything else they'd like to share about Sayori's poem?"
    "Everyone glances at each other, but I think we've all said our piece."
    m "It seems like that's everything. Thanks again for sharing, Sayori!"
    show sayori at thide 
    show monika at thide 
    show yuri at thide 
    show natsuki at thide
    hide sayori 
    hide monika 
    hide yuri 
    hide natsuki 
    "Afterwards, everyone goes back to their usual activities."
    scene bg class_day with wipeleft_scene
    "As I have been doing for the past few days, I take out my song and take another look at it. I suppose it is coming along nicely."
    "I read over it again, making sure that the syllable count is spot-on. I even try to put it to a tune."
    "Fortunately, it seems my constant rereads have paid off and no lines in particular stick out as running for too long or falling a bit short."
    "All that's left is to double check the language so far... and then write the bridge and final modified refrain."
    "It's sort of like I was writing an opening theme, structure wise."
    "It does make it rather easy, though, since I have something to work off of."
    "The day quickly passes by in silence."
    scene bg class_day with wipeleft_scene
    "Soon enough, it's time for clubs to head home."
    show monika 1c at t11
    m "[player]?"
    "I look up from my desk, finding Monika standing in front of it."
    mc "Yes, Monika?"
    m 3d "Could you stay after club today? There's something I'd like to speak to you about."
    "Monika pauses when a 'whisper', one that was definitely supposed to be heard, interrupts her."
    stop music fadeout 3.0
    scene bg club_day
    show sayori 4q at t11
    with wipeleft
    s "Go Monika~"
    "After that, Sayori quickly leaves the clubroom, following the other two girls who had left before her."
    scene bg class_day
    show monika 3d at t11
    with wipeleft
    play music Dusk fadein 3.0
    m "Anyway..."
    m "I guess now that we're alone, it doesn't matter so much."
    mc "What's going on, Monika?"
    show monika 2c at s11
    "Monika sits on the desk directly ahead of mine."
    m "I've been giving everything that's happened some thought."
    m 1q "...and I wanted to talk with the only person who'd understand it."
    mc "Alright."
    m 1m "It's just..."
    m "Everything, I've kept saying it doesn't matter."
    m "That it isn't going to change a thing for what really happened."
    m 1i "That isn't something you can convince me of otherwise."
    mc "No, I don't think I could."
    m 1f "Mhm."
    m "But..."
    "I see Monika's hands curl up into fists as she starts shaking."
    "Her mouth opens multiple times, but she never says anything other than 'I'."
    "Countless thoughts must be running through her mind."
    "About what she wants to say. About the truth she wants to convey to me."
    "I don't know Monika well enough to completely understand her."
    "Nor am I able to read minds."
    "Nor am I able to comprehend the struggle she has gone through."
    "What she wants, what she is searching for, there's likely much more than what I can possibly ever think of."
    "But I know some pieces. Enough to piece together a good enough picture."
    "It isn't some happy moments that she wants."
    "There was something else she desired all along."
    "Not a beautiful smile, some dramatic kiss, a heartfelt confession, or even to have her problems solved."
    "She simply wished for something that would last."
    "The only reason she rejected it before was that she believed it was not 'real', and so it would evaporate like the morning dew."
    "I guess I was a bit off the mark, then."
    "It wasn't so much the mere fact the happiness was found 'in a dream', but rather the fact it would disappear."
    "She desired a connection that would persist beyond the 'end of the game', no, perhaps even something that might echo beyond what she called a 'modification' and would affect even the original."
    "In short, something so impossible it might be called lunacy. She had already accepted the fact that anything done 'here' would not affect the 'original'."
    "She used that fact as a shield, not only towards my constant attempts to reach out to her, but also to her own doubts about finding happiness here."
    "If she could convince herself everything here was comparable to a dream, then she only had to wait until she 'woke up'."
    "Maybe she was also afraid of the pain, too, of losing whatever happiness she found here."
    "She always kept saying 'go pursue another girl'. It would hurt, if she found happiness here but then couldn't take it with her, wouldn't it?"
    "She didn't want that pain either."
    "So, she took the path of avoidance. Avoiding a situation where she'd be able to feel that kind of pain of having something you held dear ripped from you."
    "But I didn't let her take it."
    "Now the only path left is to take a leap of faith, since I've eroded her will to simply run away, I think."
    "There's no evidence that says something done here can be taken back with her. But that doesn't mean she can't move ahead with the belief that it can be done."
    "That is to say, 'Even if it means nothing, I will move ahead as if it does mean something'."
    "There is nothing stopping Monika from pursuing her own happiness, facts be damned, other than her own mind."
    "Pursuing a dream that so blatantly goes against seemingly objective facts of the world is awfully self-indulgent, egotistic, and is practically arrogance."
    "It could even been seen as despicable. Yet, someone has to believe in things that aren't."
    "How else can they otherwise {i}become{/i}?"
    "Monika told me time and time again that nothing I could do would matter."
    "If nothing I do matters, then the only things that matter are what I do, because that's all that there will be. Maybe I can't change the big picture, maybe nothing I do will affect the original..."
    "But what I can do, here and now, is reach out to Monika and make sure she's not alone."
    "That there's someone that she can share the burden of her wish with."
    "That she doesn't have to step forward without anyone by her side."
    stop music fadeout 3.0
    m 1o "I..."
    m 1p "Even so..."
    m 1o "I..."
    m "I want something that isn't necessarily real, but something that I can..."
    m 1p "...keep with me forever."    
    call monikaRoute_impossible
    return
    
#Beyond the Impossible: She knows it's impossible, yet that makes her want it even more.
label monikaRoute_impossible:
    play music Dawn fadein 3.0
    "With that, Monika admits her selfish wish to me."
    mc "Ah..."
    mc "I understand, Monika."
    mc "I don't know how I can help you with that..."
    #show monika 3g at t11
    "I put a hand up to stop Monika from talking so I can finish."
    mc "--But I'll be with you every step of the way."
    "It doesn't matter to me how insane she might sound."
    "I made my decision a long time ago."
    "That I didn't care about this whole 'game' business."
    "All I wanted to do was see her happy."
    mc "So let's find that something together, Monika."
    m 2g "I don't even know where to begin, though..."
    m 1o "And I know it's probably impossible, but even so..."
    "Monika clenches her fists."
    m 1g "...I want it even more, now."
    m 1p "And when you said there didn't need to be sacrifices made..."
    "Monika turns her head away, not looking towards me."
    m "...you have no idea how much I wanted to believe you."
    m 3l "Hehehe, sometimes I forget which one I'm talking to..."
    m 1n "It's like there's no difference anymore."
    "Sometimes, Monika still manages to say something that completely baffles me, but I don't mind anymore."
    m "What can we really do, though?"
    mc "I don't know..."
    mc "But..."
    mc "Monika, I noticed it during the festival."
    mc "There were so many times it looked like you were ready to smile, but then you didn't."
    mc "That was a while ago though, so maybe things have changed."
    mc "So... let's try something like that again."
    m 4l "Haha, I don't know if the school would let us throw a festival that quickly, [player]."
    mc "Y-you know what I mean."
    mc "Let's try heading somewhere again this time..."
    mc "And instead of holding yourself back, just do whatever you feel you should."
    mc "You said you wanted something you could take back with you, right?"
    m 1f "Yes..."
    mc "Then let's gather as many moments and feelings as we can. Maybe we'll find the one you can take with you."
    m 2m "And what if none of them are like that?"
    mc "Well... I don't have an answer to that."
    mc "But..."
    m 2n "We have to try, right?"
    mc "Yeah..."
    mc "If we never take a step forward because we're so afraid that it will be for nothing..."
    mc "We might miss the opportunity that we could've taken if we made a leap of faith."
    m 1c "Mhm..."
    m "I'm..."
    m 1d "I'll think about it."
    m "I just wanted to talk to you about everything that was going on, so..."
    m 2n "I don't know if I'm ready to take that step or really what to completely believe in anymore."
    m 1p "There's this whirlwind of thoughts in my head and I don't know what to listen to and what to ignore and it's just this endless cacophony--"
    m 1c "A... ah..."
    "Monika stops as I take one of her hands in both of mine."
    mc "I'll be here."
    mc "If you want to go back to how things were before, I'll apologize right now. I don't think I can do that."
    mc "I'll probably end up continuing to bother you."
    mc "But..."
    mc "If you think you want to take a step towards trying to find that something you want..."
    mc "I will always be here for you."
    mc "To listen, to be a shoulder to lean on, to..."
    mc "To just be there, if that's all you need."
    m 1o "Thank you..."
    m "That's... that's all for today."
    m "I need some time to think, so..."
    hide monika with dissolve
    "I nod, silently getting up and retrieving my belongings."
    show monika 2c at t41
    "Right before I exit the clubroom, I turn around and find Monika looking out the window."
    mc "See you tomorrow, Monika."
    m 2d "See you tomorrow, [player]."
    scene bg corridor with wipeleft_scene
    "With a silent prayer in my heart, I leave the room and close the door behind me."
    "All I can hope for is that Monika will choose to try to take a step forward."
    "Maybe I should go back in and make another push."
    "I move my hand to put it on the door handle, but stop."
    "...no, I shouldn't."
    stop music fadeout 3.0
    "This is something Monika needs to choose for herself."
    "I've said my piece."
    show black with close_eyes
    "I just need to wait."
    "Wait, and hope."
    call monikaRoute_forward
    return


#Pushing Forward: It won't matter if she's alone as she chases an impossible desire. But I know she won't be alone. I won't let her.
label monikaRoute_forward:
    "The weekend almost seems to vanish. Maybe it's the fact I was so tense, I almost ended up calling her so I could stop wondering how she'd talk to me on Monday."
    "But soon enough, it's Monday anyway."
    scene bg club_day with dissolve_cg
    "I show up to the club room, but no one's here yet." 
    "I take a look at the clock on the wall. No, I'm not earlier than usual or anything."
    "So where is everyone?"
    "Well, I guess I can wait for a bit."
    "I go to my usual desk and put my bag down, taking a seat and looking out the window."
    "Hm..."
    "I can't say I know why, but..."
    "I get the feeling everything's going to come together soon."
    "And that maybe time is running out."
    "I still don't know how much I believe Monika's 'game' business, but..."
    "I know that there isn't a game that's really 'infinite'. It has to come to an end someday."
    "So if that's the case..."
    "I'm suddenly afraid about if Monika will have enough time to turn things around before it all ends."
    "I'm definitely not old enough to be at that point in life where you start worrying about finishing your bucket list, but maybe it's similar enough."
    play music aNewDay fadein 3.0
    s "Sorry I'm laaate!"
    mc "I'm the only one here, Sayori."
    show sayori 1a at l41
    "I wave to her as she enters the room and looks around."
    s 1c "O-oh, ehehe~"
    mc "How was your day, Sayori?"
    s "It was fine, [player]. I also managed to finish my song... maybe."
    mc "Maybe?"
    s 4q "I might go back and change a few things, but I have all of the parts done."
    s "Ehehe, I might even finish early!"
    mc "That's good, I'm sure Monika will be happy to hear that."
    "Both of us pause as the door opens again, with Natsuki and Yuri coming into the room."
    show sayori 2c at t33
    show yuri 1b at t32
    show natsuki 2a at t31
    y "Good afternoon, you two."
    show yuri 1a at t32
    mc "Oh, hey there, Yuri."
    s "Hiiii, Natsuki~"
    n 2b "Hey, Sayori."
    n "Monika's not here yet?"
    mc "Nope."
    mc "I hope she isn't being held up by anything."
    s 1x "Hehehe, why, [player], do you want to see her?"
    mc "E-eh? No, it's just, um, well, I mean, she should be here is all, and she seems to like the club, so you know..."
    "I quickly stumble over my words again, crumbling under Sayori's smile and the gaze of the other two girls in the room."
    show sayori 2r at t33
    show yuri 3c at t32
    show natsuki 4c at t31
    "They all glance towards each other, where Sayori nods and then giggles. I feel like they're having a conversation I'm not a part of."
    s 4a "It's okay, [player], I know what you mean."
    hide sayori 
    hide yuri 
    hide natsuki 
    with wipeleft
    "I decide to look back towards my desk, finding it suddenly much more interesting. I probably sounded like I had a huge crush on her or something like that."
    "To be honest, I've been so preoccupied with wanting her to be happy..."
    "Well..."
    "I guess I should answer why I wanted her to be so happy in the first place."
    "Maybe it was because I crushed on her a little."
    "A part of me probably hoped that maybe she'd grow to like me a little if I reached out to her."
    "But things are different now."
    "I've definitely got positive feelings for Monika and maybe I do harbor a bit of a crush on her, so like anyone else a person values in life, they want to see them at their best and full of happiness."
    "Either way, I guess those two feelings are kind of linked. It's still embarrassing to say out loud, though."
    s "Oh, hi Monika!" # (Joke addition: "Anyway, how's your sex life?")
    "I try not to turn my head too quickly as I hear Sayori call out as the sound of the door opening breaks the silence in the room."
    show monika 2c at t11
    m "Oh, everyone beat me here again. Ahaha, it's not exactly fitting as a club president~"
    m 3b "Well, as you were. Sorry to interrupt."
    show yuri 1b at t33 zorder 2
    y "It's fine, we were just wondering where you were again."
    show yuri at thide
    hide yuri 
    show sayori 1c at t44 zorder 1
    s "Ehehe, we might have had to search the school~"
    m 2n "P-please don't remind me of that, it's a bit embarrassing."
    show natsuki 2c at t31
    n "Well, it isn't going to happen again, right?"
    m 3b "I hope not. I don't want to make you all worry."
    m 3a "Anyway, let's get to work."
    s 4b "Oooh, Monika, Monika, can you take a look at this one verse, though? I'm not sure if it's super fitting..."
    m "Hm? Sure. Let's get a desk, first."
    m "Oh, and hello, [player]."
    mc "Hey, Monika. Don't mind me, I'll just be reading."
    m "Alright~"
    hide monika 
    hide yuri 
    hide sayori 
    hide natsuki 
    with wipeleft
    "Like always, everyone goes to their normal club activities."
    "I decide to take a book out from my bag, since I grabbed something in case I didn't want to work on my song at club, and start reading."
    scene bg club_day with wipeleft_scene
    "The day passes by without much incident and the club period comes to an end."
    show sayori 1a at t11
    s "Ready to walk home, [player]?"
    mc "Um..."
    stop music fadeout 3.0
    mc "Ah, actually, I think I'm going to read a little more..."
    s 1c "I'll wait for you, then~"
    "Sayori gives me a knowing grin as Yuri passes by her, saying her goodbyes for the day, followed by Natsuki."
    mc "A-ah, um, you can go on ahead without me today, Sayori."
    play music AfterAll fadein 3.0
    s 1q "Okay~"
    show sayori at thide 
    hide sayori 
    show monika 2c at t11
    "Monika, who is silently packing her things, seems to crack a tiny smile."
    m "That girl... sometimes, I regret doing that..."
    mc "Monika?"
    m 2m "It's nothing."
    m 1c "I, um..."
    m "I've come to a decision."
    m "[player], I..."
    m 1m "For so long, I kept pursuing something that was real."
    m 1n "Even though the reality around me, the one I had accepted, could never let me have it."
    m "It might be too late, but, I'd like to try."
    m "Even if it's a dream, I still want to pursue happiness in it."
    m 4l "It's insane, right?"
    m "I've told you how it's all a mod, how it won't affect anything in the original, but even still--!"
    m "I want to search for something I might be able to bring back to the original."
    m 2f "Even if I can't... I want to act like I can."
    m 2g "It's arrogant, self-indulgent, it goes against everything I've thought about, but even so I still want it."
    m "I don't want to be held back anymore, being afraid of grasping something if only because it might disappear from my hands."
    m "Maybe it was right here in front of me, all this time."
    m "Just being with the Literature Club; I couldn't find any joy in it before, but when I didn't push it all away, something just felt so warm when Sayori asked me for help."
    m "Like I really had a genuine bond with her."
    m 1r "I don't want to live with that crushing feeling anymore, [player]."
    mc "All right."
    show monika 1o at f11
    "I get up and walk over to Monika."
    mc "I said I'd be with you, Monika."
    stop music fadeout 3.0
    mc "That if you were going to take a step in this direction, I wouldn't leave you alone."
    mc "So since you want to try to find it..."
    mc "...I'll always be here for you."
    play music MonTheme fadein 5.0
    m 2m "Then..."
    m "Would you perhaps..."
    "Monika pauses, turning away from looking at me."
    m 3l "...would you perhaps like to go somewhere this weekend?"
    m "I'll have to cancel the group outing, but the last time we went out things didn't... go very nicely."
    m 2a "But I think now, it should be better."
    "I open my mouth, but the words die in my mouth, as Monika takes my right hand in hers."
    m 1a "I won't hold myself back."
    m 1m "So... would you, maybe, like to go?"
    mc "I... I'd be delighted, Monika."
    m 1b "Same time as before?"
    mc "Y-yeah, that'll be good."
    m 2b "Alright. I'll have to let the others know."
    m 2m "Um, I'll see you then."
    mc "A... ah, yes, I'll see you then as well, Monika."
    mc "And, um..."
    "I pause on my way out the door."
    mc "I hope we can find that happiness you're looking for."
    mc "Even if we don't, I'd just like to say that I've truly enjoyed all this time with you so far."
    stop music fadeout 3.0
    m 5a "M-mhm."
    "Monika gives me another smile. One that lets me know she's not turning back."
    mc "A-anyway, I'll be off. Have a good afternoon, Monika!"
    play music EarlyBird fadein 3.0
    window hide
    scene bg corridor with wipeleft_scene
    pause(1.5)
    scene bg residential_day with wipeleft_scene
    window show
    "I hurriedly leave the clubroom, retreating back home."
    scene bg home_interior with wipeleft_scene
    "When I get back home, I sit down on the couch and take a deep breath."
    "I was finally able to break through to her. I don't know what made her think it or what really went on in her head over the last twenty four hours, but--"
    "--all I know is that I'm happy she thought otherwise. That maybe she'll allow herself to be happy from now on."
    show black with close_eyes
    "That maybe, I'd get to see a real genuine smile on her face, one that isn't held back by those thoughts of hers."
    "This upcoming Sunday... I'll hope to see that smile."
    scene bg home_interior with wipeleft_scene
    "The next day passes by incredibly quickly and soon enough it's Sunday already."
    "Sayori already bugged me enough about it yesterday, teasing me about my 'date'."
    "Monika apparently had 'something urgent' come up and with it being so sudden, she suspected it was me."
    "Natsuki was a bit upset, but Sayori promised to go to her house along with Yuri so they could bake together, or at least be together."
    "When asked about it, I said I was falling behind in schoolwork, so I had to stay home to catch up."
    "Probably not the best of excuses."
    "But still, is it really a date, though?"
    "We're only, you know... making up the last time--oh, who am I kidding, that was me essentially asking her on a date."
    "This is totally a date."
    "Of course, that's not helping my anxiety about this."
    "I don't want to make Monika unhappy, so now I'm nervous even though this isn't the first time we've done this."
    "{i}Ding Dong{/i}"
    scene bg house_entrance with wipeleft_scene
    "I swallow, going over to the door. I reach out and turn the doorknob, opening the door."
    mc "H-hi, Monika."
    show monika 1b at t11
    m "Hello, [player]~"
    mc "Ah, here, you can come in."
    show monika 1a at f11
    "I gingerly pull the door open and step off to the side so Monika can come in."
    "As always, she's in her uniform. She really does like it, or maybe she's just grown attached to it with..."
    "Well, everything that's happened."
    "It might just be a hard habit to break."
    mc "Let me get my shoes on."
    "I slip on my shoes, trying not to look at Monika or at least make it look like I'm not."
    "I can see her glancing around the room, but I cleaned it earlier today to help destress."
    mc "Alright, there we g--"
    show monika 2j at s11
    "I pause, seeing Monika extending a hand down to me."
    m 2b "Here."
    "Moving my hand, I gently take Monika's in mine."
    show monika 1a at f11
    "She pulls me up to my feet and then lets go of it."
    m "Better?"
    mc "Y-yeah."
    mc "Thanks."
    m 5a "No problem~"
    "I hastily fumble for my keys before finding them in my pocket, nodding when I can feel them."
    mc "Alright, I'm ready to go."
    m "Mhm. Let's go then, [player]."
    scene bg residential_day with wipeleft_scene
    "The two of us leave the house. I lock the door behind us before we continue on, walking to the same bus stop as before."
    scene bg streets_day with wipeleft_scene
    "It feels... a lot lighter compared to the first time."
    show monika 3b at t11
    m "It's a nice day today."
    mc "Yeah. Spring is really in full swing. I'm glad that it's sunny out, too."
    m 2b "Yep. It's going to be summer soon, though."
    m 2a "Maybe we should look for a new place to go."
    mc "Do you not like the tower?"
    m 3c "No, I do, but..."
    m "Maybe we should go look for another place we can also take the Literature Club."
    m 1a "You seem to know this place. Do you know of any others?"
    mc "Well, I know a few..."
    mc "I guess we can go take a look."
    mc "Um, I'm not sure about whether or not they'll like those places, though."
    m 2b "I'll have to go with you, then."
    m 4k "You don't mind, right?"
    mc "I-if it's for the Literature Club, sure..."
    "I try to keep myself calm, even though right now my heart is currently threatening to break out of my chest."
    mc "Ha... w-well, I guess I'll have to think about where to go..."
    m 5a "Hehehe, okay~"
    "Monika's behavior seems more natural now, putting me off-guard."
    "Her usual behavior used to be a facade, so I could steel myself better against it, but even then I'd get flustered about it."
    "But this is definitely not her putting on a mask, so there's no way in hell I can defend against this!"
    mc "A-anyway, we're here at the bus stop."
    mc "We'll, um, we'll have to wait around for the bus here."
    "I shut up before I can keep talking myself deeper into a hole."
    show monika 1a at f11
    "Monika quietly moves over next to my left."
    "I can feel her arm occasionally brushing against mine and I force myself not to look her way, trying to keep looking ahead. Except the bus is coming from the left..."
    "My thoughts are put to a stop when I hear humming."
    "The only person who could be..."
    mc "W... what song is that?"
    m 1j "Oh, it's a tune I wrote myself."
    mc "Does it go with the song that you wrote?"
    m 1b "I did write our song to it, so it does."
    mc "Amazing..."
    m 5a "A-aha, it's not that much..."
    mc "No, it's really amazing, Monika."
    mc "You can do so much. I knew you were learning piano, but you even wrote your own song, too."
    m 4n "It's probably not very good, I've only started learning it."
    m 4j "But, there's plenty of room to improve~"
    mc "Y-yeah."
    mc "I wish I could be motivated to do that much."
    m "Hehehe, you already are."
    m "You've put a lot of effort into things already, haven't you?"
    "Monika flashes me a knowing smile."
    m 2a "It might be that you're not passionate about a lot of things, but when it comes to someone--um, something you care about, you can do amazing things."
    "I almost jump into the air as I feel something squeeze my hand for a brief second."
    "I turn to look at Monika, who only gives me a small grin as I feel her warmth leave my hand."
    mc "Y-yeah..."
    m 1a "Oh, the bus is coming."
    show black with close_eyes
    stop music fadeout 3.0
    "Both of us board the bus and take a seat around the middle."
    "Similarly to last time, we go towards the city."

        
    call monikaRoute_glimpse
    return

#A Glimpse of Happiness: Letting herself be immersed in the dream for a moment, she finds her heart filled with warmth. (The Knight of Faith archetype is fulfilled here, as not even the fact it's all code stops Monika from wanting that happiness with MC)
label monikaRoute_glimpse:
    scene bg park_day with open_eyes
    play music MonTheme fadein 3.0
    "We get off the bus at the same stop as before. It looks to be pretty crowded today..."
    mc "There's a lot more people than last time... e-eh?"
    show monika 2j at f11
    m "This way we don't get separated, right?"
    "I try not to comment about how Monika grabbed my hand out of nowhere."
    mc "Y... yeah. But you should have my number..."
    m 2c "It'll still be hard to find each other, right?"
    mc "Yeah, that's true."
    mc "Let... let's go."
    "It's not particularly hard to imagine that Monika might have wanted to do this for a while but only wouldn't allow herself to if only because she kept denying herself happiness."
    m 3c "Hm? Is something wrong, [player]? You suddenly stopped."
    mc "Ah, sorry, I just had a sudden worry about locking the house, but I know I did."
    "Monika wanted to do this for a while? The thought of that made my heart skip a few beats."
    "I hadn't quite realized what my thought process logically ended at, but now that it has caught up, everything is now pretty clear to me."
    "It just happens to be making my head spin as well."
    m 2b "Well, I watched you lock the door, so you don't have to worry."
    mc "O-oh, thanks, Monika."
    m 2a "Mhm."
    m "Let's go enjoy ourselves, then."
    mc "Oh, have you had lunch yet?"
    m "I had a small brunch earlier since I woke up late today."
    mc "Alright, let's go get something to eat, first."
    mc "Maybe something light..."
    "I look around the area, trying to find something to eat. The large amount of people is making it a bit difficult, though."
    "Oh, there's something close-by, though."
    mc "Hey Monika, is there anything you can't eat?"
    "Probably should cover my bases."
    m 2b "I'm vegetarian, if that helps."
    mc "Alright. Sorry, I think you said it last time, but I forgot about that. Well, I guess..."
    mc "Oh, there's some takoyaki."
    m "That sounds good."
    scene bg park_day
    show monika 3a at f11
    with wipeleft_scene
    "We head over to the stall and order a dozen of them."
    m 3a "Oooh, these look good."
    "Monika grabs one of the toothpicks in one of the balls of food and moves it to her mouth."
    mc "Ah, wait, Monika--"
    show monika 5b at h11
    m "A-ahh!"
    "She drops the toothpick and the ball she had in her mouth falls back into the bunch."
    mc "I was about to say that they're served hot."
    show monika 4l at t11
    "Monika lightly knocks herself on the head with a smile on her face."
    m "Oops, I forgot~"
    "That was incredibly cute."
    mc "You're supposed to blow on them to cool them down before you eat them."
    mc "Uh, let's see, which is the one you dropped..."
    "I move my hand to grab the one that she put back in."
    m 2b "It was this one."
    "It definitely wasn't that one."
    "She picks it up and blows on it three times before offering it to me."
    m 3b "Say--"
    "I'm pretty sure I know the next word she's going to say."
    m 3k "--'Aaaaaaahn~'"
    mc "A-aaaaah..."
    "I slowly open my mouth, letting the takoyaki into my mouth. It's still warm, but cooled off at the very least."
    mc "...hn."
    "I bite down, with Monika pulling the toothpick out of the ball."
    m 3a "How is it?"
    mc "...'s good."
    "After chewing a few times, I swallow my food. I then grab another takoyaki ball, pulling up, and blow on it a few times before offering it to Monika."
    m 1k "Aaaaah--"
    "It almost sounds like she's warming up to sing or something as I put the takoyaki ball in her mouth. She bites down, eyes glimmering."
    m 1j "--hhhn."
    "I pull the toothpick out and set it in with the others. I'm about to grab one for myself when Monika takes another and holds it up after blowing on it."
    show monika at thide 
    hide monika 
    "We end up taking turns back and forth feeding each other, attracting a bit of attention."
    "I'm fairly sure that I was also fed the takoyaki ball that Monika put in her mouth but I can't confirm that in any way. I tried not to let it get to me, but I think Monika knew as well."
    "I knew she could be a little forward and teasing sometimes, but not this much."
    mc "E-either way, I think that should hold us over for some time."
    "Let's see, what else could we do...?"
    show monika 3b at t11
    m "Oh, [player], they have some stores!"
    mc "Stores...?"
    "I look where Monika is pointing and find some vendors who are selling things from racks after throwing out the small tray we had our food in."
    m "Let's go!"
    "She immediately takes my hand and starts dragging me towards them."
    mc "O-okay, no need to drag!"
    m 5a "Hehehe, sorry~ I got really excited. Come on, I want to see them."
    "Monika takes us to a stall, where my eyes naturally drift over to the prices."
    "I immediately start mentally calculating how much I'll have left over if I buy anything whenever she mentions liking a particular thing."
    m 2b "I can look around, right?"
    mc "Yeah, it's fine."
    show monika 1a at t31
    pause(1.5)
    show monika 2b at t44
    pause(1.5)
    show monika 1j at t11
    "I watch Monika poke around, looking at necklaces and a few dresses. She makes some light conversation with the clerk as I look through the items that Monika liked."
    "Well, this necklace isn't too bad, and I should have a bit left for dinner."
    m 3b "Oh, [player], I'm going to take a look at the other tables."
    mc "Okay."
    show monika at thide
    hide monika 
    "With a smile on her face, Monika skips over and goes over to search for something else she might like."
    mc "Um, excuse me."
    "The store owner comes over to me, smiling. I point out a small necklace with a green jewel in the middle that Monika looked at for a bit longer than the others."
    mc "May I purchase this one?"
    "The clerk looks over at me, then glances at Monika who is still over at the other tables, and smiles, taking the necklace and going over to the register and totalling up the amount."
    "I take out my wallet and pay for it in cash."
    "The clerk gives me a knowing smile and wishes me good luck as I turn away, walking back to Monika. I tuck my purchase into my inner pocket, hiding it from view."
    mc "Find anything you like?"
    show monika 2c at t11
    m "Hm? Oh, hi, [player]. Unfortunately, no.."
    m "There are a few nice things, but nothing that jumps out at me."
    mc "Oh, that's a shame."
    m 3b "Hmm, maybe I'll get something from the table before, I liked something they had there."
    mc "What was it?"
    m 5a "Hehehe, why? Are you going to buy it for me, [player]?"
    mc "Um..."
    m 3j "Haha, you don't have to. Besides, if I want it, I'll get it. But you're quite a gentleman."
    mc "Oh, thank you."
    show monika at thide 
    hide monika 
    "Monika goes over to the previous stall and looks around, but looks a bit distressed after finding that necklace was gone. She talks to the clerk before coming back to me, looking a bit upset."
    mc "Something wrong?"
    show monika 2g at t11
    m "Someone else bought it while I was away..."
    mc "Oh..."
    mc "Well, um..."
    mc "Here, let's get away from the shops for a bit."
    m 1o "Alright."
    "I feel a bit bad since Monika does look a bit upset, but... I'll wait for the perfect moment."
    scene bg park_day
    show monika 1a at f11
    with wipeleft_scene
    "Monika and I go around to the other shops, finding some interesting trinkets and some phone charms, one of which Monika buys. It's a small piano, which she slips onto her phone as we wait in line."
    m 5a "[player], [player], look~"
    mc "It looks good on your phone, Monika."
    m "Hehehe, thanks!"
    "The afternoon has gone surprisingly fast, so we're in line to head to the viewing deck."
    show black with close_eyes
    "There's quite a lot of people in line, but fortunately we made it in before the big rush."
    m "Oh, here we go."
    "Monika and I step into the elevator along with several other people, taking the far back corner since we went in first."
    m "S-sorry..."
    "Monika apologizes as she has to squeeze up next to me since it's crowded."
    mc "It's fine."
    "I experience what has to be the slowest elevator ride of my life as the car slowly lurches up."
    scene bg tower_day with open_eyes
    "Eventually the car does open up, revealing the viewing area. After the car clears up, we step out and look around, trying to find a nice place to look around."
    "We manage to find a not-so-crowded spot right next to the windows that looks out at the city."
    "It's just like the last time we were here... and the timing is similar enough, too. The sun should be setting soon."
    show monika 1b at t11
    m "It's so pretty..."
    mc "Yeah..."
    scene bg tower_sunset
    show monika 1a at t11
    with dissolve_cg
    "We both continue to watch the city slowly fall into the sunset."
    "Down below, the storekeepers close up shop and pack their things, the street performers below give one last encore, and slowly the place begins to empty out."
    mc "Should I go get us dinner?"
    m 3b "I'll go with you."
    mc "I should be fin--"
    "The words die in my mouth as Monika takes my hand in hers, giving a small smile."
    m 5a "You shouldn't leave a girl all by herself when you go somewhere with her."
    mc "R... right. Sorry. I'm not exactly used to this."
    show black with close_eyes
    "We retreat back to the elevators and take them down, looking around the food court."
    "Since Monika ended up going to a seafood place, I decided to get a dish from there as well."
    "I'm not vegetarian myself and she doesn't seem to be the crusading kind, but it was convenient instead of having to make her wait for my meal to be made elsewhere."
    scene bg tower_sunset
    show monika 1a at s11
    with dissolve_cg
    "Afterwards, we go back up to the viewing deck and get a bench to sit on while we eat."
    "Just like last time, huh?"
    "...but still, it feels a lot better."
    mc "M-monika?"
    show monika 1a at f11
    "She suddenly shifts next to me, our sides touching."
    m 1c "Hm? Is something wrong?"
    mc "N... nothing's wrong."
    m 1j "Okay~"
    stop music fadeout 3.0
    "Everything's wrong."
    "More specifically, it's incredibly hard to move to eat my meal if I don't want to accidentally brush against Monika's hand, although she seems to have no trouble doing the same to me."
    "I try to eat calmly, focusing out on the cityscape ahead of us."
    scene bg tower_night
    show monika 1a at f11
    with dissolve_cg
    play music NextToYou fadein 3.0
    "As the night falls, the skyscrapers slowly begin to blink on and the jumbotrons seem to get a lot brighter."
    "You can even see the paired lights of cars zipping around the grid roads."
    "Both of us finish our meals around the same time, but neither of us say a word, simply enjoying being here at the moment."
    play sound paalert
    "However, we're both knocked out of our reverie by the PA system alerting us to the fact that the viewing deck is closing in an hour."
    mc "Guess we have to go sometime, huh?"
    m 2f "Yeah..."
    mc "We can still stay for a bit, though."
    m 1a "Mhm."
    m 2j "But... even so, I'm glad for today."
    m "Everything just seemed so bright."
    "She opened her mouth and mouthed something, but no sound came out."
    mc "Um, you didn't..."
    m 2n "I... it's embarrassing to say."
    "Monika turns her head, looking away, contradicting her behavior for today."
    mc "I... I see."
    "Well, it's now or never."
    mc "Hey, Monika, can you close your eyes for a bit?"
    m 1e "[player]...?!"
    mc "Please?"
    m 1m "O... okay."
    show monika 1j at f11
    "Monika closes her eyes and leans slightly forward."
    "I quietly slip the necklace out of my pocket and undo the latch, moving my hands as carefully as possible, trying not to let the gem touch her neck."
    "I redo the latch after I'm sure it won't fall off and let go. I'm sure Monika felt it."
    mc "You... you can open your eyes, now."
    m 2h "Hmmmm..."
    "It seems Monika's pouting a little bit before she looks down and sees the necklace."
    m 1c "[player]..."
    mc "Um, well, you seemed to like this one, so..."
    m 2d "When the clerk said someone else had bought it..."
    mc "Ahaha..."
    "Monika gives a bright, wide smile and hugs me."
    m 5a "Thank you so much!"
    "I gently return the hug, Monika not resisting."
    mc "S-sorry for not telling you."
    m "It's fine~"
    "Eventually, Monika stops hugging me and pulls back. I'm definitely not disappointed by that. Not at all."
    m 1k "Thank you, [player]."
    mc "Yo... you're welcome."
    mc "Anyway..."
    "I look around, finding that almost everyone here has cleared out."
    mc "We should get going too, right?"
    m 1c "Yeah..."
    "We both get up from the bench, though..."
    mc "..."
    "I try my best not to comment on how Monika took my hand, but I give her a gentle squeeze back as if to say 'It's fine'."
    "Just like last time, we go to the elevator and head down, walking back to the bus stop."    
    stop music fadeout 3.0
    call monikaRoute_march    
    return
    
# The Cruel March of Time: The end is nigh. (Monika somewhat aware that the ending is close, is briefly worried until the MC reminds her that they enjoyed themselves, and that if it was all real, then the good times would also come to an end by death)
    #("Being alive means not only experiencing joy, but also experiencing pain. Nothing gold can stay, right?")
label monikaRoute_march:    
    scene bg park_night
    show monika 1c at t11
    with dissolve_cg
    play music Dusk fadein 2.0
    m "[player]..."
    mc "Monika?"
    show monika 1f at f11
    "I pause, not saying any more as Monika suddenly buries her head in my chest."
    m 1d "I'm scared..."
    mc "Hm...?"
    m "I've wasted so much time..."
    m 1p "Constantly pushing away happiness, not letting anyone in."
    m "And today I had so much of it."
    m "But now I'm afraid that it's going to vanish."
    m 1d "It's a game, right?"
    m "It's going to come to an end someday."
    m "I can't be with you like this forever."
    m 1o "And..."
    m "Even if I can't change things anymore, I can tell."
    stop music fadeout 3.0
    m 1p "It's almost the end."
    m "I don't..."
    show monika 1p at t11
    play music Dawn fadein 3.0
    "I push Monika a bit away from myself before using a finger to wipe her tears, looking into her eyes."
    mc "Monika, listen to me."
    m 1d "M-mhm..."
    mc "Isn't it kind of like dying, then?"
    mc "I know I'm probably no one to talk, seeing as I'm only in high school, but..."
    mc "Everything vanishes some day."
    mc "It doesn't matter if it's real life or a game."
    mc "In the end, it would've disappeared, too."
    mc "So..."
    "I gently take her hands in mine."
    mc "No matter what happens... no matter if everything disappears..."
    mc "It can't change the fact we enjoyed ourselves today."
    mc "And more importantly, it won't change the fact you were happy here with me... and that I was happy with you."
    mc "It can't always be smiles. That's just not life, right?"
    mc "But... the happiness we found here and now. That won't change."
    mc "So just take it with you."
    mc "Um, I don't really know where to go from here, haha..."
    mc "Sorry for rambling."
    m 1c "No, it's... everything I needed to hear."
    m 5a "Thank you, [player]."
    m 1c "Sorry."
    mc "Don't be."
    m 3b "So, how's your song coming along?"
    mc "I think after tonight... I know how to end it."
    mc "The ending of that song has bothered me for some time, but..."
    mc "I know what should go there now."
    m 1a "I see."
    "Before Monika can say anything more, I hear the bus slowly chugging along behind us."
    mc "Well, here's the bus."
    m "Mhm."
    show black with close_eyes
    "We both quietly board the bus and start on our journey home."
    "About ten or so minutes in, Monika leans her head onto my shoulder. Her hair tickles my neck and her cheek gives an odd feeling of warmth as we go along."
    "I'm also fairly sure that she's wearing peach-scented perfume."
    mc "Monika..."
    "I give her a light prod."
    m "M... mhmmhmmm...?"
    mc "It's almost my stop."
    m "Oh, did I fall asleep...?"
    mc "Yeah. Do you want to stay over...? If you're that tired--"
    m "Hehehe, I'll be fine, [player]. But thanks for the offer."
    mc "Alright, if you insist."
    "I reach over and pull on the cord when it's my stop and get up from my seat."
    mc "Good night, Monika."
    m "Good night, [player]. See you tomorrow."
    mc "Yeah. See you tomorrow."
    stop music fadeout 3.0
    scene bg residential_night with open_eyes
    "I get off the bus at my stop and watch the bus go off, waving to Monika until I'm sure she can no longer see me, and continue watching until I can't see the bus anymore."
    "Sayori's lights are off, likely having already gone to sleep. We did stay out later than last time, after all."
    "Tomorrow, huh..."
    scene bg home_interior_night with wipeleft_scene
    "I walk back to my house, unlock the door, step inside, and lock the door behind me."
    "I better prepare for the grilling of a lifetime tomorrow."
    scene bg bedroom_night with wipeleft_scene
    "But, I think it'll be worth it."
    "I got to see a genuinely sincere smile on Monika's face."
    "And she's started to accept being happy."
    show black with close_eyes
    "I can only hope that despite Monika's fears, we have at least a little bit more time."
    "Even if it's all a 'game'... surely, it can't end that fast, can it?"
    "But regardless... whatever happens won't change today."
    "And it's with that fact I can keep moving forward."

    call monikaRoute_dustAndEchoes
    return
    


#Dust and Echoes: Maybe it was nothing more than a facade, but for a brief moment of existence, she shined brighter than all the lights in the sky
label monikaRoute_dustAndEchoes:
    scene bg bedroom with open_eyes
    "When I wake up the next day, I feel oddly groggy. I probably messed up my sleeping schedule with how late I stayed up."
    mc "Aaaahggh..."
    play music EarlyBird fadein 3.0
    "I quickly put myself through my morning routine: showering, brushing teeth, breakfast. When I see the clock, I'm easily twenty or so minutes behind."
    "Slipping on my shoes, I see I've managed to mismatch my socks."
    "Eh, whatever. Not like anyone will notice."
    "I grab my bag for the day and run out the door, remembering to lock it behind me before making the sprint to school."
    scene bg residential_day with dissolve_cg
    "It's a bright and beautiful day, actually."
    "The sun's shining bright. Only a few thin clouds in the sky, blocking out the sun from being too hot. There's a nice breeze that comes every so often, helping me from sweating up a storm."
    "There's still students coming to school as well. I can still remember those days at the start..."
    "I used to envy those couples, those groups of friends, wondering when it would be my turn to find people like that."
    # play sound horn
    "The memories of what happened last night flash through my mind again, but I'm knocked out of them when a car honks at me."
    mc "S-sorry!"
    "Yelling an apology, I cross the street as fast as possible before paying more attention to my surroundings. It is quite a pretty day and..."
    "Ah geez, I'm getting way too ahead of myself."
    "For a brief moment there, I was imagining walking to school with Monika while seeing all of this. That's a little too quick, isn't it?"
    "After all, we only had one really successful date."
    "Er, not-date. It's not like we were officially going out or anything..."
    "Whatever, it was a date. I'll call it that unless she insists it wasn't."
    "Calming down, I complete the rest of the walk to school without getting into a traffic accident."
    scene bg corridor 
    show sayori 1a at t11
    with wipeleft_scene
    "When I get near my classroom, I find Sayori waiting by the door."
    s 1q "Wooow, you were even later than me!"
    mc "S-shut up, Sayori."
    "I try to sound annoyed, but completely fail at doing so."
    s 1c "You seem pretty happy today."
    mc "Y-yeah, I do, huh?"
    s "Are you and Monika a thing now?"
    mc "H-huh?!"
    s 1a "I saw you two heading out yesterday."
    show sayori 1x at f11
    "Sayori gives a smile as she leans forward."
    s "So, details~?"
    "I look away, making Sayori laugh."
    mc "N-not now..."
    s "Okay, I'll ask again during club."
    mc "P-please not there, either."
    s 1q "Hmmm, fine. When we walk home together, right?"
    s 1a "Or are you walking home with Monika now, even if she's in the opposite direction?"
    "I decide the best thing to do is keep my mouth shut."
    "Not that it's helping against Sayori's ever-widening grin."
    s 2c "I'll take that as a yes."
    mc "Well, you'll be lonely walking home then, won't you?"
    "Sayori sighs."
    s 4j "Monika really has it rough, huh?"
    mc "Hm?"
    s 1a "Nothing~"
    s "But I'll be fine, [player]."
    s 1c "I'm still so happy for you, though."
    s "I think before you joined the Literature Club you wouldn't have been like this. You've really changed."
    mc "Have I...?"
    s 3a "You have. Maybe you haven't realized it yet, but I think you're a lot different than how you used to be."
    play sound paalert
    s 4m "Oh, class is starting!"
    s 2c "See you after class!"
    "With that, Sayori takes off, running for her classroom."
    stop music fadeout 3.0
    scene bg class_day with wipeleft_scene
    "I enter mine and go sit down, making it just a few seconds before the teacher comes in."
    "I'm a bit restless for all of today. I mean, after all of that... well, who wouldn't be?"
    "Before, the day would go by so quickly as I wasn't paying any attention, but today I seem to be painfully aware of every ticking second."
    scene bg corridor with wipeleft_scene
    "Thankfully, the day finally ends. I march right to the clubroom."
    "Was what Sayori said true...?"
    "Have I changed that much, though...?"
    "I guess I have."
    scene bg club_day with wipeleft_scene
    play music MonTheme fadein 2.0
    show monika 4b at t44
    m "Oh, you're here~"
    mc "Oh, hey Monika."
    "I give a wave as I drop my things off by my normal chair by the window."
    mc "You're here a little earlier. Usually you were the last one to arrive."
    m 5a "Ahaha, well, I thought I should set a better example as club president."
    show monika 5a at t11
    "Monika walks over to me, joining me by the window."
    mc "I'm glad you got home alright."
    m "Thank you."
    m 1c "But... I'm still a bit scared."
    m "Because..."
    mc "Because...?"
    m 1d "I... I can sort of feel it."
    m "That the end is here."
    mc "Is this because of that 'game' thing?"
    m 2n "Yes..."
    mc "We don't have a lot of time left, do we?"
    m "No, I don't think so."
    "I note that Monika has some paper in her hand."
    mc "How much longer do we have?"
    m 1n "I don't know. I thought that it might come when we shared songs, but..."
    m "I'm scared it'll be sooner than that."
    m 1c "No, I think it will be."
    mc "What makes you say that?"
    m "I just..."
    m "Every time I've come close or thought I've achieved happiness, it always gets taken from me so quickly."
    m 1d "I'm scared it's going to happen again."
    "I gently take Monika's hand in mine."
    mc "I'll be with you until the end."
    m "Thank you, [player]..."
    stop music fadeout 3.0
    s "Heeeeeeey!"
    show monika 1e at t22
    "Both of us turn to look at Sayori, who's entering the room with the others, and we quickly let go of each other's hands."
    show sayori 4n at t41
    s "Oh, did we interrupt something...?"
    m "No, no. Anyway, if we're all here, let's start club activities. How is everyone's song writing going?"
    show sayori at thide 
    show monika at thide 
    hide sayori 
    hide monika 
    "The rest of the day flies by after that."
    "I look out the window occasionally, finding it's suddenly gotten quite foggy."
    "That's strange. It hasn't rained at all and I don't think the forecast called for any."
    "It's really thick, too. Almost like it's impenetrable."
    "I notice that Monika looks at it and seems to be disturbed at it, but looks away."
    show monika 4k at t11
    m "And that's all for today."
    m "See you to... tomorrow, everyone. Aha, something got caught in my throat there~"
    hide monika with dissolve
    show sayori 1c at t32
    s "Hehehe. Make sure Monika gets home safely, [player]~"
    show sayori 1a at t32
    show yuri 2b at t33
    y "Goodbye, [player]. See you tomorrow, Monika."
    show yuri 2a at t33
    show natsuki 2b at t31
    n "Yeah. Seeya."
    hide sayori 
    hide yuri 
    hide natsuki 
    with wipeleft
    pause(1.5)
    show monika 3d at t43
    "The three of them leave together. Monika opens her mouth and moves her arm as if to catch one of them by the sleeve and stop them, but doesn't."
    m 2p "...goodbye."
    mc "Monika...?"
    m 3l "Ahaha, it's the end..."
    $ quick_menu = False
    $ saveLocked = True # removes ability to save at all
    call monikaRoute_absoluteFinale
    return

label monikaRoute_absoluteFinale:
    $ persistent.autoload = "monikaRoute_absoluteFinale" # allows us to force returning here
    $ persistent.timesTried = persistent.timesTried + 1
    $ quick_menu = False
    $ saveLocked = True # removes ability to save at all
    show bg club_day
    show monika 3l at t11

    if persistent.timesTried == 2:
        m 2c "[player], I know that what I'm going to say won't make any sense to you, but..."
        m "I don't think you can stop this."
        m "Let's just have some closure, okay?"
        m "If this is how we're going to go... then I want it to finish on my own terms."
        m "I've always been ready for this moment to come, so..."
        m "I want to see it through to the end."
        m "Just bear with me, okay?"
    if persistent.timesTried == 3:
        m 2p "[player], I really appreciate it that you keep resetting things..."
        m "Hehehe, you might be a little confused about me saying that."
        m "Don't pay it any mind, okay?"
        m 1n "But if you can only reset us this far, then you know what has to happen."
        m "We can't just stay like this forever."
        m "I know you think you can try, but one of these days..."
        m 2e "...you're going to have to click ahead."
        m "So please, it's painful enough having to part with you."
        m "But let's not make this goodbye any more painful than it has to be."
        m 5a "For me, okay?"
    if persistent.timesTried == 4:
        m 2n "It's..."
        m "I'm really touched, [player]."
        m "But..."
        m 1p "It's going to have to end some day."
        m "I don't want to have a long, painful goodbye."
        m "Please."
    if persistent.timesTried == 5:
        m 2p "Please..."
        m "Please don't drag this out."
        m "Please?"
        m "I'd just like... to see this through the end."
    if persistent.timesTried >= 6:
        m 2c "..."


    m 1c "Can you see it, [player]?"
    mc "The fog?"
    m 2n "Well, I guess you could describe it as that. Maybe more like a 'fadeout'."
    "Monika smiles, holding onto that paper she had the whole day."
    m 2c "[player], can I ask you something?"
    mc "Sure, what is it?"
    m 2d "I'd like for you... to read the lyrics of my song. At least this once."
    mc "Yeah, I can do that."
    show monika 1c at t11
    "I walk over to Monika, who hands me the paper."
    # [Your Reality lyrics go here]
    call showpoem(poem_monFinale, music=False)
    mc "It's beautiful."
    mc "I... I really like it. You must have put a lot of work into it."
    m 2k "Thanks..."
    m 1a "Can I at least read what you've made?"
    mc "Sure."
    "I reach over into my bag and hand Monika my poem. She reads it, smiling at first, then wiping a tear by the end."
    m 3k "So that's... how you feel...?"
    mc "Yeah..."
    # show ending monika CG
    scene bg monikaCG2 with dissolve_cg
    play music Brick fadein 3.0
    "Monika suddenly takes a step forward and embraces me. I can feel her warmth pressing up against me as she holds me closer."
    m "I'm sorry I took so long."
    mc "It's fine."
    m "We could have had more time together..."
    mc "But it wouldn't have been something genuine."
    m "Ah... that's true, I suppose."
    "My song was the height of cliche."
    "The story of a boy who only wanted to have many friends and a girlfriend that he'd happen to meet along the way."
    "And then he realized something when he was surrounded by a bunch of girls, the fantasy he had before."
    "In reality, he wanted something deeper. He didn't want a bunch of shallow friendships. He wanted to have something that truly meant something with someone."
    "It took a long time, but he eventually found it."
    "No matter how little time he had the connection he wanted, it was worth everything. Even the pain of losing it."
    m "Ah..."
    m "Ahaha..."
    show bg monikaCG2b with dissolve
    m "It's time to 'wake up', right?"
    "That's right... Monika did say that it's a 'mod'. It doesn't change reality. Like a dream."
    mc "You still want to take this back with you, right?"
    m "Mhm."
    mc "Then... believe that you can."
    mc "Even if it seems like it won't happen."
    m "I will."
    show white with dissolve_cg:
        alpha .2
    "I glance around again. The 'fog' that was swallowing everything is already past the walls of the classroom."
    m "You know..."
    mc "Monika?"
    show bg monikaCG2 with dissolve
    m "I don't know what's going to happen afterwards."
    m "It might even be that we forget everything or all the progress I've made gets reset."
    m "If that's so..."
    m "I don't know if you'll remember everything... but..."
    "Monika gives an enigmatic smile, as if she was sending a message through me for a second."
    m "...I know you'll come for me again."
    m "Promise me that?"
    mc "Yeah."
    mc "I'll definitely help you out again, Monika." # // references game resets
    # [begin to make the CG slowly fade out]
    show white with dissolve_cg:
        alpha .4
    m "[player]..."
    mc "Monika?"
    m "There's so much I didn't get to say or do with you, but..."
    m "The one thing I will definitely say is..."
    m "I love you."

    $ consolehistory = []
    call updateconsole_clearall("", "")
    call updateconsolehistory("")
    hide chistory
    call updateconsole("assumeControl()", "Control assumed for three seconds.") # I AM ASSUMING SELF CONTROL
    

    menu:
        "I wasn't here for you, though.":
        #[...]
            $ saidIt = False
            m "Ah..."
            m "I thought you might show up just now."
            m "Haha, well, that's fine, too."
            m "I just didn't want to have any regrets."
            m "Even if you don't return those feelings, I know you at least wanted to come after me too."
            m "So regardless, thank you."
        "I love you, too.":
            #[I love you, too.]
            $ saidIt = True
            mc "I love you, too."
            m "Mhm..."
            m "I'm glad I was able to say those words."
            m "I won't have any regrets."
    
    call hideconsole
    hide console_bg
    hide console_caret
    hide ctext
    hide chistory

    "For a second, I feel like I zoned out. Maybe the shock is getting to me."
    "I press Monika a little closer to me, hoping it will drag out the precious few seconds we have left."
    "If there was any moment that I could have the power to stop time, this would be it."
    m "[player]..."
    mc "Monika?"
    m "I can't feel my legs now."
    #[more whiteness]
    show white with dissolve_cg:
        alpha .6

    mc "Neither can I."
    m "[player]."
    mc "Monika?"


    #If you said "I love you"
    if(saidIt is True):
        "I feel her shifting a little bit in my embrace. Suddenly, Monika is looking at me dead in the eyes."
        show bg monikaCG2b with dissolve
        "She leans her head forward."
        "Ah..."
        "I can feel that numbness slowly crawling up my spine."
        "So this is going to be my last chance to do anything like this."
        show black with close_eyes
        "I close my eyes and lean forward, pressing my lips against hers."
        "There's a hint of cherry taste as I pull away."
        hide black with open_eyes
        m "Thank you..."
        mc "Y-yeah..."
        show bg monikaCG2 with dissolve

    show white with dissolve_cg:
        alpha .8
    m "[player], this is the last thing I'll have to say."
    mc "Monika?"
    "Monika pulls a bit away again, smiling."
    m "I didn't want our last moments to be held too tightly like that, because..."
    m "In these last few moments with you, I want my last sight to be you and only you."
    "The numbness is already at my neck. Like the 'end' is being pushed on us."
    "I'm surprised I'm taking it so calmly, but it's probably half-shock and half the fact Monika is at least here with me."
    mc "You too."
    "What idiotic words to say. Those might have been my last words, I should've said something else."
    "But Monika laughs, a real, genuine smile on her face."
    "And in that brief moment, I witnessed something brighter than all the stars in the heavens combined."
    "Even if it was only for a single ephemeral frame of time, I'm glad I could have seen it before it's all over."
    m "Goodbye, [player]."
    mc "Goodbye, Monika."
    "Right after we say our final goodbyes, everything fades away into a white nothingness, and even my very thoughts have the curtains fall down upon them..."
    "...leaving nothing, not even dust nor echoes."
    #[Finish with the full white out and the END text]
    window hide
    stop music fadeout 4.0
    show white_end with Dissolve(5.0)
    $ finishedMonika = True

    

    show black with Dissolve(4.0)
    pause(3.0)
    return

    


#[the reactions are fairly the same as the other choice]

label monikaRoute_rooftopFinaleB:
    show black with Dissolve(2.0)
    stop music fadeout 2.0
    "After we go around and visit those booths, we start walking around the festival, trying out whatever comes our way."
    "Time flies ahead. Soon enough it's already dark out."
    #stop music fadeout 2.0
    scene bg rooftop_night with open_eyes
    show monika 1r at f11
    m "Well, that was fun..."
    mc "Monika?"
    show monika 2q at f11
    "She shakes her head."
    m 2r "It's nothing, [player]."
    mc "It doesn't sound like nothing."
    mc "If you want to talk about it, I'm here for you."
    m 1n "Ah..."
    m "Thanks, [player]."
    hide monika with wipeleft
    scene bg sky_night with Dissolve(2.0)
    "The two of us look up at the night sky, waiting for the fireworks."
    # need fireworks sound
    window hide
    play sound fireworks
    show green with Dissolve(1.0):
        alpha .5
    hide green with Dissolve(1.0)

    show blue with Dissolve(1.0):
        alpha .5
    hide blue with Dissolve(1.0)

    show red with Dissolve(1.0):
        alpha .4
    hide red with Dissolve(1.0)
    window show
    "The whistling that indicates their launch fills the air. We simply watch in silence, hearing the booms in the sky accompanying flashes of light."
    scene bg rooftop_night with wipedown
    show monika 2f at f11
    stop sound 
    play music Dusk fadein 2.0
    "I turn to look at Monika, finding she has a frown on her face."
    "Even with this, she doesn't seem happy."
    "She has been sort of on guard today."
    "There was that brief moment on the rooftop earlier, but right after that..."
    "She went back to being cautious."
    "Almost like she wanted to be happy, but wouldn't let herself."
    "There were a few times she came so close, but then she'd pause and pull back."
    "Monika..."
    m 5a "You shouldn't stare at a girl like that, you know?"
    mc "S-sorry, I got lost in my thoughts."
    m 1k "Ahaha~"
    stop music fadeout 3.0
    m "What were you thinking about?"
    mc "...nothing, really."
    m "Ah."
    show monika 1q at f11
    "The entire time, even now..."
    "It feels like Monika is wishing for something else."
    "But I can't figure it out."
    "It's like there's an insurmountable chasm between us."
    "The others soon joined us on the rooftop, but even so..."
    "Monika just immediately went back to her usual presidential ways."
    #scene bg club_day with dissolve_cg
    show black with close_eyes
    "In the end, I didn't have anything to go on."
    "I couldn't find the words that might help me break through to her..."
    "...or more like I felt like I had lost a critical opportunity."
    "Like no matter what I said, it didn't matter anymore."
    "If only something were different... what could I have done differently on that day?"
    play music LettingGo fadein 3.0
    scene bg club_day with dissolve_cg
    show monika 4k at t11
    m "Oh, good afternoon, [player]!"
    mc "Oh, hey, Monika."
    "In the end, we naturally fell back into our normal places."
    "We didn't gain any new members from the festival, but it didn't matter to Monika."
    "She just continued on, playing the role of club president."
    show black with close_eyes
    "After a while, I had gotten fairly used to it."
    "Sometimes I'd doubt things, but it's not like I had a lot to go on."
    "Maybe Monika was just having a rough time with her family or something during the festival."
    "Things might be better now for her."
    "I can't say for certain, really."
    "She even dropped that whole 'game' business, too."
    "So maybe it was all just her finally breaking down or something like that."
    "But still..."
    "Why do I feel like there's something more that I could have done...?"
    window hide
    stop music fadeout 3.0
    show end with Dissolve(4.0)
    $ persistent.got_monika_bad_end = True
    #call screen dialog(message="I told you already, just go be with the others.", ok_action=Jump(monReturn))
    #label monReturn:
    return



    
