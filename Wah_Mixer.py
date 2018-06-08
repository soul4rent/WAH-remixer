from pygame import mixer
import random
import time
#using pygame in case I want to add more features, like keystroke support or animations
#might have to switch so I can run two pieces of beautiful music at the same time

mixer.init()

mixer.Channel(1).play(mixer.Sound('meme_music.wav')) #so it plays at the same time


def WAH():
    mixer.Channel(0).play(mixer.Sound('wah_sound.wav')) #its beautiful


while True:
    time.sleep(random.randint(0,10) * .1) #oh no
    WAH()
