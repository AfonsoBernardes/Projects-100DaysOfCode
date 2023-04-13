alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").upper()
shift = int(input("Type the shift number: "))


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. Shift the plain message and print
# encoded message.
def encrypt(plain_message, shift_value):
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    encrypted_message = ""
    for letter in plain_message:
        letter_idx = alphabet.index(letter)
        encrypted_message += shifted_alphabet[letter_idx]

    print(f"The encoded message is: {encrypted_message}")


encrypt(plain_message=text, shift_value=shift)
