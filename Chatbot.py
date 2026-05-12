def simple_chatbot():
    print("Chatbot: Hi! I'm a simple bot. Type 'bye' to exit.")

    while True:

        # Get user input and convert to lowercase
        user_input = input("You: ").lower()

        # Check keywords
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")

        elif "name" in user_input:
            print("Chatbot: I'm just a simple Python chatbot.")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you!")

        elif "weather" in user_input:
            print("Chatbot: I can't check real weather now.")

        elif "bye" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Start chatbot
simple_chatbot()
