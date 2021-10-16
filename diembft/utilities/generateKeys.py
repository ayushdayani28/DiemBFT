from nacl.signing import SigningKey


class GenerateKeys:

    def __init__(self):
        self.private_key = SigningKey.generate()
        self.public_key = self.private_key.verify_key

    def generate_key(self,):
        return [self.private_key, self.public_key]


