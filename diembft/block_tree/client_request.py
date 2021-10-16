class ClientRequest:
    def __init__(self, client_id, request_id):
        self.client_id = client_id
        self.request_id = request_id
    
    def __repr__(self) -> str:
        return self.client_id+self.request_id