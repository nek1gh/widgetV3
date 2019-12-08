import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

JSON = 'amocrm.json'
jLoad = json.load(open(JSON))
jDumps = json.dumps(jLoad, sort_keys=True)
jData = json.loads(jDumps)
data = jData['_embedded']['items']
# number = len(data)
# print(type(data))
# print(number)
# for num in data:
#     for i in (num['custom_fields']):
#         print(i)
# i = 1
# l = 0
# for num in data:
#     if len() != 0:
#         print(i)
#     else:
#         print(l)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
row = 2
for i in data:
    id = i['id']
    name = i['name']
    for i2 in (i['custom_fields']):
        if len(i2) != 0:
            custom_fields_id = i2['id']
            custom_fields_name = i2['name']
            for i3 in (i2['values']):
                if len(i2['values']) != 1:
                    custom_fields_id_values_value = i3['value']
                    custom_fields_id_values_enum = i3['enum']
                elif len(i2['values']) == 1:
                    custom_fields_id_values_value = i3['value']
                    custom_fields_id_values_enum = ' '
                else:
                    custom_fields_id_values_value = ' '
                    custom_fields_id_values_enum = ' '
    else:
        custom_fields_id = ' '
        custom_fields_name = ' '
        custom_fields_id_values = ' '

        custom_fields_id_values_value = ' '
        custom_fields_id_values_enum = ' '
    print(id)
    print(name)
    print(custom_fields_id)
    print(custom_fields_name)
    print(custom_fields_id_values)
    print(custom_fields_id_values_value)
    print(custom_fields_id_values_enum)

    sheet = client.open("n1first").sheet1
    data = [id, name, custom_fields_id, custom_fields_name, custom_fields_id_values_value, custom_fields_id_values_enum]
    sheet.insert_row(data, row)
    row = +row
