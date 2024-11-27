import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_word(word):
    print(word, end='', flush=True)
    time.sleep(1)
    clear_screen()

def generate_word(difficulty, used_words):
    if difficulty < 5:
        words = ['hello', 'worldx', 'python', 'star', 'fine', 'comeon', 'welcome', 'flight', 'fight', 'mango']
    elif difficulty < 10:
        words = ['hacker', 'sensor', 'ducati', 'lamborghini', 'bugatti']
    elif difficulty < 15:
        words = ['elephant', 'giraffe', 'monkey', 'zebra', 'lion']
    elif difficulty < 20:
        words = ['programming', 'algorithm', 'variable', 'function', 'python']
    elif difficulty < 35:
        words = ['dangerous', 'pathetic', 'fightclub', 'kawasaki', 'ironrod']
    elif difficulty < 40:
        words = ['titanoboa', 'kakarot', 'megalodon', 'leviathan', 'kratos']
    elif difficulty < 45:
        words = ['helixnebula', 'andromeda', 'phoenix-a', 'seamounts', 'landlord']
    else:
        words = ['encyclopedia', 'university', 'extraterrestrial', 'parliament', 'xylophone']

    available_words = [word for word in words if word not in used_words]
    if not available_words:  # If all words are used, reset the used words list
        used_words.clear()
        available_words = words
    
    chosen_word = random.choice(available_words)
    used_words.add(chosen_word)
    return chosen_word

def main():
    while True:
        level = 1
        last_completed_level = 0
        used_words = set()
        while level <= 50:
            difficulty = min(level, 50)  # Limit difficulty to 50
            word = generate_word(difficulty, used_words)
            
            clear_screen()
            print(f"Level: {level}")
            display_word(word)

            user_input = input("Type the word you saw: ")

            if user_input.lower() == word:
                print("Correct! You typed the word correctly.")
                level += 1
            else:
                print("Incorrect! The correct word was:", word)
                break

        if level > 50:
            last_completed_level = 50
            print("Congratulations! You completed all levels.")
        else:
            last_completed_level = level - 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print(f"Thank you for playing! You completed {last_completed_level} level.")
            break

if __name__ == "__main__":
    main()
