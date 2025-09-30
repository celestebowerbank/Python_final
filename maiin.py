# Hangman Game - Group Project

# Celeste: Importing required module
import random

# Celeste: Greeting and name input
name = input("Hello user, what is your name? ")
print(f"Hello, {name}! Welcome to Hangman!!\n")

# Celeste: Word list setup
word_list = [
    "apple", "banana", "orange", "lemon", "lime", "pasta", "french_toast", "waffle", "pancakes", 
    "cornbread", "pizza", "fries", "noodles", "ramen", "sandwich", "milk", "cookie", "rasberries", 
    "donut", "brownies", "garlic_bread", "pineapple", "rice", "burrito", "cheese", "coconut", "kiwi", 
    "bread", "pringles", "takis", "dr_pepper", "sprite", "mango", "watermelon", "blueberries", 
    "strawberries", "grapes", "papaya", "pomegranate", "passion_fruit", "cantaloupe", "honeydew", 
    "broccoli", "carrot", "spinach", "kale", "zucchini", "bell_peppers", "cauliflower", "asparagus", 
    "eggplant", "cabbage", "chicken_breast", "steak", "salmon", "tuna", "tofu", "shrimp", "turkey", 
    "lamb", "yogurt", "butter", "cream_cheese", "ice_cream", "oat_milk", "almond_milk", "sour_cream", 
    "greek_yogurt", "muffins", "croissant", "jelly_beans", "marshmallows", "ice_cream_sandwich", 
    "fruit_snacks", "trail_mix", "granola_bar", "popsicle", "caramel", "coca-cola", "root_beer", 
    "lemonade", "hot_chocolate", "smoothie", "energy_drink", "apple_juice", "pear", "peach", "plum", 
    "apricot", "cherry", "cranberry", "dragon_fruit", "nectarine", "lettuce", "peas", "green_beans", 
    "sweet_potato", "potato", "beets", "onions", "garlic", "radish", "mushrooms", "oatmeal", "cereal", 
    "bagel", "tortilla", "biscuit", "english_muffin", "pita_bread", "rice_cakes", "sausage", "bacon", 
    "ham", "meatballs", "eggs", "hot_dog"
]

# Marshall: Hangman ASCII Art for each life
hangman_art = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
   ||   |
        |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
   |||  |
        |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
   |||  |
   |    |
        |
    =====''',
    '''
    +---+
    |   |
    O   |
   |||  |
   | |  |
        |
    ====='''
]

# Xander: Game logic and conditional handling
chosen_word = random.choice(word_list)
guessed_letters = []
lives = len(hangman_art) - 1
display = ["_" if letter != "_" else "_" for letter in chosen_word]

# Game loop
while lives > 0 and "_" in display:
    print(hangman_art[len(hangman_art) - 1 - lives])
    print("\nWord: ", " ".join(display))
    print("Guessed letters: ", ", ".join(guessed_letters))

    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print("Correct!\n")
    else:
        lives -= 1
        print("Wrong guess!\n")

# Arthur: Final output based on game result
if "_" not in display:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print(hangman_art[-1])
    print("You lost! The word was:", chosen_word)