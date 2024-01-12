'''
This module contains the backend APIs for interacting with AutoGen and ChatDev.
'''
from autogen import AutoGen
from chatdev import ChatDev
class AutoGenAPI:
    def __init__(self):
        self.autogen = AutoGen()
    def process_request(self, data):
        """
        Process AutoGen request.
        Args:
            data: The request data received from AutoGen.
        Returns:
            The response data to be sent back to AutoGen.
        """
        # Add the logic to process the AutoGen request here
        # Implement the logic to process the AutoGen request
        response = self.autogen.process(data)
        return response
class ChatDevAPI:
    def __init__(self):
        self.chatdev = ChatDev()
    def process_request(self, data):
        """
        Process ChatDev request.
        Args:
            data: The request data received from ChatDev.
        Returns:
            The response data to be sent back to ChatDev.
        """
        # Add the logic to process the ChatDev request here
        # Implement the logic to process the ChatDev request
        response = self.chatdev.process(data)
        return response