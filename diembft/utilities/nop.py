from ..mem_pool.message import Message
import uuid


class Nop(Message):

    def __init__(self, client_id, signature):
        super().__init__(client_id, ['no-op'], signature, uuid.uuid4())


