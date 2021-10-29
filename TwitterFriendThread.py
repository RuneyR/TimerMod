import tweepy
import time
import threading
from twitterStream import twitterStream


class TwitterFriendQueue:

    def __init__(self, tweety: tweepy.api):
        self.tweety = tweety

    def begin_thread(self):
        queueThread = threading.Thread(target=self.update_List)
        queueThread.setDaemon(True)
        queueThread.start()

    def update_List(self):
        while True:
            names_id_list = []
            current_id_list = self.tweety.get_friends()
            # Create newly updated list from Twitter filled with twitter users the account follows.
            for names in current_id_list:
                names_id_list.append(names.id)

            # Check the newest follow from twitter, compare it with the current working list. If theres a change,
            # run code.
            if vars(twitterStream).get('userListID')[0] == names_id_list[0]:
                print("New Follower Spotted!")
                print(names_id_list.screen_name)
            else:
                print("No change detected.")
            time.sleep(10)
