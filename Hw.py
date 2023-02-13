def tell_date(kurwa:str):
    date,time = map(str,kurwa.split())
    day,month,year = map(int,date.split('.'))
    hour,minute = map(int,time.split(':'))
    
    months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July",
              8:"August", 9:"September", 10:"October", 11:"November", 12:"December" }
    def hours(hour:int):
        if hour == 1:
            return "hour"
        else:
            return 'hours'

    def minutes(minute:int):
        if minute == 1:
            return "minute"
        else:
            return 'minutes'

    print(f"{day} {months[month]} {year} year, {hour} {hours(hour)} {minute} {minutes(minute)} ")


tell_date("01.01.2000 00:00")
tell_date("19.09.2999 01:59")
tell_date("21.10.1999 18:01")