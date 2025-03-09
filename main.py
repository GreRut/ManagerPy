from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    passwords_txt = open("passwords.txt", "a")
    website = website_t.get()
    passwords_txt.write(website)
    passwords_txt.write(" | ")

    email = e_username_t.get()
    passwords_txt.write(email)
    passwords_txt.write(" | ")

    password = password_t.get()
    passwords_txt.write(password)
    passwords_txt.write("\n")

    passwords_txt.close()
    website_t.delete(0, END)
    password_t.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE, highlightthickness=0)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# labels

website_l = Label(text="Website:", bg=WHITE)
website_l.grid(row=1, column=0)
e_username = Label(text="Email/Username:", bg=WHITE)
e_username.grid(row=2, column=0)
password_l = Label(text="Password:", bg=WHITE)
password_l.grid(row=3, column=0)

# entries
website_t = Entry(width=52)
website_t.grid(row=1, column=1, columnspan=2)
website_t.focus()
e_username_t = Entry(width=52)
e_username_t.grid(row=2, column=1, columnspan=2)
e_username_t.insert(0, "xxx@gmail.com")
password_t = Entry(width=34)
password_t.grid(row=3, column=1)

# buttons

g_password_button = Button(text="Generate Password")
g_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
