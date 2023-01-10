from datetime import datetime, date

def get_day_number(day):
    first_day=date(2023,1,1)
    date_given = datetime.strptime(day,'%d-%m-%Y').date()
    day_number = (date_given - first_day).days + 1
    return day_number

def total_saved(day):
    total_savings = 0
    day_number = get_day_number(day)


    while day_number > 0:
        total_savings = day_number+total_savings
        day_number = day_number-1
    
    return total_savings

