from threading import Barrier, Semaphore


class H2O:
    def __init__(self):
        # Create a barrier object for parties number of threads
        self.b = Barrier(3)
        # the initial value for the internal counter
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()
