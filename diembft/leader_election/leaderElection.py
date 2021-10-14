from ..utilities.constants import WINDOW_SIZE
from ..block_tree.qc import QC


class LeaderElection:

    def __init__(self, validators, exclude_size):
        self.validators = validators  # All the nodes - the node that is proposing the message
        self.window_size = WINDOW_SIZE
        self.exclude_size = exclude_size
        self.reputation_leaders = {}

    # # For the time being we are returning the leader in round robin fashion
    # def elect_reputation_leader(self, qc: QC):
    #     # Validators that signed the last window_size committed blocks
    #     active_validators = 10
    #     # Ordered set of authors of last exclude_size committed blocks
    #     return

    # def update_leaders(self, qc: QC):
    #     extended_round = qc.vote_info.parent_round
    #     qc_round = qc.vote_info.round
    #     current_round = PaceMaker().current_round
    #     if extended_round + 1 == qc_round and qc_round + 1 == current_round:
    #         self.reputation_leaders[current_round + 1] = self.elect_reputation_leader(qc)

    def get_leader(self, round):
        if round in self.reputation_leaders.keys():
            return self.reputation_leaders[round]
        index = (round / 2) % len(self.validators)
        return self.validators[index]  # Round robin leader
