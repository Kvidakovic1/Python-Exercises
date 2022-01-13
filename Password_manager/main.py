from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def get_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    file = open("data.txt", "a")
    web_name = web_input.get()
    email = name_input.get()
    password_input = password_entry.get()

    if len(web_name) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="ooops", message="Please don't leave empty fields" )
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entered: \nEmail:{email}"
                                                               f"\nPassword: {password_input} \nIs this ok to save?")

        if is_ok:
            file.write(f"{web_name} | {email} | {password_input}\n")
            file.close()
            web_input.delete(0, END)
            password_entry.delete(0, END)







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200,  highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100 , image=lock_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)


info = Label(text="Email/Username:")
info.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

name_input = Entry(width=35)
name_input.grid(column=1, row=2, columnspan=2)
name_input.insert(0, "kiki11223333@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate password", command=get_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()