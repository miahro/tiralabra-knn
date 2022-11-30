import time


class Timer:
    def __init__(self, cputime=False):
        self.cputime = cputime

    def start(self):
        if self.cputime:
            self.starttime = time.process_time()
        else:
            self.starttime = time.time()

    def stop(self):
        if self.cputime:
            self.endtime = time.process_time()
        else:
            self.endtime = time.time()

    def result(self):
        return self.endtime-self.starttime

    def print_result(self):
        print(f"runtime: {self.endtime-self.starttime} seconds")
