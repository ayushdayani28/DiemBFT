import random
from ..utilities.constants import WINDOW_SIZE, EXCLUDE_SIZE
from ..block_tree.qc import QC
from ..ledger.ledger import Ledger
from ..block_tree.block import Block


class LeaderElection:

    def __init__(self, validators):
        self.validators = validators  # All the nodes - the node that is proposing the message
        self.window_size = WINDOW_SIZE
        self.exclude_size = EXCLUDE_SIZE
        self.reputation_leaders = {}

    def elect_reputation_leader(self, qc: QC):
        # Validators that signed the last window_size committed blocks
        active_validators = []

        # Ordered set of authors of last exclude_size committed blocks
        last_authors = []
        current_qc = qc
        i = 0
        while i < self.window_size or len(last_authors) < self.exclude_size:
            # Block committed for the round r-2
            current_block: Block = Ledger.committed_block(current_qc.vote_info.parent_id)

            # Author of the block committed in round r-2
            block_author = current_block.author

            if i < self.window_size:
                # TODO : We have to get all the nodes that signed the current_qc and hence have their signatures.
                active_validators = active_validators.append(current_qc.signatures)

            if len(last_authors) < self.exclude_size:
                last_authors = last_authors.append(block_author)

            current_qc = current_block.qc

        # To convert the list to an ordered set of last_authors
        last_authors = list(dict.fromkeys(last_authors))

        # Final list of active_validators after removing the nodes that were authors in Excluded_Size of rounds.
        active_validators = [x for x in active_validators if x not in last_authors]

        # To generate pseudo random numbers based on the round number
        random.seed(qc.vote_info.round)

        return active_validators[random.randint(0, len(active_validators)-1)]

    def update_leaders(self, qc: QC):
        extended_round = qc.vote_info.parent_round
        qc_round = qc.vote_info.round
        current_round = PaceMaker().current_round
        if extended_round + 1 == qc_round and qc_round + 1 == current_round:
            self.reputation_leaders[current_round + 1] = self.elect_reputation_leader(qc)

    def get_leader(self, round):
        #
        if round in self.reputation_leaders.keys():
            return self.reputation_leaders[round]
        index = (round / 2) % len(self.validators)

        # Simply return a leader by round robin selection
        return self.validators[index]
