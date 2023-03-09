import nltk
from nltk.chat.util import Chat, reflections
import os
import json

nltk.download(
    'punkt')  # "Punkt" is a module in the Natural Language Toolkit (NLTK) library that provides a pre-trained sentence tokenizer. It is used to segment raw text into sentences based on punctuation marks such as periods, commas, and question marks. This tokenizer is particularly useful when working with natural language processing tasks such as machine translation, sentiment analysis, and information retrieval.

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
            if token.lower() == 'name':  # Check if the input contains the word "name"
                # Retrieve the user's name from the input
                user_name = ' '.join(tokens[tokens.index(token)+1:])
                coucou_data[user_name.lower()] = response.lower()  # Store the user's name and CouCou's response in the coucou_data dictionary
                with open(data_file, 'w') as f:
                    json.dump(coucou_data, f)
                return user_name  # Return the user's name so that it can be used in the response
    return None


# Define CouCou's chat function
def coucou_chat():
    # Initialize chatbot
    pairs = [
        (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
        (r'how are you?', ['I am fine, thank you.', 'I am doing well.']),
        (r'what can you do\?', ['I can talk to you, and learn new things from you!']),
        (r'what is your name\?', ['My name is CouCou!']),
        (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!'])
    ]
    chat = Chat(pairs, reflections)

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

        # If CouCou doesn't know how to respond, prompt the user for a response and learn from it
        if coucou_response == None:
            new_response = input("CouCou: I'm sorry, I don't know how to respond. What should I say? ")
            learn(user_input, new_response)
            print("CouCou: Thank you, I'll remember that.")

        # Print CouCou's response
        else:
            print("CouCou:", coucou_response)


if __name__ == "__main__":
    coucou_chat()

# Mersal Developments.
