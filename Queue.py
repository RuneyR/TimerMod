import Checker
import queue
import threading
import time
import tweepy
from Timer import TimerError


class Queue:
    def __init__(self, artist_dict: dict, tweety: tweepy.API):
        self.artist_dict = artist_dict
        self.statusQueue = queue.Queue(maxsize=0)
        self.tweety = tweety

    def beginThread(self):
        queueThread = threading.Thread(target=self.checkThenPost)
        queueThread.daemon = True
        queueThread.start()

    def checkThenPost(self):
        current_status = None
        user_in_dict = None
        can_post = False
        account_user = self.tweety.verify_credentials()
        while True:
            if self.statusQueue.qsize() == 0:
                print(("checkThenPost: StatusQueue is empty"))
                time.sleep(5)
            else:
                try:
                    print(("checkThenPost: StatusQueue has " + str(self.statusQueue.qsize()) + " element(s)" ))
                    current_status = self.statusQueue.get()
                    tid = current_status.user.id
                    name = current_status.user.screen_name
                    
                    print("checkThenPost: Tweet found by: '" + name + "'")
                    print("checkThenPost: Text: '" + current_status.text + "'")
                                    
                    # This could be used to check if a new user was added. Have it rebuild if the status returns a
                    # new ID and the dictionary returns none, which says that a new follower was added?
                    if self.artist_dict.get(tid) is not None:
                        user_in_dict = self.artist_dict.get(tid)
                        can_post = Checker.check_their_mentions(user_in_dict.mentionsMade)
                        
                        if user_in_dict.timer.start_time != None:
                            print("checkThenPost: Checking if Delay has been met")
                            can_post = can_post and Checker.elapsed_time_check_delay(user_in_dict.timer.elapsed_Time)
                        
                        # console
                        print(("checkThenPost: User " + name + " with " + str(tid) + " ID exists"))
                        user_in_dict.Print()
                        print("checkThenPost: Can post: " + str(can_post))
                        print("checkThenPost: current_status.in_reply_to_user_id: " + str(current_status.in_reply_to_user_id) + " (" + str(current_status.in_reply_to_screen_name) + ")")
                        print("checkThenPost: This account:("+ account_user.screen_name +" with ID (" + str(account_user.id) + ")")
                        
                        # On True, simply post the mention as a RT. Start the timer. If the timer already started,
                        # update elapsed time instead.
                        if can_post:
                            try:
                                print("checkThenPost: Retweeted tweet by: " + current_status.user.screen_name)
                                print("checkThenPost: Text: '" + current_status.text + "'")
                                
                                user_in_dict.mentionsMade += 1
                                print("checkThenPost: Mentions made: " + str(user_in_dict.mentionsMade))
                                
                                user_in_dict.timer.start()
                                self.tweety.retweet(current_status.id)

                            except TimerError:
                                user_in_dict.timer.elapsedTime()
                        # On False, check elapsed time.  If they mention and passed the cooldown period, rt their
                        # post. Stops then starts the timer for the new tweet.
                        else:
                            print("checkThenPost: Check Cooldown")
                            if user_in_dict.timer.start_time is not None:
                                user_in_dict.timer.elapsedTime()
                                print("checkThenPost: Checking if enough time has passed.")
                                
                            if Checker.elapsed_time_check_cooldown(user_in_dict.timer.elapsed_Time):
                                print(("checkThenPost: Cooldown has ended for user. Retweeting and starting the timer anew."))
                                print("checkThenPost: " + str(current_status.id))
                                
                                self.tweety.retweet(current_status.id)
                                user_in_dict.mentionsMade = 1
                                user_in_dict.timer.stop()
                                user_in_dict.timer.start()

                except ConnectionError:
                    continue
                except Exception as e:
                    print(e.with_traceback())
                    time.sleep(10)
                    continue
                is_RT = False
