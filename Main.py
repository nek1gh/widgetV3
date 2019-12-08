import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

JSON = 'amocrm.json'
jsondata = json.load(open(JSON))
data = json.dumps(jsondata, sort_keys=True)
dataJ = json.loads(data)

id = dataJ['_embedded']['items'][4]['id']
name = 11
phone = 12
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("n1first").sheet1
data = [id, name, phone]
row = 2
sheet.insert_row(data, row)
