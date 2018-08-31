label yuriRoute_voxPopuli:
    play music aNewDay fadein 3.0
    scene bg residential_day with wipeleft_scene
    "It’s the day after the festival."
    scene bg class_day with dissolve_cg
    "Honestly, I barely remember how or when I fell asleep, but I somehow dragged myself back to school."
    "I think the lesson is… chemistry? Huh."
    "I could get away with sleeping for just little bit…"
    play sound slap
    "{i}Thwick.{/i}"
    "Something just hit my head… I think."
    "It takes a moment for me to locate the offending object, lying next to the leg of my chair. A crumpled paper. Amazing."
    "I unwrap the note, squinting to make out the scrawl."
    $ o_name = "Note"
    o "meet me outside after class"
    "That’s it? Really?"
    "While I’m tempted to toss it back in their general direction, something keeps me holding it. I have the feeling it shouldn’t be ignored."
    
    stop music fadeout 3.0
    scene bg class_day with wipeleft_scene
    "Technically, I’m missing literature club for a dumb note. Then again, after what happened at the festival, I should probably sort through my own feelings before seeing her again."
    "Some five, ten minutes later, a scruffy-looking upperclassman arrives."
    $ o_name = "Senior"
    o "Hey, you actually showed up."
    mc "What’s that supposed to mean?"
    o "Well, how many times have people actually listened to notes that randomly hit them in the back of the head?"
    mc "Well… I was curious. So, tell me. Why’d you bring me here?"
    "The guy puts on a diplomatic smile, like he’s trying to make some kind of deal."
    o "There’s no easy way for me to say this, buuuut..."
    o "You shouldn’t be dating Yuri."
    mc "Huh? Wait, what do you mean?"
    mc "I mean, aside from the fact that we aren’t even--"
    "He raises his hands in an ‘I know, I know’ gesture."
    o "Look, I’m just saying, it would be in your best interest to not get caught up with her. People saw you at the festival, and, well…"
    "He shrugs."
    o "Over Yuri, literally anybody’s a better choice."
    o "I know this will sound harsh, but there have been, uh… incidents. Yeah, incidents."
    mc "Incidents?"
    
    
    
    
    
    menu:
        o "Look, I’m trying to be helpful. Steer clear of her. That’s all I’ll say."
        "You're a coward.":
            $ yuri_gPoints = yuri_gPoints + 1
            $ yuri_coward = True
            "I just can’t keep quiet."
            mc "You’re a coward, you know that?"
            "He blinks, caught way off guard."
            o "Excuse me?"
            "I stare at him, eye to eye."
            mc "I don’t need you, or even want you to tell me who I can or can’t be with."
            mc "And to think that you’d try and do this all behind her back?"
            mc "I don’t want any of what you’re selling."
            "I sling my bag over my shoulder, leaving him slack-jawed. My mind races."
            "Why would he care about us?"
            "What did Yuri ever do?"
            "Who the hell does he think he is?"
        "Yeah, sure.":
            $ yuri_gPoints = yuri_gPoints + 1
            $ yuri_bPoints = yuri_bPoints + 1
            "I mumble something vaguely sounding like ‘yeah’, but my mind’s in a completely different place."
            o "Good to hear we’re on the same page. I know it’s harsh, like I said, but it’s for both of your benefit."
            "I nearly retch at his manufactured kindness."
            "Why would he know about us?"
            "What did Yuri ever do?"
            "Who the hell does he think he is?"
    
    
    
    
    scene bg corridor with wipeleft
    "I should get going. I’ll probably be able to catch some part of the rest of literature club."
    "Not sure how I’m going to face Yuri after this, but I’ll cross that bridge when I get to it."
    call yuriRoute_return
    return

label yuriRoute_return:
    play music aNewDay fadein 3.0
    scene bg club_day with wipeleft_scene
    "I slide open the literature club door and walk inside. Natsuki struts in beside me, a bulky magazine folded up under her arm."
    "I should ask her about Yuri."
    "Despite their vitriol, they do seem to have been tolerating each other a little better lately."
    "It wouldn't hurt to ask if Natsuki has heard anything, even if it's unlikely for her to know about what happened."
    mc "Hey, Natsuki, can I talk to you outside for a second?"
    hide natsuki with wipeleft
    show sayori 2m at t21
    show monika 3c at t22
    stop music fadeout 3.0
    "Sayori and Monika both give me looks of confusion, but I shake my head slightly as I duck outside."
    scene bg corridor with wipeleft 
    show natsuki 4e at t11
    "A few seconds later, Natsuki walks out into the hall as well."
    n "Jeez, what the heck is this abou--"
    show natsuki 4c at t11
    "Natsuki abruptly stops, seeing the expression on my face.."
    n 2c "You… you look kinda worried. What’s wrong?"
    "I don’t bother being coy. I tell her everything."
    mc "Some guy took me aside after last class. He said I should keep away from Yuri. 'For my own sake,' actually."
    mc "What’s that even about?"
    mc "How could anyone say that about her?"
    show natsuki 2u at t11
    "Natsuki chews on her bottom lip, staring at some point on the floor."
    n "I guess you’ve finally heard, [player]."
    n "Rumors about Yuri show up from time to time, yeah."
    n "But you know that’s all they are, right? Just rumors."
    mc "You don’t know anything else about it, then?"
    mc "What are the rumors about, anyway? The guy who mentioned them was pretty vague."
    n "It shouldn’t matter what the rumors are, [player]."
    n "Like, I’ve gone to school long enough to know that rumors never end up being true anyway."
    n "Why should it be different for you?"
    n "They’re not super widespread rumors anyway."
    n "If they were, I guess Monika probably would’ve heard about it and done something by now. Or maybe she already tried and it didn’t work, but you get my point, right?"
    n "Yuri probably wouldn’t want you to get involved with those rumors anyway."
    show natsuki 1c at t11
    "Natsuki raises her eyes to look at me."
    n "She really likes you, you know."
    "I feel myself turning a little pink."
    mc "Y-yeah. I guess so."
    n "Maybe--"
    m "Okay, everyone~!"
    m "It’s time to share poems!"
    show natsuki 4c at t11
    pause(1.5)
    show natsuki at thide 
    hide natsuki 
    "Natsuki huffs, straightening her blazer before walking off to retrieve her poem."
    "I should probably go get mine as well…"
    
    show black with dissolve_cg
    "I came, I saw, I shared poems."
    "And Yuri wasn’t even there."
    call yuriRoute_amberHeart
    return
    

label yuriRoute_amberHeart:
    scene bg residential_day with wipeleft_scene
    
    show sayori 1k at t11
    s "Hey, [player]?"
    "I glance over at Sayori. She has her head bowed, kicking absentmindedly at the gravel in our path."
    s "I might be being nosy, but… what were you talking with Natsuki about?"
    "Oh--so that’s it."
    "We never really discussed it, and I thought she’d just forgotten. I never seem to give her enough credit, I guess."
    s 1l "[player]?"
    play music Thoughts fadein 3.0
    mc "Ah, uh…"
    mc "Well..."
    mc "I think you know about Yuri and I, right?"
    "Sayori nods, looking me over tentatively."
    s 1h "Yeah…?"
    mc "Well, it’s like… there have been rumors."
    s "Rumors?"
    mc "I mean, somebody told me to stay away from Yuri."
    show sayori 2g at t11
    "Sayori seems to have the same reaction I did. Confused and worried."
    s "That’s mean…"
    mc "I know. But what can I do? He didn’t tell me the why of it."
    show sayori 2u at t11
    "Sayori gives a tiny nod."
    mc "I figured Natsuki might know about why she’s so insulated, but she beat around the bush too."
    mc "Do you know?"
    s "I… don’t. Sorry, [player]."
    show sayori 2g at h11
    "I reach over and prod her cheek, causing her to yelp."
    mc "Don’t worry about it. It’s my problem to deal with, okay?"
    show sayori 1u at t11
    "Sayori shakes her head, hefting her backpack."
    s 1g "[player]."
    mc "Yeah?"
    s "I need you to understand that I’m here for you. {i}We’re{/i} here for you."
    mc "I know."
    s "But do you? I feel like you’re only holding back because you don’t trust us."
    "Sayori peers at me, her bubbly personality replaced by a serious demeanor."
    stop music fadeout 3.0
    mc "Well… if you have ideas, I’m welcome to hear them."
    "Sayori nods, pushing the tips of her fingers together."
    play music aNewDay fadein 3.0
    s 1x "Well, why don’t you invite her out? Then you can talk about it there."
    mc "I was planning to, yeah."
    show sayori 1x at h11
    "She claps her hands together, nodding."
    s "That should work! Just make sure you take her someplace nice!"
    mc "Nice?"
    s 2c "Well, you can’t just take her anywhere, you know?"
    mc "Y-yeah, I know."
    "Sayori skips to a stop in front of my house."
    s 4x "You better make a good impression. I'll be watching!"
    "I give a small laugh, waving."
    mc "Keep me honest, okay?"
    stop music fadeout 2.0
    show black with close_eyes
    "Sayori doesn’t answer back."
    call yuriRoute_tasseography
    return

label yuriRoute_tasseography:
    "A bookstore. That should be easy enough, right?"
    "Unless you’re me, who spent what should have been my sleeping hours searching up the prime location for what might technically be our 'first date'."
    "In which case it feels more like pulling out your own tooth."
    s "I’m sure she’ll love it!"
    scene bg residential_day
    show sayori 4x at t11
    with open_eyes
    play music aNewDay fadein 3.0
    "Sayori grins, skipping alongside me as we head up to school. She was the one who helped me put this together, so she might have a point."
    "And she’s known her longer, too."
    show sayori 4m at h11
    s "Aah!"
    "Sayori comes to an abrupt halt, eyes wide. While I’m looking around for whatever caused the reaction, she nudges me forward."
    s 1c "It’s Yuri! This is your chance!"
    show sayori 1a at t44
    show yuri 1a at t41
    "It is, indeed, Yuri, leaning on the street corner."
    "Waiting for me?"
    "Maybe?"
    "I can only hope."
    show sayori 1c at f44
    "I brush the front of my blazer, mouth suddenly gone dry. Sayori nudges me forward."
    s "Go on! This is what you planned, isn’t it?"
    show sayori at thide 
    hide sayori
    show yuri 1b at t11
    "I stumble forward, rehearsing a greeting as Yuri turns to me."

    
    
    $ firstThreeChars = player[:3]
    $ o_name = "[firstThreeChars]+Yuri"
    o "Hi there!"
    "We say at the same time. If I could sink into the ground now, I would. At the very least, Yuri looks just as embarrassed."
    y 2j "Sayori, erm… Sayori told me you passed this way."
    "I glance quickly over my shoulder."
    play music EarlyBird fadein 3.0
    "The woman in question has already fled the scene. Just as well, I guess."
    mc "Well, here I am now, at least. Do you want to get going?"
    show yuri 1a at t11
    "Yuri nods quickly, and we quickly fall in step next to one another."
    "I clear my throat nervously."
    mc "Did you have fun at the festival? It was the first time I had actually helped a club set their booth up."
    show yuri 1m at t11
    "Yuri nods, a smile spreading across her face."
    y "I did! It was very heartening to see students enjoy our poetry."
    mc "You mean {i}your poetry{/i}, right?"
    "Yuri turns visibly pink."
    y 3v "That’s not true. Your poems at the least give me inspiration..."
    show yuri 3g at t11
    "I laugh, which makes her turn to me, a pout on her face."
    mc "I just write words and hope they stick. That was entirely you, and it was really good."
    y 3h "I..."
    y 3j "Well… thank you."
    show yuri 2a at t11
    "We keep walking in silence, but it’s more of a cozy one than an awkward one."
    "As we approach the school gates, I slow to a stop."
    mc "And... one more thing?"
    y 2f "Oh?"
    mc "You’re still okay with our date after school?"
    y 1m "Oh! Y-yes! Definitely!"
    "Yuri perks up, suddenly on edge."
    mc "Okay, that’s great. Meet back here?"
    "Yuri nods quickly, grinning still."
    y 1b "I should head to class soon." 
    mc "Right, right."
    show yuri 1c at lhide
    hide yuri 
    stop music fadeout 3.0
    "She strolls off, leaving me to get to my own class."
    "I know right now I won’t be able to concentrate on schooling."
    "Win some, lose some, I guess."
    scene bg residential_day with wipeleft_scene
    
    "In the end, it didn’t take much more than 'Yuri and I are on a date' to excuse us from literature club and for Yuri to turn an interesting shade of burgundy."
    show yuri 2v at t11
    y "Y-you didn’t have to do that, [player]."
    mc "Well, yeah. But I didn’t want to just buzz off without any warning."
    show yuri 1c at t11
    "Yuri nods, smiling faintly."
    mc "Anyway, the bookstore is really close. You might have already been there, actually..."
    y 1d "Well, maybe, but not... Accompanied."
    "I smile in spite of myself, nudging her with my shoulder."
    mc "First time for everything, right?"
    scene bg streets_day
    show yuri 1c at t11
    with wipeleft_scene
    pause(1.0)
    scene bg bookstore
    show yuri 1a at t11
    with wipeleft_scene
    play music YurTheme fadein 3.0
    "Yuri and I walk into the bookstore I picked for our date. Anxiety swells throughout my body, as I’m afraid of the possibility that this won’t go well."
    "Luckily, there’s a noticeably small number of people currently in this store, making it a great location for a date."
    "At least, that’s what I hope."
    mc "So… uh, here we are."
    "Yuri looks over at me, struggling to make eye contact."
    y 2o "Y-Yes, we are…"
    "She looks about as nervous as I am, if not more."
    "Man, what do I even do here? People go to bookstores to shop for books, right? But where do I even start?"
    "I guess it’d be easy enough to browse through and see if anything looks interesting."
    mc "You like horror, right, Yuri?"
    "Yuri peeks over at me again and nods her head."
    y 1a "That is correct. I do enjoy horror."
    mc "Would you like to look through the horror aisle, then?"
    "The nervous expression on Yuri’s face returns."
    y 2o "Only if you want to…"
    "I don’t think Yuri completely got what I was driving at, but it doesn’t matter."
    hide yuri with wipeleft
    "We make our way to the horror aisle of books, and I freeze up once we do."
    "Man... Now what? I know nothing about books! Yuri’s basically an expert, so what am I supposed to do that won’t make me look like an idiot?"
    "For now, I glance through the various titles. If nothing else, at least I can admire the well drawn cover art."
    show yuri 1b at t11
    y "Have you found a book you’re interested in, [player]?"
    "Yuri catches me off guard, and I make a small jump backwards."
    mc "Ah! I was just eyeing…"
    "I grab the nearest book next to me, not taking enough time to actually check what it is."
    y 1f "At the Mountains of Madness?"
    mc "Yeah! I mean, the cover art looks pretty cool… I think. The empty, snowy landscape makes you feel a little bit of dread, see?"
    y 1c "Uhuhu."
    y 1d "Well, that doesn’t quite mean the book itself is spectacular, but the front cover does make an impression."
    mc "You think so?"
    y "Yes. It’s interesting how the cover art for a book can be the most iconic thing about it, even if the writing is sub-par."
    "I still feel a bit lost about how to interpret books and writing and all that, but Yuri seems like she knows what she’s talking about, as usual."
    mc "I think I’ll buy this one, then."
    mc "Is there anything you’re interested in here, Yuri?"
    y 2o "Ah, well… I go to this bookstore all the time, and there doesn’t appear to be any new stock, so…"
    "Yuri looks away, frustrated."
    y 2p "I should’ve told you I always go here so you could’ve picked a different location. I can’t even go without ruining our first date…"
    "Yuri’s face falls even further."
    mc "No, it’s not ruined! The location isn’t what matters. I still enjoy being with you, even though I know nothing about books."
    y 2f "Really?"
    "Yuri perks up a bit."
    mc "Yeah! I’m on this date to spend time with you."
    mc "Sure, it’s unfortunate that I picked a bookstore where there’s no books you haven’t already passed on, but who cares?"
    mc "That’s not going to stop me from appreciating being with you."
    mc "We even talked earlier about how this might happen, and that I was fully prepared for it."
    mc "Besides, I never even told you the specific location of where our date would be, anyway."
    mc "You have no reason to blame yourself."
    y 3p "Ah… Well, if that’s how you feel…"
    y 3c "Thank you, [player]."
    y 3b "I’m enjoying being with you as well."
    "Awkward silence fills the air. Now what?"
    mc "Well, uh…"
    "We both stare at the ground."
    mc "Let’s sit down! Once I buy this, I mean."
    scene bg bookstore with wipeleft_scene
    show yuri 1a at s11
    "After quickly purchasing the book, we move to a nearby table and sit down next to each other."
    y 1b "Should we read together again, then?"
    mc "Maybe later, but I wanted to talk for a bit first."
    y "I see. That’s understandable."
    
    mc "So, how have you been?"
    
    y "I’ve been well enough."
    y "…"
    "The awkward silence from before returns with a vengeance. Yuri lays her head down on the table, resting on top of her crossed arms."
    y 1o "What am I supposed to do, [player]?"
    y "I have no idea how dates are supposed to work. All I’m doing is wasting your time…"
    
    mc "No, not at all!"
    mc "Like I said, just being next to you is great."
    mc "Words aren’t always everything."
    "Yuri seems a bit calmer after that comment."
    y 1b "I suppose so…"
    "I decide to change the subject."
    mc "S-so, I know you’re into poetry, but have you ever tried writing your own book?"
    y 1f "Hmm?"
    y 1b "Well, I’ve dabbled in writing fiction, I suppose."
    y 1o "But publishing a book would require me to share my work, and, well, nobody would want to read that…"
    mc "Come on, Yuri. I don’t think you’re giving yourself enough credit."
    y "It’s true, though."
    mc "Please. Your poetry is incredible, so I bet that if you tried writing a full fledged book, it would be amazing."
    y "I’m not sure if you can make that comparison that easily. Writing poetry is much different than writing a traditional story."
    y "Dealing with a narrative structure, having to develop interesting characters, and all the other facets of that type of writing…"
    y "It’s a huge undertaking, and is difficult for reasons other than why writing well done poetry is difficult."
    y "I bet you’d be disappointed if you read any of my attempts at a novel."
    mc "I doubt that. Maybe we could read your work sometime together."
    y 1a "If you really want to… maybe one day."
    "A smile tugs at the corners of Yuri’s lips."
    mc "Anyway, how about that book I just bought? Let’s see what it’s like."
    y "Yes, let’s."
    show black with close_eyes
    "Yuri and I read the book for a few hours, stopping about halfway through."
    hide black with open_eyes
    mc "What do you think of it?"
    y 1b "My impressions? It’s hard to judge without having read the full story, but I’m enjoying it so far."
    mc "Yeah. I’m not an expert on what good horror is like, but I had fun reading it, I think. This Lovecraft guy had a dark mind..."
    mc "It was pretty creepy, which I guess fits considering the genre, but this has kind of been a new experience to me."
    mc "Having you right next to me made it a lot more comfortable, though."
    "Yuri’s cheeks quickly redden."
    y 4a "Thank you…"
    mc "We should read the rest of this sometime."
    y 1d "I would like that."
    mc "I’ve really enjoyed this date, Yuri."
    y 1b "Ah… that’s right, I had forgotten that this was a date."
    y 1b "I’ve enjoyed it as well."
    "We look into each other’s eyes, until Yuri recoils from nervousness."
    y 1o "Sorry… I’m still getting used to this."
    mc "It’s fine, Yuri. We can go as slow or fast as you’d like."
    y "You must really like me, don’t you?"
    y "To be able to tolerate my company, and actually enjoy going to a bookstore with me…"
    y "There’s not many people like that."
    y "I’m thankful that you feel the way how you do about me."
    mc "Hey, I’m sure there’s a lot of people out there who would be honored to be in a relationship with you. I’m honestly shocked that you even like {i}me{/i}--in a good way, of course!"
    y "Less people than you think, [player]."
    stop music fadeout 3.0
    y "…a lot less."
    "Yuri seems to be saddened from this conversation. I have to find a way to salvage this."
    mc "Well… you’ve got me now, right? And the rest of the literature club, too. Regardless of how many people like you, what’s important is that there {i}are{/i} people who do like you."
    mc "What more do you need?"
    y 1j "I… I suppose that’s one way to put it."
    show yuri 1c at t11
    "Yuri seems slightly happier after hearing that, chuckling softly to herself."
    mc "I’d love to spend more time with you today, but it’s going to be evening soon, isn’t it?"
    mc "We should probably get ready to leave now."
    "Disappointment flits across Yuri’s face."
    y 1k "True. I wish we could be together for longer, but I guess this is how it is."
    mc "Yeah, sadly so…"
    "We hold hands together as we leave the store."
    scene bg streets_afternoon
    show yuri 1c at t11
    with wipeleft_scene
    "As we walk, though, I notice a certain someone on the sidewalk."
    
    "That guy… he’s from my school, isn’t he? The one who warned me off. As I stop to look over at him, he spots us. A small smirk spreads over his face as we simultaneously recognize one another."
    y 1f "[player]?"
    "I look away and begin walking again."
    mc "Sorry! It’s nothing."
    "Yeah, it would make sense to see him around town every once in a while, I think."
    "Why did this time feel so ominous? A premonition? Maybe the smirk. Yeah, that was sort of creepy." 
    
    
    "Not that it matters, I guess."
    "And wasn’t I supposed to talk about the rumors going on with Yuri?"
    show black with close_eyes
    "Ugh… guess I’ll just have to wait until next time."
    call yuriRoute_interlude
    return

label yuriRoute_interlude:
    scene bg bedroom with open_eyes
    play music aNewDay fadein 3.0
    "It’s been a week or so since my last date with Yuri."
    "I had planned to talk to her about the rumors I had heard about before, but couldn’t muster up the courage to do so."
    "I feel like it's a heavy topic, and I don't want to screw it up."
    "Nothing particularly bad has come up as a result of those rumors, though."
    "As much as I’d love to live in blissful ignorance forever, I’m going to have to talk to Yuri about it sooner or later, so I guess I may as well get it over with."
    "Groggily getting out of bed, I check my phone to see a text from Yuri sent a few minutes ago."
    $ o_name = "Phone"
    o "{i}Good morning, [player].{/i}"
    "At least Yuri still trusts me... I sort of feel bad about that. All the better to get this out in the open."
    "Once I’m done texting her back, I get ready for school and then head off."
    
    scene bg club_day with wipeleft_scene
    "Once my classes are over, I head over to the Literature Club, anxiety continuing to build up in the pit of my stomach."
    show yuri 1a at t44
    "As per usual, I spot Yuri reading a book at a desk."
    show monika 1b at t41
    show sayori 1c at t42
    "Monika and Sayori both try greeting me, but it goes in one ear and out the other as I pace over to Yuri."
    show monika at thide 
    show sayori at thide
    hide monika 
    hide sayori 
    show yuri 1a at t11
    mc "Hey."
    "Yuri turns and notices me. She quickly closes the book she’s reading, her finger caught between the page she was reading as a pseudo-bookmark."
    y 1b "Ah! Hello, [player]. I apologize for not noticing you as you came in."
    mc "It’s fine, don’t worry about it."
    mc "There was something I wanted to talk to you about, though…"
    show yuri 3o at t11
    "A vaguely nervous look crosses Yuri’s face."
    y "Hmm?"
    mc "See, there’s, um…"
    "How do I even word this?"
    mc "Basically, t-there’s, uh…"
    "I’m a stuttering mess right now."
    y 1n "Take your time, [player]."
    "I manage to blurt out what’s on my mind."
    stop music
    mc "There’s been rumors about us!"
    y 2r "What?!"
    "Way to go."
    mc "This guy, who’s one of my classmates, he came up to me."
    mc "He said something about there being ‘incidents’ involving you, and that I shouldn’t get caught up with you."
    mc "I know it’s not true!"
    mc "Yeah, it’s definitely not true. But what are we going to do, Yuri?"
    mc "You know how rumors go. They keep getting worse and worse, until… you know…"
    show yuri 1u at t11
    play music Amber fadein 3.0
    "A melancholic look passes over her face."
    y "…"
    mc "Yuri?"
    y 1v "This was a bad idea from the start, wasn’t it?"
    y "I knew that all I would do is cause problems for you."
    y "I’m sorry, [player]. This was all a mistake."
    "I notice Monika hesitantly come over."
    show monika 3b at t21
    show yuri 1u at t11
    m "Is everything okay over here?"
    m "I’m not entirely sure what’s going on, but perhaps you’d want to do this outside of the clubroom?"
    m "I mean, you don’t have to take my suggestion, but are you alright?"
    mc "We’re fine, Monika."
    mc "Just… please let us figure this out ourselves."
    show monika 1a at thide 
    hide monika 
    "Monika nods silently, going back and guiding Natsuki and Sayori to the far side of the classroom."
    "I really just don’t want to end up dragging anyone else into this."
    y 2v "[player], I…"
    mc "Look, Yuri. The rumors don’t seem to have gotten too bad. If they did, we’d probably be hearing more of them, right?"
    "Not necessarily true, but it’s what I’m going with for now."
    mc "First, we need to calm down. How about we just go out someplace after school?"
    "Yuri still seems frightened."
    y 2t "Are you sure?"
    mc "Yeah! It’ll be a great way to take our minds off of all of this."
    mc "Because if we do decide we want to do something about the rumors, then we should make sure we’re calm first, right?"
    y 2v "I suppose that might take off a bit of stress."
    y "If you absolutely think this will work, then I can oblige."
    mc "We can leave right after school, even. We’ll go to a park or something. That sounds fine, right?"
    show yuri 1s at t11
    stop music fadeout 3.0
    "I say that, but I think I’m just as anxious as Yuri is. I don’t even know if going on a date will work, but I have to try."
    "Once literature club is over, Yuri and I get up together and walk outside the school."
    "We have each other. I know for a fact that we'll be fine in the end." 
    call yuriRoute_petrichor
    return

label yuriRoute_petrichor:
    scene bg park_rain with wipeleft_scene
    "A gentle breeze blows past."
    "The sun shines through the clouds, warming the air to just the right temperature."
    "There’s nobody here but us."
    "Nobody but us to enjoy a perfect date at a park."
    mc "This is a pretty nice place, huh, Yuri?"
    play music YurTheme fadein 3.0
    show yuri 2n at t11
    "I turn to Yuri, sitting next to me on a bench."
    y 2m "Yes, this location is quite nice."
    y "It’s incredibly peaceful, as well."
    mc "Yeah. The real highlight is getting to spend time with you, though."
    "I motion for Yuri to scoot closer to me."
    y "Really?"
    y 2o "Are you sure that’s okay?"
    mc "Of course! We’re on a date, after all."
    y "I suppose that’s true…"
    show yuri 1q at f11
    "Yuri slowly scoots closer to me as I put my arm around her."
    mc "This is great, isn’t it? Or at least good, if nothing else."
    y 3c "This is nice, I’ll admit."
    mc "That’s what I thought. I feel kinda bad that I didn’t pick this spot for our first date, but whatever."
    y 2s "The fact that you’re considerate enough to feel remorse for even small things like that…"
    y "My feelings for you keep growing stronger, [player]."
    show yuri 1p at t11
    "After saying that, Yuri quickly scoots away."
    mc "Whoa! You okay, Yuri?"
    y 1o "That was too forward of me, wasn’t it?!"
    y "You must think I’m trying to take things too quickly..."
    y "I’m so sorry, [player]."
    mc "Not at all, Yuri. I’m perfectly fine with it."
    mc "I find it romantic, actually."
    y 1t "Are you sure?"
    mc "Yes, Yuri. I’m sure."
    "Yuri scoots back little by little."
    show yuri 1t at f11
    y "Thank you for not getting upset, [player]."
    y 1v "You know those rumors are false, right? You said you do, but I wouldn’t fault you for being mistaken…"
    mc "No rumor is ever going to change how I feel about you, Yuri."
    mc "Even though I’m not totally sure what those people have in mind, I know that it’s not true."
    mc "I love you, Yuri. That’s all that matters."
    y 1b "I… Thank you, [player]."
    "The day slowly progresses as Yuri and I sit, idling in the park. We sometimes talk to each other throughout it, but for the most part we’re enjoying the tranquil silence and one another."
    mc "You know, Yuri, about what you said earlier…"
    mc "I think my feelings for you are getting stronger, too."
    y 1f "Really?"
    "Yuri looks surprised."
    mc "Yeah! You’ve got a lot of great qualities. I think it’s cool how much passion you have for stuff like poetry."
    y 2v "You’re flattering me too much, [player]."
    y "But that’s something I like about you, too."
    y "The way you respect me, no matter how involved I am in my interests…"
    show yuri 3s at f11
    "Yuri looks up at me and leans in. I follow suit."
    show yuri 3s at face(y=600) with dissolve
    "Our lips are barely inches away from each other."
    "Closer and closer…"
    show white
    stop music
    play sound thunder

    "{i}KRA-BOOM.{/i}"
    hide white
    play sound rain
    "Dammit."
    mc "What? It’s not supposed to rain until tomorrow!"
    "The mood is ruined as the sky splits open in a fit of thunder, dousing us in rain."
    scene bg residential_rain with wipeleft_scene
    "I take Yuri's hand and make a break for it, pulling her through the streets."
    "We manage to find some shelter, even if it's not much."
    mc "Ugh…"
    show yuri 1v at f11
    y "Ah… I should’ve tried sooner. I’m sorry, [player]."
    mc "No, it’s fine. Just not something I expected."
    "The rain pours harder."
    mc "What do we do now?"
    y 3q "We could spend some more time at your house."
    y 3p "O-Only if you want to, of course!"
    "Yuri is flustered, but I understand what she’s saying nonetheless."
    mc "We can go back to my house, sure."
    mc "Might as well get up now before the rain gets any worse."
    y 3q "I agree."
    
    scene bg house_entrance_night with wipeleft_scene
    "As we dash up to my house, I open my front door and we step in."
    stop sound fadeout 3.0
    mc "Much better."
    mc "Want a seat, Yuri?"
    show yuri 1b at t11
    y "Seeing as you’re offering me one, it’d be rude for me to turn it down."
    
    scene bg home_interior_night with wipeleft_scene
    show yuri 1a at s11
    "Yuri makes her way over to the living room couch and sits down, as I proceed to sit down next to her."
    "The couch’ll end up wet, but it's not something that I really care enough to worry about right now." 
    mc "Man, if I had known it was going to rain, I would’ve brought an umbrella."
    "Yuri shivers."
    y 1b "It’s fine, you didn’t know it was going to rain."
    mc "I know, but still. You seem pretty cold."
    "Yuri realizes that she’s been slightly shaking."
    y "I can live with it…"
    show yuri 3p at h11
    y 3p "I hope I haven’t gotten your couch wet!"
    "Yuri quickly tries to get up."
    mc "Hey, it’s fine. Sit back down, please. I care more about you than a dumb couch."
    show yuri 2u at s11
    "Yuri is reluctant, but slowly sits down again."
    mc "Here."
    "I take off my jacket and give it to Yuri."
    y 3o "Huh?"
    mc "Wear it. The outside’s wet, but the inside is still warm."
    y 2v "Are you sure?"
    mc "Yup. That’s why I’m giving it to you."
    y 3c "I see… Thank you, [player]."
    mc "I can’t let my girlfriend freeze to death, can I?"
    "Yuri quietly laughs."
    y 1b "Even though the rainstorm interrupted our date, isn’t the sound of rain incredible?"
    mc "I don’t know if I’ve put too much thought into appreciating it, but it is kind of nice in a way."
    y "Yes. The magnificence of the constant droplets, accompanied with the thrashing sounds of lightning… It’s truly beautiful."
    mc "I can see where you’re coming fro--"
    mc "Huh?!"
    show yuri 3n at f11
    "Yuri’s arms are tightly wrapped around me."
    y "You must be cold too, [player]."
    y "Why don’t we warm each other up?"
    y 3o "You may hate me later for doing this, but I-I wanted to at least give it a try."
    mc "I mean, sure? I-I’ve got no complaints about this."
    "I wrap my arms around Yuri as well."
    "Things are definitely heating up in some sense, at least."
    show black with close_eyes
    "We stay there for about twenty minutes, just listening to the rain pour down."
    
    "{i}BZZT!{/i}"
    hide black with open_eyes
    "My pocket vibrates with a notification."
    "On instinct, I take my phone out to see that a new email message has been sent to me."
    y 3f "[player]?"
    mc "It’s nothing, just an email. I’ll read it as quickly as I can."
    show yuri at thide 
    hide yuri
    "But as I scan this email, something is very, {i}very{/i} wrong."
    
    "{i}Subject: Freak Alert!{/i}" 
    "{i}You guys know how much of a freak Yuri is, right? I mean, we've all seen the scars, and we've all seen how she acts, too.{/i}"
    "{i}She gets turned on from cutting herself! Kinda messed up when you think about it, you know? Actually, even if you don’t, but hey.{/i}"
    "Oh, no." 
    
    "{i}So, right, she’s a loser, whatever. I mean, every school has its freaks.{/i}"
    "{i}You know what’s even more messed up, though? She’s dating [player]. Yep, you heard right, folks.{/i}"
    "{i}Someone in this school was either desperate enough or just as much of a freak to date fucking Yuri.{/i}"
    "No no no no no." 
    "Please, no."
    "{i}But really, can you even guess what absolutely horrifying crap they do? I bet they both get turned on from cutting each other!{/i}"
    "{i}Is that even legal? Probably not, but let’s be real, do they care? It’s just really funny, but also kind of absolutely, disgustingly awful.{/i}"
    "Why can’t I stop reading this? Why can’t this all be a bad dream?" 
    "{i}And you know what? I can see it now. Once they’re done cutting each other, Yuri gets all hot and bothered.{/i}"
    "{i}And then--Well, I won’t finish that sentence, but you know what they do, though. I’d be willing to place bets. The truth’s out there, folks.{/i}"
    "…"
    "{i}Matter of fact, I’d be willing to place bets on what Yuri’s other fetishes are, too. Bloodplay’s an obvious one, but what else?{/i}" 
    "{i}Probably something super gross. Piss? I’d expect nothing less from her. I wonder what [player]’s fetishes are, though. Think they’re better or worse?{/i}"
    "…" 
    "…"
    "{i}Y’know, in a way, I’m happy to find out all this. You guys know what it’s like to feel bad about yourself, right?{/i}"
    "{i}But knowing that freaks like these exist… it makes me feel a bit better about myself, honestly.{/i}"
    "{i}I hope that it makes all of you feel better, too, for not being human garbage.{/i}"
    "…"
    "{i}So yeah, I was just warning everyone. Long story short, stay away from Yuri and [player].{/i}"
    "{i}They’ll probably go slicing up anyone nearby when they get the urge, so I want to make sure you all stay safe, alright?{/i}"
    
    "This… can’t be real." 
    "I look, and… of course."
    "Of course this message got sent to my whole school." 
    "Why would it have been anything else?"
    "It’s the natural progression of the rumors I thought were beneath me. Beneath {i}us{/i}."
    show yuri 3b at t11
    y "[player]."
    show yuri at thide 
    hide yuri
    "Here I am now. What do I do?! Did the message get sent to Yuri, too?"
    "If the message did get sent to Yuri, what the hell am I supposed to do about it? What the hell {i}can{/i} I do about it?"
    "I feel like puking... screw this."
    "{i}BZZT!{/i}"
    "I get another notification, and it’s a second email."
    "{i}Subject: What’s up, freako?{/i}"
    "It’s from the asshole that sent the mass email, of course. This message is addressed to me specifically."
    "{i}Hey, [player]! Y’know, I hadn’t planned on calling you by your name, but I think the students of our school need to know the what’s what when it comes to you.{/i}"
    "{i}Hope you like the new nickname, either way!{/i}"
    "{i}But seriously, how are you doing? I bet you and your girlfriend are cutting yourselves like you always do.{/i}"
    "{i}I mean, sorry if I’m interrupting anything, if that’s what’s happening.{/i}"
    "{i}Aaaaaaaanyway, I was saying, your girlfriend didn’t get a notification for the email, right?{/i}"
    "{i}I didn’t send it to her. But I’m going to shortly after sending this, soo…{/i}"
    "Each sentence I read feels like a physical blow, a dozen knives twisting in my chest."
    "{i}Bet you’re freaking out, huh? But hey, you freak us out, too, so it’s basically karma.{/i}"
    "{i}I drafted this email earlier today, y’know, just thinking of the face I know you have right now.{/i}"
    "{i}Now, you may think I’m doing this to get something out of you, but really, that’s not it. Like I said, I’m trying to keep everyone safe.{/i}"
    "{i}I know for a fact that sickos like you and Yuri can’t be trusted. I mean, we’ve been down this road before with just Yuri, but another guy, too?{/i}"
    "{i}I'm only doing what's right. You get that, yeah?{/i}"
    "I… I…"
    "{i}But enough of that from me. By the time you’re done finishing reading this message, you’re going to hear a wonderful little jingle on your girlfriend’s phone.{/i}"
    "{i}I wonder what that jingle’s going to play for? What will her notification contain?{/i}"
    "{i}I think you’ve already got a good guess what it is, though, unless you really are that stupid… which wouldn’t surprise me, but whatever.{/i}"
    "{i}The real question is… how will you react?{/i}"
    "{i}Okay, I’m done now. Later, freako! And please, take a shower, would ya? Thanks.{/i}"
    "My insides tie up into a knot as I hear Yuri’s phone vibrate."
    "{i}BZZT!{/i}"
    y 1e "Hmm? It seems I have a notification as well…"
    "I don’t have time to decide whether or not this is a good decision, but I rush to grab the phone from Yuri before she can turn on the screen."
    "Yuri is confused, but I hardly pay attention to that as I go as quickly as I can to delete the email she just got. {i}Friendly message from the student body.{/i} Right."
    y 1f "[player]? What are you doing with my phone?!"
    "A few swipes, and it’s gone, as if it’d never existed. {i}As if.{/i}"
    "Now I just need to come up with an excuse."
    mc "Sorry! It was a spam email. I got one with the same title just a minute ago, so I thought that you had been sent the same one. It seems my hunch was right, too."
    show yuri 1h at f11
    "Yuri looks skeptical."
    y "Really?"
    mc "Yes, really. I promise, Yuri. It’s nothing to worry about."
    y 1f "You’re absolutely sure?"
    mc "I am."
    "I’ve already messed up. I’m already going to face the consequences of this soon enough."
    y "Hmm…"
    y 2v "[player]..."
    mc "It was nothing important. Plus, if I seriously wanted to pull something with your phone, it would’ve taken me longer than three seconds to do so."
    y 1f "You’re acting suspicious, [player]."
    y "I think even you realize that."
    mc "Let’s… let’s just move on, okay? There’s nothing to get worked up over, so why should we waste any time doing so?"
    show yuri at thide
    hide yuri
    "But I know I can’t do that. I know it’s not going to be the same after reading that email."
    "I don’t think {i}anything{/i} will be the same after reading that email."
    show black with close_eyes
    call yuriRoute_shatter
    return

label yuriRoute_shatter:
    pause(2.0)
    scene bg corridor with open_eyes
    play music Amber fadein 3.0
    "--It’s Monday. Time to face the music."
    "So far, Yuri hasn’t figured out anything about the chain email that’s already spread across the school, but it’s only a matter of time."
    "I want to expunge this, before Yuri ever catches on. I don’t even think I can, but I have to try. I couldn’t stand to see her face when she realizes. I know exactly how that conversation will go down."
    "My phone buzzes with a text. Yuri."
    $ o_name = "Phone"
    o "I didn’t see you in our usual place. Are you going to school today?"
    scene bg club_day with wipeleft_scene
    "I did rush to school today, when I think about it."
    "I slide down into my seat, tapping out a brief response."
    mc "Yeah--I needed to take care of some business with the teacher before class. Sorry!"
    p "Alright. I love you, [player]."
    "I stuff the phone back into my pocket and exhale softly. I have my plan. Find the source of the email, first off."
    "And if my instincts are anything to go on, I know just where to start."
    play sound crowds fadein 3.0
    scene bg corridor with wipeleft_scene
    
    mc "Hey."
    "Talking to the guy who warned me about Yuri seems like it could give me a clue or two."
    
    "The boy seems surprised for a second before he adopts a neutral expression, throwing up a hand."
    $ o_name = "Senior"
    o "Yo, [player]."
    mc "Hello."
    "The conversation, if it could even be called that, stalls on the ground."
    "He probably knows I’m suspicious. Now he’s waiting for me to make the first move."
    "I frown."
    mc "Have you gotten any strange emails recently?"
    "He blinks, then shakes his head."
    o "Nothing outta the ordinary, my man."
    stop sound fadeout 2.0
    "Finishing with a shrug, he plays it off so well I doubt my first instincts that it was him."
    "Doubts begin to creep up as I nod quietly, heading to my classroom."
    scene bg class_day with wipeleft_scene   
    "After all, there could always be others--and I was running essentially with blinkers on all sides…."
    "I could’ve missed something... something obvious."
    "But who else has the following but him to swing this?"
    scene bg class_day with wipeleft_scene    
    
    play sound bell
    "Well, there goes half my day."
    "I raise my head from the desk, having previously just been napping away the time. History’s the next class, so I should get my stuff for that."
    "I’ve decided to gather information in the afternoon. I’ll be skipping going to the Literature Club, but I’d argue it’s for a good cause."
    play sound closet_open
    stop music
    "The back door of the classroom slides open, and {i}he{/i} steps back inside, followed by a group of his cronies."
    "I try not to be too judgmental."
    "I’m failing."
    o "It wasn’t all me, actually--"
    $ o_name = "Other Student"
    o "Well, o’course not. But didn’t the guy get on your case? You told us he did, at least."
    "He shrugs. The same dismissive, contemptuous shrug."
    $ o_name = "Senior"
    o "I mean, I did try to warn him, didn’t I?"
    o "This is just a fun idea I had, y’know? Been awhile since I’ve seen a good chain-email go round."
    $ o_name = "Other Student"
    o "Yeah, that’s true, that’s true."
    $ o_name = "Senior"
    o "Who knows, maybe he’s into that. A cutting fetish? What do they call that, anyway?"
    $ o_name = "Other Student"
    o "I think it’s like… bloodplay?"
    $ o_name = "Senior"
    o "Yeah, that. Wait, how do you know about that, huuuuh?"
    "Another boy snorts."
    $ o_name = "Other Student"
    o "Probably was just going after someone with low self-esteem for the easy win."
    show red with dissolve:
        alpha .3
    "My blood boils over."
    "Fuming, I stand up, stalking over to the huddled mass of boys. Only the blonde one, the one who started this mess, even bothers looking up."
    "He looks at me and his face shifts into some midpoint of confusion and humor."
    $ o_name = "Senior"
    o "Yo, [player]. How you holding up?"
    
    "I’m not gonna listen any longer."
    
    show red with dissolve  
    window hide 
    pause(3.0)
    scene black with wipeleft_scene 
    window show
    $ o_name = "Principal"
    o "So… then you punched him."
    "The blonde guy snorts, folding his arms. He’s got the principal on his side, which means anything I say is irrelevant."
    "I did start it, though, so it’s only to be expected."
    "I nod quietly."
    o "More than once, I should add. According to eyewitnesses, it looked like you were trying to kill him."
    "I frown, staring at the knot of his tie."
    mc "I’m not apologizing."
    "The stout principal sighs as he takes off his glasses, lacing his fingers together."
    o "I can’t act about hearsay, but starting a fight is a serious offense."
    o "As for you..."
    "The principal looks at the boy and continues speaking."
    o "...you may go. Have the nurse take a look at you if needed."
    "I take some small satisfaction in seeing him wince as he tries to nod. It’s childish, but I’ll take what I can."
    o "[player]."
    "Oh, joy."
    o "I am giving you a two-day suspension. You will need to gather your things and call your family."
    "I give a ragged sigh, nodding back."
    mc "Yes, sir."
    o "And try to keep your temper in check for the next time?"
    "I bite the inside of my cheek, stifling a response. Instead, I turn on a heel and walk out."
    
    scene bg bedroom with wipeleft_scene    
    
    "That went about as well as could be expected, really."
    "I stare up from my bed. My phone has been buzzing non-stop for about five minutes. No doubt Sayori trying to check in. Texting in class? I should scold her."
    "I appreciate the concern, but right now I just need quiet."
    "I need to figure out how to handle this, because I’ve done something unbelievably stupid."
    "I got so caught up in my own anger I lost sight of what my actual goal was."
    "I mean - maybe, if I’m lucky, the fight I started will give them something else to gossip about…"
    "But if I know anything about the student body, it’ll just get tacked on as extra material to the main story."
    "Eventually, my phone stops buzzing."
    "I turn over onto my side, curling into the sheets on the bed."
    

    call yuriRoute_aftermath
    return