import logging

import nacl.hash
import nacl.encoding
from diembft.utilities.generateKeys import GenerateKeys
from diembft.utilities.publicKeyToNodesMapper import PublicKeyNodeMapper
hasher = nacl.hash.sha256


class Verifier:

    def __init__(self, mapper: dict, keys: list):
        self.keys = keys
        self.mapper = PublicKeyNodeMapper(mapper)

    @staticmethod
    def encode(message):
        message = bytes(message, 'utf-16')
        return Verifier.decode(hasher(message, encoder=nacl.encoding.HexEncoder))

    @staticmethod
    def decode(message):
        try:
            return message.decode('utf-16')
        except (UnicodeDecodeError, AttributeError):
            raise UnicodeDecodeError or AttributeError

    def sign(self, message):
        private_key, public_key = self.keys
        message = bytes(message, 'utf-16')
        return (private_key.sign(message, encoder=nacl.encoding.HexEncoder)).decode('utf-16')

    def verify(self, node_id, message):
        if not node_id or not message:
            return True
        try:
            public_key = self.mapper.get_node_public_key(node_id)
            public_key.verify(bytes(message, 'utf-16'))
            return True
        except nacl.exceptions.BadSignatureError as error:
            # TODO: Add Logs
            print(error)
            return False



