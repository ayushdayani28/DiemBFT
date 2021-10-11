import voteinfo as VoteInfo
from diembft.ledger.ledgerCommitInfo import LedgerCommitInfo
import qc as QC

class VoteMsg:

    def __init__(self):
        self.vote_info = VoteInfo()
        self.ledger_commit_info = LedgerCommitInfo()
        self.high_commit_qc = QC()
        self.sender = ''
        self.signature = ''