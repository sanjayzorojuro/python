import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


#loading data 
def load_weather_data(filepath):
    df=pd.read_csv(filepath , parse_dates=['date'])
    print("Date Loaded Successfully.\n")
    print(f"Date Range:{df['date'].min().date()} to {df['date'].max().date()}")
    return df

#summirizing the statistics 
def show_summary(df):
    print("Weather Summary Statstics:")
    print(df.describe())

#Filter by dates
def filter_bydate(df,start,end):
    mask=(df['date'] >= start) & (df['date'] <= end)
    return df.loc[mask]

#mix/min temperature
def temperature(df):
    max_temp=df ['temperature'].max()
    min_temp=df['temperature'].min()
    print(f"Max Temperature:{max_temp}°C, Min Temperature:{min_temp}°C")

#average humidity
def average_humidity(df):
    avg_humidity=df['humidity'].mean()
    print(f"Average Humidity:{avg_humidity:.2f}%")


def plot_temperature(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['date'], df['temperature'], marker='o', linestyle='-')
    plt.title("Daily temperatures")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


#main porgram
def main():
    filepath="weather_data.csv"
    df = load_weather_data(filepath)

    while True:
        print("\nOptions:")
        print("1. View summary")
        print("2. Filter by date")
        print("3. Show max/min temperature")
        print("4. Show average humidity")
        print("5. Plot temperature")
        print("6. Exit")
        choice=input("choose an option:")


        if choice == '1':
            show_summary(df)
        elif choice == '2':
            start=input("Start date (YYYY-MM-DD):")
            end=input("End date (YYYY-MM-DD):")
            filterd=filter_bydate(df,start,end)
            if filterd.empty:
                print("No data available in the range")
            else:
                print(filterd)
        elif choice == '3':
            temperature(df)
        elif choice == '4':
            average_humidity(df)
        elif choice == '5':
            plot_temperature(df)
        elif choice =='6':
            print("Exiting weather data explorer. ")
            break
        else:
            print("invalid choice")

if __name__== "__main__":
    main()






