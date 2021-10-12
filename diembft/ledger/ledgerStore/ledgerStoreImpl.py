from ledgerStore import LedgerStore
from diembft.block_tree.block import Block


class LedgerStoreImpl(LedgerStore):

    def __init__(self):
        LedgerStore.__init__()

    def add(self, block: Block, parent: Block):
        pass

    def delete(self, block: Block):
        pass

    def find(self, block_id):
        pass

