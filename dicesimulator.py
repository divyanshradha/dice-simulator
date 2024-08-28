import random

def roll_die():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the die (or type 'exit' to quit): ")
        result = roll_die()
        print(f"You rolled a {result}!")
        
        user_input = input("Would you like to roll again? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

