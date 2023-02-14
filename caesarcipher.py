from art import caesar_logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Please type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift =  shift % 26

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")

def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        if direction == "decode":
            new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    if direction == "encode":
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        print(f"The decoded text is {cipher_text}")
    else:
        print("There was an error with your input.")

# if direction == 'encode':
#     encrypt(text, shift)
# if direction == 'decode':
#     decrypt(text, shift)
caesar(text,shift, direction)