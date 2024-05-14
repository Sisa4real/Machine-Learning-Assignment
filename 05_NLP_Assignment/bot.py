import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define keywords and corresponding responses
keyword_responses = {
    'why': "I'm sorry, I don't have the answer to that question.",
    'how': "I'm still learning how to do that myself!",
    'bye': "Goodbye! It was nice chatting with you."
}

# Definining the random responses
random_responses = [
    "Interesting!",
    "Tell me more.",
    "I'm not sure.",
    "That's a good question.",
    "I'll have to think about that.",
    "I'm sorry, I don't understand."
]

# Function to generate a response
def generate_response(input_text):
    # Tokenize the input text
    tokens = word_tokenize(input_text.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    # Check if any keyword is present in the input text
    for keyword in keyword_responses.keys():
        if keyword in lemmatized_tokens:
            return keyword_responses[keyword]
    
    # If no keyword is found, return a random response
    return random.choice(random_responses)

# Main conversation loop
print("Bot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Bot:", response)
    if 'bye' in user_input.lower():
        break
