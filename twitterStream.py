import tweepy
import time
from Queue import Queue
from urllib3.exceptions import ProtocolError

Que_Thread = None


class twitterStream:
    def __init__(self, userListID: list, thread: Queue, cons_key: str, cons_sec: str, access_key: str, access_sec: str):
        self.userListID = userListID
        self.cK = cons_key
        self.cS = cons_sec
        self.aK = access_key
        self.aS = access_sec
        global Que_Thread
        Que_Thread = thread

    def listen(self):
        print(self.userListID)
        stream = MyStreamListener(self.cK, self.cS, self.aK, self.aS)

        while True:
            try:
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
        Que_Thread.statusQueue.put(status)
        # statusQueue.put(status)

    def on_limit(self, track):
        print("Being rate limited. Standby...")
        time.sleep(10)
        print("Restarting")
        return True

    def on_error(self, status_code):
        print("Error occurred from tweeter!")
        print(status_code)
