import random

# Predefined word list
words = ["python", "code", "alpha", "hangman", "script"]

# Pick a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print(" Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Good guess!")
    else:
        attempts -= 1
        print(f" Wrong! {attempts} attempts left.")

    # Show word progress
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Word:", " ".join(display))

    if "_" not in display:
        print("🎉 You won! The word was:", word)
        break
else:
    print("💀 Game over! The word was:", word)
