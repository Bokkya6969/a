import random
import re

# Predefined rules: (regex pattern, list of possible responses)
RULES = [
    (
        r"\b(hi|hello|hey|howdy)\b",
        [
            "Hello! How can I help you today?",
            "Hey there! What's on your mind?",
            "Hi! Good to see you.",
        ],
    ),
    (
        r"how are you",
        [
            "I'm running smoothly! How are you doing?",
            "All systems operational. How about you?",
        ],
    ),
    (
        r"what is your name",
        [
            "I'm RuleBot, a simple pattern-matching assistant.",
            "You can call me RuleBot!",
        ],
    ),
    (
        r"help|what can you do",
        [
            "I can chat with you using predefined patterns! Try asking about my name, saying hello, or talking about the weather.",
        ],
    ),
    (
        r"weather",
        [
            "I don't have live sensors, but I hope it's sunny where you are!",
            "Always clear skies inside my code environment.",
        ],
    ),
    (
        r"i feel (.*)",
        [
            "Why do you feel {0}?",
            "How long have you been feeling {0}?",
        ],
    ),
    (
        r"\b(bye|exit|quit|goodbye)\b",
        [
            "Goodbye! Have a great day!",
            "See you later!",
        ],
    ),
]

# Fallback answers when no pattern matches
DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting! Tell me more.",
    "Can you say that in another way?",
]


def match_rule(user_input):
    """Matches user input against predefined regex patterns."""
    clean_input = user_input.strip().lower()

    for pattern, responses in RULES:
        match = re.search(pattern, clean_input)
        if match:
            response = random.choice(responses)
            # If pattern captures groups (like 'i feel (.*)'), fill placeholder
            if match.groups():
                return response.format(*match.groups())
            return response

    return random.choice(DEFAULT_RESPONSES)


def chat():
    """Main interaction loop."""
    print("RuleBot: Hello! Type 'bye' or 'exit' to quit.\n")

    while True:
        user_message = input("You: ")
        if not user_message.strip():
            continue

        bot_reply = match_rule(user_message)
        print(f"RuleBot: {bot_reply}")

        # Terminate if the user says goodbye
        if re.search(r"\b(bye|exit|quit|goodbye)\b", user_message.lower()):
            break


if __name__ == "__main__":
    chat()