from diembft.block_tree.block import Block


class LedgerStore:

    def __init__(self):
        pass

    def add(self, block_id, exec_state_id, prev_block_id, block: Block):
        pass

    def delete(self, block_id):
        pass

    def find(self, block_id):
        pass

    def prune(self, block_id):
        pass

    def show(self):
        pass
