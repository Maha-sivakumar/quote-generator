import random

quotes = {
    'motivation': [
        {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
        {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
        {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
        {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"}
    ],
    'success': [
        {"quote": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer"},
        {"quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
        {"quote": "The road to success and the road to failure are almost exactly the same.", "author": "Colin R. Davis"},
        {"quote": "Success is not in what you have, but who you are.", "author": "Bo Bennett"},
        {"quote": "The only place where success comes before work is in the dictionary.", "author": "Vidal Sassoon"}
    ],
    'life': [
        {"quote": "In the end, it's not the years in your life that count. It's the life in your years.", "author": "Abraham Lincoln"},
        {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
        {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
        {"quote": "Life is really simple, but we insist on making it complicated.", "author": "Confucius"},
        {"quote": "Life is either a daring adventure or nothing at all.", "author": "Helen Keller"}
    ],
    'love': [
        {"quote": "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.", "author": "Victor Hugo"},
        {"quote": "Love is composed of a single soul inhabiting two bodies.", "author": "Aristotle"},
        {"quote": "A successful marriage requires falling in love many times, always with the same person.", "author": "Mignon McLaughlin"},
        {"quote": "The best thing to hold onto in life is each other.", "author": "Audrey Hepburn"},
        {"quote": "Where there is love, there is life.", "author": "Mahatma Gandhi"}
    ],
    'friendship': [
        {"quote": "Friendship is born at that moment when one person says to another: 'What! You too? I thought I was the only one.'", "author": "C.S. Lewis"},
        {"quote": "A real friend is one who walks in when the rest of the world walks out.", "author": "Walter Winchell"},
        {"quote": "Friendship is the only cement that will ever hold the world together.", "author": "Woodrow Wilson"},
        {"quote": "A true friend is someone who is always there during the ups and downs, I'm grateful to have you as my friend.", "author": "Unknown"},
        {"quote": "A friend is someone who knows all about you and still loves you.", "author": "Elbert Hubbard"}
    ],
    'wisdom': [
        {"quote": "The only true wisdom is in knowing you know nothing.", "author": "Socrates"},
        {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
        {"quote": "Knowledge speaks, but wisdom listens.", "author": "Jimi Hendrix"},
        {"quote": "Wisdom is not a product of schooling but of the lifelong attempt to acquire it.", "author": "Albert Einstein"}
    ]
}

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
        print("Invalid input. Please try again.")

def generate_quote():
    name = get_user_input("Enter your name: ")
    print()

    print("Select a category for the quote:")
    categories = list(quotes.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")

    while True:
        category_choice = get_user_input("Enter the category number: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            break
        print("Invalid category number. Please try again.")

    random_quote = random.choice(quotes[category])
    quote = random_quote["quote"]
    author = random_quote["author"]

    formatted_quote = f"{name}, {quote} - {author}"
    print(f"\n{formatted_quote}")

generate_quote()
