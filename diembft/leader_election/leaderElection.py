from ..utilities.constants import WINDOW_SIZE
from ..block_tree.qc import QC

class LeaderElection:

    def __init__(self, validators, exclude_size):
        self.validators = validators
        self.window_size = WINDOW_SIZE
        self.exclude_size = exclude_size
        self.reputation_leaders = {}


    def elect_reputation_leader(self, qc : QC):
        # Validators that signed the last window_size committed blocks
        active_validators = 10
        # Ordered set of authors of last exclude_size committed blocks

    def update_leaders(self, qc : QC):
        extended_round = qc.vote_info
