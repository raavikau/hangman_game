import random
from hangman_img import stages
word_list = ['difficult', 'trouble', 'worthy', 'gold', 'understand', 'future', 'decision', 'motion']
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
display = []
for _ in chosen_word:
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess the letter ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):  # Check the position of letter
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:  # Check if user is wrong.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loss")

    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You Won!")
    print(stages[lives])

