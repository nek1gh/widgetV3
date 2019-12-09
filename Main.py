import json
import datetime
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials


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
    row_data['updated_at'] = str(change_date(i['updated_at']))
    pprint(row_data)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("n1first").sheet1
data = ['ID', 'Имя статуса', 'ID компании', 'Имя компании', 'Дата создания', 'Дата завершения', 'Дата Отгрузки']
sheet.insert_row(data, 1)
'''
ID	
Имя статуса	
ID компании	
Имя компании	
Дата создания	
Дата завершения	
Дата Отгрузки
'''
