# CB, MW, XP, AH 7th 
import random
#Arthur- Conditionals/print statement
#Xander- incharge of conditionals in code
#Marshall- Outputting the hangman, printing the words
#Celeste- Incharge of the basic set up of the game, the base, up until the users use input

#Celeste
name = input("hello user, what is your name? ")
print(f"Hello, {name}! welcome to Hangman!!") 
#Marshall



#Marshall
# HANGMAN ART
#  +---+
#  |   |
#  O   |
# |||  |
# | |  |
#      |
#
#  +---+
#  |   |
#  O   |
# |||  |
# |    |
#      |
#
#   +---+
#  |   |
#  O   |
# |||  |
#      |
#      |
#
#  +---+
#  |   |
#  O   |
# ||   |
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

#Celeste:
word_list = ["apple","banana","orange","lemon","lime","pasta","french_toast","waffle","pancakes","cornbread","pizza","fries","noodles","ramen","sandwich","milk","cookie","rasberries","donut","brownies","garlic_bread","pineapple","rice","burrito","cheese","coconut","kiwi","bread","pringles","takis","dr_pepper","sprite","mango","watermelon","blueberries","strawberries","grapes","papaya","pomegranate","passion_fruit","cantaloupe","honeydew","broccoli","carrot","spinach","kale","zucchini","bell_peppers","cauliflower","asparagus","eggplant","cabbage","chicken_breast","steak","salmon","tuna","tofu","shrimp","turkey","lamb","yogurt","butter","cream_cheese","ice_cream","oat_milk","almond_milk","sour_cream","greek_yogurt","muffins","croissant", "jelly_beans","marshmallows","ice_cream_sandwich","fruit_snacks","trail_mix","granola_bar","popsicle","caramel","coca-cola","root_beer","lemonade","hot_chocolate","smoothie","energy_drink","apple_juice","pear","peach","plum","apricot","cherry","cranberry","dragon_fruit","nectarine","lettuce","peas","green_beans","sweet_potato","potato","beets","onions","garlic","radish","mushrooms","oatmeal","cereal","bagel","tortilla","biscuit","english_muffin","pita_bread","rice_cakes","sausage","bacon","ham","meatballs","eggs","hot_dog","roast_beef","chicken_nuggets","fish_sticks","whipped_cream","parmesan_cheese","mozzarella","cheddar_cheese","milkshake","chocolate_bar","candy_cane","gummy_bears","cupcake","cheesecake","pudding","pie","chips","nachos","crackers","orange_juice","grape_juice","cranberry_juice","chocolate_milk","bubble_tea","macaroni_and_cheese","chicken_soup","chili","casserole","lasagna","quesadilla","tacos","enchiladas","spring_rolls","sushi"]
def choose_word():
    return random.choice(word_list)

def display_word_state(word, guessed_letters):
   display_word_state

#marshall
chosen_word = choose_word()
lives=6
guessed_letters = ["a,","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#arthur
pieces = ["Head", "Body", "Left arm", "Right arm", "Left leg", "Right leg"]
next = 5
piece_number = 0
def lives_left():
    if lives > next:
        print(f"You have {lives} lives left")
    elif lives == next:
        print(f"You have {next} lives left and have just added", pieces[piece_number])
        next -= 1
        peace_number += 1
    else:
        print(f"The code is broken. Restart the game")

#Xander
while lives > 0:
    display_word_state(chosen_word, guessed_letters)
    print(f"Lives remaining: {lives_left}")

    if len(guess) != 1 or not guess.isalpha():
        print("Please input a letter.")

    if guess in guessed_letters:
        print("You have already guessed this. Please input a letter you have not guessed.")

    guessed_letters.append(guess)

    if guess in chosen_word:
         print("That is in the word!")
    if all(guessed_letters in guessed_letters for guessed_letters in chosen_word):
        print(f"congratulations! you guessed the word: {chosen_word}")
    break
else:
     print("Wrong guess!")
lives -= 1

if lives == 0:
    print(f"You ran out of lives! the chosen word was: {chosen_word}")        