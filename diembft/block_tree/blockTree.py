from ..block_tree.block import Block
from ..block_tree.qc import QC
from ..ledger.ledger import Ledger
from diembft.messages.voteMsg import VoteMsg
from ..utilities.constants import F
from ..utilities.verifier import Verifier
from ..block_tree.blockId import BlockId


class BlockTree:
    def __init__(self):
        self.pending_block_tree = list()
        self.pending_votes = {}
        self.high_qc: QC = None
        self.high_commit_qc: QC = None

    def generate_block(self, transactions, current_round):

        # Create a BlockId object and hash it.
        block_id = BlockId('', current_round, transactions, self.high_qc)

        hash_id = Verifier.encode(block_id)

        return Block(self, current_round, transactions, self.high_qc, hash_id)

    def execute_and_insert(self, b: Block):

        Ledger.speculate(b.qc.id, b.id, b)

        self.pending_block_tree.append(b)

    def process_vote(self, v: VoteMsg):

        self.process_qc(v.high_commit_qc)

        vote_idx = Verifier.encode(v.ledger_commit_info)

        if vote_idx in self.pending_votes.keys():
            self.pending_votes[vote_idx].append(v.signature)
        else:
            self.pending_votes[vote_idx] = list(v.signature)

        if len(self.pending_votes[vote_idx]) == 2 * F + 1:
            # Create a QC
            qc = QC(vote_info=v.vote_info, ledger_commit_info=v.ledger_commit_info)

            return qc

        return None

    def process_qc(self, qc: QC):

        if qc.ledger_commit_info.commit_state_id is not None:
            Ledger.commit(qc.vote_info.parent_id)

            self.pending_block_tree.pop(qc.vote_info.parent_id)

            self.high_commit_qc = max(qc, self.high_commit_qc, key=lambda a, b: a.vote_info.round > b.vote_info.round)

        self.high_qc = max(qc, self.high_qc, key=lambda a, b: a.vote_info.round > b.vote_info.round)
