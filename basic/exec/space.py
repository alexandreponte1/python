import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
# print(response.content)

json = response.json()

print("The people current in space are: ")
for person in json['people']:
   print(person['name'])