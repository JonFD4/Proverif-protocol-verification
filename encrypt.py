def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        encrypted_char = chr(ord(char) + key)
        encrypted_message += encrypted_char
    return encrypted_message

# Test the encryption
message = input("Enter a message: ")
key = int(input("Enter an encryption key: "))
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)