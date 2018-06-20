# WAH-Remixer

This is a small little script that takes Waluigi's Iconic "WAH" sound, inserts it randomly into song posts that are popular on reddit, and then reuploads the "Wah'd" Version to Tumblr. All automatically.

Its dumb, its silly, and its fun.

I'm putting it under the Apache 2 license if you want to use it, but I don't suggest using it in any way that isn't fair use. I'm using copyrighted assets to learn various media manipulation in python.

All rights go to their respective copyright holders.

# Getting Started

You can probably get away with using "Git Clone" to clone this repository and just running the main.

However, you do need to install the following:

>Python 3.6 - Might work with later versions, but this is the version this project was built with. Not guaranteed to work on earlier versions of Python 3.X

>FFMPEG - Install and add to the path (different for windows/osx/linux)

>pytumblr - Can be installed via "pip install pytumblr"

>pytube - Can be installed via "pip install pytube"

>pydub - Can be installed via "pip install pydub"

>praw - Can be installed via "pip install praw"


In addition, you need to get bot keys / tokens from both python and tumblr. You need to get the following keys:

>Reddit Client

>Reddit Secret

>Reddit Username

>Reddit Password

>Tumblr Client

>Tumblr Secret

>Tumblr Oauth Token

>Tumblr Oauth Secret

In this project, I put these in a file called "secure.py" and imported it, since I didn't want to show the world my passwords.

# Recommended setup:

(NOT IMPLEMENTED YET) Waluigi-Bot uses a simple CRON job to automatically run once per day. It runs "sudo Python3 <name of main>" via the following Crontab setup:

> 0 0 * * *

Translating to "every day at 0:00". For more information about cron commands, I recommend typing "man cron" in the terminal of a linux machine, as it goes over various important things such as setup and options.

# Authors
- Kyle Wadsworth (Main Author)
