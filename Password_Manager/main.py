from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passkey():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        lower_or_upper = random.randint(0, 1)
        if lower_or_upper == 0:
            password_list.append(random.choice(letters))
        else:
            password_list.append(random.choice(letters).upper())

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    gen_password = ""

    for char in password_list:
        gen_password += char
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)

    # print(f"Your password is: {gen_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_input.get()
    user_name = em_un_entry.get()
    passkey = password_entry.get()
    new_data = {
        website_data: {
            "email": user_name,
            "password": passkey,
        }
    }

    if len(website_data) == 0 or len(user_name) == 0 or len(passkey) == 0:
        messagebox.showerror(title="Incomplete data", message="Please complete the form")
    else:
        is_ok = messagebox.askokcancel(title="info", message=f"These are the details entered: \nEmail: {user_name}"
                                                             f"\nPassword: {passkey} \nIs it ok to save?")
        if is_ok:
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{website_data} | {user_name} | {passkey}\n")
            try:
                with open("data.json", "r") as data_file:
                    # json.dump(new_data, data_file, indent=4)
                    # Reading the old data
                    my_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                my_data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(my_data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def search_password():
    website_details = website_input.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            # print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website_details in data:
            messagebox.showinfo(title="Login Details", message=f"Email/User Name: {data[website_details]['email']}\n"
                                                               f"Password: {data[website_details]['password']}")
        else:
            messagebox.showinfo(title="Warning", message="The website data is not available. Please try again!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
graphic_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=graphic_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
email_user_name = Label(text="Email/Username:")
email_user_name.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

website_input = Entry(width=27)
website_input.grid(column=1, row=1)
em_un_entry = Entry(width=45)
em_un_entry.insert(0, "@mail.com")
em_un_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_passkey)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)

add_data = Button(text="Add", width=40, command=save)
add_data.grid(column=1, row=4, columnspan=2)

window.mainloop()
