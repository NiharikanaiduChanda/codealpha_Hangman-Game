import random

# List of 5 predefined words
word_list = ["apple", "house", "zebra", "candy", "robot"]

# Choose a random word from the list
word_to_guess = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a list with underscores for each letter in the word
display_word = ["_" for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to make wrong guesses.\n")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[idx] = guess
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess.\n")

# Game over messages
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Sorry, you lost. The word was:", word_to_guess)
