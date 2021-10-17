from diembft.certificates.qc import QC
from nacl.signing import SignedMessage
from diembft.utilities.signature import Signature


# TODO: Add signatureDiemBFT
class TimeOutInfo:

    def __init__(self, round: int, high_qc: QC, sender: str, signature: Signature):
        self.round = round
        self.high_qc = high_qc
        self.sender = sender
        self.signature = signature

