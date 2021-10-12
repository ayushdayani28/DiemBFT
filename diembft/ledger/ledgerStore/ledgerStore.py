from diembft.block_tree.block import Block


class LedgerStore:

    def __init__(self):
        pass

    def add(self, block: Block, parent: Block):
        pass

    def delete(self, block: Block):
        pass

    def find(self, block_id):
        pass
