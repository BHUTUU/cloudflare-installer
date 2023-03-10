from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# create a new chatbot instance
chatbot = ChatBot(name="Mybot")

# create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# train the chatbot using sample conversations
trainer.train([
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing great.",
    "That's good to hear.",
    "Thank you",
    "You're welcome."
])

# test the chatbot
response = chatbot.get_response("Hello")
print(response)
