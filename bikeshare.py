import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please choose one of the three cities ( chicago or new york city or washington) ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        print('Sorry, your input should be chicago or new york city or washington')
        city = input("please choose one of the three cities ( chicago or new york city or washington) ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february'", "march", "april", "may", "june", "all"]
    while True:
        month = input("please choose a month  between january and june or  choose all for all of them ").lower()
        if month in months:
            break
        else:
            print('Sorry, your input should be january, february, march, april, may, june or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while True:
        day = input("please choose a day of the week or choose all for all of them ").lower()
        if day in days:
            break
        else:
            print("Sorry, your input should be a day of the week or all of them")

    print("thank you for choosing {}, {} and {} \nthe data you need will be shown in seconds ".format(city, month, day))
    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', popular_day_of_week)

    # display the most common start hour
    popular_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    group_fields = df.groupby(['Start Station', 'End Station'])
    Most_frequent_combination_station = group_fields.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', Most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    # to prompt the user if he likes to display the raw data of that city as chunks of 5 rows based upon user input.
    print('\nRaw data is available to check... \n')
    index = 0
    user_input = input("would you like to display 5 rows of raw data? , please type yes or No ").lower()
    if user_input not in ['yes', 'no']:
        print("pleas type yes or no")
        user_input = input("would you like to display 5 rows of raw data?, please type yes or No").lower()
    elif user_input != "yes":
        print('Thank You')
    else:
        while index + 5 < df.shape[0]:
            print(df.iloc[index:index + 5])
            index += 5
            user_input = input("would you like to display more 5 rows of raw data? ").lower()
            if user_input != 'yes':
                print('Thank You')
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("thank you")
            break


if __name__ == "__main__":
    main()
