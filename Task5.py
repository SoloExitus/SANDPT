from datetime import date,datetime,timedelta

def format(c:int):
    if c >= 10:
        return str(c)
    return "0" + str(c)

def dateFormat(date:date):
    return f"{format(date.day)}-{format(date.month)}-{format(date.year)} {format(date.hour)}:{format(date.minute)}:{format(date.second)}"

def date_in_future(count):
    currentDate = datetime.now()
    if not type(count) == int:
        return dateFormat(currentDate)

    delta = timedelta(count)

    return dateFormat(currentDate + delta)



print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня