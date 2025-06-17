import datetime #import the module for datetime
from datetime import timedelta #import modules for calculating a future date with amount of days 


def display_current_datetime(): # defining function to display current datetime
    current_date = datetime.datetime.now()
    return current_date



def calculate_future_date(): #defining function to calculate future date using timedelta
    a = display_current_datetime() #initializing the variable of current time to a
    b = a.strftime("%Y-%m-%d %H:%M:%S") #formating the currentime to display yyyy-mm-d H:M:S without the milliseconds
    print(f'Current date and time: {b}') # print the current date
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = a + timedelta(days=number_of_days)
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}') #print future date with appropriate formatting

calculate_future_date()
