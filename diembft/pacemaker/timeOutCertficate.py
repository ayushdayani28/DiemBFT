
# TODO: Add Signatures
class TimeOutCertificate:

    def __init__(self, round: int, tmo_high_qc_rounds, signatures):
        self.round = round
        self.tmo_high_qc_rounds = tmo_high_qc_rounds
        self.tmo_signatures = signatures
