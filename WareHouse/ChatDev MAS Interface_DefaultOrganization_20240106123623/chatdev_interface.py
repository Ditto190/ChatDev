'''
User interface for managing interactions with ChatDev and Autogen.
'''
import tkinter as tk
from tkinter import filedialog
from autogen_interface import AutogenInterface
class ChatDevInterface(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.autogen_interface = AutogenInterface(self)
        self.create_widgets()
    def create_widgets(self):
        self.file_button = tk.Button(self, text="Upload File", command=self.upload_file)
        self.file_button.pack()
        self.chat_button = tk.Button(self, text="New Chat", command=self.start_chat)
        self.chat_button.pack()
        self.resume_button = tk.Button(self, text="Resume Chat", command=self.resume_chat)
        self.resume_button.pack()
    def upload_file(self):
        file_path = filedialog.askopenfilename()
        # Code to handle file upload
        if file_path:
            print("File uploaded:", file_path)
    def start_chat(self):
        self.autogen_interface.start_chat()
    def resume_chat(self):
        self.autogen_interface.resume_chat()