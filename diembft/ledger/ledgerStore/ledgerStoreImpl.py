from ledgerStore import LedgerStore
from diembft.block_tree.block import Block
from treelib import Node, Tree
from diembft.constants import GENESIS

class LedgerStoreImpl(LedgerStore):

    def __init__(self):
        LedgerStore.__init__()
        tree = Tree()
        tree.create_node(GENESIS)

    def add(self, block_id: Block, parent_id: Block):
        return tree.create_node(tag=block.id, identifier=block.id, parent=parent.id, data=block.payload)

    def delete(self, block: Block):
        return tree.remove_node(block.id)

    def find(self, block_id):
        return tree.get_node(block_id)


