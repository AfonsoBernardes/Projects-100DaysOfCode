from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password = ""
    character_list = []
    number_characters = nr_letters + nr_symbols + nr_numbers

    # Create list with random letters, numbers and symbols.
    for l in range(0, nr_letters):
        random_letter = LETTERS[random.randint(0, len(LETTERS) - 1)]
        character_list.append(random_letter)

    for s in range(0, nr_symbols):
        random_symbol = SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        character_list.append(random_symbol)

    for n in range(0, nr_numbers):
        random_number = NUMBERS[random.randint(0, len(NUMBERS) - 1)]
        character_list.append(random_number)

    # For the list created, randomly shuffle the list.
    random.shuffle(character_list)
    password = ''.join(character_list)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_empty = len(website) == 0 or len(email) == 0 or len(password) == 0

    if is_empty:
        messagebox.showinfo(title="EMPTY FIELDS", message="Please fill all the information necessary.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details provided for this website: "
                                                              f"\nEmail: {email} "
                                                              f"\nPassword: {password} "
                                                              f"\nIs it ok to save?")

        if is_ok:
            with open('passwords.txt', mode="a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")

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

website_entry = Entry(width=46)
website_entry.grid(row=1, column=1, columnspan=2, padx=3, pady=5)
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

add_button = Button(text="Add", width=39, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=3, pady=5)

window.mainloop()
