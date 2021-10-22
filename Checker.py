# Check if the account mentioning will be RT by main account.
# Only check if they can post whenever the Listener receives a mention. Do not constantly check for it.
MENTION_LIMIT = 3
# Cool down is 3 days
# COOL_DOWN_TIME = 259200.0
COOL_DOWN_TIME = 180.0


def check_their_mentions(count):
    """:returns Boolean - True if mentions has not hit the Mention Limit. """
    if count < MENTION_LIMIT:
        return True
    else:
        return False


def elapsed_time_check(elapsed_time: float):
    """:returns Boolean - True if the time passed is greater the the Cool Down Limit. """
    if elapsed_time >= COOL_DOWN_TIME:
        return True
    else:
        return False
