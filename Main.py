import gspread
from oauth2client.service_account import ServiceAccountCredentials

id = int(input())
name = input()
phone = input()
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("n1first").sheet1
data = [id, name, phone]
row = 2
sheet.insert_row(data, row)
