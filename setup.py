from setuptools import setup, find_packages

setup(
    name="basecipher",
    version="1.0.0",
    description="A lightweight library for encrypting and decrypting strings with AES, producing compact Base58-encoded output.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Trần Ngọc Minh Hiếu",
    author_email="tnmhieu@gmail.com",
    url="https://github.com/tranngocminhhieu/base-cipher",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pycryptodomex",
        "base58"
    ],

    keywords="encryption aes base58 cryptography lightweight",
    license="MIT",
)