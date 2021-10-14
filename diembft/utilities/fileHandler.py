class FileHandler:

    def __init__(self):
        self.node_id = 1 #TODO : We have to suppply the node_id
        file_name = "ledger_" + str(self.node_id) + ".txt"
        self.file = open(file_name, "a")

    def write_file(self, data):
        self.file.write(data)
