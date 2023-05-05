# Iterate names in invited_names.txt
with open('./Input/Names/invited_names.txt', mode='r') as invited_names:
    for person_name in invited_names.readlines():
        # With each name, replace [name] in starting_letter.txt
        with open('./Input/Letters/starting_letter.txt', mode='r') as starting_letter:
            customised_letter = starting_letter.read().replace('[name]', f'{person_name.strip()}')
            # Save customised letter to file and save the letters in the folder "ReadyToSend".
            with open(f'./Output/ReadyToSend/{person_name.strip()}_Letter.txt', mode='w') as file:
                file.write(customised_letter)
