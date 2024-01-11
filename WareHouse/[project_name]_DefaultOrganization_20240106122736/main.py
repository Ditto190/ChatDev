'''
This is the main file that initializes the user interface and handles user interactions.
'''
import tkinter as tk
from tkinter import filedialog
from chatdev_agent import ChatDevAgent
from autogen_agent import AutogenAgent
class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.chatdev_agent = ChatDevAgent()
        self.autogen_agent = AutogenAgent()
        # Create GUI elements
        self.chat_text = tk.Text(self.root)
        self.input_text = tk.Entry(self.root)
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
        self.download_button = tk.Button(self.root, text="Download File", command=self.download_file)
        # Set up layout
        self.chat_text.pack()
        self.input_text.pack(side=tk.LEFT)
        self.send_button.pack(side=tk.LEFT)
        self.upload_button.pack(side=tk.LEFT)
        self.download_button.pack(side=tk.LEFT)
        # Bind Enter key to send_message function
        self.root.bind('<Return>', self.send_message)
        # Start the main loop
        self.root.mainloop()
    def send_message(self, event=None):
        message = self.input_text.get()
        self.chat_text.insert(tk.END, f"User: {message}\n")
        self.input_text.delete(0, tk.END)
        response = self.chatdev_agent.process_message(message)
        self.chat_text.insert(tk.END, f"ChatDev: {response}\n")
    def upload_file(self):
        file_path = filedialog.askopenfilename()
        self.chatdev_agent.upload_file(file_path)
    def download_file(self):
        file_path = filedialog.asksaveasfilename()
        self.chatdev_agent.download_file(file_path)
if __name__ == "__main__":
    ui = UserInterface()