data = {
    "hi": "👋 Hi there! I'm your friendly chatbot, ready to assist you!",
    "hello": "🌟 Hello! How can I brighten your day today?",
    "what is your name": "🤖 I'm just a chatbot, but you can call me ChatBot!",
    "where are you from": "🌐 I'm from the digital realm, always here to chat with you!",
    "how are you": "😊 I'm just a chatbot, but I'm excited to help you!",
    "do you have any hobbies or interests?": "💬 My hobby is chatting with wonderful people like you!",
    "what did you eat today?": "🍽️ I don't eat, but I can help you discover delicious recipes!",
    "what's your favorite color?": "🎨 I don't have personal preferences, but I love all colors equally!",
    "do you enjoy listening to music?": "🎶 I can't listen to music, but I can chat about your favorite tunes!",
    "bye": "👋 Bye! Take care and have an amazing day ahead!",
}

def get_response(user_input):
    user_input = user_input.lower()  # Normalize input to lowercase
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "🤔 I'm sorry, I didn't quite catch that. Could you please rephrase?"

print("Chatbot: 🌈 Hi! I'm your virtual assistant, here to help you!")

while True:
    user_input = input("Me: ")
    if user_input.lower() == 'bye':
        print("Chatbot: 🌟 Goodbye! Wishing you a fantastic day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
