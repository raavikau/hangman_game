## Hangman game implement in python
### Initial state
* The game initialize by randomly choose a word from the list.
* The randomly chosen word represent with the underscore(_) for each letter.
### Running State
* User guess a letter, and it is converted to lowercase to ensure case insensitivity.
* If the letter has already been guessed, inform to player.
* If the guessed letter is in chosen word, then the corresponding letter in the is revealed in correct position.
* When word is wrong then player looses a life, and current visual stage of the hangman is displayed.
### Terminal State
* When the player wins by guessing all letters of entire word.
* The player losses if they ran out of all six lives, then the game is over.
