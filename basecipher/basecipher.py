from Cryptodome.Cipher import AES
import base58
import hashlib

class BaseCipher:
    def __init__(self, key: str):
        """
        Encrypt and Decrypt with AES.MODE_CTR.
        Use Base58 for shorter output.
        :param salt: Any string, used to derive the key and nonce.
        """
        if not key:
            raise ValueError("Key must not be empty.")
        # Derive key and fixed part of nonce
        self.key = hashlib.sha256(key.encode()).digest()  # Key 32 bytes
        self.prefix_nonce = self.key[-14:]

    def encrypt(self, data: str) -> str:
        """
        Encrypt the plaintext string.
        :param data: The plaintext string to encrypt.
        :return: Base58-encoded encrypted string.
        """
        # Generate a dynamic nonce
        private_nonce = hashlib.sha256(data.encode()).digest()[-1:]
        nonce = self.prefix_nonce + private_nonce # Total: 15 bytes

        # Encrypt using CTR mode
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
        encrypted_data = cipher.encrypt(data.encode())

        # Encode encrypted data and private_nonce in Base58
        return base58.b58encode(encrypted_data + private_nonce).decode()

    def decrypt(self, data: str) -> str:
        """
        Decrypt the encrypted string.
        :param data: The Base58-encoded encrypted string.
        :return: The original plaintext string.
        """
        decoded_data = base58.b58decode(data)
        encrypted_data, private_nonce = decoded_data[:-1], decoded_data[-1:] # Extract private_nonce
        nonce = self.prefix_nonce + private_nonce
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
        return cipher.decrypt(encrypted_data).decode()


if __name__ == '__main__':
    bc = BaseCipher(key="Keep it secret")
    plaintext = "Hello world!"

    encrypted = bc.encrypt(plaintext)
    print("Encrypted:", encrypted)

    decrypted = bc.decrypt(encrypted)
    print("Decrypted:", decrypted)