from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# Password entry and button.
password_label = Label(text="Password:", bg="black", fg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = Entry(width=33, justify="left")
password_entry.grid(row=3, column=1, padx=3, pady=5)

generator_button = Button(text="Generate", width=10, highlightthickness=0)
generator_button.grid(row=3, column=2)

add_button = Button(text="Add", width=39, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2, padx=3, pady=5)

window.mainloop()
