from tkinter import *
from tkinter import messagebox

class Session:
    def __init__(self, root, userID=None):
        self.current_user = userID
        self.root = root

    def logout(self):
        pass

def quit(inst):
    inst.root.quit()

def login(inst):
    # This function should always be referencing a "logged-out" instance

    # Check to see if user from entry exits, if so login and switch to new instance
    pass

def create_menus(inst):
    top = Menu(inst.root)
    root.config(menu=top)

    # Add user tab
    user = Menu(top, tearoff=False)
    user.add_separator()

    if inst.current_user is not None:
        # Logged in user features:

        user.add_command(label='Logout', command= lambda: inst.logout, underline=0)

        # Add Database view tab
        view_inventory = Menu(top, tearoff=False)
        view_inventory.add_separator()
        top.add_cascade(label='View Inventory', menu=view_inventory, underline=0)

        # Add Database edit tab
        edit_inventory = Menu(top, tearoff=False)
        edit_inventory.add_separator()
        top.add_cascade(label='Edit Inventory', menu=edit_inventory, underline=0)

    else:
        # This is an 'empty instance'

        login_label = Label(inst.root, text="Please Login To Continue", relief=RAISED, font=("Arial", 25))
        login_label.pack(side='top', fill=BOTH, expand=1)

        login_frame = Frame(inst.root)

        login_frame_left = Frame(login_frame)
        login_userid = Label(login_frame_left, text="Please Enter User ID: ", font=("Arial", 12))
        login_userpassword = Label(login_frame_left, text="Please Enter User Password: ", font=("Arial", 12))
        login_userid.pack(side='top', fill=BOTH, expand=1)
        login_userpassword.pack(side='top', fill=BOTH, expand=1)

        login_frame_right = Frame(login_frame)
        userid_entry = Entry(login_frame_right, font=("Arial", 12))
        userpassword_entry = Entry(login_frame_right, font=("Arial", 12), show="*")
        userid_entry.pack(side='top', fill=BOTH, expand=1, padx=40, pady=40)
        userpassword_entry.pack(side='top', fill=BOTH, expand=1, padx=40, pady=40)

        login_frame_left.pack(side='left', fill=BOTH, expand=1)
        login_frame_right.pack(side='right', fill=BOTH, expand=1)

        login_frame.pack(side='top', fill=BOTH, expand=1)

        login_button = Button(inst.root, command=lambda: login(inst),
                              text="Login", font=("Arial", 15))
        login_button.pack(side='top', fill=BOTH, expand=1, padx=40, pady=40)


    # Universal Menu(s)
    user.add_command(label='Quit', command= lambda: quit(inst), underline=0)
    top.add_cascade(label='User', menu=user, underline=0)
def create_searchpage(root):
    pass

def create_editpage(root):
    pass


# Initialize tk
root = Tk()
root.title('Persistent Inventory Management System')
root.geometry("800x600")

# App instance, by default instance is a 'logged out instance'
instance = Session(root)

# Create app menus appropriate to that instance (loggin'd in user)
create_menus(instance)


root.mainloop()
