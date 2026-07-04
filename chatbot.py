from datetime import datetime
import random

print("=" * 50)
print("      SMART RULE-BASED CHATBOT")
print("=" * 50)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

user_name = ""

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? It caught a virus!",
    "Why was the computer cold? It left its Windows open!"
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and all that you are.",
    "Every day is a new opportunity to learn."
]

while True:

    user_input = input("You: ").lower().strip()

    
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    
    elif user_input.startswith("my name is"):
        user_name = user_input.replace("my name is", "").strip().title()
        print(f"Bot: Nice to meet you, {user_name}!")

    elif "what is my name" in user_input:
        if user_name:
            print(f"Bot: Your name is {user_name}.")
        else:
            print("Bot: I don't know your name yet.")

    
    elif "your name" in user_input:
        print("Bot: My name is SmartBot.")

   
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

  
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

  
    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")


    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))

   
    elif "motivate" in user_input or "quote" in user_input:
        print("Bot:", random.choice(quotes))

  
    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid calculation.")

    
    elif "weather" in user_input:
        print("Bot: Weather service is not connected yet.")

    
    elif "thanks" in user_input:
        print("Bot: You're welcome!")

    
    elif user_input == "help":
        print("\nAvailable Commands:")
        print("- hello / hi")
        print("- my name is <name>")
        print("- what is my name")
        print("- what is your name")
        print("- how are you")
        print("- time")
        print("- date")
        print("- joke")
        print("- motivate me")
        print("- calculate 10+20")
        print("- weather")
        print("- thank you")
        print("- bye\n")

    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    
    else:
        print("Bot: Sorry, I didn't understand that. Type 'help' for options.")
