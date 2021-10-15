from diembft.block_tree.blockTree import BlockTree
from diembft.ledger.ledgerImpl import LedgerImpl
from diembft.block_tree.block import Block
from diembft.certificates.qc import QC
from diembft.block_tree.voteinfo import VoteInfo
from diembft.block_tree.ledgerCommitInfo import LedgerCommitInfo
from diembft.utilities.verifier import Verifier
from diembft.block_tree.blockId import BlockId

if __name__ == '__main__':
    ledger = LedgerImpl('1')
    b = BlockTree('1', ledger)
    genesis_vote_info = VoteInfo(
        '10000',
        0,
        None,
        None,
        None
    )
    genesis_qc = QC(
        genesis_vote_info,
        None,
        0,
        []
    )
    # parent_block_id = BlockId(
    #     'parent',
    #     1,
    #     ['dsjahds'],
    #     genesis_qc
    # )
    block_id = BlockId(
        'skdsa',
        1,
        ['q'],
        genesis_qc
    )
    vote_info = VoteInfo(
        Verifier.encode(str(block_id)),
        1,
        '10000',
        0,
        'abc'
    )
    ledger_commit_info = LedgerCommitInfo(
        '32231',
        Verifier.encode(str(vote_info))
    )
    qc = QC(
        vote_info,
        ledger_commit_info,
        1,
        []
    )
    block = Block(
        'skdsa',
        1,
        ['q'],
        qc,
        Verifier.encode(str(block_id))
    )

    b.execute_and_insert(block)

