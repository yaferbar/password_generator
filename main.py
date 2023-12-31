from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adding():
    website = website_entry.get()
    email = email_entry.get()
    gen_password = password_entry.get()

    if len(website) == 0 or len(gen_password) == 0:
        messagebox.showinfo(title="Error", message="Please, dint leave any blink space")

    if len(website) != 0 and len(gen_password) != 0:
        with open("password_list.txt", "a") as file:
            file.write(f"{website} | {email} | {gen_password} \n")
            messagebox.showinfo(title="Confirmation", message="Your entry has been saved")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
'''Window'''
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

'''Canvas'''
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(row=0, column=1)

'''Labels'''
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/User name:")
email_label.grid(row=2, column=0,)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

'''# Entry'''
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')

email_entry = Entry(width=35)
email_entry.insert(0, "")
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1, sticky='EW')

'''# Buttons'''
generate_button = Button(text="Generate", width=15, command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=adding)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
