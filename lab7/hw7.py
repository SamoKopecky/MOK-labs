import rsa
import numpy as np
from hashlib import sha256
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh

from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


class Server:
    def __init__(self, df_sk):
        self.pub_key, self.secret_key = rsa.newkeys(512)
        self.dh_sk = df_sk
        self.dh_pk = self.dh_sk.public_key()
        self.client_pk = None
        self.key = None

    def sign(self, message):
        y = message + b"ACCEPT"
        return y, rsa.sign(y, self.secret_key, "SHA-1"), self.dh_pk

    def verify(self, client_dh_pk, pi):
        message = sha256(
            client_dh_pk.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
        ).digest()
        rsa.verify(message, pi, self.client_pk)
        self.key = self.dh_sk.exchange(client_dh_pk)


class Client:
    def __init__(self, df_sk, server_pk):
        self.pub_key, self.secret_key = rsa.newkeys(512)
        self.dh_sk = df_sk
        self.dh_pk = self.dh_sk.public_key()
        self.cid = np.random.randint(low=0, high=2**10)
        self.server_pk = server_pk
        self.key = None

    def hello(self):
        symmetric_alg = b"AES"
        hash_alg = b"SHA-1"
        return self.cid.to_bytes(2, "little") + symmetric_alg + hash_alg

    def verify(self, message, signature, server_dh_pk):
        # Throws error if verification fails
        rsa.verify(message, signature, self.server_pk)
        self.key = self.dh_sk.exchange(server_dh_pk)
        message = sha256(
            self.dh_pk.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
        ).digest()
        pi = rsa.sign(message, self.secret_key, "SHA-1")
        return self.dh_pk, pi


def main():
    print("Initialization, if any signature verification fails, error is thrown.")
    params = dh.generate_parameters(
        generator=2, key_size=512, backend=default_backend()
    )
    server = Server(params.generate_private_key())
    client = Client(params.generate_private_key(), server.pub_key)
    server.client_pk = client.pub_key
    print("RSA Public keys have been exchanged.")

    print("Client sends his message containing CID.")
    message = client.hello()
    print("Server signs clients message and sends his public key for key exchange")
    y, signature, server_pk = server.sign(message)
    print(
        "Client verifies servers signature, generates shared key and sends his public key together with its signature"
    )
    client_dh_pk, pi = client.verify(y, signature, server_pk)
    print("Server verifies clients signature and generates a shared key")
    server.verify(client_dh_pk, pi)
    print('Servers shared key:', server.key.hex())
    print('Clients shared key:', client.key.hex())


if __name__ == "__main__":
    main()
