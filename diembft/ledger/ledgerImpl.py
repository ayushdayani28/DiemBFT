from diembft.utilities.fileHandler import FileHandler
from diembft.ledger.ledger import Ledger
from diembft.ledger.ledgerStore.ledgerStoreImpl import LedgerStoreImpl
from diembft.block_tree.block import Block
from diembft.utilities.verifier import Verifier
from diembft.ledger.helper.stateId import StateId


class LedgerImpl(Ledger):

    def __init__(self, node_id: str):
        super().__init__()
        self.ledger_store = LedgerStoreImpl()
        self.file = FileHandler(node_id=node_id)

    def speculate(self, prev_block_id, block_id, block: Block):
        prev_state_id = self.pending_state(prev_block_id)
        # Generate the hash for prev_state_id || transactions to cover the history of the ledger
        exec_state_id = Verifier.encode(str(StateId(prev_state_id, block.payload)))
        # self.log_info('Adding node with block_id: ' + str(block_id) + ',exec_state_id: ' + str(exec_state_id) + ' to ' + 'parent: ' + str(prev_block_id))
        return self.ledger_store.add(block_id=block_id, exec_state_id=exec_state_id, prev_block_id=prev_block_id,
                                     block=block).tag

    # Returns the pending state for the given block_id or None if not present
    def pending_state(self, block_id):
        try:
            return self.ledger_store.find(block_id).tag
        except AttributeError:
            # self.log_info("No pending state found in the tree")
            print('')
        return None

    # Exports the branch to persistent layer
    # Discard speculate branches that fork from ancestors
    def commit(self, block_id):
        self.write_ledger_to_file(block_id)
        self.ledger_store.prune(block_id)

    # Returns the Block from the in cache tree
    def committed_block(self, block_id):
        return self.ledger_store.find(block_id).data

    def write_ledger_to_file(self, block_id):
        node = self.ledger_store.find(block_id)
        if not node or not node.data:
            return
        self.file.write_file(str(block_id) + " ")
        self.file.write_file(str(node.data.payload) + "\n")

# if __name__ == "__main__":
#     a = LedgerStoreImpl()
#     b = LedgerImpl(a)
#
#     b.speculate(100, 1, "Add")
#     b.speculate(100, 2, "Add")
#     b.speculate(100, 3, "Add")
#     b.speculate(3, 4, "Add")
#     b.speculate(3, 5, "Add")
#     b.speculate(3, 6, "Add")
#
#     b.commit(5)
