from diembft.logger.logger import Logger


class Ledger(Logger):

    def __init__(self):
        pass

    def speculate(self, prev_block_id, block_id, block):
        pass

    def pending_state(self, block_id):
        pass

    def commit(self, block_id):
        pass

    def committed_block(self, block_id):
        pass
