class Block:

    def __init__(self, author, round, transactions, high_qc, id):
        self.author = author
        self.round = round
        self.payload = transactions
        self.qc: qc = high_qc
        self.id = id
