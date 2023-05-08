from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
df_words_to_learn = pd.DataFrame()

# Get data from CSV file. If there are words to learn, upload from that file.
try:
    df_words_to_learn = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df_words_to_learn = pd.read_csv("./data/french_words.csv")
finally:
    words_to_learn = df_words_to_learn.to_dict(orient="records")
    original_language = df_words_to_learn.columns[0]
    translated_language = df_words_to_learn.columns[1]


def generate_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(words_to_learn)
    original_word = current_card[original_language]

    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text=original_language)
    canvas.itemconfig(card_word, text=original_word)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    translated_word = current_card[translated_language]
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text=translated_language)
    canvas.itemconfig(card_word, text=translated_word)


def is_known():
    # If user knows the word, remove card from words_to_learn
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv(path_or_buf="./data/words_to_learn.csv", index=False)
    generate_card()


# UI Setup
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 270, text="", font=("Ariel", 60, "bold"))
generate_card()

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
