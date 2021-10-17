class Message:

    def __init__(self, transactions, signature, client_request):
        self.transactions = transactions
        self.signature = signature
        self.client_request = client_request


