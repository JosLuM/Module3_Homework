# This is the Jeu Pendu project

import sys
import random


def read_file_words():
    try:
        with open("mots_pendu.txt", 'r') as f:
            # Read the contents of the file
            content = f.read()
    except Exception as e:
        print("There is no file with words provided")
        return
    return content


def choose_word():
    word_list = read_file_words()
    words_final = word_list.replace("'", '"')
    words = words_final.strip().split('\n')
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess


def play_again():
    play = input("Do you want to play again? (yes/no): ").lower()
    return play == "yes"


def jeu_du_pendu():
    chosen_word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = display_word(chosen_word, guessed_letters)

        if guessed_word == chosen_word:
            print("Congratulations! You won!")
            print(chosen_word)
            break

        print("Current word: " + guessed_word)
        print("Tries left: " + str(tries))
        guess = get_guess(guessed_letters)

        if guess not in chosen_word:
            print("Sorry, you are wrong!")
            tries -= 1

        guessed_letters.append(guess)

    else:
        print("You lost! The word was: " + chosen_word)

    if play_again():
        jeu_du_pendu()


def main():
    jeu_du_pendu()


if __name__ == "__main__":
    main()