alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. Shift the plain message and print
# encoded message.
def ceaser_cipher(message, shift_value, cipher_direction):
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    processed_message = ""
    for letter in message:
        if letter in alphabet:
            if cipher_direction == "ENCODE":
                letter_idx = alphabet.index(letter)
                processed_message += shifted_alphabet[letter_idx]
            elif cipher_direction == "DECODE":
                letter_idx = shifted_alphabet.index(letter)
                processed_message += alphabet[letter_idx]
        else:
            # If it's a number or symbol, simply add that.
            processed_message += letter

    print(f"The {cipher_direction.lower()}d message is: {processed_message}")


# This loop asks for the user to encode/decode, if input is not valid, asks again.
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").upper()
    if direction == "ENCODE" or direction == "DECODE":
        text = input("Type your message: ").upper()
        shift = int(input("Type the shift number: "))
        # Any shift number can be introduced, but it only counts from 0-26.
        if shift > 26:
            shift = shift % 26
        ceaser_cipher(message=text, shift_value=shift, cipher_direction=direction)

        while True:
            restart = input("\nDo you want to restart the cipher program? ").upper()
            if restart == "NO":
                should_continue = False
                print("GOODBYE!")
                break
            elif restart == "YES":
                break
            elif restart != "YES":
                print("That answer is not valid...")
    else:
        print("Invalid input, try again.\n")
