from diembft.block_tree.voteinfo import VoteInfo
from diembft.block_tree.ledgerCommitInfo import LedgerCommitInfo


class QC:
    def __init__(self, vote_info: VoteInfo = None, ledger_commit_info: LedgerCommitInfo = None, round: int = None, signatures: list = None):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.signatures = signatures
        self.author = ''
        self.author_signature = ''
        self.round = round
        # block id
        self.block_id = 0
