import hashlib
import secrets
import string

class CyberVault:
    def __init__(self, password):
        self.salt = secrets.token_bytes(32)
        self.key = self._derive(password)
        
    def _derive(self, password):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode(), self.salt, 200_000
        )
        
    def verify(self, password):
        candidate = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), self.salt, 200_000
        )
        return secrets.compare_digest(self.key, candidate)
        