"""sisältää luona Timer"""
import time


class Timer:
    """luokka suoritusajan mittaamista varten"""

    def __init__(self, cputime=False):
        """konstruktori Timer-oliolle
        Args cputime: True/False (default False)
                määrittää mitaanko suoritinaikaa vai normaalia aikaa"""
        self.cputime = cputime
        self.starttime = None
        self.endtime = None

    def start(self):
        """tallentaa aloitusajan"""
        if self.cputime:
            self.starttime = time.process_time()
        else:
            self.starttime = time.time()

    def stop(self):
        """tallentaa lopetusajan"""
        if self.cputime:
            self.endtime = time.process_time()
        else:
            self.endtime = time.time()

    def result(self):
        """palauttaa suoritusajan sekunteina"""
        return self.endtime-self.starttime

    def print_result(self):
        """tulostaa suoritusajan konsoliin"""
        print(f"runtime: {self.endtime-self.starttime} seconds")
