import requests

city = 'Oslo'
city = requests.get('http://weathers.co/api.php?city={}'.format(city))
weather = city.json()

# Taking out data
'''
>>> weather.get('data')
{'location': 'Oslo', 'temperature': '-18', 'skytext': 'Sky is Clear', 'humidity': '65', 'wind': '6.62 km/h', 'date': '01-15-2017', 'day': 'Sunday'}

>>> weather.get('data')['location']
'Oslo'

>>> weather.get('data')['temperature']
'-18'

>>> weather.get('data')['skytext']
'Sky is Clear

>>> weather.get('data')['wind']
'6.62 km/h'

# Using get() to return error.
>>> weather.get('data').get('wind', 'Error no data')
'3.56 km/h'

>>> weather.get('data').get('hello', 'Error no data')
'Error no data'
'''
