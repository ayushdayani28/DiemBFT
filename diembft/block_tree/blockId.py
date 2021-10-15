from diembft.certificates.qc import QC


class BlockId:
    def __init__(self, author, round, payload, qc: QC()):
        self.author = author
        self.round = round
        self.payload = payload
        self.id = qc.vote_info.id
        self.signatures = qc.signatures
