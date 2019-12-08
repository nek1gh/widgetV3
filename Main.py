import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

JSON = 'amocrm.json'
jLoad = json.load(open(JSON))
jDumps = json.dumps(jLoad, sort_keys=True)
jData = json.loads(jDumps)
data = jData['_embedded']['items']
number = len(data)
print(type(data))
print(number)
for num in data:
    for i in (num['custom_fields']):
        print(i)
# i = 1
# l = 0
# for num in data:
#     if len() != 0:
#         print(i)
#     else:
#         print(l)

# phone = 12
# two = 1
# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# client = gspread.authorize(creds)
# row = 2
# for i in data:
#     id = i['id']
#     name = i['name']
#     if len(i['custom_fields']) != 0:
#         custom_fields_id = i['custom_fields']['id']
#         custom_fields_name = i['custom_fields']['name']
#         if len (i['custom_fields']['values']) != 1:
#             custom_fields_id_values = i['custom_fields']['values']['value']
#             custom_fields_id_values = i['custom_fields']['values']['value']
#     else:
#         custom_fields_id = ' '
#         custom_fields_name = ' '
#         custom_fields_id_values = ' '
#     sheet = client.open("n1first").sheet1
#     data = [id, name, phone, two]
#     sheet.insert_row(data, row)
#     row = +row
