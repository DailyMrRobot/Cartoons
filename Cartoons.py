import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)




load_dotenv()
TOKEN = os.getenv('OTQ2Mjk4NTA2NzMyMjQ5MTI5.YhcrKQ.50zvacHb5Fngtxd1YP6vplZclIk')

bot = commands.Bot(command_prefix='!')

@bot.command(name='Ed')
async def eddy(ctx):
    ed_edd_eddy_quotes = [
    "Hey Eddy! He-ha! What's up?",
    "Dogpile!",
    "Hi! Hiya, Double D. He-ha! You guys make me laugh.",
    "We'll buy a truck-load of jawbreakers!",
    "What do you mean?",
    "Hey, Eddo. What's a ghost's favorite lunch meat?",
    "Don't worry, Ed. We'll see it on TV in a year.",
    "Yeah with all the good stuff cut out.",
    "Do not sweat it, guys.",
    "I think I swallowed a turtle.",
    "What country are we in?",
    "Here is a list of some quotes from your favorite cartoon network show, that is big on humor.",
    "Ricky dinky stinky winky!",
    "Can we visit the planet of bacon men and have the marrow sucked from our bones",
    "I dispense with you, disgusting detergent of the deep!",
    "In the void of space, Zorba the Two-Headed Mutant...",
    "Silly little Jilly frolicked through the daisies...",
    "Spewing slime from its tentacles!",
    "Im so silly, said Jilly... ",
    "As Zorba sucked his brain!",
    "I wish I were a potato, so that a prince would like me!",
    "He gagged on its bones!",
    "The stench of immortal doom still thickens the air, yes? Or perhaps it is Wilfreds cabbage evacuations? Hard to tell.",
    "If we do not find dry land soon, I will have to feast upon your succulent… noggin…",
    "I cannot hear you, I am invisible! Goodbye, I have gone to the market!",
    "Those Ed-Boys are crazy like chickens. Except they lay no eggs! Ah, candied beets to calm my nerves.",
    "That dirty toucher took my dolly Poo-Poo!",
    "Wow, Eddy, cool car!",
    "Hey dork! Whose car is it, you twerp?!",
    "What have you done, Plank is a mindless zombie!",
    "My nose, its flat! And somebody wrote on it!",
    "See, Plank? I told you bunnies would take over the world, and the have! Luckily we prepared for this day, huh, pal?",
    "Edd: Well, that was close.",
    "Hi Ed, Edd and Eddy. You boys look cool. Mind if I join you?",
 
 ]
    response = random.choice(ed_edd_eddy_quotes)
    await ctx.send(response)

@bot.command(name='Spongebob')
async def bob(ctx):
    spongebob_quotes = [
     "Hey Patrick, I thought of something funnier than 24… 25!” : Spongebob",
     "I knew I should not have gotten out of bed today. : Squidward",
     "I am hotter than a hickory smoked sausage!” : Sandy",
     "Goodbye everyone, I’ll remember you all in therapy. – Plankton",
     "Wake me up when I care. – Squidward",
     "A 5 letter word for happiness – MONEY. : Mr. Krabs",
     "It’s just a cruel reminder that I’m single and likely to remain that way forever. : Squidward",
     "If I was a mom…this would be kind of shocking. Just call me daddy! :  Patrick",
     "If I don’t make any money today I’ll surely break out in a rash!” : Mr. Krabs",
     "I might as well sleep for 100 years or so. : Squidward",
     "I’m ugly and I’m proud! : Spongebob",
     "My name’s not RIIIIIIIIIIIICK!” : Patrick", 
     "Future, future, future. : Squidward",
     "Holographic Meatloaf... My favorite! : Plankton",
     "Is mayonnaise an instrument... : Patrick",
     "Ah, a few blobs of ink doesn’t prove a thing. I’m as evil as ever, I’ll prove it right now by stealing the Krabby Patty secret formula. – Plankton", 
     "You’re about as ugly as homemade soup! :Sandy",
     "It all started when I was born.  : Squidward",
     "Stupidity isn’t a virus, but it sure is spreading like one. – Sandy",
     "Congratulations, sir! You have just given me my one-millionth dollar! – Mr. Krabs",
     "I don’t get it. No matter what I do, I always end up being squashed by someone bigger than me. – Plankton",
     "If I were to die right now in a fiery explosion due to the carelessness of a friend, hen it would just be alright. – Spongebob",
     "Give to the Children’s fund? What have the children ever done for me? – Mr. Krabs",
     "I’ll have you know that I stubbed by toe last week and only cried for 20 minutes. – Spongebob",
     "Three cheers for the world’s greatest fry cook…SpongeBob! – Mr. Krabs",
     "You’re nothing but pure evil…just like newspaper comics. – Sandy",
     "No, I’m not on my way to the grand opening ceremony. I’m busy planning to rule the world! – Plankton",
     "I was trying to tell you that I was choking on snow but the snow melted and turned into water and I drank all the water now I’m better. – Patrick",
     "Yeah, well I’d hate you even if I didn’t hate you.” – Patrick",
     "Home is where you’re surrounded by other critters that care about you. – Sandy",
     "Don’t you DARE take the name of Texas in vain. – Sandy",
     "What’s so great about a nerdy pickle... – Patrick",
     "You need six hundred to pass, you got six. – Mrs. Puff",
     "Just when I thought they couldn’t get any stupider. – Squidward",
     "Wait, Spongebob, we’re not cavemen. We have technology. – Patrick",
     "Did you smell it... That smell. A kind of smelly smell. The smelly smell that smells…smelly. – Mr. Krabs",
     "If you believe in yourself, with a tiny pinch of magic all your dreams can come true! – Spongebob",
     "The inner machinations of my mind are an enigma. – Patrick",
     "No, not because I cheated! Because I’m an evil genius. And you’re just a kid. – Plankton", 
     "Well, it may be stupid, but it’s also dumb. – Patrick",
     "Always follow your heart unless your heart is bad with directions. – Spongebob",
     "If there’s one thing we Atlanteans enjoy, it’s a healthy dose of dark humor!” – Lord Royal Highness",
     "Next time I’ll bring more granola! – Sandy",
     "Holographic Meatloaf... My favorite!” – Plankton",
     "Don’t you have to be stupid somewhere else... - Sandy",  
     "Not until 4. - Patrick",
     "Listen, instead of killing yourselves, I’ve got something really important for you to do for me. Now, are you men ready for you super… special…. secret…. assignment?” – Mr. Krabs",
     "Well, it’s no secret that the best thing about a secret is secretly telling someone your secret, thereby adding another secret to their secret collection of secrets, secretly.” – SpongeBob",
     "I thought I was going to steal something. Can’t imagine why. So, I’m just enjoying this lovely day!” – Plankton.",
     "That’s it, mister! You just lost your brain privileges.” – Plankton.",
     "Can you give SpongeBob his brain back, I had to borrow it for the week.” – Patrick",
     "Well, it wouldn’t be the first time you ruined everything.” – Squidward",
     "I order the food, you cook the food. The customer gets the food. We do that for 40 years, and then we die. – Squidward",
     "I can’t see my forehead! –  Patrick",
     "I know of a place where you never get harmed. A magical place with magical charm. Indoors, indoors, indoors!” – Spongebob",
     "I have a square head and a real ghost has a round one. All we have to do is make my head round and boo, I’m scary!” – Spongebob",
     "A five-letter word for happiness…money.” – Mr. Krabs",
     "We should take Bikini Bottom and push it somewhere else!” – Patrick ",
     "Once upon a time there was an ugly barnacle. He was so ugly that everyone died. The end!” – Patrick",
     "Being grown up is boring. Besides, I don’t ‘get’ jazz.” – Patrick",
     "Well, the way I see it, there are three possibilities: One, you stole it; two, you stole it; or three, you stole it!” – Mr. Krabs",
     "I’m so loyal, I don’t mind sleeping out in the cold, hard ground while Captain Krabs sleeps in his warm, dry tent.” – Spongebob",
     "Ha, ha! It’s a giraffe!” –  Patrick" ,
     "You don’t need a license to drive a sandwich. – Spongebob",
     "See, no one says ‘cool’ anymore. That’s such an old person thing. Now we say ‘coral’, as in ‘That nose job is so coral.’” – Pearl Krabs.",
     "Well, if I was a robot, which I’m not, at least I’m well put together.” – Mr. Krabs",
     "SpongeBob is the only guy I know who can have fun with a jellyfish…for 12 hours!” – Squidward.",
     "I guess hibernation is the opposite of beauty sleep!” – Patrick" ,
     "Dumb people are always blissfully unaware of how dumb they really are…” – Patrick",
     "Always follow your heart – unless your heart is bad with directions.” –  Spongebob",
     "I’ve waited years for this moment. I’m gonna go in there, march straight up to the manager, look at him straight in the eye, lay it on the line, and – I can’t do it!” – Patrick" ,
     "Pull your pants up, Patrick. We’re going home. – Spongebob",
     "What’s this ‘we’ stuff... You fed him the tainted patty. Looks like it’s the stony lonesome for you!” – Mr. Krabs.",
     "That Plankton is a clever beast. You’ve got to keep a sharp eye out for him, SpongeBob.” – Mr. Krabs.",
     "Spongebob: “I used to have a dream.” / Mr. Krabs.: “Yeah? I used to have a kidney stone. Everything passes eventually." ,
     "Run Mr. Krabs! Run like you’re not in a coma!” – Spongebob",
     "So much later that the old narrator got tired of waiting and they had to hire a new one. – Narrator",
     "I’m a good noodle!” – SpongeBob",
     "Oh, yes you do, no world means no money, so, either save the world, or you’re fired!” – Mr. Krabs",
     "Remember, licking doorknobs is illegal on other planets.” – Spongebob",
     "Squidward, your ceiling is talking to me.” – Patrick", 
     "We don’t need television…not as long as we have our imagination.” – Spongebob",
     "Gary, I’m absorbing his blows like I’m made of some sort of spongy material.” – Spongebob.",
     "Squidward… I used your clarinet to unclog my toilet!” – Spongebob.",
     "The Krusty Krab pizza is the pizza for you and me.” – Spongebob",
     "You never really know the true value of a moment, until it becomes a memory.” – SpongeBob",
     "Good people don’t rip other people’s arms off.” – Spongebob",
     "We shall never deny a guest even the most ridiculous request.” – Mr. Krabs",
     "All I know is fine dining and breathing.” – SpongeBob",
     "Me, aggressive! How dare you! Maybe you’re right… I command you to help me be a nicer person!” – Plankton",
     "Hello. You’ve reached the house of unrecognized talent.” – Squidward",
     "Squidward that’s not the peace treaty, that’s a copy of the peace treaty.” – Spongebob",
     "Remember, licking doorknobs is illegal on other planets.” – SpongeBob",
     "Gary, I’m absorbing his blows like I’m made of some sort of spongy material. – Spongebob",
     "I knew a guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy’s cousin… – SpongeBob",
     "Excuse me, sir, but you’re sitting on my body, which is also my face. – Spongebob",
     "It took three days to make that potato salad, three days!!! – SpongeBob",
     "Oh well, I guess I’m not wearing any pants today! – SpongeBob",
     "SpongeBob is the only guy I know who can have fun with a jellyfish…for 12 hours!” – Squidward",
     "Caller: “Is this the Krusty Krab?” / Patrick: No, this is Patrick.",
     "The best time to wear a striped sweater is all the time!” – SpongeBob",
     "Another day, another migraine” – Squidward",
     "It’s just a cruel reminder that I’m single and likely to remain that way forever. – Squidward",
     "There it is. The finest eating establishment ever established for eating. The Krusty Krab, home of the Krabby Patty, with the Help Wanted sign on the front. – Patrick" ,
     "But it’s my only night to be fancy! – Squidward",
     "Look at all the hip young people eating sal-ads.” – SpongeBob",
     "SpongeBob, before we’re torn to shreds, I’d like to thank you for helping me look for Spot. – Plankton.",
     "What... It’s just obvious that I’m a complete failure and a waste of a lower life form! Oh, woe is me! = Plankton.",
     "Hello, we’re with the pet hospital down the street, and I understand you have a dying animal on the premises. – SpongeBob",
     "Squidward: “You mean you’ve never heard the story of the… hash-slinging slasher",
     " Spongebob: “The slash-bringing hasher?” / Squidward: “The hash-slinging slasher.” Spongebob: “The sash wringing, the trash thinging, mash flinging… the flash springing, bringing the the crash thinging the…” / Squidward: “Yes. The hash-slinging slasher.",
     "This is not your average, everyday darkness. This is… ADVANCED darkness.” – Spongebob",
     "Home is where you’re surrounded by other critters that care about you.” – Sandy",
     "Police: “If you can’t do the time, don’t do the crime. [locks SpongeBob and Patrick in jail cell and opens it again after a second] Okay, time’s up. Now get out!”  SpongeBob: “But…we stole a balloon!”  Police: “Yeah, on free balloon day!”",
     "Can I be excused for the rest of my life?” – Spongebob",
     "You’re part of my crew now, and our job is to sail around and frighten people. It’ll be grueling, mind-numbing, and repetitive. Just like… daytime television.”  – Flying Dutchman",
     "Too bad Spongebob is not here to enjoy Spongebob not being here.” – Squidward",
     "I don’t get it. I made my house a mess, which was making it clean, which made Squidward clean my yard, but that really means he’s messing it up. But the opposite of clean is filth, which means filth is clean, that means Squidward is really making my yard a wreck, but I normally wreck my own yard which means, Squidward is being the opposite of Squidward which means he’s Spongebob!” – Spongebob",
     "F is for a fire that burns down the whole town, U is for Uranium…bombs! N is for no survivors!” – Plankton",
     "I don’t get it. If a free salad bar won’t bring in new customers… what will? –  Krabs",
     "You can’t fool me. I listen to public radio!” – Squidward",
     "Well, I don’t know nothin’ about Alaska, but looky here. Back in Texas I wrangled bulls and I wrangled worms. As far as I’m concerned, doing both together just saves rope.” – Sandy" ,
     "Ravioli ravioli. Give me the formuoli. – Spongebob",
     "Tell you what. You give me back the sock and I’ll give you… three wishes.” – Flying Dutchman",
     "Booooo! Prepare to be burdened with the haunting memory of my ghostly ghost pirates!” – Flying Dutchman",
     "Spongebob: “Now that we’re men, we have facial hair.”  Patrick: “Now that we’re men I changed my underwear.”",
     "Mr. Krabs: “That hat makes you look like a girl.”  SpongeBob: “Am I a pretty girl!”",
     "Squidward : “OK now, how many of you have played musical instruments before?”  Plankton : “Do instruments of torture count...”  Squidward : “No.” Patrick : “Is mayonnaise an instrument?” Squidward : “No, Patrick, mayonnaise is not an instrument. Horseradish is not an instrument either.”",
     "Spongebob: Hi, Kevin. I’m your biggest fan.” Kevin the Sea Cucumber: “You’re too kind. Security!”",
     "Patrick: Who are you calling Pinhead... I wanna be Dirty Dan.   Spongebob : “What makes you think you can be Dirty Dan...”  Patrick : “I’m dirty.”",
     "How did I ever get surrounded by such loser neighbors?” – Squidward" ,
     "I was five years old and my father gave me a dollar. I loved that dollar. Loved it like a brother. Me and that dollar went everywhere together.” – Mr. Krabs",
     "And tonight, after my big promotion, we’re gonna party till we’re purple.” – SpongeBob",
     "Boy, that critter put up some sort of fight, but as you can see, I’m from Texas, and no worm is a match for me. I even found my tail!” – Sandy" ,
     "Spongebob: “Patrick, I don’t think ‘wumbo’ is a real word.” / Patrick: “Oh come on SpongeBob! You know, I wumbo, You wumbo, He she me wumbo, wumbo, Wumboing, We’ll have thee wumbo, Wumborama, Wumbology, The study of wumbo? It’s first grade SpongeBob!",
     "Spongebob: Squidward, you can’t eat all those Krabby Patties at once! Squidward!” Squidward: “Oh, what’s going to happen? Am I gonna blow up?” Spongebob: “No, worse. They’ll go right to your thighs.” Squidward: “My thighs?” Spongebob: “And then you’ll blow up.”  Paramedic: “Yeah, I remember my first Krabby Patty.” Spongebob: “Would you like to hear one of my secrets?” Patrick: “Do I?” Spongebob: “Let’s see… uh, did you know that you’re my best friend?” Patrick: “No… way! Tell me another secret.” Spongebob: “Well, secretly, I’m a little bit naive.”  Patrick: “Wow! I’ll never look at you the same way again.” ",
     "That’s it mister! You just lost your brain privileges!” – Plankton",
     "Well, the way I see it, there are three possibilities: One, you stole it; two, you stole it; or three, you stole it! – Mr. Krabs",
     "We should take Bikini Bottom and push it somewhere else! – Patrick",
     "So much later that the old narrator got tired of waiting and they had to hire a new one. – The New Narrator",
    ]

    response = random.choice(spongebob_quotes)
    await ctx.send(response)

@bot.command(name="Garfield")
async def gar(ctx):
    garfield_quotes = ["Love me, feed me, never leave me.-Garfield",
    "When the lasagna content in my blood gets low, I get mean. -Garfield",
    "I'm not overweight. I'm undertall. -Garfield",
    "Eat your heart out, [person].-Garfield",
    "I hate Mondays. -Garfield",
    "I’m not messy. I’m organizationally challenged! -Garfield",
    "Big fat hairy deal. -Garfield" ,
    "Who ever should be dragged out into the street and shot. -Garfield",
    "Diet is ‘die’ with a ‘t.’ -Garfield", 
    "I never met a lasagna I didn’t like. -Garfield",
    "Eat every meal as though it were your last. -Garfield",
    "It's not that I dislike you, I just don't like you near me. -Garfield",
    "Momma? Umm...I don't know, Penelope... -Garfield",
    "It's not that I dislike you, I just don't like you near me. -Garfield",
    "You know it’s Monday when you wake up, and it’s Tuesday. -Garfield"
    ]
    response = random.choice(garfield_quotes)
    await ctx.send(response)
@bot.command(name="AdventureTime")
async def at(ctx):
    adventure_time_quotes = [
        "I don’t need to feel like I’m waiting to be noticed. I know who I am, and I’ll know what I want if and when it ever comes along. - Fionna",
        "I say creepy is just another label we used to distance ourselves from stuff we don’t understand. Or that it reminds us of something in ourselves that we’re not comfortable with. It just ain’t a real thing, ya know? Unless you choose to believe it. - Finn the Human",
        "What am I talking about?! [Sighs and assumes] PB, I was.... geh...eh.. [Blushes] I was in love with you! Okay?! And you didn't love me back! Now I'm ready to move on, and it's like...rrmph!! You're gonna build me up all over again! Well, I'm done! I'm done - Finn the Human",
        "Something Weird might just be something familiar viewed from a different angle, and that’s not scary, right? - Marceline's Mom",
        "What you're feeling is called infatuation. The pain is the product of you overvaluing a projected, imaginary relationship with me. - Princess Bubblegum",
        "People get built different. We don't need to figure it out, we just need to respect it. - Princess Bubblegum",
        "Dating girls is like riding a bicycle. If you mess up, you could get really hurt forever or hurt someone you really care about. - Finn",
        "People make mistakes. It's all part of growing up, and you never really stop growing. - Duke of Nuts",
        "Dude, sucking at something is the first step towards being sorta good at something. - Jake the Dog",
        "You know I care about you. I think you're making the right choice. Your natural lifespan is going to be richer and fuller than you can imagine. And someday, when you die, I'll be the one that puts you on the ground. - Marceline the Vampire Queen",
        "When bad things happen, I know you want to believe they are a joke, But sometimes life is scary and dark. That is why we must find the light - BMO",
        "Who are you? Ha ha ha! I know, you're probably like a... a biiiiiiig neeeerd! Hey baby, why don't you try being cool like me? - Ice King",
    ]

    response = random.choice(adventure_time_quotes)
    await ctx.send(response)
bot.run('')
