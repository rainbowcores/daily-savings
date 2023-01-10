from app.save import get_day_number
def main():
    day =  input("Please a date in format (dd-mm-yyyy eg. 31-01-2023): ")
    print(day + " is Day Number: " + str(get_day_number(day)) )

main()