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
        (str) month - month's name to filter by, or "all" to apply no month filter
        (str) day - day of week's name to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Please enter the name of the city with a value of chicago, new york city or washington to analyse\n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
         city = input('Please enter the name of the city with a value of chicago, new york city or washington to analyse\n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('Please enter the name of the month with a value of all, january, february, ... or june for filter\n').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Please enter the name of the month with a value of all, january, february, ... or june for filter\n').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the name of the day of week with a value of all, monday, tuesday, ... sunday for filter\n').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Please enter the name of the day of week with a value of all, monday, tuesday, ... sunday for filter\n').lower()
    
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
    import pandas as pd
    # Load data based on city name
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    
    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)

    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print('Most common day of week: ', common_dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour: ', common_start_hour)
    
    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #concat start and end station to have a combinaison of start station and end station trip
    df['Start and End Station'] = df['Start Station']+'  '+df['End Station']
    common_start_end_station = df['Start and End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip: ', common_start_end_station)
    
    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: %s seconds.' % total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: %s seconds." % round(mean_travel_time),1)
    
    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city not in ['chicago','new york city']:
        print('\nCount of gender only apply for "chicago" and "new york city" cities')
    else:
        gender_counts = df['Gender'].value_counts()
        print('\nCount of gender: \n', gender_counts)  
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if city not in ['chicago','new york city']:
        print('\nYear of birth only exist for "chicago" and "new york city" cities')
    else:
        earliest_common_birth_year = int(df['Birth Year'].min())
        print('\nEarliest year of birth: ', earliest_common_birth_year)
        most_recent_birth_year = int(df['Birth Year'].max())
        print('\nMost recent year of birth: ', most_recent_birth_year) 
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nMost common year of birth: ', most_common_birth_year) 

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
    
def display_raw_data(df):
    """ Print 5 rows of the data at a time contained in raw data in df data frame if user answer 'yes'"""
    start_time = time.time()
    i = 0
    raw = input("Please enter only 'yes' or 'no'to see 5 rows user data or to cancel\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Please enter only 'yes' or 'no' to see the next 5 rows user data or to cancel\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes', 'no']:
            restart = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
        if restart == 'no':
            break
 

if __name__ == "__main__":
	main()
