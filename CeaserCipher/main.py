alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. Shift the plain message and print
# encoded message.
def encrypt(plain_message, shift_value):
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    encrypted_message = ""
    for letter in plain_message:
        # If it's a number or symbol, simply add that.
        if letter in alphabet:
            letter_idx = alphabet.index(letter)
            encrypted_message += shifted_alphabet[letter_idx]
        else:
            encrypted_message += letter

    print(f"The encoded message is: {encrypted_message}")


def decrypt(encrypted_message, shift_value):
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    decrypted_message = ""
    for letter in encrypted_message:
        # If it's a number or symbol, simply add that.
        if letter in alphabet:
            letter_idx = shifted_alphabet.index(letter)
            decrypted_message += alphabet[letter_idx]
        else:
            decrypted_message += letter

    print(f"The decoded message is: {decrypted_message}")


# This loop asks for the user to encode/decode, if input is not valid, asks again.
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").upper()
    if direction == "ENCODE":
        text = input("Type your message: ").upper()
        shift = int(input("Type the shift number: "))
        encrypt(plain_message=text, shift_value=shift)
        break
    elif direction == "DECODE":
        text = input("Type your message: ").upper()
        shift = int(input("Type the shift number: "))
        decrypt(encrypted_message=text, shift_value=shift)
        break
    else:
        print("Invalid input, try again.\n")
