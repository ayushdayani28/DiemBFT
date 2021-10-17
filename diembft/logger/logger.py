import logging


class Logger:

    def __init__(self, node_id: str):
        logging.basicConfig(filename=node_id+'_log.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

        self.logger = logging.getLogger(__name__)
        self.node_id = node_id

    def log_info(self, message: str):
        self.logger.log(logging.INFO, [self.node_id, message])

    def log_error(self, message: str):
        self.logger.log(logging.ERROR, [self.node_id, message])

    def log_debug(self, message: str):
        self.logger.log(logging.DEBUG, [self.node_id, message])






