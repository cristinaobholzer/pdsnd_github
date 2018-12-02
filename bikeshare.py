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
        (str) first_lines - shows the first five lines of raw data if requested by the user
    """
    print('Hello! Let\'s explore US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        first_lines = input('Before we display any info, would you like to see the first five lines of the raw data? y or n: ').lower().strip()
        if first_lines == 'y':
            break
        elif first_lines == 'n':
            break
        else:
            print('Please type y or n')
            
            
    while True:
        city = input('Which city would you like to analyse?(type Chicago, Washington or New York City) ').lower().strip()
        if city in ('chicago', 'washington', 'new york city'):
            break
        else:
            print('\nIt seems like you typed the wrong city name. Could you please try again?')


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('january', 'february','march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all')
    while True:
        month = input('\nWhich month(s)?\n(type January, February, March, April, May, June, July, August, September, October, November, December or all) ').lower().strip()
        if month in months:
            break
        else:
            print ('\nPlease type one of the suggested values for month. ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday','wednesday', 'thursday', 'friday','saturday', 'sunday')
    while True:
        day = input('Which weekday would you like to analyse? Please type Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n' ).lower().strip()
        if day in days:
            break
        else:
            print ('\nPlease type one of the suggested values for days. ')

    print('-'*40)
    return city, month, day, first_lines


def load_data(city, month, day, first_lines):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) first_lines - shows the first five lines of raw data if requested by the user
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
def load_data(city, month, day, first_lines):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if first_lines == 'y':
        print('The first lines of raw data from {} are: \n'.format(city).strip().lower())
        print(df.head())
    else:
        print('no raw data about {} will be displayed'.format(city))
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(popular_month, ' is the most common month.')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(popular_day, ' is the most common day of the week.')

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour, ' is the most popular hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('most commonly used start station: ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('most commonly used end station: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + " & " + df['End Station']
    popular_combo = df['combo'].mode()[0]
    print('most frequent combination of start station and end station trip: ', popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_total = df['Trip Duration'].sum()
    print('total travel time: ', travel_total)

# TO DO: display mean travel time
    travel_avg = df['Trip Duration'].mean()
    print('average travel time: ', travel_avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('--Count of user type--')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('--Count of user gender--')
        print(df['Gender'].value_counts(),'\n')
    else:
        print('Gender not specified file')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        latest = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print('earliest birth year: ', earliest)
        print('most recent birth year: ', latest)
        print('most common birth year: ', common)
    else:
        print('Birth year not specified in the file')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, first_lines = get_filters()
        df = load_data(city, month, day, first_lines)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
