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
        '2018-11-01': 156.78,
        '2018-11-02': 166.78,
        '2018-11-03': 176.78,
    }

    return googlesc
# Functions End

googleSpending: Dict[str, float] = getGoogleSpending()
googleSC: Dict[str, float] = getGoogleSC()

allDates: List[str] = []

allDates = getAllDates()

