import random
from WordHangMan import word_list

logo = ''' 
 _                                             
| |  Welcome to...                                          
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_the_game = False
lives = 6


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Your solution is {chosen_word}.')
#

display = []

for _ in range(word_length):
    display += "_"

while not end_the_game:
    guess = input(f"Guess a letter: ").lower()

    if guess in display:
        print(f"You`re already guessed '{guess}' ")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            print("Nice job, keep going.")

    if guess not in chosen_word:
        print(f"You`re guessed {guess}, that`s not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_the_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("Good job, you did all the letters.")
        end_of_game = True
        print("You won.")
    print(stages[lives])
