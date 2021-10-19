class TwitterArtist:
    def __init__(self, TwitterID: int, canRT: bool, mentionsMade: int, timer: object):
        self.TwitterID = TwitterID
        self.canRT = canRT
        self.mentionsMade = mentionsMade
        self.timer = timer

    def get_TwitterID(self):
        return self.TwitterID

    def get_canRT(self):
        return self.canRT

    def get_mentionsMade(self):
        return self.mentionsMade

    def get_timer(self):
        return self.timer

    def set_TwitterID(self, TwitterID: int):
        self.TwitterID = TwitterID

    def set_canRT(self, canRT: bool):
        self.canRT = canRT

    def set_mentionsMade(self, mentionsMade: int):
        self.mentionsMade = mentionsMade

    def set_timer(self, timer: object):
        self.timer = timer
