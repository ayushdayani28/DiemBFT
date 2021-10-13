from diembft.pacemaker.timeoutInfo import TimeOutInfo
from diembft.pacemaker.timeOutCertficate import TimeOutCertificate
from diembft.block_tree.qc import QC


class TimeOutMessage:

    def __init__(self):
        self.tmo_info = TimeOutInfo()
        self.last_round_tc = TimeOutCertificate()
        self.high_commit_qc = QC()

