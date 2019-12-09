import json
from pprint import pprint
import datetime


def change_date(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp // 24 // 60 // 60 * 60 * 60 * 24)


sJSON = 'status.json'
dataStatus = json.load(open(sJSON))
status = dataStatus['_embedded']['items']
status_all = {status[funnel]['statuses'][i]['id']: status[funnel]['statuses'][i]['name'] for funnel in status for i
              in status[funnel]['statuses']}

JSON = 'amocrm.json'
data = json.load(open(JSON))
deal = data['_embedded']['items']
# pprint(deal[12])
for i in deal[:1]:
    row_data = dict()
    row_data['id'] = i['id']
    row_data['status_id'] = status_all[i['status_id']]
    row_data['company_id'] = i['company']['id'] if i['company'] != {} else ""
    row_data['company_name'] = i['company']['name'] if i['company'] != {} else ""
    row_data['created_at'] = str(change_date(i['created_at']))
    row_data['updated_at'] = change_date(i['updated_at'])
    pprint(row_data)

'''
ID	
Имя статуса	
ID компании	
Имя компании	
Дата создания	
Дата завершения	
Дата Отгрузки
'''
'''
row = 2
for i in data:
    row_data = dict()
    row += 1
    row_data['id'] = i['id']
    row_data['name'] = i['name']
    # print(type(row_data))
    # pprint(row_data)
 row_data["cust1"] = ""
    custom_fields_name = '2'
    custom_fields_id_values_value = '3'
    custom_fields_id_values_enum = '4'
    for i2 in (i['custom_fields']):
        if len(i2) != 0:
            custom_fields_id = i2['id']
            custom_fields_name = i2['name']
            custom_fields_id_values_value = '5'
            custom_fields_id_values_enum = '6'
            for i3 in (i2['values']):
                custom_fields_id_values_value = i3['value']
                if len(i2['values']) != 1:
                    custom_fields_id_values_enum = i3['enum']
                elif len(i2['values']) == 1:
                    custom_fields_id_values_enum = '7'
                else:
                    custom_fields_id_values_enum = '8'
        else:
            custom_fields_id = '9'
            custom_fields_name = '10'
            custom_fields_id_values_value = '11'
            custom_fields_id_values_enum = '12'
'''
'''      
        print(id)
        print(name)
        print(custom_fields_id)
        print(custom_fields_name)
        print(custom_fields_id_values_value)
        print(custom_fields_id_values_enum)'''
'''
    sheet = client.open("n1first").sheet1
    data = [id, name, custom_fields_id, custom_fields_name, custom_fields_id_values_value, custom_fields_id_values_enum]
    sheet.insert_row(data, row)

'''
