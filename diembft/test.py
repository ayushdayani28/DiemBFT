# ledger = LedgerImpl('1')
    # genesis_vote_info = VoteInfo(
    #     '10000',
    #     0,
    #     None,
    #     None,
    #     None
    # )
    # genesis_qc = QC(
    #     genesis_vote_info,
    #     None,
    #     0,
    #     []
    # )
    # b = BlockTree('1', ledger, genesis_qc)
    # block_id = BlockId(
    #     'author',
    #     2,
    #     ['add'],
    #     genesis_qc  # id = 10000
    # )
    # vote_info = VoteInfo(
    #     '10000',
    #     1,
    #     '10000',
    #     0,
    #     'abc'
    # )
    # ledger_commit_info = LedgerCommitInfo(
    #     '32231',
    #     Verifier.encode(str(vote_info))
    # )
    # high_qc = QC(
    #     vote_info,
    #     ledger_commit_info,
    #     1,
    #     []
    # )
    #
    # block_vote_info = VoteInfo(
    #     Verifier.encode(str(block_id)),
    #     2,
    #     '10000',
    #     1,
    #     'def'
    # )
    #
    # block_qc = QC(
    #     block_vote_info,
    #     ledger_commit_info,
    #     2,
    #     []
    # )
    #
    # block = Block(
    #     'skdsa',
    #     2,
    #     ['add'],
    #     high_qc,
    #     Verifier.encode(str(block_id))
    # )
    #
    # block1_id = BlockId(
    #     'author',
    #     3,
    #     ['add1'],
    #     block_qc  # id = 10000
    # )
    #
    # block1 = Block(
    #     'skdsa',
    #     3,
    #     ['add1'],
    #     block_qc,
    #     Verifier.encode(str(block1_id))
    # )
    # block1_vote_info = VoteInfo(
    #     Verifier.encode(str(block1_id)),
    #     3,
    #     Verifier.encode(str(block_id)),
    #     2,
    #     'def'
    # )
    # block1_qc = QC(
    #     block1_vote_info,
    #     ledger_commit_info,
    #     3,
    #     []
    # )
    #
    # block2_id = BlockId(
    #     'author',
    #     4,
    #     ['delete'],
    #     block1_qc  # id = 10000
    # )
    #
    # block2 = Block(
    #     'skdsa',
    #     4,
    #     ['delete'],
    #     block1_qc,
    #     Verifier.encode(str(block2_id))
    # )
    #
    # b.execute_and_insert(block)
    # b.execute_and_insert(block1)
    # b.execute_and_insert(block2)
    #
    # # b.process_qc(block2.qc)
    #
    # # b.generate_block(['add'], 1).id
    #
    # voteMsg = VoteMsg(
    #     vote_info=block1_vote_info,
    #     ledger_commit_info=ledger_commit_info,
    #     high_commit_qc=block_qc,
    #     sender='sender',
    #     signature=[]
    # )
    #
    # b.process_vote(voteMsg)