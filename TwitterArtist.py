class TwitterArtist:
    def __init__(self, TwitterID: int, canRT: bool, mentionsMade: int, timer: object):
        self.TwitterID = TwitterID
        self.canRT = canRT
        self.mentionsMade = mentionsMade
        self.timer = timer
