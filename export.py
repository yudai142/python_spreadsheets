import gspread
from oauth2client.service_account import ServiceAccountCredentialss
import sys

#jsonファイルを使って認証情報を取得
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
c = ServiceAccountCredentials.from_json_keyfile_name('tenacious-ether-339201-6b7114c9fa99.json', scope)

#認証情報を使ってスプレッドシートの操作権を取得
gs = gspread.authorize(c)

#共有したスプレッドシートのキー（後述）を使ってシートの情報を取得
SPREADSHEET_KEY = '1uCzL_evf6AVRtnZr8HVmXHRzzRFAcBqgS53bDGGeTOY'
workbook = gs.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.worksheet("発注管理表")

sys.argv.pop(0)
worksheet.append_row(sys.argv)