import requests


for i in range(1000):
    for j in ['2001-2010', '2011-2020', '2021-2030']:
        url = f'https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_{i}_{j}.zip'
        response = requests.get(url)
        print(i, j)
