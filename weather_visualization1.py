import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define function to fetch weather data
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Parse weather data into a pandas DataFrame
def parse_weather_data(data):
    # Extract relevant information
    dates = []
    temperatures = []
    humidities = []
    for entry in data['list']:
        dates.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])
        humidities.append(entry['main']['humidity'])
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Temperature': temperatures,
        'Humidity': humidities
    })
    
    return df

# Plot the data
def plot_weather_data(df):
    # Create two subplots (Temperature and Humidity)
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Plot Temperature
    sns.lineplot(data=df, x='Date', y='Temperature', ax=ax[0], color='tab:blue')
    ax[0].set_title('Temperature Over Time')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Temperature (°C)')

    # Plot Humidity
    sns.lineplot(data=df, x='Date', y='Humidity', ax=ax[1], color='tab:green')
    ax[1].set_title('Humidity Over Time')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Humidity (%)')

    plt.tight_layout()
    plt.show()

# Main function to fetch data and create visualizations
def main():
    city = "London"  # Change the city as needed
    api_key = "67e74303180869122f6265626218d3de"  # Replace with your OpenWeatherMap API key
    data = get_weather_data(city, api_key)
    df = parse_weather_data(data)
    plot_weather_data(df)

if __name__ == "__main__":
    main()
