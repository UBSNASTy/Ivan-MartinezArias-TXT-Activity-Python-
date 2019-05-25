# Asks the user for the input of the name
print("Butler: Good Evening today. What is your name?")
user_name = input()  # Stores the input name into a variable

# Repeats the name that was given
print("Butler: Good Evening today,", user_name, ".")

# Stores the value 0 into x in order to add one and end the while loop
x = 0

"""
    While x = 0, it asks the user for a food input.
    Once it asks the user for the food they want, 
    the butler will ask the user if the food they
    stated was correct, inputting Y or N.
"""
while x == 0:
    # Prompts the user what food choice they would like
    print("Butler: What would you like to order?")
    user_food = input()

    # Asks the user if the order is correct or not
    print("Butler: This is your choice, correct?", user_food, "?", "\n(Input: Y/N)")
    user_correct_choice = input()

    # If "Y", the butler has received the confirmation and will go receive his order, as well
    # as incrementing the variable x to 1, which will end the while loop.
    if user_correct_choice == 'Y':
        print("Butler: Understood. I will be right back with your order,", user_name, ".")
        x += 1

    # If "N", the butler will loop back to the while loop and ask for the user input once more.
    elif user_correct_choice == 'N':
        print("Butler: My apologies,", user_name, ".")

    # If neither "Y" or "N", the butler will be confused and restart the order and loop back.
    else:
        print("Butler: My apologies, what did you say? I was not able to understand what you said.")