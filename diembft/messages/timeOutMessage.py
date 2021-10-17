from diembft.pacemaker.timeoutInfo import TimeOutInfo
from diembft.certificates.timeOutCertficate import TimeOutCertificate
from diembft.certificates.qc import QC


class TimeOutMessage:

    def __init__(self, time_out_info: TimeOutInfo, last_round_tc: TimeOutCertificate, high_commit_qc: QC):
        self.tmo_info = time_out_info
        self.last_round_tc = last_round_tc
        self.high_commit_qc = high_commit_qc

    def __repr__(self):
        return str(self.tmo_info) + str(self.last_round_tc) + str(self.high_commit_qc)

