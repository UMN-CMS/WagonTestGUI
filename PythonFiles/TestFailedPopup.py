#################################################################################

import tkinter as tk
    
#################################################################################


class TestFailedPopup():
    
    #################################################

    def __init__(self, parent):
        self.test_failed_popup(parent)
    
    #################################################

    # Function to make retry or continue window if the test fails
    def test_failed_popup(self, parent):

        # Creates a popup to ask whether or not to retry the test
        self.popup = tk.Tk()
        self.popup.title("Test Failed") 
        self.popup.geometry("300x150")
        self.popup.eval("tk::PlaceWindow . center")

        # Creates frame in the new window
        frm_popup = tk.Frame(self.popup)
        frm_popup.pack()

        # Creates label in the frame
        lbl_popup = tk.Label(frm_popup, text = "The board failed a test. Would you like to retry?")
        lbl_popup.grid(column = 0, row = 0, columnspan = 2, pady = 25)

        # Creates retry and continue buttons
        btn_retry = tk.Button(
             frm_popup,
             text = "Retry", 
             relief = tk.RAISED, 
             command = lambda: self.retry_function(parent, self.previous_frame)
             ) 
        btn_retry.grid(column = 0, row = 1)

        btn_continue = tk.Button(
            frm_popup,
            text = "Continue",
            relief = tk.RAISED,
            command = lambda: self.continue_function(parent)
        )
        btn_continue.grid(column = 1, row = 1)

    #################################################
    
    # Called when the no button is pressed to destroy popup and return you to the main window
    def retry_function(self, parent):
        self.popup.destroy()

        #TODO This needs to be overhauled
        parent.go_to_next_test()
        
    #################################################

    # Called to continue on in the testing procedure
    def continue_function(self, _parent):
        self.popup.destroy()
        _parent.go_to_next_test()

    #################################################


#################################################################################