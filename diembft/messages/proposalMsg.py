from diembft.block_tree.block import Block
from diembft.certificates.timeOutCertficate import TimeOutCertificate
from diembft.certificates.qc import QC


class ProposalMsg:

    def __init__(self):
        self.block = Block()
        self.last_round_tc = TimeOutCertificate()
        self.high_commit_qc = QC()