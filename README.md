# Base Cipher

Base Cipher is a lightweight Python library for encryption and decryption, designed for the specific purpose of obfuscating original data by securely encrypting strings. Key highlights include:
- **Salt support**: Derive encryption keys securely using a user-defined salt.
- **Compact output**: Produces short, Base58-encoded results ideal for sharing, storing or reading (does not contain special characters).
- **Strong security**: Implements AES encryption with robust key derivation.

With its simplicity and focus on efficiency, Base Cipher is ideal for applications where you need to hide sensitive data in a compact and secure way.

## Installation

Install the library directly from GitHub using the following command:
```commandline
pip install git+https://github.com/tranngocminhhieu/base-cipher.git
```

## Usage

Encrypt and decrypt text with ease using the BaseCipher class:
```python
from basecipher import BaseCipher

# Initialize with a secret salt
bc = BaseCipher(key="Keep it secret")
plaintext = "Hello world!"

# Encrypt the plaintext
encrypted = bc.encrypt(plaintext) # Output: EVxbw6A5g7y2QajoLM

# Decrypt the encrypted text
decrypted = bc.decrypt(encrypted) # Output: Hello world!
```

---
This library is open-sourced under the MIT License. Contributions and feedback are welcome!