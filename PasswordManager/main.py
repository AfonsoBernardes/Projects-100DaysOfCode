from tkinter import *
from tkinter import messagebox
from random import randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)


def generate_password():
    character_list = []

    # Create list with random letters, numbers and symbols.
    for l in range(0, nr_letters):
        random_letter = LETTERS[randint(0, len(LETTERS) - 1)]
        character_list.append(random_letter)

    for s in range(0, nr_symbols):
        random_symbol = SYMBOLS[randint(0, len(SYMBOLS) - 1)]
        character_list.append(random_symbol)

    for n in range(0, nr_numbers):
        random_number = NUMBERS[randint(0, len(NUMBERS) - 1)]
        character_list.append(random_number)

    # For the list created, randomly shuffle the list.
    shuffle(character_list)
    password = ''.join(character_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_empty = len(website) == 0

    if is_empty:
        messagebox.showinfo(title="EMPTY WEBSITE FIELD", message="Please fill 'website' field in order to retrieve "
                                                                 "corresponding password.")
    else:
        try:
            # Try loading file.
            with open('password_data.json', mode="r") as password_json:
                password_data = json.load(password_json)  # Load pre-existing data.

        except FileNotFoundError as nf_message:  # File does not exist. Create it and add info.
            messagebox.showinfo(title="FILE NOT FOUND", message="No file was found. You haven't saved any passwords.")

        else:
            try:
                website_password = password_data[website]['password']
            except KeyError:
                messagebox.showinfo(title="PASSWORD NOT FOUND", message=f"No password associated with '{website}' was "
                                                                        f"found.")
            else:
                password_entry.insert(0, website_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    is_empty = len(website) == 0 or len(email) == 0 or len(password) == 0
    if is_empty:
        messagebox.showinfo(title="EMPTY FIELDS", message="Please fill all the information necessary.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details provided for this website: "
                                                              f"\nEmail: {email} "
                                                              f"\nPassword: {password} "
                                                              f"\nIs it ok to save?")

        if is_ok:
            try:
                # Try loading file.
                with open('password_data.json', mode="r") as password_json:
                    data = json.load(password_json)  # Load pre-existing data.

            except FileNotFoundError as nf_message:  # File does not exist. Create it and add info.
                print(f"{nf_message} was not found. Creating file.")
                with open('password_data.json', mode="w") as password_json:
                    json.dump(new_data, password_json, indent=4)

            else:
                # If file existed before, update already existing data with new data and save to .json file.
                data.update(new_data)
                with open('password_data.json', mode="w") as password_json:
                    json.dump(data, password_json, indent=4)

            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50, bg="black")

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

# Website entry.
website_label = Label(text="Website:", bg="black", fg="white", highlightthickness=0)
website_label.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, padx=3, pady=5)
website_entry.focus()

# Email entry.
email_label = Label(text="Email/Username:", bg="black", fg="white", highlightthickness=0)
email_label.grid(row=2, column=0)

email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2, padx=3, pady=5)
email_entry.insert(0, 'afonsobern@gmail.com')

# Password entry and button.
password_label = Label(text="Password:", bg="black", fg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = Entry(width=33, justify="left")
password_entry.grid(row=3, column=1, padx=3, pady=5)

generator_button = Button(text="Generate", width=10, highlightthickness=0, command=generate_password)
generator_button.grid(row=3, column=2)

search_button = Button(text="Search", width=10, highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=39, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=3, pady=5)

window.mainloop()
