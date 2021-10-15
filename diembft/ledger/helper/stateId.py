class StateId:
    def __init__(self, prev_state_id, transactions):
        self.prev_state_id = str(prev_state_id)
        self.transactions = str(transactions)

    def __repr__(self):
        return self.prev_state_id + self.transactions
