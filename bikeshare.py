import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
              'chi': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'wash': 'washington.csv'
            }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city
    city=""
    while city not in CITY_DATA.keys():
        city = input("Enter the city name (chicago, new york city, washington): ").lower()
    print("Great!  Data is from {}.\n".format(city).title())

    # TO DO: get user input for month
    month=""
    while month not in ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']:
        month = input("Enter the month abbreviation(all, jan, feb, mar, ... , jun): ").lower()

    # TO DO: get user input for day of week
    day = ""
    while day not in ["sun", "mon", "tue", "wed", "thu", "fri", "sat", "all"]:
        day = input("Enter the abbreviation for the day of week (all, sun, mon, tue, wed,...sat): ").lower()

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

    months = {'all':0,'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6}
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if months[month] > 0:
        df=df[df['month']==months[month]]

    days = {"all":"All","sun":"Sunday", "mon":"Monday", "tue":"Tuesday", "wed":"Wednesday", "thu":"Thursday", "fri":"Friday", "sat":"Saturday"}
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    if days[day]!="All":
        df=df[df['weekday_name']==days[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month_name'] = df['Start Time'].dt.month_name()
    print('The most common month is: {}.'.format(df['month_name'].mode()[0]))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print('The most common day of the week is: {}.'.format(df['weekday_name'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}:00.'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most commonly used combination of start and end station is: \n{}".format(df.groupby(['Start Station', 'End Station']).size().nlargest(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    import datetime
    print("The total travel time is:",str(datetime.timedelta(seconds=int(df['Trip Duration'].sum()))))

    # TO DO: display mean travel time
    print("The average travel time is: ",str(datetime.timedelta(seconds=int(df['Trip Duration'].mean().sum()))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type Counts:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("\nGender Type Counts:")
        print(df['Gender'].value_counts())
    else:
        print("\nGender is not found in the data.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("\nThe earliest birth year is: ", df['Birth Year'].min())
        print("The most recent birth year is: ", df['Birth Year'].max())
        print("The most common birth year is: ", df['Birth Year'].mode()[0])
    else:
        print("\nBirth Year is not found in the data.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i=0
        while input("\nWould you like to see 5 lines of raw data (yes or no)?\n").lower() == 'yes':
                print(df[i:i+5])
                i+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
