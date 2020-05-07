import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print("Hello! Let's explore some US bikeshare data!")
    while True:
        city = input("Which city would you like to see the data for? ").lower()
        if city in ('new york city', 'washington', 'chicago'):
            break
        else:
            print("Invalid Input")
    response= input("Would you like to filter the data by month, day or none?").lower()
    month='all'
    day='all'
    if response == 'month':
        while True:
            month = input("Which month to filter by? Input month of January till June???").lower()
            months = ['january','february','march','april','may','june']
            if month in months:
                print('Filtering by {},{}'.format(city,month))
                break
            else:
                print("Re-enter month")
    elif response == 'day':
        while True:
            print("Which day to filter by? Enter integer from 1 to 7(monday=1,tues=2.....)")
            day = int(input())
            days = [1,2,3,4,5,6,7]
            if day in days:
                print('Filtering by {},{}'.format(city,day))
                break
            else:
                print("Invalid response. Please enter integer values from 1 to 7")
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df

def time_stats(df):
    print('Calculating The Most Frequent Times of Travel...')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    popular_month = df['month'].mode()[0]
    popular_day = df['day'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    print('Most common month, day, hour is {},{},{}'.format(popular_month,popular_day,popular_hour))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()
    m_station=df['Start Station'].mode()[0]
    me_station=df["End Station"].mode()[0]
    df['comb_station'] = df['Start Station'] + df['Start Station']
    comb_station=df['comb_station'].mode()[0]
    print('most common start,end,combination station is {},{},{}'.format(m_station,me_station,comb_station))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('Calculating Trip Duration...')
    start_time = time.time()
    travel=df['Trip Duration']
    tot_travel=travel.sum(axis=0)
    mean_travel=travel.mean(axis=0)
    print("Total travel time :{}".format(tot_travel))
    print('Mean travel time:{}'.format(mean_travel))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('Calculating User Stats...')
    city_1=input('Enter city again : ').lower()
    start_time = time.time()
    if city_1=='washington':
        while True:
            user_types = df['User Type'].value_counts()
            print('user type count:{}'.format(user_types))
            break
        else:
            input('enter city again')
    elif city_1=='chicago' or city=='new york city':
        while True:
            user_types = df['User Type'].value_counts()
            gender_count = df['Gender'].value_counts()
            earliest=df['Birth Year'].min(axis=0,skipna=True)
            recent=df['Birth Year'].max(axis=0,skipna=True)
            common=df['Birth Year'].mode()[0]
            # output can be improved on to make things clearer
            print('user type count:{}, gender count:{} '.format(user_types,gender_count))
            print('Earliest birth year:{}, most recent birth year:{}, most common birthdates:{}'.format(earliest,recent,common))
            break
    else:
        input('enter city again')
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        start,end=-5,0
        raw_data=input('would you like to see raw data?')
        if raw_data.lower() != 'yes':
            restart = input('Would you like to restart? Enter yes or no.')
            if restart.lower() != 'yes':
                break
        else:
            start+=5
            end+=5
            print(df[start:end])

        restart = input('Would you like to restart? Enter yes or no.')
        if restart.lower() != 'yes':
            break





if __name__ == "__main__":
	main()
