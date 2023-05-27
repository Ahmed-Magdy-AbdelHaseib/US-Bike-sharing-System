import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

## Frist Function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    
    Cities = ['chicago', 'new york city', 'washington']
    Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    Days = ['all', 'monday', 'tuesday', 'wednesday',
            'thrusday', 'friday', 'saturday', 'sunday']

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input(
        "Please! Enter the city (chicago, new york city, washington)\n>>> ").lower()
        
        if city in Cities:
            break
        else:
            print("please! Enter a valid city")
    while True:
        filtering = input("Would you like to filter the data by \"month\" or \"day\" or \"both\" \
---> enter \"none\" to skipe filtering\n>>> ").lower()
        if filtering == 'none':
            month = 'all'
            day = 'all'
            break
        elif filtering == 'month':
            day = "all"
        # get user input for month (all, january, february, ... , june)
            while True:
                month = input("Please! Enter the month (all, january, february, ... , june) ---> enter \
\"all\" to select the all months\n>>> ").lower()

                if month in Months:
                    break
                else:
                    print("please! Enter a valid Month")
            break
        elif filtering == 'day':
            month = "all"
            # get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day = input("Please! Enter the day ('all', 'monday', 'tuesday', '........', 'sunday') \
---> enter \"all\" to select the all days\n>>> ").lower()

                if day in Days:
                    break
                else:
                    print("please! Enter a valid day")
            break
        elif filtering == 'both':
            while True:
                month = input("Please! Enter the month (all, january, february, ... , june) ---> enter \
\"all\" to select the all months\n>>> ").lower()

                if month in Months:
                    break
                else:
                    print("please! Enter a valid Month")

            while True:
                day = input("Please! Enter the day ('all', 'monday', 'tuesday', '........', 'sunday') \
---> enter \"all\" to select the all days\n>>> ").lower()

                if day in Days:
                    break
                else:
                    print("please! Enter a valid day")
            break
        else:
            print("please Enter a valid value")

    print('-'*40)
    return city, month, day
# ===============================================================================

## The Loading Data function
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    data_file = pd.read_csv(CITY_DATA[city])
    # convert the data type of "Start Time" colunm
    data_file["Start Time"] = pd.to_datetime(data_file["Start Time"])
    # creat "months" and "Days" and "hours" colunms
    data_file["months"] = data_file["Start Time"].dt.month_name()
    data_file["day of week"] = data_file["Start Time"].dt.day_name()
    data_file['Hours'] = data_file["Start Time"].dt.hour
    # filter by month
    if month != 'all':
        data_file = data_file[data_file['months'] == month.title()]
    
    # filter by day
    if day != 'all':
        data_file = data_file[data_file['day of week'] == day.title()]


    return data_file
## =================================================================================
# The time stats function
def time_stats(data_file,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if month == 'all' and day == 'all':
        #  display the most common month
        common_month = data_file['months'].mode()[0]
        print("The most common month is ",common_month)
        print('-'*40)
        #  display the most common day of week
        common_day = data_file['day of week'].mode()[0]
        print("The most common day is ",common_day)
        print('-'*40)
        #  display the most common start hour
        common_hour = data_file['Hours'].mode()[0]
        print("The most common hour is ",common_hour)
        print('-'*40)
    elif month != "all" and day != 'all':
        #  display the most common start hour
        common_hour = data_file['Hours'].mode()[0]
        print("The most common hour is ",common_hour)
        print('-'*40)
    elif month != "all" and day == 'all':
        #  display the most common day of week
        common_day = data_file['day of week'].mode()[0]
        print("The most common day is ",common_day)
        print('-'*40)
        #  display the most common start hour
        common_hour = data_file['Hours'].mode()[0]
        print("The most common hour is ",common_hour)
        print('-'*40)
    elif month == "all" and day != 'all':
        #  display the most common month
        common_month = data_file['months'].mode()[0]
        print("The most common month is ",common_month)
        print('-'*40)
        #  display the most common start hour
        common_hour = data_file['Hours'].mode()[0]
        print("The most common hour is ",common_hour)
        print('-'*40)
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
## ====================================================================================
## The station stats function
def station_stats(data_file):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('-'*40)
    # TO DO: display most commonly used start station
    common_start_station = data_file['Start Station'].mode()[0]
    print("The most common start station is [{}]".format(common_start_station))
    print('-'*40)
    # TO DO: display most commonly used end station
    common_end_station = data_file['End Station'].mode()[0]
    print("The most common end station is [{}]".format(common_end_station))
    print('-'*40)
    # TO DO: display most frequent combination of start station and end station trip
    data_file['route'] = data_file['Start Station'] + "] ---> [" + data_file['End Station']
    common_rout_of_start_end_station = data_file['route'].mode()[0]
    print("The most common route of start end stations is [{}]".format(common_rout_of_start_end_station))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
## ============================================================================================
## The trip duration stats function
def trip_duration_stats(data_file):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('-'*40)
    # TO DO: display total travel time
    total_travel_time = (data_file['Trip Duration'].sum())/(60*60) # total travel time in hours
    print("The Total travel time = {} h".format(total_travel_time))
    print('-'*40)
    # TO DO: display mean travel time
    mean_travel_time = (data_file['Trip Duration'].mean())/(60) # mean travel time in minutes
    print("The mean travel time = {} min".format(mean_travel_time))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
## ===============================================================================================
## The user stats function
def user_stats(data_file,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = data_file['User Type'].value_counts().to_frame()
    print("The counts of user type is\n",user_type)
    print('-'*40)
    if city != 'washington':
        # TO DO: Display counts of gender
        counts_of_gender = data_file['Gender'].value_counts().to_frame()
        print("The counts of geneder is\n",counts_of_gender)
        print('-'*40)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(data_file['Birth Year'].min())
        print("The earlist year of birth is [{}]".format(earliest))
        print('-'*40)
        most_recent = int(data_file['Birth Year'].max())
        print("The most recent year of birth is [{}]".format(most_recent))
        print('-'*40)
        common_year = int(data_file['Birth Year'].mode()[0])
        print("The most common year of birth is [{}]".format(common_year))
        print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
## ===================================================================================================
## The Raw data fuction
def raw_data(data_file):
    print("---> The Raw data is available to check <---\n")
    print('-'*40)
    start_point = 0
    while True:
        order = input("would you like to see the first 5 rows in the raw data ---> \
Please enter \"yes\" or \"no\"\n>>> ").lower() 
        if order not in ["yes", "no"]:
            print("Not valid value. Please! Enter \"yes\" or \"no\"")
            print('-'*40)
        elif order == "yes":
            print(data_file.iloc[start_point : start_point + 5])
            print('-'*40)
            start_point += 5
            while True:
                next = input("would you like to see the next 5 rows in the raw data ---> \
Please enter \"yes\" or \"no\"\n>>> ").lower()
                print('-'*40)
                if next not in ["yes", "no"]:
                    print("Not valid value. Please! Enter \"yes\" or \"no\"")
                    print('-'*40)
                elif next == "yes":
                    print(data_file.iloc[start_point : start_point + 5])
                    print('-'*40)
                    start_point += 5
                else:
                    break
            break
        else:
            print("Thank you. Good luck!")
            break
    print('='*40)
## ===================================================================================================
## The main function
def main():
    while True:
        city, month, day = get_filters()
        data_file = load_data(city, month, day)

        time_stats(data_file,month,day)
        station_stats(data_file)
        trip_duration_stats(data_file)
        user_stats(data_file,city)
        raw_data(data_file)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n>>> ').lower()
        if restart != 'yes':
            print("Thank you. Good luck!")
            break
## ==================================================================================================

if __name__ == "__main__":
    main()