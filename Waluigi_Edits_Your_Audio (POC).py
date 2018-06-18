from pydub import AudioSegment
import random


def WahDividers(sndLength):
    return sndLength - random.randint(0,sndLength) 

wahCount = 100 #number of wahs
sound = AudioSegment.from_file("meme_music.wav")
wahSound = AudioSegment.from_file("wah_sound.wav") #a beautiful cry of a beautiful perrson
wahPoints = []


for x in range(wahCount):
    wahPoints.append(WahDividers(len(sound)))
wahPoints = sorted(wahPoints) #points where waluigi annoyingly yells "wah"


print (wahPoints)
print(len(sound))

completeSound = sound
for x in range(0, len(wahPoints)):
    completeSound = completeSound.overlay(wahSound, position=wahPoints[x])


completeSound.export("beauty.wav", format="wav")

