import voteinfo as VoteInfo
from diembft.block_tree.ledgerCommitInfo import LedgerCommitInfo


class QC:
    def __init__(self, vote_info: VoteInfo, ledger_commit_info: LedgerCommitInfo, round: int):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.signatures = []
        self.author = ''
        self.author_signature = ''
        self.round = round
        # block id
        self.id = 0
