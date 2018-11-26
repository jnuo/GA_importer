import datetime
import timedelta
import GA

def reportDay(day):
    # get analytics data for the day
    # get adwords data for the day
    # calculate roi for (in Google Ads class)
    #   Dynamic Remarketing
    #   SEM (Brand)
    #   SEM (Non-Brand)
    GA.main()


LASTXDAYS = 1

today = datetime.datetime.now().date()

dayz = []
i = 0
while i < LASTXDAYS:
    dayscount = i + 1
    thatDay = today - timedelta.Timedelta( days = dayscount )
    dayz.append(thatDay)
    i = dayscount

print(dayz)

for d in dayz:
    reportDay(d)
