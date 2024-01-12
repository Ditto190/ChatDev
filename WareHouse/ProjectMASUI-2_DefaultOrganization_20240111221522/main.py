from backend import AutoGenAPI, ChatDevAPI
# Add necessary code for initializing and using the backend APIs
# Initialize the backend APIs
autogen_api = AutoGenAPI()
chatdev_api = ChatDevAPI()
# Process requests using the backend APIs
autogen_data = {}  # Replace with actual AutoGen request data
autogen_response = autogen_api.process_request(autogen_data)
chatdev_data = {}  # Replace with actual ChatDev request data
chatdev_response = chatdev_api.process_request(chatdev_data)
# Print the responses for testing
print("AutoGen Response:", autogen_response)
print("ChatDev Response:", chatdev_response)