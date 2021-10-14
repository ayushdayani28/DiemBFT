from diembft.utilities.fileHandler import FileHandler
from ledger import Ledger
from ledgerStore.ledgerStore import LedgerStore


class LedgerImpl(Ledger):

    def __init__(self, ledger_store: LedgerStore):
        super().__init__()
        self.ledger_store = ledger_store
        self.file = FileHandler(1)

    def speculate(self, prev_block_id, block_id, transactions):
        return self.ledger_store.add(prev_block_id, block_id, transactions)

    def pending_state(self, block_id):
        pass

    # Exports the branch to persistent layer
    # Discard speculate branches that fork from ancestors
    def commit(self, block_id):
        self.write_ledger_to_file(block_id)
        self.ledger_store.prune(block_id)

    # Returns the committed block from the in cache tree
    def committed_block(self, block_id):
        self.ledger_store.find(block_id)

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
