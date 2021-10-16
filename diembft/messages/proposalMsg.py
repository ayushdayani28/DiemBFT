from diembft.block_tree.block import Block
from diembft.certificates.timeOutCertficate import TimeOutCertificate
from diembft.certificates.qc import QC


class ProposalMsg:

    def __init__(self, block: Block, last_tc: TimeOutCertificate, qc: QC, sender: str):
        self.sender = sender
        self.block = block
        self.last_round_tc = last_tc
        self.high_commit_qc = qc