# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")

define m = Character("Mitchell")
    # remember to redefine m as "Mitch" when the time comes.
define dude = Character("Dude Bro")
# "dude" is for before we know Mitchell's name.

define s = Character("Stephan")
define zoo = Character("Zoo Supervisor")
# "zoo" is for before we know Stephan's name.

define o = Character("Ollie")

#######################

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ########################################################
    ## PLAYER NAME INPUT ##

    python:
        mcname = renpy.input("What's your name?")

        mcname = mcname.strip()

        # .strip() removes any accidental extra spaces.

        if not mcname:
            mcname = "Mona"

    mc "My name is [mcname]."

    ########################################################
    ## STORY START - PROLOGUE ##

    scene cg grad day
    with fade

    "{i}Congratulations, class of 20XX!{/i}"

    "{b}Everyone{/b}" "Hurray!"

    mc "{i}Wow, the day has finally come."
    mc "{i}After what felt like forever, I've finally graduated university, class of 20XX."

    menu:
        mc "{i}I officially have a Bachelor's degree in...{/i} (choice doesn't matter)"

        "Anthropology":
            $ major = "Anthropology"
            jump picked_major

        "Engineering":
            $ major = "Engineering"
            jump picked_major

        "Music":
            $ major = "Music"
            jump picked_major

        "Fine Arts":
            $ major = "Fine Arts"
            jump picked_major

        "Literature":
            $ major = "Literature"
            jump picked_major

        "Mathematics":
            $ major = "Mathematics"
            jump picked_major

        "Computer Science":
            $ major = "Computer Science"
            jump picked_major


label picked_major:

    mc "{i}I officially have a Bachelor's in [major]. And now... I'll be thrown out into the world, I guess.{/i}"

    mc "{i}A job? What's that?{/i}"

    mc "{i}People usually start applying as soon as fall breaks and it's back to winter, but I don't know what it was, I just couldn't do that.{/i}"

    mc "{i}I didn't know enough about my direction or future at that point to start taking that step.{/i}"

    mc "{i}And to be honest, even though it's commencement day, I still don't know.{/i}"

    mc "{i}It's not that I don't have ambitions. Or that I don't see a strong future for myself. I really do."

    mc "{i}To be honest, when I'm finally prepared and I put myself to it, I know that I'll kick total ass.{/i}"

    mc "{i}It's just... I'm not there yet, even though maybe I should be.{/i}"

    mc "{i}But I know it's common, so much that it's stereotypical, for fresh college grads to feel pretty lost.{/i}"

    mc "{i}My mom keeps asking me about my job hunt. I don't know what to tell her.{/i}"

    mc "{i}I'll achieve just fine at some point, I know that, but after the final push of finishing school, I just need to...{w} regroup. Take a breath.{/i}"

    #############################################################

    scene

    show mona neutral smile
    # some sort of transition. fade?
    mc "I've decided, at least for this summer, that I'm going to take it slow."

    show mona thoughtful
    mc "It's my first summer of real {i}freedom{/i}— I'm gonna try not to rush myself."

    show mona happy
    mc "I'm going to work part-time, stay in town, save up, and just take some time to clear my head before taking the next step."

    show mona determined
    mc "If I'm on the verge of starting life's next big chapter, I think it's fine to appreciate the time I still have in this one before I finally turn the page."
    mc "Take some time to reflect, time for myself, and maybe just to figure out my direction."

    # fade out

    jump prologue_stephan

    #################################################

label prologue_stephan:

    # fade in - scene @ petting zoo desk
    scene #petting zoo
    with fade

    show mona earnest talking
    mc "Um, yeah, the name's [mcname]. We talked on the phone?"

    hide mona
    show stephan neutral
    zoo "Right. So you want to... work at the petting zoo?"

    "He looks down at the paperwork in front of him nonchalantly."
    "{i}I don't know what it is, but the way he said that felt weird. Judgy?{/i}"
    "{i}That doesn't seem right, considering...{w} this is HIS petting zoo...{/i}"

    hide stephan
    show mona nervous laugh
    mc "Uh, yeah. Is there... a problem?"

    hide mona
    show stephan neutral
    zoo "Oh, no. I'm just used to working alone."
    # "i just haven't worked with many people outside my family"? idk

    "The zoo supervisor is going through the papers, not making much eye contact with me."

    hide stephan
    show mona alert
    mc "Oh, um... Is there not... other staff?"

    hide mona
    show stephan neutral # change this to unimpressed sprite
    zoo "Does it look like a large enterprise?"

    "He gestures vaguely around him."

    show stephan neutral
    zoo "We're connected with plenty of folks who regularly come around to help, or check up on the animals, bring hay and feed, etcetera. And of course, we're always connected with the veterinarian."
    show stephan happy
    zoo "But the zoo is not exactly rocket science. I'm familiar with these animals. When my parents ran the place I worked here often. I'm comfortable with them and have lots of experience."
    show stephan neutral
    zoo "We might get contracted for a carnival, or a birthday party. It's common in the summer. But really, I handle it myself most of the time.{w} Except for the odd volunteer."

    "He looks at me, perhaps pointedly?"

    hide stephan
    show mona intrigued talking
    mc "Or... part-timer?"

    hide mona
    show stephan neutral
    zoo "Right."

    "There's a silence."

    hide stephan
    show mona intrigued
    mc "So... I'll just be working with you?"

    hide mona
    show stephan neutral
    zoo "Well, you'll still be working with the local farmers and other points of contact here."

    hide stephan
    show mona neutral smile
    mc "But as far as the day-to-day goes? Working with the animals and the guests?"

    hide mona
    show stephan neutral
    zoo "Yes."

    hide stephan
    show mona very happy
    mc "Sounds fun."

    "I smile to him, not being sarcastic. He doesn't seem too impressed."

    hide mona
    show stephan suspicious
    zoo "...Indeed."
    show stephan neutral
    zoo "Anyway, we'll be working alongside each other, but I'm still your supervisor."
    zoo "My contact information is on your onboarding sheets. Are there any questions?"

    "I glance down at the sheets he's handed to me. I see his name: Stephan Kaur."

    hide stephan
    show mona happy
    mc "No... I don't think so. We'll cover most of it on my first day, right?"

    hide mona
    show stephan happy
    s "Yes. I'll show you around the enclosure and tell you how to tend to the animals, as well as deal with children, along with the more administrative work."

    hide stephan
    show mona overjoyed
    mc "Oh, well, I don't think you have to worry about the children. I love kids, I'm really great with them. I have some experience as a nanny."

    hide mona
    "{i}Talking about it makes me think of the last family I worked with, and the children and families I've had some of the longest relationships with.{/i}"
    "{i}It's been a while since the last time I've done it, but I honestly miss it.{/i}"
    "{i}Being a positive influence to children means a lot to me, even if it's small, so I'm looking forward to working with kids again this summer.{/i}"

    show stephan neutral
    s "Well, alright then. But I see you don't have previous experience working with animals, so you'll have to go through training as well as learning how we run."
    s "And I'm certain we'll be requested for several events during the summer, so as those approach, I'll have to prepare you for them as well."

    hide stephan
    show mona amused
    mc "Sounds good."

    "I smile again, trying to show that I'm eager."

    hide mona
    show stephan neutral
    s "..."

    hide stephan
    show mona nervous laugh
    mc "...I look forward to it."

    hide mona
    show stephan neutral
    s "...Alright. Well, we'll be in contact. I'll see you on your first day."

    hide stephan
    show mona very happy
    mc "Alright. Thank you, Stephan!"

    hide mona
    show stephan confused
    s "..."

    hide stephan
    show mona thinking # change to a better sprite
    mc "..."
    show mona intrigued talking
    mc "...Mr. Kaur?"

    "I can't tell if calling him by his first came off to him as too informal or familiar. But I mean, we're basically going to be coworkers."
    "He's not that much older than me, so calling him \"Mr. Kaur\" just seems weird. But I mean hey, if he prefers it I'll absolutely be respectful."

    hide mona
    show stephan annoyed
    s "...{w}Ah, forget it."
    show stephan intrigued
    s "I'd rather correct you to \"Mr. Kaur\", but when I was about to say it, it still sounded odd."
    show stephan confused talking
    s "Those who've worked here have been family, and it's not like I've had many \"subordinates\". So there's no precedent I'm used to,{w} though referring to my first name seems inappropriately comfortable."
    show stephan amused
    s "But forget it, it's not like this is corporate. It ultimately doesn't matter. I can't really bother to come up with a preferred way to refer to me, so just do what you'd like."

    "{i}Wow, thanks! That was super helpful and totally clear and now I TOTALLY know the right thing to call you. \*Sighs\*{/i}"
    # ^ rewrite this?

    hide stephan
    show mona awk laugh sweat drop
    mc "Uh... thanks..... Mr. Kaur?"

    "That still feels weird, but I'm just playing it safe."

    hide mona
    show stephan happy
    "Mr. Kaur?" "Sure."

    hide stephan
    "I turn around and walk away from Mr. Kaur (Stephan?) at the zoo's front booth, feeling a little awkward."
    "{i}Ah, whatever. The zoo guy's pretty stuffy, but it's going to be fine. I mean, it's a petting zoo— how hard can it be, and also, I feel like my more-chipper personality is a way better fit than... whatever he is!{/i}"
    "{i}Working with him might be a bit of a learning curve but other than that, I know I'm gonna do great. Working with the animals is going to be fun, too.{/i}"

    scene # street or whatever

    "Before I head back to my apartment, I take a moment to look at my surroundings."
    "{i}This is where I'll be spending most of my time this summer, huh?{/i}"
    "Admittedly, I can be kind of a homebody, even when it's summer. Living in Hawthorne, CA, it's almost blasphemous."
    "It's a total beach town, with gorgeous (but ugh, HOT) summers, and most of the folks around here are practically glued to their boards as soon as the weather's nice enough."

    "The petting zoo I applied to is close to the beach; most of its business when there isn't a festival or something comes from people on the boardwalk."
    "Having animals near the beach might be kind of weird, but it's actually sort of genius once you consider how much business ricochets to them from the beachgoing crowd alone."

    "How many families take their kids out to the beach during the summer? A million, probably."
    "And when a kid unexpectedly gets the chance to pet cute animals, and they're already hyped because of the beach, you {i}know{/i} they're dragging their parents there."
    "It's a rather nice little ecosystem, when you think about it."

    "{i}It's funny, that guy at the zoo doesn't really seem like someone who's exactly great with kids. I guess he comes off as the type of guy who might not like them?{/i}"
    "{i}But kids are probably who he encounters the most at his job, so I don't know, I guess he makes it work.{/i}"

    "Anyway, even if I won't exactly be spending by time on the beach while I'm working, it'll be nice just to be around the lively people and salty air."
    "Just being around a California beach in the summer is gonna rub off on me and make me want to go outside more, and hell, the beach will be a perfect place to take my breaks or hang out after my shifts."
    "Even if I spend the summer busy doing nothing, I think it's gonna be great."

    #######################################
    #fade
    # a few days later

    "After a few days, it's my first shift. Mr. Kaur— Stephan?— closed the place up for a little while so he could show me around."
    "After going over the materials at home that he gave me when I first came around, I know a bit about the different types of animals that are here, what feed they eat, etc."
    "The hardest parts will probably be in actually handling them (not to mention cleaning up— eugh) and instructing the kids on how to pet them, making sure the animals don't get manhandled. Or that kids don't get bitten..."

    "Stephan shows me around the chickens, goats, and rabbits. He shows me how to handle them— the right ways to pick them up, right and wrong ways to feed them, how to read the behavior, blah blah blah."
    "The admin stuff is pretty simple— working at the front, handling tickets and customers, knowing the calendar, knowing how to balance the number of people in the enclosure at a time."

    show stephan neutral
    s "For your first several shifts I'll keep you at the front. Talking to customers and handling admission."
    s "We'll spend more time with the animals after close, and I'll train you on that throughout the week. Once you have the hang of that you can start working in the enclosure."

    "{i}Bleh, I don't really want to spend time off the clock working on more training.{i}"
    "But whatever, an extra hour or whatever each day to spend time with the animals sounds kinda fun."

    hide stephan
    show mona happy
    mc "Awesome! Thanks so much."

    hide mona
    show stephan intrigued
    s "Thanks for what?"
    #raised eyebrow or whatever

    hide stephan
    show mona nervous laugh
    mc "Uh, I dunno... Showing me the ropes and everything?"
    show mona nervous smile
    "{i}I don't know, I'm just being polite, dude! Just say \"no problem\" or \"see you tomorrow\" or something!"

    "He just looks confused."

    hide mona
    show stephan neutral
    s "Well, yes, it's the job."

    "{i}God, this fucking guy.{/i} Whatever."

    hide stephan
    show mona unimpressed # annoyed sprite?
    mc "Ugh, whatever."
    show mona neutral
    mc "So when I'm able to work in the enclosure, will we take turns working there and in the front?"

    hide mona
    show stephan neutral
    s "Yes. Really, I'll deal with whatever needs more attention and give you the other. I'll also call you for assistants or tasks whenever it's needed."

    hide stephan
    show mona happy
    mc "Okay, sounds good."

    "{i}Kind of boring, but really doesn't sound too demanding. I think the work will be straightforward, it sounds like he'll deal with the stuff that's actually hard. That's pretty nice.{/i}"

    hide mona
    show stephan happy
    s "Well then, let's open up."

    "He turns with a little smile as he unlocks the door and pushes it open. He flips the sign out front from \"closed\" to \"open\", and heads back toward the enclosure while I man the front."

    jump prologue_mitchell

    ##########################################################

label prologue_mitchell:

    scene #view from desk

    "Some time passes just talking with families, handing stickers to kids, y'know, the usual."
    "It's not just families and kids that come to the booth; there's a good number of teens and people my age who come to the beach with their friends and stop in."
    "At one point, a dude-bro looking group of guys around my age come by the booth, holding their surfboards and joking around amongst themselves."
    "People like that make me a little self conscious— I'm not \"uncool\" or anything, in fact, I think I have a pretty solid personal brand— but being around overtly \"cool-looking\" people, I can't help but feel like I need to act a certain way."

    "{i}What are they gonna do, take you out back for a freakin' swirly? Obviously not, jeez.{/i}"
    "But still, I feel a little under the microscope when gaggles of obviously popular kids come 'round and start talking to me."

    "And...{w} ah god, they've come 'round to start talking to me. Of course!"

    "{i}Okay, just chill out. Jesus, what's your deal?{/i}"

    "This \"you know I had to do it to 'em\"-looking dude comes up to the booth, with a group of about five friends behind him."

    # mitchell sprite

    dude "Hey, little tomboy."

    mc "...{w} Excuse me?"
    "{i}I don't mean it like I'm offended, I'm just... what does that even mean??{/i}"

    "The guy laughed a little, affably."

    dude "Oh, sorry. You just reminded me of something.{w} I like your shirt."

    mc "Uh, thanks."
    mc "I like your... shorts?"

    "I had to peer over the desk a little to be able to actually see anyone's legs. He's wearing, like... deck shorts, but I like the color."

    dude "Hey, thanks."

    "He smiles at me."
    "{i}Man, people this straightforwardly confident get me kind of on edge. I can't tell if I'm acting like a fool or if they're actually just being nice.{/i}"

    "He looks back behind him for a second, mentally counting the heads of his friend group. He turns back around to me."

    dude "Uh, can we have six tickets?"

    mc "Um, sure. You guys will have to wait a little bit since you're a larger group."
    mc "If you just wait over there for a few minutes, I'll call you over when we're ready."

    "I point to a nearby bench outside, our unofficial waiting area."

    dude "Sweet. Thanks."

    "He turns back to his friends, getting ticket fare from everyone before turning to hand the money to me."

    dude "Here you go."

    "I take the money, punching into the till and printing off the tickets."

    mc "Alright, here you go."

    "I hand him off the tickets."

    mc "What name should I call for you guys?"

    dude "Mitchell's fine."

    mc "Alright Mitchell, well thanks for coming by the zoo. Your group should be able to go in pretty soon, about 5-10 minutes."

    "He gives me a bright smile before heading towards the bench with his friends. I awkwardly smile back."

    "{i}(A few minutes later...){/i}"

    "I help a group of four parents and their gaggle of kids out of the zoo. The kids are so excited and jumping around; one of the little girls grabs her mom's hand, talking excitedly about the rabbits."
    "The mom smiles at me, thanking us, as the group tries to lead their kids back towards the beach."
    "{i}It makes me feel really happy and full seeing those kids so excited...{/i}"
    "I glance around, seeing that group from before sitting by the bench. Oh, right."

    "I open the gate-door-thing by the front desk area, walking out to approach the group. They seem to be happily talking and joking around."

    mc "Mitchell?"

    "I can't tell if they heard me. I look around to the friends."

    "Dude Friend" "Hey, Mitch, I think she's talking to you."

    "The guy from before was distracted in a conversation, but he quickly turns around."

    m "Oh yeah, hey! Sorry."

    mc "You guys can go in now."

    "He stands up with another bright smile. It seems genuine, but the guy's still a little much."

    m "Awesome, thanks!"

    "I notice that they start looking around at their surfboards, unsure what to do with them."

    mc "I can keep your boards right behind the desk. Just come back for them once you leave, alright?"

    m "Excellent. Thanks. Hey, I'll help walk them up with you."

    mc "Alright, thanks."

    "I smile, appreciative of the help. I'm definitely kinda small; it would have taken me a couple trips to carry them all."
    "I take two boards under my arms while he grabs the others. We walk back up toward the desk, where I open the gate with my foot and we place the boards up against the wall. I dust off my hands."

    mc "Alright, well, I hope y'all have fun. Stephan should be able to help you if you guys have any questions while you're there."

    "Mitchell smiles at me again. I guess it must naturally just be bright. I guess I'm a little more used to it now after constant exposure, and it's a little endearing."

    m "Thanks, [mcname]."

    "I'm immediately caught off guard by that. I realize he's looking towards my shirt, and I look down—{w} Oh, my name tag... duh..."
    "I guess that mental calculation took enough time that I couldn't come back with some witty response, not that I had one."
    "When I look back up he's out of my desk area, giving me one last wave as he turns back to follow his friends towards the enclosure."

    jump prologue_ollie

    ############################

label prologue_ollie:

    # scene - mona at desk

    "I while away the next few hours at the desk,{w} conferring with the flowers, consulting with the breeze..."
    "...Sorry, starting that sentence made me think of the Wizard of Oz. But really, the rest of the day goes by without much incident."
    "There are definitely some slow patches, and other blocks of time where a ton of people come by at once, but either way, it thankfully wasn't too boring."
    "Even when nothing's going on, I can look towards the sprawling beach in front of me, or just people watch, or even take a second to myself to breathe in the fresh salty air. It's kind of nice, really."

    "Work comes to a close, and now it's time to get some animal training from Stephan in the back."
    "The lesson only lasts for about an hour and a half, and as the sun starts to head over the horizon, it's time for us to head home."
    "I say bye to Stephan and start the walk to my apartment, putting my headphones on so I can listen to music."

    "This town is where I've grown up, so it's common for me to see familiar faces when I'm out and around."
    "A lot of the time, people ending up leaving town after high school or college; usually other places in California, but sometimes other spots in the country."
    "Honestly, I'll probably end up doing that too at some point— not because I don't like Hawthorne, I love the place, but I've never wanted to be someone who always stays in their hometown."
    "Anyway, I usually end up seeing the family of people I know around town a lot more than I actually run into those people themselves."

    "Speaking of, I can actually see my old friend Ollie's family over there. I think this neighborhood is around where their house was? (Still is?)"
    "His parents are out walking Banana, and it looks like there's a couple others; his sister, I think, and maybe someone else."

    "After noticing them, I continue walking home, hands in my pockets with my thumbs through my belt loops."
    "..."
    "There's a moment where I see something moving a lot in my peripheral vision. I turn to look towards it."
    "Oh shit! It's Ollie's dad. He's waving his arms at me trying to catch my attention; I guess one of them noticed me. I think he's saying or shouting something, but I can't understand him."
    "I quickly take off my headphones, probably looking like a deer caught in the headlights."

    mc "Huh?"
    "Ollie's Dad" "Hey, [mcname]!"

    "Now that I noticed them, he starts to wave me over. They're on the opposite side of the street, so I check for cars before doing a light jog over."
    "{i}I haven't really talked with them much, and it's not like I've been in touch with Ollie lately. What's the deal?{/i}"
    "As I get closer, I can see the whole group. {i}There's Ollie's parents with Banana, his older sister, and...{w}Oh shit, that's Ollie!{/i}"
    "My jog breaks out into a short sprint as I run up beside them, looking at Ollie with surprise."

    mc "Oh my god hey, what's up?!"

    "I exhale a laugh, partly panting 'cause shit, I'm out of shape. I turn towards the whole group, who look all in good spirits."

    mc "Hey Theresa, Eric! Hi, Caroline!"

    "Ollie's Dad" "It's good to see you, [mcname]."

    "Smiling appreciatively towards them, I turn back towards Ollie."

    mc "I didn't know you were here! I guess that's why you're all together, huh?"

    "I gesture at the group. Caroline moved out back while Ollie was in high school, so I don't see them all together around town too much."

    o "Yeah, I thought I'd come back."

    mc "How long are you visiting?"

    "I smile; it's good to see him. Ollie packed up and split for the city a year or two ago. I haven't kept in touch with him as much since he moved away, so it's a total (pleasant!) surprise to run into him."

    o "I'm...moving back, actually."

    mc "Oh shit, really?"

    "That catches me off guard."

    "Ollie's Mom" "Yes, Oliver's come back home."

    "Ollie gives a quick laugh."

    o "At least for now, yeah, for a little while. While I figure out what's next again."
    o "My sister helped me drive all my stuff."

    "He gestures a thumb towards Caroline."

    "Caroline" "The big-time was too much for little bro."
    "Caroline" "I guess he found out that the lonely life isn't so pretty."

    o "Ah, shove it."

    "Ollie playfully gives his sister a shove with his shoulder."

    mc "Well, that's awesome. I just graduated but I'm staying in town, I guess also \"at least for now\". I guess I'll see you around??"

    o "Yeah, definitely!"

    mc "I'm working at that petting zoo by the beach. You should definitely come by! I'll text you the days I work."

    o "Oh, that place?? That's awesome. I bet it's fun."
    o "I probably would have come by anyways; I didn't have an opportunity to touch cute farm animals my whole time in LA."

    mc "Yeah, I actually just got off my first day, haha. But, I think it's going to be fun."

    "Ollie's Dad" "Haha, well then, it's good that we caught you."

    mc "Yeah, it's great to see you guys."

    o "It's really good to see you, [mcname]."

    "Ollie gives me a really heartfelt smile."

    o "I'll catch up with you this week?"

    mc "Yeah, that sounds great!"

    "I happily wave bye to Ollie as he and his family start to walk on. After checking again for cars, I jog back across the street and continue my way home."

    #########################################









    # This ends the game.

    return
