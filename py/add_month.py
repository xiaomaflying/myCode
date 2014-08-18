import datetime,time
import calendar
import sys

def add_month(dt, months):
    if isinstance(dt, datetime.datetime) :
        pass
        #print "is datetime"
    elif isinstance(dt, str) or isinstance(dt, int) :
        dt = datetime.datetime.fromtimestamp(int(dt))
    else : 
        print "Wrong input args: not time type"
        return
    print "now datetime is : ", dt
    year = dt.year + (dt.month + months)/12
    month = (dt.month + months) % 12
    day = min(dt.day, calendar.monthrange(year, month)[1])
    result = dt.replace(year=year, month=month, day=day)
    print "after add %s months datetime is %s" % (months, result)
    return result

def main() :
    if len(sys.argv)==3 :
        dt = sys.argv[1]
        months = int(sys.argv[2])
    elif len(sys.argv)==2 :
        dt = datetime.datetime.now().replace(day=31)
        months = int(sys.argv[1])
    else : 
        print "argv number is not right"
    print add_month(dt, months)

main()

