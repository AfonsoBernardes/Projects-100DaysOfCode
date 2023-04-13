alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. Shift the plain message and print
# encoded message.
def ceaser_cipher(message, shift_value, direction):
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    processed_message = ""
    for letter in message:
        if letter in alphabet:
            if direction == "ENCODE":
                letter_idx = alphabet.index(letter)
                processed_message += shifted_alphabet[letter_idx]
            elif direction == "DECODE":
                letter_idx = shifted_alphabet.index(letter)
                processed_message += alphabet[letter_idx]
        else:
            # If it's a number or symbol, simply add that.
            processed_message += letter

    print(f"The decoded message is: {processed_message}")


# This loop asks for the user to encode/decode, if input is not valid, asks again.
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").upper()
    if direction == "ENCODE" or direction == "DECODE":
        text = input("Type your message: ").upper()
        shift = int(input("Type the shift number: "))
        ceaser_cipher(message=text, shift_value=shift, direction=direction)
        break
    else:
        print("Invalid input, try again.\n")
