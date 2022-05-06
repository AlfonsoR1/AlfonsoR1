##############################################
#    
#   Write a Boolean function named is_prime which
#   takes an integer as an argument and returns
#   true if the argument is a prime number, or
#   false otherwise. Use the function in a
#   program that prompts the user to enter a number
#   and then prints whether the number is prime.
#   Now using your new function, write a program that
#   asks the user for a range of numbers with a start
#   and end point and list all of the numbers that are
#   prime numbers in that range.
#     
#   Author: Alfonso Rocha
#   Date Written: 03/23/2022 
#   Version: 1.0
#
#############################################

import math

#CONSTANTS
INTRO = print("Welcome the prime number verification program.","\n"
             "This program will take two numbers inputted and","\n"
             'verifiy the numbers are prime within the range.',"\n"
              'Rule #1:The starting number must be smaller than the ending number.','\n')
PRIME_2 = 2
PRIME_3 = 3



def main():
    print(INTRO)
    # User input for first number  
    startNum = input('Please enter a positive starting number.\t')
    # User input for second number 
    endNum = input('Please enter a positive ending number.\t')
    
    # Input Validation for first number
    while startNum != '':
        if not isValid(startNum):
            print('ERROR: You did not enter a positive integer.')
            startNum = input('Please enter a positive starting number.\t')
        else:
            break
    intNumStart = int(startNum)
    
    # Input Validation for second number
    while endNum != '':
        if not isValid(endNum):
            print('ERROR: You did not enter a positive integer.')
            endNum = input('Please enter a positive ending number.\t')
        else:
            break
    intNumEnd = int(endNum)

    if intNumStart >= intNumEnd:
        print('Error: The starting number must be smaller than the ending number.')
    else:
        for num in range(intNumStart,intNumEnd+1):
            if is_prime(num):
                print('The number',num,'is a prime number.')
    
def isValid(n):
    if n.isdigit():
        return True
    else:
        return False
        
def is_prime(number):
    if number <= 1: # checks for negative numbers and 1 is not prime 
        return False
    if number == PRIME_2 or number == PRIME_3: # if number is 2 or 3 is prime
        return True
    elif number%2 == 0: # if it's divisible by 2 otherwise, it isn't prime
        return False 
    else:
        for i in range(3, int(math.sqrt(number))+1, 2):
            if number%i == 0:
                return False
        return True

main()
