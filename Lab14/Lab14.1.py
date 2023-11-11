import matplotlib.pyplot as plt
import requests


def fetch_data(country_code, indicator_code):
    api_url = f"http://api.worldbank.org/v2/country/{
        country_code}/indicator/{indicator_code}?date=2000:2019&format=json"
    response = requests.get(api_url)
    data = response.json()
    return data[1]


def plot_graph(years, values1, values2, country1, country2, indicator_name):
    plt.plot(years, values1, label=country1)
    plt.plot(years, values2, label=country2)

    plt.xlabel('Year')
    plt.ylabel(indicator_name)
    plt.title(f"{indicator_name} Dynamics ({country1} vs {country2})")
    plt.legend()
    plt.show()


def bar_chart(country, values, indicator_name):
    plt.bar(country, values, color=['blue', 'orange'])
    plt.xlabel('Country')
    plt.ylabel(indicator_name)
    plt.title(f"{indicator_name} for {country[0]} and {country[1]}")
    plt.show()


country_code_ukraine = "UA"
country_code_usa = "US"
indicator_code = "SE.PRM.UNER"


data_ukraine = fetch_data(country_code_ukraine, indicator_code)
data_usa = fetch_data(country_code_usa, indicator_code)


years = [entry['date'] for entry in data_ukraine]
values_ukraine = [entry['value'] for entry in data_ukraine]
values_usa = [entry['value'] for entry in data_usa]


plot_graph(years, values_ukraine, values_usa, "Ukraine",
           "USA", "Children out of school, primary")


selected_country = input(
    "Enter a country for the bar chart (Ukraine or USA): ").capitalize()
bar_values = [values_ukraine[years.index(
    "2019")], values_usa[years.index("2019")]]
bar_chart([selected_country, "Other"], bar_values,
          "Children out of school, primary")
