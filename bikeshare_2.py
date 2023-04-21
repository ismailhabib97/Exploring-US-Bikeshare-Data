import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
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
    city = ''
    while city == '':
        city = input('What city you would like to view: ').lower()
        if city not in CITY_DATA:
            print('please make sure you entered the city name correctly and try again!')
            city = ''

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month == '':
        month = input('Would you like to view a certain month? enter the name of the month or type "all" to view all months: ').lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month not in months:
            print('please make sure you entered the month correctly and try again!')
            month = ''
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day == '':
        day = input('Which day of the week you would like to view? enter the day or type "all" to view all days: ').lower()
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in days:
            print('please make sure you entered the day correctly and try again!')
            day = ''
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df

def raw_data(df):
    i=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    if month == 'all':
        popular_month = df['Month'].mode()[0]
        print('the most common month is {}'.format(popular_month))

    # display the most common day of week
    if day == 'all':
        popular_day = df['Day'].mode()[0]
        print('the most common day of week is {}'.format(popular_day))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    #print((df['Day']))
    #print((df['Hour']))
    #print(df['Day'].mode())
    #print(df['Hour'].mode())
    popular_hour = df['Hour'].mode()[0]
    print('the most common start hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Start and End Combined'] = df['Start Station'] + ' ' + df['End Station']
    popular_combination = df['Start and End Combined'].mode()[0]

    print('the most commonly used start station is {}'.format(popular_start_station))
    print('the most commonly used end station is {}'.format(popular_end_station))
    print('the most frequent combination of start station and end station is {}'.format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('the total travel time is {}'.format(total_travel_time))
    print('the mean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types are {}'.format(user_types))
    # Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('counts of gender are {}'.format(gender))

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('earliest year of birth of users is {}'.format(earliest_year))
        print('most recent year of birth of users is {}'.format(most_recent_year))
        print('most common year of birth of users is {}'.format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
