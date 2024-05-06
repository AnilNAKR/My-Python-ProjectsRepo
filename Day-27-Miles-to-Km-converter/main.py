from tkinter import *

window = Tk()
window.title("Miles to Kms converter")
# window.geometry("300x140")
window.config(padx=20, pady=20)

user_input = Entry(width=10, font=("Arial", 15, "normal"))
user_input.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Arial", 15, "normal"))
miles_text.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 15, "normal"))
is_equal_to.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 15, "normal"))
result.grid(column=1, row=1)

kms = Label(text="Kms", font=("Arial", 15, "normal"))
kms.grid(column=2, row=1)


def calculate_to_kms():
    output = float(user_input.get()) * 1.60934
    result.config(text=f"{output:.2f}")


button = Button(text="Calculate", command=calculate_to_kms, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

window.mainloop()
