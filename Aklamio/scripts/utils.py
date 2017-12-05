import io
import os
import errno
import datetime
from datetime import date, timedelta

def getfullpath(filename):
    path= os.path.dirname(os.getcwd())+'\\data\\'+filename+'.csv'
    if not os.path.isfile(path):
     raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    else :
        return path

#10/26/2017 - 12/5/2016
def convertDate(date,format):
    _date=datetime.datetime.strptime(date,format) #date, "%m/%d/%y")
    return _date
    #  raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    # else :
    #     return path


def dateRange(startdate,enddate):
    dates=[]
    for result in calculateDateRange(convertDate(startdate,'%Y-%m-%d'), convertDate(enddate,'%Y-%m-%d'), timedelta(days=1)):
        #print(result)
        dates.append(result.strftime('%Y-%m-%d'))
    return dates

def calculateDateRange(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta