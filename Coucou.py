import nltk
from nltk.chat.util import Chat, reflections
import os
import json

# Define CouCou's responses
responses = {
    "What's your name?": "My name is CouCou.",
    "How are you?": "I'm doing well, thank you for asking.",
    "What can you do?": "I can talk to you and learn new information.",
    "What's the weather like?": "I'm sorry, I don't know the answer to that question.",
    "What's my name?": "I'm sorry, I don't know your name yet.",
}

# Define CouCou's learning data file
data_file = "coucou_data.json"
if os.path.isfile(data_file):
    with open(data_file) as f:
        coucou_data = json.load(f)
else:
    coucou_data = {}

# Define CouCou's learning function
def learn(input, response):
    tokens = nltk.word_tokenize(input)
    for token in tokens:
        if token.isalpha():
            coucou_data[token.lower()] = response.lower()
            with open(data_file, 'w') as f:
                json.dump(coucou_data, f)

# Define CouCou's chat function
def coucou_chat():
    # Initialize chatbot
    responses = nltk.chat.util.reflections
    pairs = [
        (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
        (r'how are you?', ['I am fine, thank you.', 'I am doing well.']),
        (r'what can you do\?', ['I can talk to you, and learn new things from you!']),
        (r'what is your name\?', ['My name is CouCou!']),
        (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!'])
    ]
    chat = nltk.chat.util.Chat(pairs, reflections)

    # Start conversation loop
    print("Hello! I'm CouCou.")
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ['bye', 'goodbye']:
            print("CouCou: Goodbye!")
            break

        # Get CouCou's response
        coucou_response = chat.respond(user_input)

        # Print CouCou's response
        print("CouCou:", coucou_response)


if __name__ == "__main__":
    coucou_chat()
