#------------------------------------------------------------------INFO

#Welcome to Bloody Escape! I had a lot of fun creating this game—there was plenty
#of sweating and bug-hunting along the way, but it’s finally finished. I hope you enjoy it. Have fun!

#------------------------------------------------------------------Imports

import random
import os
from datetime import datetime

#------------------------------------------------------------------Document
# Make sure the save file is created in the SAME folder as the program
SAVE_FILE = os.path.join(os.path.dirname(__file__), "Bloody_results.txt")


def document(name, score, level, user_answers_list, correct_answers_list, riddles_list):
    wrong = level - score
    
    if level <= 0:
        level = len(riddles_list)

    wrong = level - score
    percentage = round((score / level) * 100, 2) if level > 0 else 0.0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"===== BLOODY ESCAPE RESULT - {timestamp} =====\n"

    with open(SAVE_FILE, "a", encoding="utf-8") as file:
        file.write(header)
        file.write(f"Speler: {name}\n")
        file.write(f"Totaal aantal raadsels (gevraagd): {level}\n")
        file.write(f"Goed opgelost: {score}\n")
        file.write(f"Fout opgelost: {wrong}\n")
        file.write(f"Score percentage: {percentage}%\n\n")
        file.write("------------ DETAILS PER RAADSEL ------------\n")

        
        total = min(level, len(riddles_list))
        
        for i in range(total):
            r = riddles_list[i]
            ua = user_answers_list[i] if i < len(user_answers_list) else "<geen antwoord>"
            ca = correct_answers_list[i] if i < len(correct_answers_list) else "<geen correct antwoord>"
            file.write(f"\nRiddle {i+1}: {r}\n")
            file.write(f"-Jouw antwoord: {ua}\n")
            file.write(f"-Correct antwoord: {ca}\n")
            file.write("-Resultaat: " + ("Correct\n\n" if ua.lower() == ca.lower() else "Fout\n\n"))
            file.write("-" * 80)

        file.write("\n\n")


#------------------------------------------------------------------Menu
def menu():
    open(SAVE_FILE, "a").close()
    while True:
        print("=" *30)
        print("|| Welcome to""\033[91m Bloody Escape \033[0m" "||")
        print("=" *30)
        print("\nPress the numbers")
        print("1. Play")
        print("2. Credits")
        print("3. Socials")
        print("4. Quit\n")
        
        try:
            vraag = int(input("Make your choice:"))
        except ValueError:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-4 X")
            print("X" *34)
            continue
            
        if vraag == 1:
            name = input("What is your name?:").strip() or "Speler"
            while True:
                try:
                    level = int(input("How many riddles from 0 to 10?:"))
                    print("\n")
                    break
                    
                except ValueError:
                    print("\n")
                    print("X" *35)
                    print("X WRONG CHOICE: Only numbers 1-10 X")
                    print("X" *35)
                    
            if level > 10:
                print("X" *68)
                print("X You cannot choose more than 10 riddles. Level has been set to 10 X")
                print("X" *68)
                level = 10
                continue
                    
            if level <= -1:
                print("X" *47)
                print("X Minimum level is 1. Level has been set to 1 X")
                print("X" *47)
                level = 1
                continue
                
            
            if level == 0:
                print("☮" *20)
                print("\n-The game has ended-")
                print("You have no sins.\n")
                print("☮" *20)
                break
            
            play(name, level)
                
                    
                    
        elif vraag == 2:
            print("\n")
            print("-Credits-")
            print("=" *28)
            print("-Mikey Sorgeloos-")
            print("=" *28)
            
        elif vraag == 3:
            print("\n")
            print("-Socials-")
            print("=" *28)
            print("|FB: Mikey Sorgeloos       |")
            print("|Insta: De_MIKEE           |")
            print("|Snap: De_mikee            |")
            print("|LinkedIN: Mikey Sorgeloos |")
            print("=" *28)
        
        elif vraag == 4:
            print("\n")
            print("☮" *20)
            print("\n-The game has ended-\n")
            print("☮" *20)
            break
        
        else:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-4 X")
            print("X" *34)
        
#------------------------------------------------------------------PART 1: OUTSIDE
            
def play(name, level):
    print("-BEGIN LINE-")
    print("=" *133,"""\nHelp…
Help… HEEEELP AAAAUWHHWHHHHEEEERRRRRGGGG!

You jolt awake, lying on the cold ground. Your head throbs as you push yourself upright. All around you stretches a dark forest—endless,
silent. Too silent. No animals. No wind. Nothing. The air feels wrong, like the world is holding its breath.

Then—
A light.
Faint at first, growing stronger.

You step toward it, cautious but desperate for anything familiar. It’s a lantern. Old. Rusted. Flickering with a weak orange glow.
You pick it up, and as you do, you notice a note beneath it.

“I KNOW WHAT YOU ARE.”

Your heart stops. Panic claws at your throat, but you force yourself to breathe. Focus. You need to stay focused.

You start walking, lantern trembling in your hand. The forest swallows the path until finally… a shape emerges in the darkness.

A cabin. Abandoned, decayed, leaning to one side like it could collapse with a sigh. A heavy padlock keeps the door shut.
And on that door, smeared in dark, tacky red:

FIND THE CODE

“Is… is that blood?” you whisper.

Your stomach twists. Your pulse spikes.

Where are you?

With no other choice, you begin searching the surroundings…""")
    print("=" *133)
    
    
    while True:
        print("1. The old shed")
        print("2. The grave")
        print("3. The old mail")
        print("4. The padlock on the door")
        
        try:
            vraag = int(input("check:"))
            print("\n")
                
        except ValueError:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-4 X")
            print("X" *34)
            continue
        
        if vraag == 1:
            print("-BEGIN LINE-")
            print("=" *133,"""\nYou cautiously approach the old shed, every step crunching on dead leaves. Your hand shakes as you reach for the door—and,
surprisingly, it swings open easily.

Inside, shards of broken glass litter the floor, catching the lantern’s weak glow. The room is empty… except for the wall ahead.

Blood, smeared and dark, forms the numbers: 2009.

Next to it, a note flutters slightly as if moved by a ghostly breath. You pick it up and read: 45.

Confusion knots your stomach. What could it mean?

Shoving the cryptic note into your pocket, you turn back toward the abandoned cabin, heart hammering with more questions than answers.""")
            print("=" *133)
            
        
        elif vraag == 2:
            print("-BEGIN LINE-")
            print("=" *133,"""\nAs you approach the grave, something catches your eye—a shovel, carelessly laid across the mound.
A sticky note clings to its handle, scrawled in hurried letters:

DIG ME UP

Your hands tremble as you lift the shovel. Each strike into the earth feels heavier than the last,
and what seems like hours pass in a blur of dirt and sweat. Finally, the edge of wood breaks through the soil.

An old coffin. Its lid splinters under your blows. The moment it cracks open, a putrid stench hits you,
so foul it makes your stomach churn. You shine your lantern inside.

A corpse lies within, twisted and decayed beyond recognition. You can’t tell if it was a boy or a girl.
You fight the urge to gag.

Something catches your eye—a small yellow paper wedged between the corpse’s teeth. With shaking hands, you pry its mouth open.
The brittle sound of cracking bones echoes in the silent night.

The note reads: 66. Around the edges of the paper, written in jagged letters: REDRUM.

Your chest tightens. The forest seems darker now. The cold wind brushes past you, whispering something you can’t quite hear.

Shoving the horrifying discovery into your mind, you turn back toward the abandoned cabin,
the lantern flickering like a fragile heartbeat.""")
            print("=" *133)
            
        elif vraag == 3:
            print("-BEGIN LINE-")
            print("=" *133,"""\nYou crouch down and begin rifling through the old mail scattered across the floor—bills yellowed with age,
letters with curled edges. Some are somber, beginning with “In loving memory…”; others are harsh,
warning of overdue payments and last notices.

Amid the piles, a torn piece of newspaper catches your eye. Half-burned, its edges blackened,
it tells of a murder—but the names, dates, and details are obscured, lost to time and fire.

Pinned beneath the newspaper is a number, written hastily: 66. Under it, a single word: LIES.

A chill runs down your spine. You straighten up, heart pounding, the cabin feeling colder, darker, heavier than before.""")
            print("=" *133)
            
                
        
        elif vraag == 4:
                unlocked = padlock(name, level)
                if unlocked:
                    return
            
        else:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-4 X")
            print("X" *34)
        
#----------------------------------------Padlock       
        
def padlock(name, level):
    while True:
        print("∞" *30)
        print("You look at the padlock")
        print("∞" *30)
        print("1. Enter the code")
        print("2. Back")
        print("∞" *30)
        
        
        keuze = input("Choose:").strip()
        print("\n")
            

            
        if keuze == "1":
            code_input = input("Enter code:").strip()       
            if not code_input.isdigit():
                print("\n")
                print("X" *27)
                print("X WRONG CHOICE: 6 numeric X")
                print("X" *27)
                continue
                    
            if code_input == "456666":
                    print("\n")
                    print("ꗃ" *10)
                    print("ꗃ UNLOCKED ꗃ")
                    print("ꗃ" *10)
                    print("\n")
                    print("=" *133,"""\nYou walk inside and catch a strange smell,
but you ignore it and keep moving. The place feels old, partly burned and forgotten.
You take a moment to look around.""")
                    print("=" *133)
                    inside(name, level)
                    return True
                    
            else:
                print("\n")
                print("X" *21)
                print("X wrong combination X")
                print("X" *31)
                        
                    
        elif keuze == "2":
            print("\n")
            print("⬅" *15)
            print("⬅You step back from the padlock⬅")
            print("⬅" *15)
            return False
        
        else:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-2 X")
            print("X" *34)

                                
#------------------------------------------------------------------PART 2: INSIDE

def inside(name, level):
    while True:
        try:
            print("1. The bathroom")
            print("2. The Living room")
            print("3. The toilet")
            print("4. The Kitchen")
            print("5. The basement")
            
            vraag = int(input("Enter:"))
            print("\n")
            
        except ValueError:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-5 X")
            print("X" *34)
            continue
            
        if vraag == 1:
            print("-BEGIN LINE-")
            print("=" *133, """\nAs you step into the bathroom, the stench intensifies—thick, sour, suffocating.
Your eyes drift to the bathtub. A rotting corpse lies slumped inside.

A shiver races down your spine.
Its fingers are nearly gone, decayed to gnawed stubs. A dark hole gapes in its skull,
the unmistakable mark of a bullet tearing straight through.

You stumble back, unable to look any longer, and hurry out of the bathroom, your heart pounding in your throat.""")
            print("=" *133)
            
        
        elif vraag == 2:
            print("-BEGIN LINE-")
            print("=" *133, """\nThe living room—if it can even be called that anymore—looks like it might once have been warm and cozy.
Now it’s nothing but a broken shell. Furniture collapsed in on itself, curtains moth-eaten, and old bloodstains dried into the wood like bruises on the house itself.

Your eyes drift to a faded calendar hanging crooked on the wall.
25 September 2009.
The date where time… simply stopped.

But why?

A cold unease creeps up your neck.
You decide it’s best to leave and head back.""")
            print("=" *133)
            
        elif vraag == 3:
            print("-BEGIN LINE-")
            print("=" *133,"""\nYou open the toilet door and stop—candlelight flickers everywhere.
Photos cover the walls, most with their faces violently scratched out.

Then you spot one that isn’t.
A photo of you.

Your stomach drops.
“What… how is this here?”

You turn it over.
On the back, a name is written""")
            print("=" *133)
            print(f"""
|----------------------|
|                      |
| {name}                |
|                      |
|                      |
|                      |
|    BETRAYAL          |
|                      |
|----------------------|

""")
            print("=" *133, """\nMy stomach plummets. It knows my name.
It has my picture. I have to get out—now.""")
            print("=" *133)
            
        
        
        elif vraag == 4:
            print("-BEGIN LINE-")
            print("=" *133, """\nAs you move to step into the kitchen, you feel resistance—the door won’t budge.
You shove it, and a cascade of charred wood crashes to the floor.
Wow. That nearly took my head off. And beyond it… nothing remains.
Burned out. Caved in.
Everything is gone.....""")
            print("=" *133)
            
        
        elif vraag == 5:
           print("-BEGIN LINE-")
           print("=" * 133, """\nYou move down the stairs, every creak threatening to collapse under your feet.
The air grows dense, almost suffocating. You open the basement door into absolute darkness. A table. A chair. A TV waiting in the corner.
You barely sit down before the TV suddenly flicks on by itself.""")
           print("""
               o
          o    |
           \   |
            \  |
             \.|-.
             (\|  )
    .==================.
    | .--------------. |
    | |--.__.--.__.--| |
    | |--.__.--.__.--| |
    | |--.👁_.--👁.-- | |
    | |--.__.--.__.--| |
    | |--.__.--.__.--| |
    | '--------------'o|
    | LI LI """""""   o|
    '=================='

""")

           print("=" *133)
           print(f"""Hello {name}, i wanna play a game You may not remember me, but I remember you. In 2009, during that robbery, you ran.
You left innocent people—my wife—behind. She was only 45."

The room floods with light.
As you narrow your eyes at the mirror, your best friend comes into focus—along with the shadow of someone standing just behind him.

“I’m giving you a second chance. This time you don’t get to run. Put your hands in the iron lock.”

Panic surges through you. You obey.

“Good. Now we begin. Each question you get wrong costs you a finger. {level} Lives were lost that day—that’s how many chances you get.”

“Let the game begin.""")
           print("=" *133)
           the_game(name, level)
           return
            
            
        else:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-5 X")
            print("X" *34)
            continue
            
    
#------------------------------------------------------------------PART 3: THE GAME
def the_game(name, level):
    riddles = [
        ("What gets smaller every time it takes a bath?", "soap"),
        ("What is more useful when it is broken?", "egg"),
        ("What date could be seen on the calender?", "25 september 2009"),
        ("What was written on the back of the picture and no not your name something else?", "betrayal"),
        ("I am strong enough to smash ships, but I fear the Sun. What am I?", "ice"),
        ("I watch you sleep, I haunt you by day. You stare at me and saw nothing, but darkness. What am I?", "fear"),
        ("What is a cereal's worst fear?", "cereal killer"),
        ("What do you call a person who is afraid of Santa Claus?", "claustrophobic"),
        ("""What does man love more than life, fear more than death or mortal strife, What the poor have,
the rich require, and what contented men desire, What the miser spends and the spendthrift saves
And all men carry to their graves?""", "nothing"),
        ("""It can't be seen, can't be felt, can't be heard, and can't be smelt. It lies behind stars and under hills,
And empty holes it fills. It comes first and follows after, Ends life, and kills laughter. What is it?""", "the dark"),
        ("""There is a clerk at the butcher shop, he is five feet ten inches tall,
and he wears size 13 sneakers. He has a wife and 2 kids. What does he weigh?""", "meat"),
        ("""Something that requires our mental skill to decode it, our imagination to understand it,
our knowledge is tested to its max, it confuses us at every stage, it seems easy yet difficult,
only those who are used to, will get through. What is it?""", "a riddle"),
        ("What kills you inside the more you keep it and sets you free the moment you release it?", "guilt"),
        ("Why did the man shoot the clock?", "killing time"),
        ("Why was the clock arrested?", "killing time"),
        ("A color is seen on a stoplight, an item you use to eliminate the darkness. What comic book character is it?", "green lantern"),
        ("If seven cats kill seven rats in 7 minutes, how many would be needed to kill one hundred rats in 50 minutes?", "14"),
        ("Who was the most famous Skeleton detective?", "sherlock bones"),
        ("What is a ghost's favorite dessert?", "ice scream"),
        ]
    
    lives = level
    score = 0
    
    #Beveiliging niet boven 10
    level = min(level, len(riddles)) 
    
    #voor later in bestand te schrijve 
    user_answers_list = []
    correct_answers_list = []
    riddles_list = []
    
    vragenlijst = random.sample(riddles, level)
    
    for i, (riddle, answer) in enumerate(vragenlijst, start=1):
        print("\n")
        print("-" * 13)
        print(f"Riddle {i} / {level}")
        print("☠" * 68)
        print("\n")
        print(riddle)
        print("\n")
        print("☠" * 68)
                
        user_answer = input("Give answer:").strip()
        
        # opslaan
        user_answers_list.append(user_answer)
        correct_answers_list.append(answer)
        riddles_list.append(riddle)
        
        if user_answer.lower() == answer.lower():
            print("Correct.\n")
            print("^" * 95)
            score += 1
            
        else:
            print(f"WRONG! The answer was: {answer}\n")
            print("(A finger has been cut, a sharp burst of pain tears through you, and you scream, “LET ME OUT!”)\n")
            print("^" * 95)
            lives -= 1
            
            if lives <= 0:
                print("\n")
                print("=" *103)
                print("NOT EVEN ONE, WHAT A SHAME")
                print("""you will have to live with the consequences""")
                document(name, score, level, user_answers_list, correct_answers_list, riddles_list)
                ending(name, level, score)
                return
            
    
    print("\n")
    document(name, score, level, user_answers_list, correct_answers_list, riddles_list)
    ending(name, level, score)
    return
    
                
                
#------------------------------------------------------------------Einding
def ending(name, level, score):
    if level <= 0:
        level = 1
    minimum_required = level // 2
    passed = score >= minimum_required

    
    if passed:
        result = ("""You passed. You managed to save your friend—but this isn’t over.
There are others being held captive here.
And they’re waiting for you.
Enter the next room. And be smart about it. think about the others before you do anything stupid.""")
        
        
    else:
        result = ("""You did not pass the challenge. what a shame...... Time seems to crawl, every second stretching thin.
Before you can speak, a deafening bang echoes through the house.

A voice roars from the darkness:
I’m sorry about your friend… but he isn’t the only one here.

Enter the next room. And be smart about it. think about the others before you do anything stupid.""")
        
    print("=" * 103)
    print(result)
    print("=" * 103)
    print(f"Your score: {score}/{level}")
    print(f"Required to pass: {minimum_required} ({level//2}+ correct answers)")
    print("=" * 41)

    while True:
        print("1. Try to run")
        print("2. Enter the next room")
        try:
            vraag = int(input("Make a choice:"))
        
        except ValueError:
            print("\n")
            print("X" *34)
            print("X WRONG CHOICE: Only numbers 1-2 X")
            print("X" *34)
            continue
            
        if vraag == 1:
            print("\n")
            print("-BEGIN LINE-")
            print("=" * 133, """\nYou hold your breath, waiting for the right moment. The room is tight with tension.
You spin toward the door, reaching for the handle—

A sudden crack explodes through the air. Glass rains down around you. A sharp impact steals your breath, and the world tilts as your knees hit the floor.

“Wrong choice.”

Another echoing shot splits the silence.

“I expected more from you.\n”""")
            print("\n2 Weeks later......\n")
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⠿⣿⡇⠀⠀
⠀⠀⢸⣿⣈⣉⠙⠛⠻⠿⣿⣶⣤⡀⠀⠀⢀⣤⣶⠿⠛⠋⠉⠀⠀⠀⢸⡇⠀⠀
⠀⠀⢸⣿⠛⠻⣿⢷⣶⣦⣤⣈⡉⣿⡇⢸⡟⠉⠀⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠀
⠀⠀⢸⣿⠿⠶⣿⣤⣴⣿⣏⣉⣙⣿⡇⢸⡇⠀⠀⣀⣀⣤⣴⣶⠿⠿⣿⡇⠀⠀
⠀⠀⢸⣷⣶⣤⣤⣤⣄⣈⣉⠙⠛⣿⡇⢸⣷⠾⠟⠛⢉⣿⣧⣤⣴⣶⣿⡇⠀⠀
⠀⠀⢸⣯⣤⣄⣸⣿⣏⠙⠛⠛⠛⣿⡇⢸⣿⣴⣶⡿⠿⠛⠛⣿⣇⣤⣽⡇⠀⠀
⠀⠀⢸⡏⠉⠛⠛⠛⢿⡿⠿⢿⣶⣿⡇⢸⣿⣉⣤⣤⡶⠾⠛⠛⢉⣉⣽⡇⠀⠀
⠀⠀⢸⡇⠀⠀⠀⠀⢸⡷⠶⢤⣤⣿⡇⢸⣿⣉⣥⣿⣶⣶⠞⠛⠋⠉⢹⡇⠀⠀
⠀⠀⢸⡇⠀⠀⠀⠀⢸⣷⣦⣤⣤⣿⡇⢸⣿⠋⣉⣉⣨⣿⠀⣿⣿⡇⢸⡇⠀⠀
⠀⠀⢸⣇⣀⣀⣀⡀⢸⣧⣄⣉⣉⣿⡇⢸⣿⠛⠋⣉⣹⣿⣀⣉⣉⣠⣼⡇⠀⠀
⠀⠀⠈⠉⠉⠉⠉⠛⠛⠛⠿⠿⢿⣿⡇⢸⣿⡿⠿⠿⠛⠛⠛⠉⠉⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
BODY FOUND IN ADVANCED DECOMPOSITION
Authorities report that the victim has not yet been identified due to the severe level of decomposition.
Investigators confirmed that the teeth and fingernails had been deliberately removed.

Officials are now questioning whether this is the killer’s first victim—or one of many.
Police warn the public that a potential serial offender may be involved.

Anyone with information is urged to contact authorities as they work to uncover the identity of the Jane Doe.""")
            print("=" * 133)
            print("1. Back to menu")
            
            while True:
                press_input = input("Press the number: ").strip()
                try:
                    press = int(press_input)
                except ValueError:
                    print("\n" + "X" * 31)
                    print("X WRONG CHOICE: Only number 1 X")
                    print("X" * 31)
                    continue

                if press == 1:
                    return
                
                else:
                    print("X" * 31)
                    print("X WRONG CHOICE: Only number 1 X")
                    print("X" * 31)
        
        elif vraag == 2:
            print("\n")
            print("-BEGIN LINE-")
            print("=" * 80, """
 _____       _                            _   _                      _       
|_   _|__   | |__   ___    ___ ___  _ __ | |_(_)_ __  _   _  ___  __| |      
  | |/ _ \  | '_ \ / _ \  / __/ _ \| '_ \| __| | '_ \| | | |/ _ \/ _` |      
  | | (_) | | |_) |  __/ | (_| (_) | | | | |_| | | | | |_| |  __/ (_| |_ _ _ 
  |_|\___/  |_.__/ \___|  \___\___/|_| |_|\__|_|_| |_|\__,_|\___|\__,_(_|_|_)""")
            print("\n")
            print("=" * 80)
            print(f"Congratulations {name} you’ve completed the first part of the game!")
            print("=" * 80)
            print("1. Back to menu")
            
            while True:
                press_input = input("Press the number: ").strip()
                try:
                    press = int(press_input)
                except ValueError:
                    print("\n" + "X" * 31)
                    print("X WRONG CHOICE: Only number 1 X")
                    print("X" * 31)
                    continue

                if press == 1:
                    return
                else:
                    print("X" * 31)
                    print("X WRONG CHOICE: Only number 1 X")
                    print("X" * 31)
        
        else:
            print("X" *33)
            print("X WRONG CHOICE: Only numbers 1-2 X")
            print("X" *33)
    
    
    
#------------------------------------------------------------------Opstart
if __name__ == "__main__":
    menu()