# Timer purpose it to be created when Checker.py returns a False boolean.
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:

    def __init__(self):
        self.start_time = None
        self.elapsed_Time = 0.0

    def start(self):
        """Start a new timer by recording time at call."""
        if self.start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
            pass
        self.start_time = time.perf_counter()

    def elapsedTime(self):
        """Assign elapsed time."""
        self.elapsed_Time = time.perf_counter() - self.start_time

    def stop(self):
        """Stop the timer and resets time."""
        if self.start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        self.start_time = None
    
    def Print(self):
        """print the start time and elapsed time"""
        print("Start time: " + str(self.start_time))
        print("Elapsed time: " + str(self.elapsed_Time))
