##############################################
#    Write a program that allows the user to enter
#   the name of an MLB baseball team and displays the
#   number of times the team has won the World Series
#   in the years from 1903 through 2009.
#   Read the file, WorldSeriesWinners.txt into a list.
#   When the user enters the team's name, the program
#   should step through the list, counting the number
#   of times the selected team appears.
#   
#   Author: Alfonso Rocha
#   Date Written: 04/06/2022 
#   Version: 1.0
#
#############################################

# CONSTANTS
WINNERS_FILE = 'WorldSeriesWinners.txt'


def main():
    # variable keeps track of wins
    win_count = 0
    # empty list 
    list_of_winners = []
    # While loop variable
    anotherTeam = 'Y'
    # Open file
    try:
        inputfile = open(WINNERS_FILE,'r')
    except IOError:
        print('The file is not found')
        exit()
    except:
        print('There was a error in the code. Goodbye')
        exit()
    # make a list of the file
    winners = inputfile.readlines()
    # variable must be global to be used in getTeam function 
     
    print('The list contains',len(winners),'winners.\n')
    # removes (\n and converts to upper case) and places list inside empty list
    for index in range(len(winners)):
        winners[index] = winners[index].rstrip('\n').upper()
        if winners[index] not in list_of_winners:
            list_of_winners.append(winners[index])
            
    # sort the empty list alphabetically 
    list_of_winners.sort()
    print('The list contains',len(list_of_winners),'winning teams.\n')
    # prints a list of winning teams 
    for team in list_of_winners:
        print(team)
    # while loop to ask user if they want to input a team more than once
    while anotherTeam == 'Y':
        user_team = input('Enter the name of a team:').upper()
        # if statement that checks users input and calculates how many wins the team has 
        if user_team not in winners:
            print('The team you entered',team,'has never won a World Series.')
        else:
            for team in winners:
                if team == user_team:
                    win_count += 1
            print('The team you entered',user_team,'has won the World Series',
              win_count,'times between 1903 and 2009.')
        anotherTeam = input('Would you like to enter another team name? Enter Y:')
        
        print('Thank you for using the program.')

   
main()
