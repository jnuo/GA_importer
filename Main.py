# Versions:
#   Version 1: Google Spending Data & TotalSC by Day & Report ROI by Day
#   Version 2: From 2 excel files (or csv)
#   Version 3: Export to Google Sheets * Report in Datastudio
#   Version 4: Get Google Spending and TotalSC data from API
#   Version 5: Make this a batch job
#               and make it run everyday, feeding data to Datastudio
#   Next versions: Add Criteo, Facebook, etc, etc.

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# import PyOpenSSL

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('ROIReport-101da91f6b59.json', scope)

gc = gspread.authorize(credentials)

# Functions Begin
# def getAllDates():
#     dates: List[str] = []
#
#     for i in googleSpending.keys():
#         try:
#             b = dates.index(i)
#         except:
#             dates.append(i)
#     for i in googleSC.keys():
#         try:
#             b = dates.index(i)
#         except:
#             dates.append(i)
#     return dates
#
#
# def getGoogleSpending():
#     googleSpendingFileName = 'GoogleSpendings.xlsx'
#     director = os.path.dirname(__file__) + "/docs/"
#     path = director + googleSpendingFileName
#     wb = load_workbook(path)
#
#     sheet = wb['Sheet1']
#     row_count = sheet.max_row
#     column_count = sheet.max_column
#
#     googleCost: Dict[str, float] = {}
#
#     i = 2
#     while i <= row_count:
#         indexDate = "A" + str(i)
#         indexCost = "B" + str(i)
#         cell = sheet[indexDate].value
#         valueDate = ""
#         try:
#             valueDate = str(cell.strftime("%Y-%m-%d"))
#         except:
#             continue
#
#         valueCost = sheet[indexCost].value
#         if valueDate not in googleCost:
#             googleCost[valueDate] = valueCost
#         i = i + 1
#
#     return googleCost
#
#
# def getGoogleSC():
#     googleProfitFileName = 'GoogleProfits.xlsx'
#     director = os.path.dirname(__file__) + "/docs/"
#     path = director + googleProfitFileName
#     wb = load_workbook(path)
#
#     sheet = wb['Sheet1']
#     row_count = sheet.max_row
#     column_count = sheet.max_column
#
#     googlesc: Dict[str, float] = {}
#
#     i = 2
#     while i <= row_count:
#         indexDate = "A" + str(i)
#         indexProfit = "B" + str(i)
#         cell = sheet[indexDate].value
#         valueDate = ""
#         try:
#             valueDate = str(cell.strftime("%Y-%m-%d"))
#         except:
#             continue
#
#         valueCost = sheet[indexProfit].value
#         if valueDate not in googlesc:
#             googlesc[valueDate] = valueCost
#         i = i + 1
#
#     return googlesc
#
#
# def calculateRoi(dates, costs, profits):
#     rois: Dict[str, float] = {}
#     cost = 0
#     profit = 0
#     roi = 0
#     for i in dates:
#         if i in costs:
#             cost = costs[i]
#         else:
#             rois[i] = "-"
#             continue
#         if i in profits:
#             profit = profits[i]
#         else:
#             rois[i] = "-"
#             continue
#         roi = float(profit / cost)
#         rois[i] = roi
#
#     return rois
#
#
# # Functions End
#
# googleSpending: Dict[str, float] = getGoogleSpending()
# googleSC: Dict[str, float] = getGoogleSC()
# googleRois = {}
# allDates: List[str] = []
#
# allDates = getAllDates()
#
# googleRois = calculateRoi(allDates, googleSpending, googleSC)

# def merge():
wks = gc.open('ROI Report').sheet1
# for i in googleRois:
#     date = i
#     profit = googleSC[i]
#     cost = googleSpending[i]
#     roi = float(profit / cost)
#     wks.append_row([date, profit, cost, roi])

# print(wks.get_all_records())

# wks.acell('A2').value = '2018-11-04'
# print(wks.acell('A2').value)

wks.update_acell('A2', '2018-11-01')
print(wks.get_all_records())

