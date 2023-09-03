from datetime import datetime


def getTimestamp():
    dt = str(datetime.now().month) + '/' + str(datetime.now().day) + ' '
    hr = str(datetime.now().hour) if len(str(datetime.now().hour)) > 1 else '0' + str(datetime.now().hour)
    minute = str(datetime.now().minute) if len(str(datetime.now().minute)) > 1 else '0' + str(datetime.now().minute)
    t = '[' + hr + ':' + minute + '] '
    return dt + t
