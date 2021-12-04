import tweepy
import Timer


class TwitterArtist:
    def __init__(self, twitterID: int, mentionsMade: int, timer: Timer.Timer):
        self.TwitterID = twitterID
        self.mentionsMade = mentionsMade
        self.timer = timer

    def Print(self):
        print("Twitter ID: " + str(self.TwitterID))
        print("mentionsMade: " + str(self.mentionsMade))
        self.timer.Print()