from cryptography.fernet import Fernet
import base64
import hashlib



def create_key(quantum_key):

    hash_key = hashlib.sha256(
        quantum_key.encode()
    ).digest()

    return base64.urlsafe_b64encode(
        hash_key
    )



def encrypt_message(message, quantum_key):

    key = create_key(quantum_key)

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        message.encode()
    )

    return encrypted.decode()



def decrypt_message(encrypted_message, quantum_key):

    key = create_key(quantum_key)

    cipher = Fernet(key)

    decrypted = cipher.decrypt(
        encrypted_message.encode()
    )

    return decrypted.decode()