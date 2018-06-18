import pytumblr
import pytube
import praw
import secure

def getYoutubeURLFromReddit():
    bot = praw.Reddit(user_agent='GameDealBot v0.1',
                  client_id=secure.client_id,
                  client_secret=secure.client_secret,
                  username=secure.user,
                  password=secure.password)
    
    subreddit = bot.subreddit("Music")
    
    for submission in subreddit.hot(limit=50):
        if ("youtube" in submission.url or "youtu.be" in submission.url) and "[" in submission.title:
            print(submission.title)
            return submission.url   #whatever is popular on reddit at the time
        
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #never gonna give you up


def getAudioFromYoutubeVideo():
    print("test")
    #todo: pipe through ffmpeg


print(getYoutubeURLFromReddit())
