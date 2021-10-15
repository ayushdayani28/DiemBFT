from nacl.signing import SignedMessage


class Signature:

    def __init__(self, node_id: str, message: SignedMessage):
        self.node_id = node_id
        self.message = message

    def __repr__(self):
        return self.node_id+self.message