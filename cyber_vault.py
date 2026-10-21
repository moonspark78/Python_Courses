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
        
def generate_password(length=24):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password))
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "!@#$%^&*" for c in password)):
            return password

vault = CyberVault("MotDePasse_Secret42!")
vault2 = CyberVault("AutreMotDePasse99!")