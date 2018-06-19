import pytumblr
from pytube import YouTube
from pydub import AudioSegment
import praw
import os
import subprocess
import random
import secure


#crawls reddit /r/music for a popular youtube song link on /r/music
def getYoutubeURLFromReddit():
    bot = praw.Reddit(user_agent='WaluigiBot v0.1', #login to reddit 
                  client_id=secure.client_id,
                  client_secret=secure.client_secret,
                  username=secure.user,
                  password=secure.password)
    
    subreddit = bot.subreddit("Music")
    
    for submission in subreddit.hot(limit=50):
        #songs on /r/music are usually youtube links, and tagged with "[GENRE]" in the post title
        #regex might be better in the future, but this is fine for now.
        if ("youtube" in submission.url or "youtu.be" in submission.url) and "[" in submission.title:
            print(submission.title)
            return str(submission.url)   #whatever is popular on reddit at the time (get youtube link to song)
        
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #never gonna give you up if it can't find anything




#downloads a youtube video and pipes it through ffmpeg to get audio
def getAudioFromYoutube(ytlink):
    yt = YouTube(ytlink)
    filename = ''

    print('-YT download')
    try:
        yt.streams.filter(subtype='mp4').first().download()
        filename = yt.streams.filter(subtype='mp4').first().default_filename
        #see if mp4 is availible
    except:
        yt.streams.first().download()
        filename = yt.streams.first().default_filename
        #download any stream

    #use ffmpeg to extract audio from youtube video
    print('-ffmpeg conversion')
    try:
        command = "ffmpeg -i \""+filename+"\" -ab 160k -ac 2 -ar 22050 -vn audio.wav"
        subprocess.call(command, shell=True)
    except:
        print("ERR: FFMPEG COMMAND FAILED. COULD NOT FIND FILENAME OR COULD NOT PROCESS FILE.")

    #cleanup
    print('-cleanup (removing video)')
    try:
        os.remove(filename)
        print("Youtube File Removed!")
    except:
        print("ERR: FILE NOT REMOVED, OR COULDN'T BE FOUND")




#used by Waluigify()
#generates a random point in the song to place a "wah"
def WahDividers(sndLength):
    return sndLength - random.randint(0,sndLength) 


#takes audio file named "audio.wav", and randomly disperses "Wahs" made by Waluigi
#creates file named "beauty.mp3" in the process
#WARNING: DELETES "audio.wav" FOR CLEANUP (this prevents ffmpeg from breaking if ran again)
def Waluigify():

    print("-WAH")
    wahCount = 100 #number of wahs
    sound = AudioSegment.from_file("audio.wav")
    wahSound = AudioSegment.from_file("media/wah_sound.wav") #a beautiful cry of a beautiful perrson
    wahPoints = []


    #randomly insert "wahs" throught the soundtrack
    for x in range(wahCount):
        wahPoints.append(WahDividers(len(sound)))
    wahPoints = sorted(wahPoints) #points where waluigi annoyingly yells "wah"

    completeSound = sound
    for x in range(0, len(wahPoints)):
        completeSound = completeSound.overlay(wahSound, position=wahPoints[x]) #beautify audio

    completeSound.export("beauty.mp3", format="mp3")


    #cleanup
    print("-cleanup two (removing non-wah'd audio)")
    try:
        os.remove("audio.wav")
        print("WAV File Removed!")
    except:
        print("ERR: WAV FILE NOT REMOVED, OR COULDN'T BE FOUND")


def postOnTumblr():
    client = pytumblr.TumblrRestClient(
        secure.tumblrClient,
        secure.tumblrClientSecret,
        secure.tumblrOauthToken,
        secure.tumblrOauthSecret
    )

    # Make the request
    print("-posting on Tumblr")
    client.create_audio("waluigi-bot",  caption="Waluigi-Bot uses ADVANCED ALGORITHMS to WAH along to the following song:", data="beauty.mp3", tags = ["waluigi", "super mario", "mario", "memes", "beauty", "video games", "gaming"])


getAudioFromYoutube(getYoutubeURLFromReddit())
Waluigify()
postOnTumblr()
