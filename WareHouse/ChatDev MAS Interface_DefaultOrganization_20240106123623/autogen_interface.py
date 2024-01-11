'''
User interface for interacting with Autogen.
'''
import tkinter as tk
class AutogenInterface(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def start_chat(self):
        # Code to initiate a new chat session with Autogen
        print("Starting a new chat session with Autogen")
    def resume_chat(self):
        # Code to resume previous conversations with Autogen
        print("Resuming previous conversations with Autogen")