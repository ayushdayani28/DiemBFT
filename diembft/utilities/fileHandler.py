class FileHandler:

    def __init__(self, node_id):
        self.node_id = node_id
        file_name = "ledger_" + str(node_id) + ".txt"
        self.file = open(file_name, "a")

    def write_file(self, data):
        self.file.write(data)
