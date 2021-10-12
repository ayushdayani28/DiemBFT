from ..utilities.nop import Nop


class Queue:

    def __init__(self):
        self.queue = []

    def deque(self):

        queue = self.queue

        if len(queue) > 0:
            return queue.pop(0)

        else:
            return Nop()

    def enque(self, message: Message):


