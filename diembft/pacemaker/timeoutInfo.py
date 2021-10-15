from ..block_tree.qc import QC
from nacl.signing import SignedMessage


# TODO: Add Signature
class TimeOutInfo:

    def __init__(self, round: int, high_qc: QC, sender: str, signature: SignedMessage):
        self.round = round
        self.high_qc = high_qc
        self.sender = sender
        self.signature = signature

