from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
EMAIL = "maia.mlynczak@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    entry_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for l in range(nr_letters)]

    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #



def save_info():
    email = entry_email_username.get()
    password = entry_password.get()
    website = entry_website.get()

    new_data= {
        website: {"email": email,
                   "password": password

    }
    }
    if len(entry_website.get())==0 or len(entry_email_username.get())==0 or len(entry_password.get())==0:
        messagebox.showerror(title="I ❤ Darko!", message="Please do not leave any of the fields empty.")
    else:
        user_confirm = messagebox.askokcancel(title= "I ❤ Darko.", message= f' username/email = {entry_email_username.get()}\n '
                                                         f'Website: {entry_website.get()} \n'
                                                         f' Password ={entry_password.get()}\n')
        if user_confirm == True:
            try:
                with open("password_manager.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password_manager.json", "w") as file:
                    json.dump(new_data, file)
            else:

                with open("password_manager.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
            # entry_email_username.delete(0, END)

def search_data():
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            return_password = data[entry_website.get()]["password"]
            return_email = data[entry_website.get()]["email"]
            messagebox.showinfo(title="Password", message=f"Website : {entry_website.get()} \n Password : {return_password }"
                                                          f"\n email: {return_email}")
    except KeyError:
        messagebox.showerror(title= "Error", message=f"There is no '{entry_website.get()}' saved in the data base.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.config()
canvas.grid(row=0,column=1)


label_website = Label(text="Website:")
label_website.grid(row=1,column=0,sticky=EW)

entry_website = Entry()
entry_website.grid(row=1, column=1, columnspan=2,sticky=EW)
entry_website.config(width=36)
entry_website.focus()



label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0,sticky=EW)

entry_email_username = Entry(width=36)
entry_email_username.grid(row=2, column=1, columnspan=2,sticky=EW)
entry_email_username.insert(0,EMAIL)



label_password = Label(text="Password:")
label_password.grid(row=3, column=0,sticky=EW)
# label_password.config(padx=100)

entry_password = Entry()
entry_password.grid(row=3, column=1,columnspan=1,sticky=EW)

# entry_password.config(width=21)

button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3, column=2,columnspan=1,sticky=EW)
button_generate_password.config(command=pass_gen)

button_add = Button(text="Add")
button_add.grid(row=4,column=1, columnspan=2,sticky=EW)
button_add.config(width=36, command=save_info)

button_search = Button(text="Search")
button_search.grid(row=1, column=2, sticky=EW)
button_search.config(command=search_data)
window.mainloop()