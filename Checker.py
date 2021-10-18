# Check if the account mentioning will be RT by main account.
# Only check if they can post whenever the Listener receives a mention. Do not constantly check for it.
MENTION_LIMIT = 3
# Cool down is 3 days
COOL_DOWN_TIME = 259200.0


def check_their_mentions(count):
    """:returns Boolean - False if mentioned hit their Mention Limit. """
    if count > MENTION_LIMIT:
        return False
    else:
        return True


def elapsed_time_check(elapsed_time: float, cool_down_limit: float):
    """:returns Boolean - True if the time passed is greater the the Cool Down Limit. """
    if elapsed_time >= cool_down_limit:
        return True
    else:
        return False
