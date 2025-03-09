from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE, highlightthickness=0)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# labels

website = Label(text="Website:", bg=WHITE)
website.grid(row=1, column=0)
e_username = Label(text="Email/Username:", bg=WHITE)
e_username.grid(row=2, column=0)
password = Label(text="Password:", bg=WHITE)
password.grid(row=3, column=0)

# entries

website_t = Entry(width=52)
website_t.grid(row=1, column=1, columnspan=2)
e_username_t = Entry(width=52)
e_username_t.grid(row=2, column=1, columnspan=2)
password_t = Entry(width=34)
password_t.grid(row=3, column=1)

# buttons

g_password_button = Button(text="Generate Password")
g_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
