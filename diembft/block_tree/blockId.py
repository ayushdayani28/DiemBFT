from diembft.certificates.qc import QC


class BlockId:
    def __init__(self, author, round, payload, qc: QC):
        self.author = author
        self.round = round
        self.payload = payload
        self.id = qc.vote_info.id
        self.signatures = qc.signatures

    def __repr__(self):
        return self.author+str(self.round)+self.payload+ str(self.id)+str(self.signatures)
