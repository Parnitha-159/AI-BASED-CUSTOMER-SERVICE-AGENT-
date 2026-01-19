print("🤖 Hello! I am your AI Customer Support Bot.")
print("Type 'exit' to end the chat.\n")

# Predefined FAQ dictionary
faq = {
    "working hours": "Our working hours are 9 AM to 6 PM, Monday to Friday.",
    "contact number": "You can contact us at +91 9843210624.",
    "refund policy": "Refunds are processed within 5 to 7 working days.",
    "location": "We are located in Chennai, India.",
    "services": "We provide software development and customer support services."
}

# Chat loop
while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "exit":
        print("Bot: Thank you for contacting us. Have a great day 😊")
        break

    # Check for matching FAQ
    found = False
    for question in faq:
        if question in user_input:
            print("Bot:", faq[question])
            found = True
            break

    # Default response
    if not found:
        print("Bot: Sorry, I didn't understand your question. Please try again.")
        