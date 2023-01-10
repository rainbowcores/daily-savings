from datetime import datetime, date

def get_day_number(day):
    first_day=date(2023,1,1)
    date_given = datetime.strptime(day,'%d-%m-%Y').date()
    day_number = (date_given - first_day).days + 1
    return day_number
