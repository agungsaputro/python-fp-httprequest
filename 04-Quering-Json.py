import requests
import json

url = "https://mul14.github.io/data/employees.json"
resp = requests.get(url).json()


#print(resp.text)

salary = [salary for salary in resp if salary['salary'] > 15000000]
resSalary = json.dumps(salary, indent=6)
print(resSalary)


address = [address for address in resp if address['addresses'][0]['label'] == 'home' and address['addresses'][0]['city'] == 'DKI Jakarta']
resAddress = json.dumps(address, indent=6)
print(resAddress)

depart = [depart for depart in resp if depart['department']['name'] == 'Research and development']
resDepart = json.dumps(depart,,indent=6)
print(resDepart)

