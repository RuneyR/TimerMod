# Check if the account mentioning will be RT by main account.
# Only check if they can post whenever the Listener receives a mention. Do not constantly check for it.
import math
from Parameters import MENTION_LIMIT, COOL_DOWN_TIME, RETWEET_DELAY



def check_their_mentions(count):
    """:returns Boolean - True if mentions has not hit the Mention Limit. """
    if count < MENTION_LIMIT:
        return True
    else:
        return False


def elapsed_time_check_cooldown(elapsed_time: float):
    """:returns Boolean - True if the time passed is greater the the Cool Down Limit. """
    minute = 60
    hour = 60 * 60
    if elapsed_time >= COOL_DOWN_TIME:
        return True
    else:
        difference = COOL_DOWN_TIME - elapsed_time
        print("Timer: Not enough time has passed, " + str( math.floor(difference / hour)) + " hours and " + str( math.floor(difference % hour / minute)) + " minutes left." )
        return False
        
def elapsed_time_check_delay(elapsed_time: float):
    """:returns Boolean - True if the time passed is greater the the Cool Down Limit. """
    minute = 60
    hour = 60 * 60
    if elapsed_time >= RETWEET_DELAY:
        return True
    else:
        difference = RETWEET_DELAY - elapsed_time
        print("Timer: Not enough time has passed, " + str( math.floor(difference / hour)) + " hours and " + str( math.floor(difference % hour / minute)) + " minutes left." )
        return False
