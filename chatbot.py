def chatbot_response(user_input):
    # Convert input to lowercase to match rules easily
    user_input = user_input.lower().strip()
    
    # Rule-based matching using if-elif statements
    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def run_chatbot():
    print("Welcome to the Rule-Based Chatbot!")
    print("Type something to start chatting (type 'bye' to exit).\n")
    
    # Loop to keep the conversation going
    while True:
        # Get user input
        user_message = input("You: ")
        
        # Get response using our function
        reply = chatbot_response(user_message)
        
        # Print the bot's reply
        print(f"Bot: {reply}")
        
        # Exit condition if the user says goodbye
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    run_chatbot()