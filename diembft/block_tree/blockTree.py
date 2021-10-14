from ..block_tree.block import Block
from ..block_tree.qc import QC
from ..ledger.ledger import Ledger
from treelib import Tree
from ..block_tree.voteMsg import VoteMsg
from ..utilities.constants import F


class BlockTree:
    def __init__(self):
        self.pending_block_tree = Tree()
        self.pending_votes = {}
        self.high_qc = None
        self.high_commit_qc = None

    def generate_block(self, transactions, current_round):

        # Create a BlockId object and hash it.
        hash_id = "hash(author || round || payload || qc.vote.info.id || qc.signature"

        return Block(self, current_round, transactions, self.high_qc, hash_id)

    def execute_and_insert(self, b: Block):

        Ledger.speculate(b.qc.id, b.payload)

        self.pending_block_tree.add(b)

    def process_vote(self, v: VoteMsg):

        self.process_qc(v.high_commit_qc)

        vote_idx = hash(v.ledger_commit_info)

        if vote_idx in self.pending_votes.keys():
            self.pending_votes[vote_idx].append(v.signature)
        else:
            self.pending_votes[vote_idx] = list(v.signature)

        if len(self.pending_votes[vote_idx]) == 2 * F + 1:
            # Create a QC
            qc = QC()

            return qc

        return None

    def process_qc(self, qc: QC):

        if qc.ledger_commit_info.commit_state_id is not None:

            Ledger.commit(qc.vote_info.parent_id)
            # Something needs to be done here. Not sure what to prune
            self.pending_block_tree.remove_node(qc.vote_info.parent_id)

            # Max
            self.high_commit_qc = qc.vote_info

        self.high_qc =