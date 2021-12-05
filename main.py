import tweepy
import Parameters

# Create TwitterArtist objects = to the number of returned followers the main account follows.
# If needed, add them to the filter first.
import ReadFile
from twitterStream import twitterStream
from TwitterArtist import TwitterArtist
from Timer import Timer
from Queue import Queue
from TweepyAPI import TweepyAPI
from TwitterFriendThread import TwitterFriendQueue



tweeter = None
names_list = []
twitter_obj = []
twitter_dict = {}


def assign_keys():
    global consumer_key, consumer_secret, access_key, access_secret
    ReadFile.check_key_file()
    our_keys = ReadFile.get_keys()
    consumer_key = our_keys[0]
    consumer_secret = our_keys[1]
    access_key = our_keys[2]
    access_secret = our_keys[3]


def authorize():
    callAPI = TweepyAPI(consumer_key, consumer_secret, access_key, access_secret)
    global tweeter
    tweeter = callAPI.authorize()


def populateListAndDictionary():
    followers = tweeter.get_friends()

    # The names_list is populated with User ID of people the account is following. A list of ID's is formed.
    for names in followers:
        names_list.append(names.id)

    # The twitter_obj is populate with TwitterArtist Objects, assigning unique users ID for every index in names_List
    for users in names_list:
        twitter_obj.extend([TwitterArtist(users, 0, Timer())])

    for artist in twitter_obj:
        twitter_dict[artist.TwitterID] = artist


if __name__ == '__main__':
    assign_keys()
    authorize()
    populateListAndDictionary()
    # Queue/Thread responsible for shifting through twitter status. Also posts on account's behalf.
    myQeu = Queue(twitter_dict, tweeter)
    myQeu.beginThread()
    twStream = twitterStream(names_list, myQeu, consumer_key, consumer_secret, access_key, access_secret)
    # Thread responsible for keeping follower list realtime.
    friendThread = TwitterFriendQueue(tweeter, twStream)
    friendThread.begin_thread()
    twStream.listen()
