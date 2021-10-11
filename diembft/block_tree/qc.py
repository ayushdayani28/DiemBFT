import voteinfo as VoteInfo
from diembft.ledger.ledgerCommitInfo import LedgerCommitInfo

class QC:
    def __init__(self):
        self.vote_info = VoteInfo()
        self.ledger_commit_info = LedgerCommitInfo()
        self.signatures = []
        self.author = ''
        self.author_signature = ''
