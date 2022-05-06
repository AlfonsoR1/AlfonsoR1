##############################################
#    
#   Write a program that creates a directory
#   containing course numbers and the room
#   numbers of the rooms where the courses meet.
#     
#   Author: Alfonso Rocha
#   Date Written: 05/03/2022
#   Version: 1.0
#
#############################################

# CONSTANTS
INCORRECT = 'NOT FOUND. TRY AGAIN'
COURSE_NUMBERS = ['CS101','CS102','CS103','NT110','CM241']

def main():
    intro = print('Welcome to the Course Reminder Program.')
    rule =  print('Pick from the course list and the time,',
                  'room number and instructor will show.\n')
    # turns list into a string joined by commas to remove brakets 
    striplist = ','.join(COURSE_NUMBERS)
    print('Course List:',striplist)
    
    # user input
    userInput = input('\nPlease select a course from above: OR enter 0000 to exit:')
    
    # converts input to upper case 
    upperInput = userInput.upper()
    
    # Dictionaries 
    roomNumbers = {'CS101':'3004','CS102':'4501',
                  'CS103':'6755','NT110':'1244','CM241':'1411'}
    instructors = {'CS101':'Haynes','CS102':'Alvarado',
               'CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    meetingTimes = {'CS101':'8:00am','CS102':'9:00am',
               'CS103':'10:00am','NT110':'11:00am','CM241':'11:00pm'}

    #while upperInput != 0000
    while upperInput != '0000':
        try:
            print('The course selected',upperInput,'meets in room number:',roomNumbers[upperInput])
            print('The course selected',upperInput,'the instructor is:',instructors[upperInput])
            print('The course selected',upperInput,'meets at the time:',meetingTimes[upperInput])
        except KeyError:
            print(upperInput)
            print(INCORRECT)
            
        userInput = input('\nPlease select a course from above: OR enter 0000 to exit:')
        upperInput = userInput.upper()

    print('\nThank you for using the Course Reminder Program. Goodbye')
    exit()
        
main()
