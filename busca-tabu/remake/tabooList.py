from myQueue import Queue

class TabooList:

    def __init__(self, size):
        self._size = size
        self._queue = Queue(size)
        self._length = 0

    def addMovement(self, movement):
        if self._queue.isFull():
            self._queue.pop()
        self._queue.push(movement)

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)

    def containsMovement(self, movement):
        return self._queue.contains(movement)
