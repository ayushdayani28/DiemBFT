from diembft.block_tree.client_request import ClientRequest


class LedgerCommitInfo:
    def __init__(self, commit_state_id: str, vote_info_hash: str, client_request: ClientRequest):
        self.vote_info_hash = vote_info_hash
        self.commit_state_id = commit_state_id
        self.client_request = client_request

    def __repr__(self):
        return self.vote_info_hash + self.commit_state_id + str(self.client_request)
