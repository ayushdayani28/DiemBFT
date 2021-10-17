from diembft.mem_pool.message import Message
import uuid
from diembft.block_tree.client_request import ClientRequest


class Nop(Message):

    def __init__(self, client_id:str, signature):
        client_request = ClientRequest(client_id, str(uuid.uuid4()))
        super().__init__(['no-op'], signature, client_request)


