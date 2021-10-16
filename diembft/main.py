from diembft.block_tree.blockTree import BlockTree
from diembft.ledger.ledgerImpl import LedgerImpl
from diembft.certificates.qc import QC
from diembft.block_tree.voteinfo import VoteInfo
from diembft.utilities.constants import GENESIS, BYZANTINE_NODES, GENESIS_PARENT_ROUND, GENESIS_PARENT_ID
from diembft.safety.safety import Safety
from diembft.utilities.verifier import Verifier
from diembft.pacemaker.pacemaker import Pacemaker
from diembft.messages.proposalMsg import ProposalMsg
from diembft.leader_election.leaderElection import LeaderElection
from diembft.utilities.generateKeys import GenerateKeys
from diembft.messages.voteMsg import VoteMsg


class Main:

    def __init__(self, mapper: dict, nodes: list, node_id: str, keys: list):
        self.node_id = node_id
        self.verifier = Verifier(mapper, keys)
        self.ledger = LedgerImpl(self.node_id)
        self.genesis_qc = Main.generate_genesis_qc()
        self.block_tree = BlockTree(self.node_id, self.ledger, self.genesis_qc)
        self.safety = Safety(self.block_tree, node_id, self.ledger, self.verifier)
        self.pacemaker = Pacemaker(self.safety, self.block_tree, BYZANTINE_NODES)
        self.leader_election = LeaderElection(nodes, self.pacemaker, self.ledger)

    @staticmethod
    def generate_genesis_qc():
        genesis_vote_info = VoteInfo(
            GENESIS,
            0,
            GENESIS_PARENT_ID,
            GENESIS_PARENT_ROUND,
            None
        )
        return QC(
            genesis_vote_info,
            None,
            0,
            []
        )

    def process_certificate_qc(self, qc: QC):

        self.block_tree.process_qc(qc)
        self.leader_election.update_leaders(qc)
        self.pacemaker.advance_round_qc(qc)

    def process_proposal_msg(self, p: ProposalMsg):

        self.process_certificate_qc(p.block.qc)
        self.process_certificate_qc(p.high_commit_qc)
        self.pacemaker.advance_round_tc(p.last_round_tc)
        current_round = self.pacemaker.current_round
        curr_leader = self.leader_election.get_leader(current_round)
        if p.block.round != current_round or p.sender != curr_leader or p.block.author != curr_leader:
            return
        self.block_tree.execute_and_insert(p.block)
        vote_msg = self.safety.make_vote(p.block, p.last_round_tc)
        if vote_msg is not None:
            # send vote msg
            next_leader = self.leader_election.get_leader(current_round + 1)
            return vote_msg

    def process_vote_msg(self, message: VoteMsg):
        qc = self.block_tree.process_vote(message)
        if qc is not None:
            self.process_certificate_qc(qc)
            print('All is Well ', self.pacemaker.current_round)



if __name__ == '__main__':

    gn = GenerateKeys()
    keys = gn.generate_key()

    gn2 = GenerateKeys()
    keys2 = gn2.generate_key()

    mapper = dict()

    node_1_id = 'node_id_1'
    node_2_id = 'node_id_2'

    mapper[node_2_id] = keys2[1]
    mapper[node_1_id] = keys[1]

    nodes = [node_2_id, node_1_id]

    main = Main(
        mapper,
        nodes,
        node_1_id,
        keys
    )

    main2 = Main(
        mapper,
        nodes,
        node_2_id,
        keys2
    )

    curr_round = main.pacemaker.current_round

    new_block = main2.block_tree.generate_block(['abc'], curr_round)
    qc = main.genesis_qc
    p = ProposalMsg(
        new_block,
        None,
        qc,
        'node_id_2'
    )

    vote_msg = main.process_proposal_msg(p)
    main2.process_vote_msg(vote_msg)

