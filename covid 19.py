import requests
import matplotlib.pyplot as plt

# Function to fetch COVID-19 data
def get_covid_data(country):
    url = f"https://api.covid19api.com/dayone/country/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data")
        return None

# Function to process and visualize data
def visualize_covid_data(data):
    dates = [entry['Date'][:10] for entry in data]
    confirmed = [entry['Confirmed'] for entry in data]
    deaths = [entry['Deaths'] for entry in data]
    recovered = [entry['Recovered'] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, confirmed, label="Confirmed Cases", color='orange')
    plt.plot(dates, deaths, label="Deaths", color='red')
    plt.plot(dates, recovered, label="Recovered", color='green')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title(f"COVID-19 Statistics in {data[0]['Country']}")
    plt.xticks(dates[::len(dates)//10], rotation=45)  # Show only a few dates
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    country = input("Enter the country (e.g., 'us' for United States): ").lower()
    covid_data = get_covid_data(country)
    if covid_data:
        visualize_covid_data(covid_data)
