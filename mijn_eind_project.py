#------------------------------------------------------------------Intro


print("=" *30)
print("|| Welcome to""\033[91m Bloody Escape \033[0m" "||")
print("=" *30)

#------------------------------------------------------------------Menu

def menu():
    while True:
        print("\nPress the number")
        print("1. Play")
        print("2. Credits")
        print("3. Socials")
        print("4. Quit\n")
        
        try:
            vraag = int(input("Make your choise:"))
            print("\n")
        except ValueError:
            print("X" *30)
            print("WRONG CHOICE!")
            print("X" *30)
            continue
            
        if vraag == 1:
            name = input("What is your name?:")
            
            try:
                level = int(input("From 0 to 10?:"))
            
            except ValueError:
                print("X" *30)
                print("ENTER A NUMBER")
                print("X" *30)
                continue
            
            if level == 0:
                print("☮" *20)
                print("\n-The game has ended-")
                print("You have no sins.\n")
                print("☮" *20)
                break
            
            play(name)
            break
                    
                    
        elif vraag == 2:
            print("-Credits-")
            print("=" *28)
            print("-Mikey Sorgeloos-")
            print("=" *28)
            
        elif vraag == 3:
            print("-Socials-")
            print("=" *28)
            print("|FB: Mikey Sorgeloos       |")
            print("|Insta: De_MIKEE           |")
            print("|Snap: De_mikee            |")
            print("|LinkedIN: Mikey Sorgeloos |")
            print("=" *28)
        
        elif vraag == 4:
            print("☮" *20)
            print("\n-The game has ended-")
            print("You have no sins.\n")
            print("☮" *20)
            break
        
        else:
            print("X" *30)
            print("WRONG CHOICE!")
            print("X" *30)
        
#------------------------------------------------------------------PART 1: OUTSIDE
            
def play(name):
    print("""Help…
Help… HEEEELP AAAAUWHHWHHHHEEEERRRRRGGGG!

You jolt awake, lying on the cold ground. Your head throbs as you push yourself upright. All around you stretches a dark forest—endless, silent. Too silent. No animals. No wind. Nothing. The air feels wrong, like the world is holding its breath.

Then—
A light.
Faint at first, growing stronger.

You step toward it, cautious but desperate for anything familiar. It’s a lantern. Old. Rusted. Flickering with a weak orange glow. You pick it up, and as you do, you notice a note beneath it.

“I KNOW WHAT YOU ARE.”

Your heart stops. Panic claws at your throat, but you force yourself to breathe. Focus. You need to stay focused.

You start walking, lantern trembling in your hand. The forest swallows the path until finally… a shape emerges in the darkness.

A cabin. Abandoned, decayed, leaning to one side like it could collapse with a sigh. A heavy padlock keeps the door shut. And on that door, smeared in dark, tacky red:

FIND THE CODE

“Is… is that blood?” you whisper.

Your stomach twists. Your pulse spikes.

Where are you?

With no other choice, you begin searching the surroundings…""")
    
    while True:
        print("\n")
        print("I can")
        print("-" *31)
        print("1. Go to the old shed")
        print("2. GO to the grave")
        print("3. Check the old mail")
        print("4. Try the code on the padlock")
        print("-" *31)
        
        try:
            vraag = int(input("choose to inpsect:"))
            print("\n")
                
        except ValueError:
            print("X" *30)
            print("WRONG CHOICE")
            print("X" *30)
            continue
        
        if vraag == 1:
            print("""You cautiously approach the old shed, every step crunching on dead leaves. Your hand shakes as you reach for the door—and, surprisingly, it swings open easily.

Inside, shards of broken glass litter the floor, catching the lantern’s weak glow. The room is empty… except for the wall ahead.

Blood, smeared and dark, forms the numbers: 2009.

Next to it, a note flutters slightly as if moved by a ghostly breath. You pick it up and read: 45.

Confusion knots your stomach. What could it mean?

Shoving the cryptic note into your pocket, you turn back toward the abandoned cabin, heart hammering with more questions than answers.""")
            
        
        elif vraag == 2:
            print("""As you approach the grave, something catches your eye—a shovel, carelessly laid across the mound. A sticky note clings to its handle, scrawled in hurried letters:

DIG ME UP

Your hands tremble as you lift the shovel. Each strike into the earth feels heavier than the last, and what seems like hours pass in a blur of dirt and sweat. Finally, the edge of wood breaks through the soil.

An old coffin. Its lid splinters under your blows. The moment it cracks open, a putrid stench hits you, so foul it makes your stomach churn. You shine your lantern inside.

A corpse lies within, twisted and decayed beyond recognition. You can’t tell if it was a boy or a girl. You fight the urge to gag.

Something catches your eye—a small yellow paper wedged between the corpse’s teeth. With shaking hands, you pry its mouth open. The brittle sound of cracking bones echoes in the silent night.

The note reads: 66. Around the edges of the paper, written in jagged letters: REDRUM.

Your chest tightens. The forest seems darker now. The cold wind brushes past you, whispering something you can’t quite hear.

Shoving the horrifying discovery into your mind, you turn back toward the abandoned cabin, the lantern flickering like a fragile heartbeat.""")
            
        elif vraag == 3:
            print("""You crouch down and begin rifling through the old mail scattered across the floor—bills yellowed with age, letters with curled edges. Some are somber, beginning with “In loving memory…”; others are harsh, warning of overdue payments and last notices.

Amid the piles, a torn piece of newspaper catches your eye. Half-burned, its edges blackened, it tells of a murder—but the names, dates, and details are obscured, lost to time and fire.

Pinned beneath the newspaper is a number, written hastily: 66. Under it, a single word: LIES.

A chill runs down your spine. You straighten up, heart pounding, the cabin feeling colder, darker, heavier than before.""")
                
        
        elif vraag == 4:
            if padlock():
                break
            
        else:
            print("X" *30)
            print("WRONG CHOICE")
            print("X" *30)
        
#----------------------------------------Padlock       
        
def padlock():
    while True:
        print("You look at the padlock")
        print("-" *30)
        print("1. Enter the code")
        print("2. Back")
        print("-" *30)
        
        
        keuze = input("Choose:")
            

            
        if keuze == "1":
            code_input = input("Enter code:")
            
            
                    
            if not code_input.isdigit():
                print("X" *30)
                print("ITS A NUMERIC CODE")
                print("X" *30)
                print("\n")
                continue
                    
            if code_input == "456666":
                inside()
                return True
                    
            else:
                print("X" *30)
                print("wrong combination")
                print("X" *30)
                print("\n")
                        
                    
        elif keuze == "2":
            print("You step back from the padlock.")
            return False
        
        else:
            print("X" *30)
            print("WRONG CHOICE")
            print("X" *30)
            print("\n")

                                
#------------------------------------------------------------------PART 2: INSIDE

def inside():
    print("Next part coming soon")
    
#------------------------------------------------------------------Opstart

menu()