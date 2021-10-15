from diembft.utilities.nop import Nop
from message import Message

"""
MemPool class takes care of two things:
1. When a replica receives client request, it checks if it has already processed the request.
   If so, it will forward the response 

"""

class MemPool:

    def __init__(self):
        self.queue = []

    # Only Leader deques
    def deque(self):

        queue = self.queue

        if len(queue) > 0:
            return queue.pop(0)

        # send a No-op with no-op client id and no-op signature
        # whitelist the signature and client_id
        return Nop(-1, '')

    # Client enques
    def enque(self, message: Message):
        self.queue.append(message)

