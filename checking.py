import geocoder
import geopy
import requests
from geopy.geocoders import Nominatim

Geolocator = Nominatim(user_agent="geoapiExercises")
res = requests.get('https://ipinfo.io/')
data= res.json
print(res.text)
print(str(res.text[1]))
# print(*res.text, sep='\n')

for i in (res.text):
    print(i)

# print(data['loc'])
location="21.192572,72.799736"
zipcode="800011"
locationInfo=Geolocator.geocode(zipcode)
print(locationInfo.address)

print(data.DOCTOR1)