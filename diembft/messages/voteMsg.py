class VoteMsg:

    def __init__(self, vote_info, ledger_commit_info, high_commit_qc, sender, signature):
        self.vote_info = vote_info
        self.ledger_commit_info = ledger_commit_info
        self.high_commit_qc = high_commit_qc
        self.sender = sender
        self.signature = signature
