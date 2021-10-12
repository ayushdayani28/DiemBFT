from diembft.ledger.ledger import Ledger


class LedgerFactory:

    def __init__(self):
        self.ledger = Ledger()

    def get_ledger(self):
        return self.ledger
