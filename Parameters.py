

# How many times the bot will check twitter for changes, don't make it too much otherwise the bot will get rate limited
MAX_TWITTER_CALLS_A_DAY = 1000

# How many retweets are permitted before a cooldown goes into effect
MENTION_LIMIT = 3

# How long is the cooldown before the bot resets mention count of a user 
# Cool down is 3 days
# COOL_DOWN_TIME = 259200.0
COOL_DOWN_TIME = 300

# Delay per retweet to user
RETWEET_DELAY = 1

# List of hashtags to listen for
LISTEN_TAGS = ["#InflatedEgos", "#Inflatedegos", "#inflatedegos", "#inflatedEgos", "#IE", "#IEgos"]