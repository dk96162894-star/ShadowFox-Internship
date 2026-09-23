import random

# Words with hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic machine used to process data",
    "keyboard": "Used to type on a computer",
    "internet": "A worldwide network",
    "programming": "Writing instructions for a computer"
}

word, hint = random.choice(list(words.items()))

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Hangman visual stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Welcome to Hangman!")
print("Hint:", hint)

while wrong_guesses < max_wrong_guesses:

    # Display current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    print(hangman_stages[wrong_guesses])

    # Check if player has won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

else:
    print(hangman_stages[max_wrong_guesses])
    print("Game Over!")
    print("The word was:", word)