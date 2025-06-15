class simpleChatbot:
    def __init__ (self):
        self.responses={
            'hello':'hi! how are you',
            'hi':'hello! how are you',
            'how are you':'i am good, thanks',
            'what is your name':'my name is simple chatbot',
            'default':'sorry,i am a simple chatbot i can answer only simple question!',
        }
    def get_response(self,user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return self.responses['default']
chatbot = simpleChatbot()
print('chatbot: hi ask me some simple question or type exit to end the conversation')
while True:
    user_input = input('you: ')
    if user_input.lower()=='exit':
        print('chatbot: good bye...')
        break
    print('chatbot: ',chatbot.get_response(user_input))
    
