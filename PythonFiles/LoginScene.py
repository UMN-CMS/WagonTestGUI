# importing necessary modules
import tkinter as tk


# Creates a class that is called by the GUIWindow. 
# GUIWindow instantiates an object called login_frame.
# @param parent -> passes in GUIWindow as the parent.
# @param master_window -> passes master_window as the container for everything in the class.
# @param data_holder -> passes data_holder into the class so the data_holder functions can
#       be accessed within the class.
class LoginScene(tk.Frame):
    def __init__(self, parent, master_window, data_holder):
        super().__init__(master_window, width=850, height=500)

        self.data_holder = data_holder


        

        # Creating a list of users for dropdown menu
        # Eventually need to add a way for a database to have control over this list
        User_List = [
            "Bob Johnson",
            "Spencer Higgins",
            "Amanda Holmes"
        ]

        # Creating the title for the window
        lbl_title = tk.Label(
            self, 
            text="Please Select Your Name", 
            font=('Arial', '24')
            )
        lbl_title.pack(pady=75)

        # Creating intial value in dropdown menu
        self.user_selected = tk.StringVar(self)
        self.user_selected.set("") # default value is empty

        # Creating the dropdown menu itself
        self.opt_user_dropdown = tk.OptionMenu(
            self, 
            self.user_selected, # Tells option menu to use the created initial value
            *User_List # Tells the dropdown menu to use every index in the User_List list
            ) 
        self.opt_user_dropdown.pack(pady=15)
        self.opt_user_dropdown.config(width = 20, font = ('Arial', 13))
        self.opt_user_dropdown['menu'].configure(font = ('Arial', 12))

        # Traces when the user selects an option in the dropdown menu
        # When an option is selected, it calls the show_submit_button function
        self.user_selected.trace(
            'w', 
            lambda *args: self.show_submit_button()
            )

        # Creating the submit button
        # It does not get enabled until the user selects an option menu option
        self.btn_submit = tk.Button(
            self, 
            text="Submit",
            padx = 50,
            pady = 10, 
            relief=tk.RAISED, 
            command= lambda:  self.submit_button_action(parent)
            )
        self.btn_submit.pack()
        self.btn_submit.config(state = 'disabled')


        # Creating the add user button
        self.add_user_button = tk.Button(
            self, 
            text="Add User",
            padx = 20,
            pady = 5, 
            relief=tk.RAISED, 
            command= lambda:  self.add_user_button_action(parent)
            )
        self.add_user_button.pack(pady=70)

        # Forces frame to stay the size of the main_window
        # rather than adjusting to the size of the widgets
        self.pack_propagate(0)

    # Creates the function for the submit button command
    # @params "_parent" is also a parent like "parent", but it is a different "parent",
    # passes in GUIWindow
    def submit_button_action(self, _parent):
            # Sets the user_ID in the data_holder to the selected user
        self.data_holder.user_ID = self.user_selected.get()
        current_scan_frame = _parent.get_scan_frame()
        # Changes frame to scan_frame
        _parent.set_frame(current_scan_frame)


        self.data_holder.print()

    def add_user_button_action(self, _parent):
        pass

    # A function to pack the submit button
    def show_submit_button(self):
        self.btn_submit.config(state = 'active')