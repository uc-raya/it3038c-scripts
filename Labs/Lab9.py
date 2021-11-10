import requests
import json

r = requests.get('http://localhost:3000')
data = r.json()

print("The color of Widget 1 is %s" % (data[0]['color']))
print("The color of Widget 2 is %s" % (data[1]['color']))