import requests
import matplotlib.pyplot as plt


def fetch_data(country_code, indicator_code):
    api_url = f"http://api.worldbank.org/v2/country/{
        country_code}/indicator/{indicator_code}?date=2000:2019&format=json"
    response = requests.get(api_url)
    data = response.json()
    return data[1]


indicator_code = "SE.PRM.UNER"


data_usa = fetch_data('USA', indicator_code)


years = [entry['date'] for entry in data_usa]
values = [entry['value'] if entry['value']
          is not None else 0 for entry in data_usa]


plt.figure(figsize=(8, 8))
plt.pie(values, labels=years, autopct='%1.1f%%',
        startangle=140, colors=plt.cm.Paired.colors)
plt.title('Children out of school, primary in the USA (2000-2019)')
plt.show()
