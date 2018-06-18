from pygame import mixer
from threading import Thread
import random
import time
#using pygame in case I want to add more features, like keystroke support or animations
#might have to switch so I can run two pieces of beautiful music at the same time


inp = input("Please enter the file path of the song you wish to ruin.\nFor default, press enter: ")

if inp == "":
    inp = "meme_music.wav"

mixer.init()
mixer.Channel(1).play(mixer.Sound(inp)) #so it plays at the same time
#try-except (seemingly) not needed, since mixer seemingly handles exceptions automatically.
#Will add later if wrong.)



def WAH():
    mixer.Channel(0).play(mixer.Sound('wah_sound.wav')) #its beautiful
    print(""" __          __     _    _ 
 \ \        / /\   | |  | |
  \ \  /\  / /  \  | |__| |
   \ \/  \/ / /\ \ |  __  |
    \  /\  / ____ \| |  | |
     \/  \/_/    \_\_|  |_|
                           
                           """) #keeping logs


def THREAD_WAH(): #the thread that makes Waluigi yell "Wah"
    while True:
        time.sleep(random.randint(1,10) * .1)
        WAH()

def Thread_Whitespace(): #makes timing look better
    while True:
        time.sleep(.1)
        print("") #prints whitespace between tactically timed "wahs"


if __name__ == "__main__":
    thread1 = Thread(target = THREAD_WAH)
    thread2 = Thread(target = Thread_Whitespace)
    thread1.start()
    thread2.start()
