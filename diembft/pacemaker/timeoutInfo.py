from ..block_tree.qc import QC


# TODO: Add Signature
class TimeOutInfo:

    def __init__(self):
        self.round = 0
        self.high_qc = QC()
        self.sender = ''
        self.signature = ''
