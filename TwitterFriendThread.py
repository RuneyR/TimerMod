import tweepy
import time
import threading
from twitterStream import twitterStream

SLEEP_TIME = 300


class TwitterFriendQueue:

    def __init__(self, tweety: tweepy.api, currentList: twitterStream):
        self.tweety = tweety
        self.cList = currentList

    def begin_thread(self):
        queueThread = threading.Thread(target=self.update_List)
        queueThread.setDaemon(True)
        queueThread.start()

    # Make 2 ID lists. One current list the program is working with and one fresh list from twitter. Compare the 2.
    # If not the same, the follower list on Twitter has change, update programs list to keep up to date on
    # tweets/followers.

    def update_List(self):
        while True:
            names_id_list = []
            current_working_id_list = self.cList.userListID
            current_twitter_users = self.tweety.get_friends()
            # Create newly updated list from Twitter filled with twitter users the account follows.
            for names in current_twitter_users:
                names_id_list.append(names.id)

            # Check the newest follow from twitter, compare it with the current working list. If theres a change,
            # change variables. If there is none, go to sleep to avoid rate limit.
            if current_working_id_list[0] == names_id_list[0]:
                print("No change detected.")

            else:
                print("Change detected.")
                print(current_twitter_users[0].screen_name)
                self.cList.userListID = names_id_list
                self.cList.stream.disconnect()

            time.sleep(10)
