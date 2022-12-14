# Write a function named add_time that takes in
# two required parameters and one optional parameter:

# * a start time in the 12-hour clock format (ending in AM or PM)
# * a duration time that indicates the number of hours and minutes
# * (optional) a starting day of the week, case insensitive

# The function should add the duration time to the start
# time and return the result.

# Do not import any Python libraries. Assume that the start times
# are valid times. The minutes in the duration time will be a whole
# number less than 60, but the hour can be any whole number.

from unittest import result

def add_time(start, duration, day_week = ''):
    # Initialize variables
    new_time = ''

    # Split the inputs
    start = start.split()
    duration = duration.split(':')
    # The structure of the time input obligues to divide it
    start_time = start[0].split(':')

    # I am going to divide the process: add minutes and hours
    # both functions results are going to be processed later
    result_hour = add_hours(start_time[0], duration[0])
    result_minutes = add_minutes(start_time[1], duration[1])

    # The variables contain 'raw' results
    # Functions return one list each one
    # process_minutes
    # 0: result in 60 minutes format
    # 1: hours to add
    result_minutes = process_minutes(result_minutes)

    # process_hours
    # 0: result in 12 hour format
    # 1: how many cycles of 12 hours have the result
    result_time = process_hours(result_hour, result_minutes[1])

    # print(result_minutes)
    # print(result_time)
    # print(str(result_time[0]) + ':' + str(result_minutes[0]))

    # print(result_minutes[0], result_time, start[1])

    # Takes the result and formats it
    new_time = format_result(result_minutes[0], result_time[0], result_time[1], start[1], day_week)

    return new_time

# This function checks the results and adjusts it to the desired final output
def format_result(minutes, hour, cycles, day_period, day_week):
    # Declare initial variables
    number_days = 0
    l_day_week = False

    # If variable has a value, correct it and assign value to the variable
    # (capitalize only the first letter)
    if len(day_week) > 0:
        l_day_week = True
        day_week = day_week[0].upper() + day_week[1:].lower()

    # Add hour and colon
    result = str(hour) + ':'

    # To add minutes first it is necessary check if the number is < 10 to add a zero
    if minutes < 10:
        result += '0'

    result += str(minutes)

    # Add an space before day period
    result += ' '

    # If there is no cycle, return the result as it is
    # The one line if is just a fancy solution
    # To sum up, if the paraneter is sent, we add the day of the week
    if cycles == 0:
        result += day_period + (', ' + day_week if l_day_week else '')
        return result

    # Check the cycles to define the day period (AM or PM)
    # Hint: the text period only changes if the number of cycles is odd
    if cycles % 2 == 1:
        if day_period == 'AM':
            result += 'PM'
        elif day_period == 'PM':
            result += 'AM'
    else:
        result += day_period

    # If the result will be the next day, it should show (next day) after the time.
    # If the result will be more than one day later, it should show (n days later)
    # after the time, where "n" is the number of days later.

    # Hint: Depending on the period, days are going to be added
    # Cycles move in AM-PM through time, so we have a pattern!
    # if it is PM, next period adds a day, in consequence, odds numbers add a day
    # if it is AM, two periods add a day, in consequence, even numbers add a day

    # Next day cases:
    # In PM case, one and two cycles show next day
    if day_period == 'PM':
        if cycles == 1 or cycles == 2:
            result += ', ' + get_day_week(day_week, 1) if l_day_week else ''
            result += ' (next day)'
            return result

    # In AM case, two and three cycles show next day
    if day_period == 'AM':
        if cycles == 2 or cycles == 3:
            result += ', ' + get_day_week(day_week, 1) if l_day_week else ''
            result += ' (next day)'
            return result

    # n days later cases
    # In both cases we have to do an integer division by 2 to get the number of days
    number_days = cycles // 2

    # However, in PM case, check the remainder
    # If there is a remainder, the number is odd.
    # So, check it and add one if it exists
    if day_period == 'PM':
        number_days += cycles % 2 > 0

    result += ', ' + get_day_week(day_week, number_days) if l_day_week else ''

    # Add text to the result (if it is necessary)
    if number_days > 0:
        result += ' (' + str(number_days) + ' days later)'

    return result

# Returns the day of the week given the day and number of days to add
def get_day_week(day, add):
    # Helps me to process the day and its number
    days_week = {'Sunday' : 0, 'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4,
                'Friday' : 5, 'Saturday' : 6}
    lst_days_week = list(days_week)

    # Add the number of the day and days
    real_day = days_week[day] + add

    # The result is above 7 so a trick is used
    # Get the value through remainder
    # This is the real day of week
    real_day = real_day % 7

    # Get the day of the week from the list
    return lst_days_week[real_day]

# Add the hours of the parameters of the add_time function
def add_hours(start_hour, duration_hour):
    # Convert parameters to int
    start_hour = int(start_hour)
    duration_hour = int(duration_hour)

    # Retuns the addition of the parameters
    return start_hour + duration_hour

# Add the minutes of the parameters of the add_time function
def add_minutes(start_minutes, duration_minutes):
    # Convert parameters to int
    start_minutes = int(start_minutes)
    duration_minutes = int(duration_minutes)

    # Retuns the addition of the parameters
    return start_minutes + duration_minutes

# Process result of add_minutes function
def process_minutes(result_minutes):
    # Initialize variables
    # minutes has the real time in minutes
    # hours_add has the hours to add to the main hour
    minutes = 0
    hours_add = 0

    # Check how many hours we have to add to the final result
    hours_add = result_minutes // 60
    # Check the real minutes of the result
    minutes = result_minutes % 60

    return [minutes, hours_add]

# Process result of add_hours function
def process_hours(result_hour, hours_add):
    # Initialize variables
    # hours has the real time in hours
    # cycles has 12-hour cycle to add to the main result
    hours = 0
    cycles = 0

    # Add the hours got in process_minutes function
    result_hour += hours_add

    # Check how many cycles of 12 hours we have
    cycles = result_hour // 12
    # Check the real hours of the result
    hours = result_hour % 12
    # Zero does not exists in terms of hours
    if hours == 0:
        hours = 12

    return [hours, cycles]
