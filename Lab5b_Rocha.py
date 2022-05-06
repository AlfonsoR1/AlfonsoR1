
#########################################
#
#   Design and implement an application to convert
#   temperatures from Fahrenheit to Celsius or Celsius
#   to Fahrenheit.  Create a menu based application with
#   3 options, Convert Fahrenheit to Celsius, Convert Celsius
#   to Fahrenheit, and Exit.  You'll need a conditional loop and
#   a sentinel value, (For Example: X to Exit). 
#   
#     
#   Author Alfonso Rocha
#   Date Written: 03/25/2022 
#   Version: 1.0
#
#############################################

# CONSTANTS
CONVERSION_32 = 32
CEL_TO_F = 1.8
F_TO_CEL = 5/9
INTRO = 'Welcome to the Celsius and Fahrenheit conversion program.\n'

def main():
    print (INTRO)
    Menu()
    menuSelect = input('Please make a selection from the menu.\t')
    menuSelect = menuSelect.upper()
    while menuSelect != 'E':
        if menuSelect == 'C':
            convert_Celsius_To_Fahrenheit()
        elif menuSelect == 'F':
            convert_Fahrenheit_To_Celsius()
        else:
            print('You have selected an invalid menu option. Try again\n')
        Menu()
        menuSelect = input('Please make a selection from the menu.\t')
        menuSelect = menuSelect.upper()
    print('Thank you for using the program.Goodbye')
    exit()
    
def convert_Celsius_To_Fahrenheit():
    print('You have chosen to convert Celsius to Fahrenheit.\n')
    # Input Validation for fahrenheit
    while True:
        celsius = input('Enter a number value for Celsius to convert to Fahrenheit.\t')
        try:
            fahrenheit = float(celsius)*CEL_TO_F + CONVERSION_32
        except ValueError:
            print('This is not a number value.')
            continue
        else:
            print(celsius,'Celsius in Fahrenheit is',format(fahrenheit,',.2f')+'.\n')
            return 
        
def convert_Fahrenheit_To_Celsius():
    print('You have chosen to convert Fahrenheit to Celsius.\n')
    # Input Validation for celsius
    while True:
        fahrenheit = input('Enter a number value for Fahrenheit to convert to Celsius.\t')
        try:
            celsius = (float(fahrenheit)-CONVERSION_32)*F_TO_CEL
        except ValueError:
            print('This is not a number value.')
            continue
        else:
            print(fahrenheit,'Fahrenheit in Celsius is',format(celsius,',.2f')+'.\n')
            return

def Menu():
    print('-----------Menu Options--------------------')
    print('Select C to convert Celsius to Fahrenheit.')
    print('Select F to convert Fahrenheit to Celsius.')
    print('Select E to exit the program.')
    print('-'*43)


    
main()
