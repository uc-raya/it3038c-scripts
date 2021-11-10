import requests
import json

print('Please enter your ZIP code: ')
zip = input()

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=dc8b6c42ac31d43327a3fdbcc5126fe0' % zip)
data = r.json()

#print(type(data['weather'][0]['description']))
print("The weather in %s is %s" % (zip, data['weather'][0]['description']))