class Message:

    def __init__(self, client_id, transactions, signature):
        self.client_id = client_id
        self.transactions = transactions
        self.signature = signature


