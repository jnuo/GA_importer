# Versions:
#   Version 1: Google Spending Data & TotalSC by Day & Report ROI by Day
#   Version 2: From 2 excel files (or csv)
#   Version 3: Export to Google Sheets * Report in Datastudio
#   Version 4: Get Google Spending and TotalSC data from API
#   Version 5: Make this a batch job
#               and make it run everyday, feeding data to Datastudio
#   Next versions: Add Criteo, Facebook, etc, etc.
from typing import List, Dict


# Functions Begin
def getAllDates():
    dates: List[str] = []

    for i in googleSpending.keys():
        try:
            b = dates.index(i)
        except:
            dates.append(i)
    for i in googleSC.keys():
        try:
            b = dates.index(i)
        except:
            dates.append(i)
    return dates

def getGoogleSpending():
    googleCost: Dict[str, float] = {
        '2018-11-01': 156.78,
        '2018-11-02': 166.78,
        '2018-11-03': 176.78,
    }

    return googleCost

def getGoogleSC():
    googlesc: Dict[str, float] = {
        '2018-11-01': 166.78,
        '2018-11-02': 136.78,
        '2018-11-03': 246.78,
    }

    return googlesc

def calculateRoi(dates, costs, profits):
    rois: Dict[str, float] = {}
    cost = 0
    profit = 0
    roi = 0
    for i in dates:
        if i in costs:
            cost = costs[i]
        else:
            rois[i] = "-"
            continue
        if i in profits:
            profit = profits[i]
        else:
            rois[i] = "-"
            continue
        roi = float(profit / cost)
        rois[i] = roi

    return rois
# Functions End

googleSpending: Dict[str, float] = getGoogleSpending()
googleSC: Dict[str, float] = getGoogleSC()
googleRois = {}
allDates: List[str] = []

allDates = getAllDates()

googleRois = calculateRoi(allDates, googleSpending, googleSC)

print(googleRois)
