from ..pacemaker.timeOutCertficate import TimeOutCertificate
from ..block_tree.qc import QC
from ..ledger.ledgerImpl import LedgerImpl


class Safety:

    def __init__(self):
        self.private_key = ''
        self.public_keys = []
        self.highest_vote_round = 0
        self.highest_qc_round = 0
        self.ledger = LedgerImpl()

    def increase_highest_vote_round(self, round):
        self.highest_vote_round = max(self.highest_vote_round, round)

    def update_highest_qc_round(self, qc_round ):
        self.highest_qc_round = max(self.highest_qc_round, qc_round)

    @staticmethod
    def check_consecutive(block_round, round):
        return round + 1 == block_round

    @staticmethod
    def safe_to_extend(self, block_round, qc_round, tc: TimeOutCertificate):
        return Safety.check_consecutive(block_round,tc.round) and qc_round >= max(tc.tmo_high_qc_rounds)

    def safe_to_vote(self, block_round, qc_round, tc:TimeOutCertificate):
        if block_round <= max(self.highest_vote_round, qc_round):
            return False
        return Safety.check_consecutive(block_round, qc_round) or self.safe_to_extend(block_round, qc_round, tc)

    def safe_to_timeout(self, current_round, qc_round, tc:TimeOutCertificate):
        if qc_round < self.highest_qc_round or current_round <= max(self.highest_vote_round - 1, qc_round):
            return False
        return Safety.check_consecutive(current_round, qc_round) or Safety.check_consecutive(current_round, tc.round)

    def commit_state_id(self, block_round, qc: QC):
        if Safety.check_consecutive(block_round, qc.vote_info.round):
            return self.ledger.pending_state(qc.id)
        return None
