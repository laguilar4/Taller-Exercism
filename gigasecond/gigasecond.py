import datetime
def add(moment):
    gigasecond = datetime.timedelta(seconds=1000000000)
    total = gigasecond + moment
    return total

