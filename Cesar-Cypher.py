
print("inser the message")
message = input("message")
shift = 1


def cypher():
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)

