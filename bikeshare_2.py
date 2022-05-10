import time
import pandas as pd
import numpy as np
import random

CITY_DATA = {'chicago': 'D:/chicago.csv',
             'new york': 'D:/new_york_city.csv',
             'washington': 'D:/washington.csv'}

CITY_DATA2 = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which of the following cities would you like to view the data for ? (New york, Chicago or Washington): ").lower()
    city_list = ['new york', 'chicago', 'washington']
    while city not in city_list:
        print("You've entered an invalid city name!")
        city = input("kindly enter a valid city name from the provided options: ").lower()
    # get user input for month (all, january, february, ... , june)
    month = input("Which month in the first semester of the year ? or would you like to view all months? (ex: all, January, February, etc): ").lower()
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in month_list:
        print("You've entered an invalid value!")
        month = input("Kindly enter a valid month/all :")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week ? or would you like to view all days? (ex: Saturday, Sunday, all, etc): ").lower()
    day_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while day not in day_list:
        print("You've entered an invalid value!")
        day = input("Kindly enter a valid day/all: ").lower()
    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df)

    # display the most common month

    month_list2 = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    print('*The most common month to ride a bike is in '+ month_list2[df['month'].mode()[0] - 1].title())
    print()
    # display the most common day of week

    print('*The most common day of the week to ride a bike is in '+ df['day_of_week'].mode()[0])
    print()

    # display the most common start hour

    print('*The most common hour to start a ride is ' + str(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print('*The most common used start station is '+ df['Start Station'].mode()[0])
    print()


    # display most commonly used end station

    print('*The most common used end station is ' + df['End Station'].mode()[0])
    print()


    # display most frequent combination of start station and end station trip

    df['trip'] = df['Start Station'] + ' to ' + df['End Station']

    print('*The most frequent trip is '+ df['trip'].mode()[0])
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('*The total traveled time is '+ str(df['Trip Duration'].sum()))
    print()


    # display mean travel time

    print('*The average traveled time is ' + str(df['Trip Duration'].mean()))
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('*The counts of user types are: \n' + str(df['User Type'].value_counts()))
    print()
    # Display counts of gender

    if 'Gender' in df.columns:
        print('*The count of each gender are: \n' + str(df['Gender'].value_counts()))
        print()
    else:
        print('*No information about users genders in the data of this city')
        print()


    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('*The earliest, most recent and most common years of birth are: \n' + str(df['Birth Year'].min()) + ', '+str(df['Birth Year'].max())+', '+str(df['Birth Year'].mode()[0]))
    else:
        print('*No information about users birth years in the data of this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_view(df):
    """This functions asks if the user wants to view a sample of the original data and prints it
    """
    user_inp = input('Would you like to view a sample of the original data? (y / n): ').lower()
    while user_inp == 'y':
        print(df.loc[random.sample(list(df.index),5)])
        user_inp = input('Would you like to view a sample of the original data? (y / n): ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_view(df)

        restart = input('\nWould you like to restart? (y / n): ')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
