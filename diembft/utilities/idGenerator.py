import nacl.hash
import nacl.encoding
hasher = nacl.hash.sha256


class IdGenerator:

    @staticmethod
    def get_id(message):
        message = bytes(message, 'utf-16')
        return hasher(message, encoder=nacl.encoding.HexEncoder)



