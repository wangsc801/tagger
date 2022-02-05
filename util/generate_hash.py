import hashlib


def sha1(text: str) -> str:
    sha = hashlib.sha1(text.encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts
