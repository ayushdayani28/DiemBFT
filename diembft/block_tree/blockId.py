from diembft.certificates.qc import QC


class BlockId:
    def __init__(self, author, round, payload, qc: QC, client_request):
        self.author = author
        self.round = round
        self.payload = payload
        self.id = qc.vote_info.id
        self.signatures = qc.signatures
        self.client_request = client_request

    def __repr__(self):
        return self.author+str(self.round)+ ''.join(self.payload)+ str(self.id)+''.join(self.signatures)+str(self.client_request)
