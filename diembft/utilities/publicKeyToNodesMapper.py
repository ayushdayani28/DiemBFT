class PublicKeyNodeMapper:

    def __init__(self, mapper):
        self.mapper = dict()
        for k, v in mapper.items():
            self.mapper[k] = v

    def get_node_public_key(self, node_id):
        return self.mapper[node_id]
