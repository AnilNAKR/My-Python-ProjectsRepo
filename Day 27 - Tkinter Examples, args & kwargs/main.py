from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding around the window
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 20, "bold"))
# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=4, pady=4)


def button_got_clicked():
    # print("I got clicked")
    input_text = user_input.get()
    my_label.config(text=input_text)


# Button1
button1 = Button(text="Click Me", command=button_got_clicked)
button1.grid(column=1, row=1)


def status():
    print("I am bored")


# Button2
button2 = Button(text="New Button", command=status)
button2.grid(column=2, row=0)
# Entry
user_input = Entry(width=15)
user_input.grid(column=3, row=2)

window.mainloop()
