class Block:

    def __init__(self, author, round, transactions, high_qc, id, client_request):
        self.author = author
        self.round = round
        self.payload = transactions
        self.qc = high_qc
        self.id = id
        self.client_request = client_request
