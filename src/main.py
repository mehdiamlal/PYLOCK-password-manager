from re import search
from tkinter import *
from tkinter import messagebox
from random_pw_generator import *
import json

def generate_pw():
    pw = random_pw_generator()
    password_field.delete(0, "end")
    password_field.insert(0, pw)
    #copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(pw)

def fields_empty():
    """Checks if there's at least one empty field, returns True if there are."""
    if len(website_field.get()) == 0:
        return True
    elif len(username_field.get()) == 0:
        return True
    elif len(password_field.get()) == 0:
        return True
    else:
        return False

def save_data():
    """Saves data in a .csv file, and empties the fields, expet the username one.
    Shows a warning if there's an empty field."""
    if fields_empty():
        messagebox.showwarning(title="Ooops", message="Please, enter all the required data.")
    else:
        new_data = {
            website_field.get().lower().strip(" "): {
                "username": username_field.get().lower().strip(" "),
                "password": password_field.get().strip(" ")
            }
        }

        try:
            with open("../data/data.json", "r") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            with open("../data/data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            file_data.update(new_data)
            with open("../data/data.json", "w") as file:
                json.dump(file_data, file, indent=4)
        finally:
            #cleaning the fields
            website_field.delete(0, "end")
            password_field.delete(0, "end")

        messagebox.showinfo(title="Success!", message="Your password was saved successfully!")

def search_data():
    searched_website = website_field.get().lower().strip(" ")

    if len(searched_website) == 0:
        messagebox.showwarning(title="Ooops", message="Please enter a website to search related data.")
    else:
        try:
            with open("../data/data.json", "r") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Ooops", message=f"It seems like there's no {searched_website} account.")
        else:
            found = False
            for k in file_data:
                if k == searched_website:
                    found = True
                    user = file_data[k]["username"]
                    pw = file_data[k]["password"]
                    messagebox.showinfo(title="", message=f"Username: {user}\nPassword: {pw}")
                    #copy the password to clipboard
                    window.clipboard_clear()
                    window.clipboard_append(pw)
            if not found:
                messagebox.showwarning(title="Ooops", message=f"It seems like there's no {searched_website} account.")


window = Tk()
win_width = 650
win_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))
window.title("PYLOCK")
window.geometry(f"{win_width}x{win_height}+{x}+{y}")
window.config(bg="#fff", pady=75, padx=50)
window.resizable(0, 0)
# window.iconbitmap("../img/app_icon.ico")

#logo image
logo_img = PhotoImage(file="../img/logo.png")
canvas = Canvas(height=114, width=200, bd=0, highlightthickness=0, bg="#fff")
canvas.create_image(100, 57, image=logo_img) #the position needs to be at the center, so we take width and hight and divide by 2
canvas.grid(row=0, column=1, columnspan=2, pady=5)

#website field
website_label = Label(text="Website:", bg="#fff", fg="#000")
website_label.grid(row=1, column=0)
website_field = Entry(bg="#fff", fg="#000", width=21, insertbackground="#000", highlightthickness=0.5, borderwidth=0.5)
website_field.grid(row=1, column=1, pady=5, sticky="W")

#search button
search_btn = Button(text="Search", highlightbackground="#fff", width=13, command=search_data)
search_btn.grid(row=1, column=2)

#email/username field
username_label = Label(text="Email/Username:", bg="#fff", fg="#000")
username_label.grid(row=2, column=0)
username_field = Entry(bg="#fff", fg="#000", width=39, insertbackground="#000", highlightthickness=0.5, borderwidth=0.5)
username_field.grid(row=2, column=1, columnspan=2, pady=5, sticky="W")


#password field
password_label = Label(text="Password:", bg="#fff", fg="#000")
password_label.grid(row=3, column=0)
password_field = Entry(bg="#fff", fg="#000", width=21, insertbackground="#000", highlightthickness=0.5, borderwidth=0.5)
password_field.grid(row=3, column=1, pady=5, sticky="W")

#generate password button
pw_gen_btn = Button(text="Generate Password", highlightbackground="#fff", command=generate_pw)
pw_gen_btn.grid(row=3, column=2)

#add button
add_btn = Button(text="Add", width=36, highlightbackground="#fff", command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, pady=5, sticky="W")


window.mainloop()