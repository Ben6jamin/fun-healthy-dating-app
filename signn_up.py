from tkinter import *
from tkinter import messagebox

# Creating a function for the sign up form
def sign_up():
    # Creating the form window
    signup_window = Tk()
    signup_window.title("Sign Up Form")

    # Creating labels for each field
    name_label = Label(signup_window, text="Name:")
    email_label = Label(signup_window, text="Email:")
    password_label = Label(signup_window, text="Password:")
    address_label = Label(signup_window, text="Address:")
    telephone_label = Label(signup_window, text="Telephone:")

    # Creating entry fields for each label
    name_entry = Entry(signup_window)
    email_entry = Entry(signup_window)
    password_entry = Entry(signup_window, show="*")
    address_entry = Entry(signup_window)
    telephone_entry = Entry(signup_window)

    # Placing labels and entry fields on the form
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    email_label.grid(row=1, column=0)
    email_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    address_label.grid(row=3, column=0)
    address_entry.grid(row=3, column=1)
    telephone_label.grid(row=4, column=0)
    telephone_entry.grid(row=4, column=1)

    # Creating a submit button
    submit_button = Button(signup_window, text="Submit", command=submit)
    submit_button.grid(row=5, column=1)

    # Creating a function for the submit button
    def submit():
        # Retrieving data from entry fields
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        address = address_entry.get()
        telephone = telephone_entry.get()

        # Displaying a message box with the entered data
        messagebox.showinfo("Entered Data", "Name: " + name + "\nEmail: " + email + "\nPassword: " + password + "\nAddress: " + address + "\nTelephone: " + telephone)

    # Running the form window#
    signup_window.mainloop()
