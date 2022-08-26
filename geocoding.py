import requests
import json

##Python GeoCoding
state = 'NJ'
zipcode = '07306'
city = 'Jersey City'
street = '151 Van Winkle Ave'

response = requests.get('http://dev.virtualearth.net/REST/v1/Locations/US/' + state+ '/'+zipcode+'/'+city+'/'+ street+'?o=json&key=AtJsFO9_FVk7KjHHlR7dEkZqdqLvX7YTcRa3gYzjmrn-oEqwg3R4vsWIhEF-dGxF')
r = response.json()
print(r)
print(response.status_code)
try:
	coordinates = r['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']
	print(coordinates)
	##sheet['I'+str(i)].value = coordinates[0]
	##sheet['J'+str(i)].value = coordinates[1]
except:
	print('Not found')
