class LedgerCommitInfo:
    def __init__(self, commit_state_id: str, vote_info_hash: str):
        self.vote_info_hash = vote_info_hash
        self.commit_state_id = commit_state_id

    def __repr__(self):
        return self.vote_info_hash + self.commit_state_id
