class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()

        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()

        self.queue.append(element)

        self.editing.release()
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()

        res = self.queue.popleft()

        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.q = deque()
        self.capacity = capacity
        # acquire a lock, blocking or non-blocking
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        # locked
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            # unlocked
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        # locked the de
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if val and self.en.locked():
            self.en.release()
        return val

    def size(self) -> int:
        return len(self.q)