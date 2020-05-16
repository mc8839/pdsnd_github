import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]


    # check to see if city in cities list
    while city not in cities:
        #ask for user input
        city = input("\nEnter city (chicago, new york city, washington): ")
        if city not in cities:
            print("        {} is not a valid city value or format. Please enter a valid city.".format(city))
            city = ""
        else:
            print("        {} is a valid city. Thank you.".format(city))


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october', 'november', 'december']


    #check if month in months list
    while month not in months:
        #ask for user input
        month = input("\nEnter month (all, january, february, ... , june): ")
        if month not in months:
            print("        {} is not a valid month value or format. Please enter a valid month.".format(month))
            month = ""
        else:
            print("        {} is a valid month entry. Thank you.".format(month))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


    #check if day in days list
    while day not in days:
        #ask for user input
        day = input("\nEnter day of the week (all, monday, tuesday, ... sunday): ")
        if day not in days:
            print("        {} is not a valid day value or format. Please enter a valid day.".format(day))
            day = ""
        else:
            print("        {} is a valid day entry. Thank you.".format(day))


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


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


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (DataFrame) df - dataframe of bikeshare data
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        Displays popular month, city and hour
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    if month == 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df['pop_month'] = df['Start Time'].dt.month
        popular_month = months[df['pop_month'].mode()[0]-1].title()
        print('Most popular month:', popular_month)
    else:
        print('You preselected the month of {}'. format(month.title()))


    # TO DO: display the most common day of week
    if day == 'all':
        df['day_name'] = df['Start Time'].dt.weekday_name
        popular_day = df['day_name'].mode()[0].title()
        print('Most popular day:', popular_day)
    else:
        print('You preselected the day of {}'. format(day.title()))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour


    popular_hour = df['hour'].mode()[0]


    if day == 'all' and month == 'all':
        print('Most popular start hour for all days and all months: ', popular_hour)
    elif month == 'all':
        print('Most popular start hour for {}\'s in all months: {}'.format(day.title(), popular_hour))
    elif day == 'all':
        print('Most popular start hour for all days in {} is: {}'.format(month.title(), popular_hour))
    else:
        print('Most popular start hour for {}\'s in {} is: {}'.format(day.title(), month.title(), popular_hour))


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (DataFrame) df - dataframe of bikeshare data
    Returns:
        (list) start_station_mod - Displays popular start station using mode
        (list) end_station_mod - Displays populsr end station using mode
        (list) end_start_station_mod - Displays popular start and end station combo using mode
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mod = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(start_station_mod))

    # TO DO: display most commonly used end station
    end_station_mod = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(end_station_mod))

    # TO DO: display most frequent combination of start station and end station trip
    end_start_station_mod = (df['Start Station'] + " and " + df['End Station']).mode()[0]
    print('The most commonly used start and end stations are {}'.format(end_start_station_mod))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    '''This function returns the total trip duration and average trip duration

    Args:
        (DataFrame) df - dataframe of bikeshare data
    Returns:
        (list) with two str values:
        First value: String that says the total trip duration in years, days, hours, minutes, and seconds
        Second value: String that says the average trip duration in hours, minutes, and seconds
    '''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    m, s = divmod(df['Trip Duration'].sum(),60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('Total travel time is {}-days {}-hours {}-min {}-sec'.format(int(d), int(h), int(m) , int(s)))

    # TO DO: display mean travel time
    m, s = divmod(df['Trip Duration'].mean(),60)
    h, m = divmod(m, 60)
    print('Average travel time is {}-hours {}-min {}-sec'.format(int(h), int(m) , int(s)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    '''This function returns the statistics on the users in a city

    Args:
        (DataFrame) df - dataframe of bikeshare data
        (str) city - user input of the file to be used. Washington file does not contain any Gender or Birth year

    Returns:
        if washington is the city then exits
        First value: String that says the gender by group by
        Second value: Numpy array is used to remove Nan and get min Birth year
        Third value: Numpy array is used to remove Nan and get max Birth year
        Forth value: list called popular_day for mode to get most common Birth year
    '''

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    user_type_count = df.groupby('User Type')['User Type'].count()
    print('The count of user types:')
    print(user_type_count.to_string())

    if city == 'washington':
        print('\nGender is not included in Washington file')
        print('\nBirth year is not included in Washington file')
    else:
        # TO DO: Display counts of gender
        gender_type_count = df.groupby('Gender')['Gender'].count()
        print('\nThe count of gender:')
        print(gender_type_count.to_string())

        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = np.array(df['Birth Year']) # put birth year into numpy array
        popular_day = int(df['Birth Year'].mode()[0])

        print('\nThe earliest birth year is: ', int(np.nanmin(birth_year)))
        print('The most recent birth year is: ', int(np.nanmax(birth_year)))
        print('The most common birth year is: ', popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_more_lines(df, view_display):
    """Displays rows of data with user input."""

    '''This function returns rows from df based on user input

    Args:
        df: dataframe of bikeshare data
        view_display: string user input asking to show data
        view_data: string to ask if user wants to see data
        start_loc: int of the amount of data to be shown

    Returns:
        rows of data based on start_loc in while loop
    '''

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ')
    if view_data.lower() != 'yes':
        return
    else:
        start_loc = 0

        while (view_display != 'no' ):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to see more? Enter yes or no: ").lower()



def main():
    while True:
        #Set variables to empty
        city = ""
        month = ""
        day = ""
        view_display = ""
        print('Hello! Let\'s explore some US bikeshare data!')

        city, month, day = get_filters(city, month, day)

        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        see_more_lines(df, view_display)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#stackoverflow.com
#geeksforgeeeks.com
#pythonexamples.org
