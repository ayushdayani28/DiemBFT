class Message:

    def __init__(self, client_id, transactions, signature, request_id):
        self.client_id = client_id
        self.transactions = transactions
        self.signature = signature
        self.request_id = request_id


