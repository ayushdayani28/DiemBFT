from diembft.block_tree.ledgerCommitInfo import LedgerCommitInfo
from diembft.block_tree.voteinfo import VoteInfo
from diembft.certificates.qc import QC
from diembft.utilities.signature import Signature


class VoteMsg:

    def __init__(self, vote_info: VoteInfo, ledger_commit_info: LedgerCommitInfo, high_commit_qc: QC, sender: str, signature: Signature):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.high_commit_qc = high_commit_qc
        self.sender = sender
        self.signature = signature
