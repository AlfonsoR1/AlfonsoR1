##############################################
#    
#   Write a program that asks the user for a
#   filename and reads the numbers from the file
#   and then calculates the average of all the
#   numbers stored in the file.
#
#   It should handle IOError exceptions that are
#   raised when the file is opened and data is read
#   from it by printing "Trouble opening file. Try again."
#   and not executing any more of the code.
#
#   It should handle any ValueError exceptions that
#   are raised when the items that are read from the file
#   are converted to a number by printing "File must have
#   only numbers. Try again." and not executing any more of the code.
#
#   Author: Alfonso Rocha
#   Date Written: 04/05/2022
#   Version: 1.0
#
#############################################

def main():
    print('Hello and welcome to the calculator program.\n'
            'This program will read your input file and see how many whole numbers\n'
            'are in the file, calculate the total, the average and then print.\n'
            'The only rule is the file must contain whole numbers.\n')
    
    # User input 
    infile = input('Please enter a text file name to open.\t')  # numbers10.txt
    # User input validation. Allows for multiple tries  
    while True:
        try:
            inputfile = open(infile,'r')
        except FileNotFoundError:
            print('Sorry you have entered a invalid file that is not found.\n'
            'Please try again.\t')
            infile = input('Please enter a text file name to open.\t')
        else:
            print('The file',infile,'was successfully located.')
            break
            
        


    # Running total and count 
    number_total = 0
    number_count = 0
    # for loop with a validation 
    for num in inputfile:
        try:
            number_total += int(num)
        except ValueError:
            print('ERROR: The file should only contain whole numbers.\n',
                  'Please correct the file before trying again.')
            exit()
        number_count += 1

        
    # Calculate a float value 
    average = number_total / number_count

    print('The file you opened contains',number_count,
          'numbers.\nYour total is',number_total,
          'which gives you a average of',format(average,'.2f')+'.')

main()

