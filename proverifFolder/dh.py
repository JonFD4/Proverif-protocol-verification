
import random

# Define the public parameters
p = 23  # A large prime number
g = 5   # A generator modulo p

# Define the private keys for Alice and Bob
a = random.randint(1, p-1)  # Alice's private key
b = random.randint(1, p-1)  # Bob's private key

# Compute the public keys for Alice and Bob
A = (g ** a) % p  # Alice's public key
B = (g ** b) % p  # Bob's public key

# Alice sends her public key to Bob
# Bob sends his public key to Alice

# Compute the shared secret key for Alice and Bob
secret_key_alice = (B ** a) % p
secret_key_bob = (A ** b) % p

# Print the shared secret keys
print("Shared secret key for Alice:", secret_key_alice)
print("Shared secret key for Bob:", secret_key_bob)