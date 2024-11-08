class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'hello': 'Hi, how can I assist you?',
            'how are you': 'I am doing well, thank you for asking.',
            'what is your name': 'My name is SimpleChatbot.',
            'default': "I'm sorry, I can only answer simple questions like 'Hi', 'What is your name?'"
        }
    def get_response(self,user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        return self.responses['default']
    
chatbot = SimpleChatbot()
print("Chatbot: Hi! Ask me simple questions, or type 'exit' to end the conversation.")
while True:
    user_input = input("you: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye, it was nice chatting with you.")
        break
    print("chatbot:",chatbot.get_response(user_input))