import qc as QC

class Block:
    def __init__(self):
        self.author = ''
        self.round = 0
        self.payload = ''
        self.qc = QC()
        self.id = ''
