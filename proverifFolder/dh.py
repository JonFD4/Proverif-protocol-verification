import random

# Define the participants
class Agent:
    def __init__(self):
        self.private_key = random.randint(1, 100)  # Generate a random private key

alice = Agent()
bob = Agent()

# Define the public parameters
p = random.randint(100, 1000)  # A large prime number
g = random.randint(1, p)  # A generator modulo p

# Define the public keys
A = (g ** alice.private_key) % p  # Alice's public key
B = (g ** bob.private_key) % p  # Bob's public key

# Alice sends her public key to Bob
received_A = A

# Bob sends his public key to Alice
received_B = B

# Alice computes the shared secret key
secret_key_alice = (received_B ** alice.private_key) % p

# Bob computes the shared secret key
secret_key_bob = (received_A ** bob.private_key) % p

# Secrecy properties
secrecy_alice = secret_key_alice == secret_key_bob
secrecy_bob = secret_key_bob == secret_key_alice

# Print the shared secret keys and secrecy properties
print("Shared secret key for Alice:", secret_key_alice)
print("Shared secret key for Bob:", secret_key_bob)
print("Secrecy property for Alice:", secrecy_alice)
print("Secrecy property for Bob:", secrecy_bob)

