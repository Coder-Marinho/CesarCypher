
print("inser the message")
message = input("message")
shift = input("enter with the key of cypher")

def cypher():
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char  # Mantém espaços, pontuação etc.
    return encrypted

encrypted_message = cypher(message, shift)
print("Encrypted message:", encrypted_message)