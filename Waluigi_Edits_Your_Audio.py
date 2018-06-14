from pydub import AudioSegment


sound = AudioSegment.from_file("meme_music.wav")

halfway_point = len(sound) // 2
first_half = sound[:halfway_point]
second_half = sound[halfway_point:]

# create a new file "first_half.mp3":
first_half.export("Waluigi Automatic Edits/first_half.wav", format="wav")
second_half.export("Waluigi Automatic Edits/second_half.wav", format="wav")

sound1 = AudioSegment.from_wav("Waluigi Automatic Edits/first_half.wav")
sound2 = AudioSegment.from_wav("Waluigi Automatic Edits/second_half.wav")
WAH = AudioSegment.from_wav("wah_sound.wav")

combined_sounds = sound1 + WAH + sound2
#For now, Waluigi will "WAH" in the middle of your audio.
#TODO: Random Waluigi edits.

combined_sounds.export("path.wav", format="wav")

