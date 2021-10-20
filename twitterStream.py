import tweepy
import _thread
import time
import queue

# https://www.geeksforgeeks.org/python-status-object-in-tweepy/
# Auth tokens
from urllib3.exceptions import ProtocolError

consumer_key = "1"
consumer_secret = "2"
access_key = "3"
access_secret = "4"

statusQueue = queue.Queue(maxsize=0)


class twitterListener():
    def __init__(self, userListID: list):
        self.userListID = userListID

    def listen(self):
        print(self.userListID)
        stream = MyStreamListener(consumer_key, consumer_secret, access_key, access_secret)

        while True:
            try:
                print("trying")
                stream.filter(follow=self.userListID)

            except (ProtocolError, AttributeError):
                print(time.ctime() + ": Lib probably crashed, restarting now")
                continue

            except Exception as e:
                print(e)
                print(time.ctime() + ": Something went wrong.")
                time.sleep(10)
                continue


# Override parent class.
class MyStreamListener(tweepy.Stream):
    def on_status(self, status):
        print(status)
        # statusQueue.put(status)

    def on_limit(self, track):
        print("Being rate limited. Standby...")
        time.sleep(10)
        print("Restarting")
        return True

    def on_error(self, status_code):
        print("Error occurred from tweeter!")
        print(status_code)
