from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Read the data from the csv file
try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    # Here orient="records" is used to get output -> [{'French': 'partie', 'English': 'part'}...]
    # It maps column field to row field
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_background, image=canvas_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=canvas_flip_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


def is_known():
    to_learn.remove(current_card)
    data1 = pd.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Language Learning Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = PhotoImage(file="images/card_front.png")
canvas_flip_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=canvas_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
