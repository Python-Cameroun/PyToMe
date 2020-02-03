import hashlib
import random
from flask import session
from itsdangerous import URLSafeSerializer

secret_key = "98411853541737966953"
serializer = URLSafeSerializer(secret_key)


def encrypt(chaine):
    """
    Encrypts a string
    """
    return serializer.dumps(chaine)


def decrypt(chaine):
    """
    Decrypts the string that has been encrypted
    """
    return serializer.loads(chaine)


def random_token():
    """
    Returns a token of 16 characters among those present in "elements".
    """
    elements = ["1", "3", "4211531813", "?", "F", "@", "+", "ab23cd#$",
    "f.", "d", "3629397455", "0", "O", "TytxzQ", "*", "A", "cx", "v", "des",
    "FvvT3MGWbc"]
    element = random.sample(elements, 16)
    token = "".join(element)
    return token


def generate_token():
    """
    Creates a "_csrf_token" that will be embedded in the form and
    returned at each session.
    """
    if "_csrf_token" not in session:
        session["_csrf_token"] = random_token()
    return session["_csrf_token"]
