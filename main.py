# CB, MW, XP, AH 7th 
import random
#Arthur- Conditionals/print statement
#Xander- incharge of conditionals in code
#Marshall- Outputting the hangman, printing the words
#Celeste- Incharge of the basic set up of the game, the base, up until the users use input


#Marshall
print("Welcome to Hangman!")
guessed_letter = print(input("Guess a letter.")).lower()

# HANGMAN ART
#  +---+
#  |   |
#  O   |
# /|\  |
# / \  |
#      |
#
#  +---+
#  |   |
#  O   |
# /|\  |
# /    |
#      |
#
#   +---+
#  |   |
#  O   |
# /|\  |
#      |
#      |
#
#  +---+
#  |   |
#  O   |
# /|   |
#      |
#      |
# +---+
# |   |
# O   |
# |   |
#     |
#     |


#+---+
#|   |
#O   |
#    |
#    |
#    |

#+---+
#|   |
#    |
#    |
#    |
#    |


#

#Celeste:
word_list = ["apple", "bannana", "orange", "lemon", "lime","pasta", "french toast", "waffle","pancakes","cornbread", "pizza" "fries", "noodles", "ramen", "sandwich", "milk", "cookie", "rasberries", "donut", "brownies", "garlic bread", "pineapple","rice", "burrito", "cheese", "coconut", "kiwi", "bread", "pringles", "takis", "dr pepper" "sprite","mango", "watermelon", "blueberries", "strawberries", "grapes", "papaya", "pomegranate", "passion fruit", "cantaloupe", "honeydew","broccoli", "carrots", "spinach", "kale", "zucchini", "bell peppers", "cauliflower", "asparagus", "eggplant", "cabbage","chicken breast", "beef steak", "salmon", "tuna", "tofu", "tempeh", "shrimp", "turkey", "lamb", "lentils", "yogurt", "butter", "cream cheese", "ice cream", "oat milk", "almond milk", "sour cream", "greek yogurt", "muffins", "croissant", "jelly beans", "marshmallows", "ice cream sandwich", "fruit snacks", "trail mix", "granola bar", "popsicle", "caramel","coca-cola", "root beer", "lemonade", "iced tea", "coffee", "green tea", "hot chocolate", "smoothie", "energy drink", "apple juice"]
def choose_word():
    return random.choice(word_list)

def display_word_state(word, guessed_letters):
   display_word_state


chosen_word = choose_word()
lives=6
guessed_letters = []

#arthur
peaces = ["Head", "Body", "Left arm", "Right arm", "Left leg", "Right leg"]
next = 5
peace_number = 0
def lives_left()
    if lives > next:
        print(f"you have {lives} lives left")
    else:
        print(f"you have {next} lives left and have just aded", peaces[peace_number])
        next -= 1
        peace_number += 1











#Marshall
#def play_hangman():
# """Runs the main Hangman game logic."""
# chosen_word = choose_word()
#guessed_letters = []
#lives = 6  # At least one variable
#print("Welcome to Hangman!")

    



#Xander
while lives > 0:
    display_word_state(chosen_word, guessed_letters)
    print(f"Lives remaining: {lives}")

if len(guess) != 1 or not guess.isalpha():
    print("Please input a letter.")

if guess in guessed_letters:
    print("You have already guessed this. Please input a letter you have not guessed")

guessed_letters.append(guess)

if guess in chosen_word:
    print("That is in the word!")
    if all(letters in guessed_letters for letter in chosen_word):
        print(f"congratulations! you guessed the word: {chosen_word}")
    break
else:
     print("Wrong guess!")
lives -= 1

if lives == 0:
    print("You ran out of lives! the chosen word was: {chosen_word}")        







