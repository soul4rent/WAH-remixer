from pygame import mixer
#using pygame in case I want to add more features, like keystroke support or animations
#might have to switch so I can run two pieces of beautiful music at the same time

mixer.init()
mixer.music.load("wah_sound.mp3")
mixer.music.play()

