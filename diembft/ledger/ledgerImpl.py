from diembft.utilities.fileHandler import FileHandler
from ledger import Ledger
from ledgerStore.ledgerStore import LedgerStore
from ..block_tree.block import Block
from ..utilities.verifier import Verifier


class StateId:
    def __init__(self, prev_state_id, transactions):
        self.prev_state_id = prev_state_id
        self.transactions = transactions


class LedgerImpl(Ledger):

    def __init__(self):
        super().__init__()
        self.ledger_store = LedgerStore()
        self.file = FileHandler()

    def speculate(self, prev_block_id, block_id, block: Block):
        prev_state_id = self.pending_state(prev_block_id)
        # Generate the hash for prev_state_id || transactions to cover the history of the ledger
        exec_state_id = Verifier.encode(StateId(prev_state_id, block.payload))
        return self.ledger_store.add(block_id=block_id, exec_state_id=exec_state_id, prev_block_id=prev_block_id,
                                     block=block).tag

    # Returns the pending state for the given block_id or None if not present
    def pending_state(self, block_id):
        try:
            return self.ledger_store.find(block_id).tag
        except AttributeError:
            print("No pending state found")
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
        self.file.write_file(str(block_id) + " ")
        self.file.write_file(str(node.data) + "\n")

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
