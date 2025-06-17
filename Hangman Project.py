# Hangman: 2-Player Version

import sys

def clear_screen():
    print(chr(27) + "[27")

def draw_hangman(wrong_guesses):
    stages = [
        """

          ------
          |    |
               |
               |
               |
               |
        =========""",
        """

          ------
          |    |
          O    |
               |
               |
               |
        =========""",
       """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""

    ]
    if wrong_guesses >= len(stages):
        wrong_guesses = len(stages) - 1
    print(stages[wrong_guesses])

print("Welcome to 2-Player Hangman!")
secret_word = input("Player 1, enter a word for Player 2 to guess: ").lower()

clear_screen()

display = ["_"] * len(secret_word)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while True:
    clear_screen()
    draw_hangman(wrong_guesses)
    print("\nWord: " + " ".join(display))
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Player 2, guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please Enter a single letter.")
        print("Press Enter to contine...")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        input("Press Enter to contunue...")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1

    if "_" not in display:
        clear_screen()
        draw_hangman(wrong_guesses)
        print("\nWord: " + " ".join(display))
        print("Player 2 wins! You guessed the word!")
        break

    if wrong_guesses > max_wrong_guesses:
        clear_screen()
        draw_hangman(wrong_guesses)
        print("\nYou lose! The word was:", secret_word)
        break



