class Queue:

    def __init__(self, maxSize):
        self._data = maxSize * [None]
        self._maxSize = maxSize
        self._first = None
        self._last = None
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        if not self.isEmpty():
            if self._last < self._first:
                return str(self._data[self._first: self._maxSize] + self._data[0: self._last + 1])
            else:
                return str(self._data[self._first: self._last + 1])

        return "[]"

    # Adds an element to the queue.
    def push(self, element):
        if self._length == 0:
            self._first = 0
            self._last = 0
            self._length += 1
            self._data[0] = element
        else:
            if not self.isFull():
                index = self._last + 1

                # Loops around the list.
                if index >= self._maxSize:
                    index = 0
                    self._last = 0
                else:
                    self._last += 1

                self._length += 1
                self._data[index] = element

    # Removes the "oldest" element.
    def pop(self):
        if not self.isEmpty():
            element = self._data[self._first]

            # Loops around the list.
            if self._first == self._maxSize - 1:
                self._first = 0
            else:
                self._first += 1

            self._length -= 1
            
            return element

    def isFull(self):
        if self._length == self._maxSize:
            return True

        return False

    def isEmpty(self):
        if self._length == 0:
            return True

        return False