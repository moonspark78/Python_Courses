import hashlib
import secrets
import string

class CyberVault:
    def __init__(self, password):
        self.salt = secrets.token_bytes(32)
        self.key = self._derive(password)