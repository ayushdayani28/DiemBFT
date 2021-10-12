from ledger import Ledger
from ledgerStore.ledgerStore import LedgerStore


class LedgerImpl(Ledger):

    def __init__(self, ledger_store: LedgerStore):
        Ledger.__init__()
        self.ledgerStore = ledger_store

    def speculate(self, prev_block_id, block_id, transactions):
        pass

    def pending_state(self, block_id):
        pass

    def commit(self, block_id):
        pass

    def committed_block(self, block_id):
        pass
