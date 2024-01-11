'''
Main application for managing interactions with multi-agent systems.
'''
import tkinter as tk
from chatdev_interface import ChatDevInterface
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Agent System Interface")
        self.geometry("800x600")
        self.chatdev_interface = ChatDevInterface(self)
        self.chatdev_interface.pack(fill=tk.BOTH, expand=True)
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()