import voteinfo as VoteInfo
from diembft.block_tree.ledgerCommitInfo import LedgerCommitInfo


class QC:
    def __init__(self, vote_info, ):
        self.vote_info = VoteInfo()
        self.ledger_commit_info = LedgerCommitInfo()
        self.signatures = []
        self.author = ''
        self.author_signature = ''
        # block id
        self.id = 0
