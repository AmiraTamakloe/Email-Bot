import csv
import praw


r = praw.Reddit('bot1')
subreddit = r.subreddit("HipHopHeads")

post_title = []
song = []
created_utc = []
score = []
url = []

for submission in subreddit.hot(limit=1000):
    if submission.title.startswith("[FRESH]") or submission.title.startswith("[FRESH VIDEO]") or \
            submission.title.startswith("[Hype]") or submission.title.startswith("[ORIGINAL]") or \
            submission.title.startswith("[THROWBACK THURSDAY]"):
        song.append(submission.title)
        post_title.append("SONG")
        url.append(submission.url)
        score.append(submission.score)
        created_utc.append(submission.created_utc)

    elif submission.title.startswith('[FRESH ALBUM]'):
        post_title.append("ALBUM")
        song.append(submission.selftext)
        url.append(submission.url)
        score.append(submission.score)
        created_utc.append(submission.created_utc)

    elif "TRACKLIST" or "tracklist" in submission.selftext:
        post_title.append("ALBUM")
        song.append(submission.selftext)
        url.append(submission.url)
        score.append(submission.score)
        created_utc.append(submission.created_utc)

    else:
        continue

zippedlist= list(zip(post_title, song, created_utc, score, url))

with open("song.csv", "w") as music :
    music_writer = csv.writer(music, delimiter=",")
    for ligne in zippedlist:
        music_writer.writerow(ligne)
    music.close()