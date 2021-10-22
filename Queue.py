import queue
import threading
import time
import Checker

from Timer import Timer, TimerError


class Queue:
    def __init__(self, artist_dict: dict):
        self.artist_dict = artist_dict
        self.statusQueue = queue.Queue(maxsize=0)

    def beginThread(self):
        queueThread = threading.Thread(target=self.checkThenPost)
        queueThread.daemon = True
        queueThread.start()

    def checkThenPost(self):
        current_status = None
        user_in_dict = None
        can_post = False
        while True:
            if self.statusQueue.qsize() == 0:
                time.sleep(2)
            else:
                try:
                    current_status = self.statusQueue.get()
                    tid = current_status.user.id
                    # This could be used to check if a new user was added. Have it rebuild if the status returns a
                    # new ID and the dictionary returns none, which says that a new follower was added?
                    if self.artist_dict.get(tid) is not None:
                        user_in_dict = self.artist_dict.get(tid)
                        can_post = Checker.check_their_mentions(user_in_dict.mentionsMade)
                        user_in_dict.mentionsMade += 1
                        if can_post:
                            print(current_status.id)
                            try:
                                user_in_dict.timer.start()
                            except TimerError as a:
                                user_in_dict.timer.elapsedTime()



                        else:
                            user_in_dict.timer.elapsedTime()
                            if Checker.elapsed_time_check(user_in_dict.timer.elapsed_Time):
                                user_in_dict.mentionsMade = 1
                                user_in_dict.timer.stop()



                except ConnectionError:

                    continue
                except Exception as e:
                    print(e.with_traceback())
                    time.sleep(10)
                    continue

                is_RT = False
