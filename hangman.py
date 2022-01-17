import random
import os
from stage import stages 

print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,/
| |          (\`_.'
| |         .-`--'.
| |      * // . . \ \*
| |      *// |   | \ \*
| |     *//  | . |  \ \*
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |          || ||
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .''')

print("WELCOME TO THE HANGMAN GAME!!!!!")
lives = 6
display = []
from word_list import word_list
chosen_word = random.choice(word_list)
for dis in chosen_word:
    display.append("_")
print(display)
while "_" in display:
    guess = (input("Guess a letter: ")).lower()
    os.system('cls')
    if guess in display:
        print(f"You already guessed '{guess}' this letter")
    for let in range(len(chosen_word)):
        if chosen_word[let] == guess:
            display[let] = guess
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -=1
        if lives<=0:
            print("You lose")
            break
    print(lives)
    if lives ==6:
        print(stages[-1])  
    elif lives == 5:
        print(stages[-2])  
    elif lives == 4:
        print(stages[-3]) 
    elif lives == 3:
        print(stages[-4]) 
    elif lives == 2:
        print(stages[-5]) 
    elif lives == 1:
        print(stages[-6]) 
if "_" not in  display:
    print("CONGRATULATIONS!!!!YOU WON THE HANGMAN GAME")



