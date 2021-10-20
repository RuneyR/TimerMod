import tweepy

# Create TwitterArtist objects = to the number of returned followers the main account follows.
# If needed, add them to the filter first.
from TwitterArtist import TwitterArtist
from Timer import Timer

consumer_key = "1"
consumer_secret = "2"
access_key = "3"
access_secret = "5"

tweeter = None
names_list = []
twitter_obj = []


def authorize():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    global tweeter
    tweeter = tweepy.API(auth)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    authorize()
    followers = tweeter.get_friends()

    # The names_list is populated with User ID of people the account is following. A list of ID's is formed.
    for names in followers:
        names_list.append(names.id)

    # The twitter_obj is populate with TwitterArtist Objects, assigning unique users ID for every index in names_List
    for users in names_list:
        twitter_obj.extend([TwitterArtist(users, True, 0, Timer())])
