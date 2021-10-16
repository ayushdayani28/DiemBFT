from diembft.block_tree.block import Block
from diembft.certificates.qc import QC
from diembft.ledger.ledgerImpl import LedgerImpl
from diembft.messages.voteMsg import VoteMsg
from diembft.utilities.constants import BYZANTINE_NODES
from diembft.utilities.verifier import Verifier
from diembft.block_tree.blockId import BlockId
from diembft.utilities.constants import GENESIS


class BlockTree:
    def __init__(self, node_id, ledger: LedgerImpl, genesis_qc: QC):
        self.pending_block_tree = list()
        self.pending_votes = {}
        self.high_qc: QC = genesis_qc
        self.high_commit_qc: QC = genesis_qc  # At the start we have the genesis QC as the high_qc
        self.node_id = node_id
        self.ledger = ledger

    def generate_block(self, transactions, current_round):

        # Create a BlockId object and hash it.
        block_id = BlockId(self.node_id, current_round, transactions, self.high_qc)

        hash_id = Verifier.encode(str(block_id))

        return Block(self.node_id, current_round, transactions, self.high_qc, hash_id)

    def execute_and_insert(self, b: Block):

        self.ledger.speculate(b.qc.vote_info.id, b.id, b)

        self.pending_block_tree.append(b.qc.vote_info.parent_id)

    def process_vote(self, v: VoteMsg):

        self.process_qc(v.high_commit_qc)

        vote_idx = Verifier.encode(str(v.ledger_commit_info))

        if vote_idx in self.pending_votes.keys():
            self.pending_votes[vote_idx].append(v.signature)
        else:
            self.pending_votes[vote_idx] = [v.signature]

        if len(self.pending_votes[vote_idx]) == 2 * BYZANTINE_NODES + 1:
            # Create a QC
            qc = QC(v.vote_info,v.ledger_commit_info, v.vote_info.round, self.pending_votes[vote_idx])

            return qc

        return None

    def process_qc(self, qc: QC):

        if qc.ledger_commit_info and qc.ledger_commit_info.commit_state_id is not None and qc.vote_info.parent_id != GENESIS:
            self.ledger.commit(qc.vote_info.parent_id)

            self.pending_block_tree.remove(qc.vote_info.parent_id)

            self.high_commit_qc = qc if qc.vote_info.round > self.high_commit_qc.round else self.high_commit_qc

            # self.high_commit_qc = max(qc, self.high_commit_qc, key=lambda a, b: a.vote_info.round > b.vote_info.round)

        # self.high_qc = max(qc, self.high_qc, key=lambda a, b: a.vote_info.round > b.vote_info.round)
        self.high_qc = qc if qc.vote_info.round > self.high_qc.round else self.high_qc
