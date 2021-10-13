from ..block_tree.block import Block
from ..pacemaker.timeOutCertficate import TimeOutCertificate
from ..block_tree.qc import QC


class ProposalMsg:

    def __init__(self):
        self.block = Block()
        self.last_round_tc = TimeOutCertificate()
        self.high_commit_qc = QC()