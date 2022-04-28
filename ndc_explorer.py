'''
Adapted from https://github.com/arl009/ForgetMeNot/blob/main/py/retreiver.py

Get API https://open.fda.gov/apis/drug/ndc/how-to-use-the-endpoint/

'''

import requests
import json


product_ndc = "22840-0209"
package_ndc = "22840-0209-4"
generic_name = "Ambrosia confertiflora"

response_API = requests.get('https://api.fda.gov/drug/ndc.json?search=product_ndc:"' + product_ndc + '"&limit=5')
#response_API = requests.get('https://api.fda.gov/drug/ndc.json?search=generic_name:"' + generic_name + '"&limit=5')


# print(response_API.status_code) # 200 = SUCCESS
data = response_API.text
parse_data = json.loads(data)


name = parse_data['results'][0]['generic_name'].title()
brand = parse_data["results"][0]["brand_name"]
manufact = parse_data["results"][0]["labeler_name"]
print("Name: ", name)
print("Brand: ", brand)
print("Manufacturer: " + manufact)


print("\nActive Ingredients: ")
for i in parse_data['results'][0]["active_ingredients"]:
  act_ingred_name = i['name'].title()
  act_ingred_stren = i['strength']
  print('Name: ' + act_ingred_name)
  print('Strength: ' + act_ingred_stren)

exp_date = parse_data['results'][0]["listing_expiration_date"]
exp_date_formatted = exp_date[5:6] + "/" + exp_date[7:] + "/" + exp_date[:4]

print("\nExpiration Date: ", exp_date_formatted)

medical_type = parse_data['results'][0]["dosage_form"].title()
medical_use = parse_data['results'][0]["product_type"].title()
print("Type: ", medical_type)
print("Use: ", medical_use)


for i in parse_data['results'][0]["packaging"]:
  if i["package_ndc"] == package_ndc:
    dosage = i['description']
    print('Dosage: ' + dosage)

#Pharmesutical Classes
print("\nPharmesutical Classes: ",)
for i in parse_data['results'][0]["pharm_class"]:
  print('     - ', i.title())
