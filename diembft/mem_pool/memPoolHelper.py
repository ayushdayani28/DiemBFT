from ..mem_pool.mem_pool import MemPool
from ..mem_pool.message import Message


class MemPoolHelper:

    # cache of client's requests handled
    def __init__(self):
        self.mem_pool = MemPool()

    def get_message(self):
        return self.mem_pool.deque()

    def put_message(self, message:Message):
        self.mem_pool.enque(message)
