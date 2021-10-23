import tweepy
import Timer


class TwitterArtist:
    def __init__(self, twitterID: int, mentionsMade: int, timer: Timer.Timer):
        self.TwitterID = twitterID
        self.mentionsMade = mentionsMade
        self.timer = timer
