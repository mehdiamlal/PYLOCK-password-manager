from tkinter import *
# from tkmacosx import Button

window = Tk()
window.title("PYLOCK")
window.geometry("700x600")
window.config(bg="#fff", pady=75, padx=50)
window.resizable(0, 0)

#logo image
logo_img = PhotoImage(file="../img/logo.png")
canvas = Canvas(height=114, width=200, bd=0, highlightthickness=0, bg="#fff")
canvas.create_image(100, 57, image=logo_img) #the position needs to be at the center, so we take width and hight and divide by 2
canvas.grid(row=0, column=1, columnspan=2, pady=5)

#website field
website_label = Label(text="Website:", bg="#fff", fg="#000")
website_label.grid(row=1, column=0)
website_field = Entry(bg="#fff", fg="#000", width=39, insertbackground="#000", highlightthickness=0.5, borderwidth=0.5)
website_field.grid(row=1, column=1, columnspan=2, pady=5, sticky="W")

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
pw_gen_btn = Button(text="Generate Password", highlightbackground="#fff")
pw_gen_btn.grid(row=3, column=2)

#add button
add_btn = Button(text="Add", width=36, highlightbackground="#fff")
add_btn.grid(row=4, column=1, columnspan=2, pady=5, sticky="W")


window.mainloop()