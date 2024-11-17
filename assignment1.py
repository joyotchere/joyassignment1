#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Student Name"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    ...

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
#!/usr/bin/env python3
# Author ID: JoyOtchere

from datetime import datetime  # Add this import to use datetime functions

def leap_year(year):
    # Check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(year, month):
    # Ensure year is greater than month
    if year < month:
        year, month = month, year  # Swap values if needed
    
    # Validate the month input
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Must be between 1 and 12.")
    
    # List of days in each month; index 0 is a placeholder
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year and update February
    if month == 2 and leap_year(year):
        return 29
    
    # Return days in the given month
    return days_in_month[month]

def after(date):
    # Determine the following day
    year, month, day = map(int, date.split('-'))
    day += 1
    if day > mon_max(year, month):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year:04d}-{month:02d}-{day:02d}"

# Checks if a given date is valid (in YYYY-MM-DD format)
def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Attempt to parse the date
        return True
    except ValueError:
        return False

# Given a date, returns the name of the day of the week
def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day_name_index = f % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_name_index]

# Counts weekends (Saturday and Sunday) between two dates
def day_count(start_date, end_date):
    weekends = 0
    current_date = start_date
    
    while current_date <= end_date:
        year, month, day = map(int, current_date.split('-'))
        
        # Get the day of the week
        day_name = day_of_week(year, month, day)  # Renamed variable to avoid conflict
        
        # Count weekends (Saturday or Sunday)
        if day_name == "Saturday" or day_name == "Sunday":
            weekends += 1
        
        # Move to the next day
        current_date = after(current_date)
    
    return weekends


# Test cases
if __name__ == "__main__":
    # Test the functions
    print(valid_date("2023-06-19"))  # Should return True
    print(valid_date("2023-02-29"))  # Should return False
    print(day_count("2023-06-19", "2023-12-03"))  # Should return the number of weekends
        



