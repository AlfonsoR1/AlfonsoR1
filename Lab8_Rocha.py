##############################################
#
#   Write a program that has two functions,
#   translate_to_english and translate_to_piglatin.
#   Piglatin has a few rules.
#   1.  If a word starts with a consonant, move
#   the first letter to the end and add the letters,
#   'ay'.  Example the word truck would become rucktay.
#   2. If a word starts with a vowel (aeiou), add the
#   letters 'yay'.
#   Example:  the word are would become areyay.
#   Ignore any punctuation in the sentence or phrase to
#   be translated and convert the sentence to all lower case
#   letters, whether translating into piglatin or english.
#     
#   Author: Alfonso Rocha
#   Date Written: 
#   Version: 1.0
#
#############################################

# CONSTANTS
VOWELS = ['a','e','i','o','u']
YAY = '-yay'
AY = '-ay'

def main():
    # Introduction 
    intro = print('Hello and welcome to the English/Piglatin program.')
    # display the menu
    menuselection()
    # User Input and loop to exit the program if X selected and keep retrying 
    user_select = input('Please make a selection from the menu:')
    user_select = user_select.upper()
    while user_select != 'X':
        if user_select == 'E':
            translate_to_english()
        elif user_select == 'P':
            translate_to_piglatin()
        else:
            print('You have selected an invalid menu option. Please try again.\n')
        menuselection()
        user_select = input('Please make a selection from the menu:')
        user_select = user_select.upper()
    print('Thank you for using the program. Goodbye')
    exit()
        
def menuselection():
    print('\nEnter E to translate from Piglatin to English.')
    print('Enter P to translate from English to Piglatin.')
    print('Enter X to exit the program.\n')
    
# Ask for user input and return 
def userinput():
    user_input = input('Please enter the statement that you would like to convert:')
    
    return user_input
    
def translate_to_english():
    print('You have chosen to translate from Piglatin to English.')
    pig_input = userinput().lower()
    # Splits elements and turns into a list
    convert2list = pig_input.split()
    # Empty list to store statement
    statement = []

    # For loop that checks the statement for vowels and translates to english
    for word in convert2list:
        if word.endswith(YAY):
            new_word = word.strip(YAY)
        else:
            new_word = word.strip(AY)
            new_word = new_word[-1] + new_word[:-1]
        statement.append(new_word)
        
    # Removes list brackets and print 
    final_statement = ' '.join(statement)
    print('\nThe piglatin statement to english:',final_statement)
        
def translate_to_piglatin():
    print('You have chosen to translate from English to Piglatin.')
    # Makes statement lowercase 
    english_input = userinput().lower()
    # Empty list to store statement
    statement = []
    # Splits elements and turns into a list
    convert2list = english_input.split()

    # For loop that checks the statement for vowels and translates to piglatin 
    for word in convert2list:
        if word[0] in VOWELS:
            new_word = word + YAY
        else:
            new_word = word[1:] + word[0] + AY
        statement.append(new_word)
            
        # Removes list brackets and print 
    final_statement = ' '.join(statement)
    print('\nThe eglish statement to piglatin:',final_statement)
    
    
main()
