day = 1
day_of_week = 1
day_of_year = 1
month = 1
year = 1900
day_of_month = 1
first_sunday_count = 0
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days_in_month = days_in_month
leap_year_days_in_month[1] = 29
while year <= 2000 or month != 12:
    if day_of_week == 7 and day_of_month == 1 and year >= 1901:
        first_sunday_count = first_sunday_count + 1
    leap_year = (year % 400) == 0 or ((year % 100 != 0) and (year % 4 == 0))
    chosen_days_in_month = leap_year_days_in_month if leap_year else days_in_month
    day = day + 1
    day_of_week = day_of_week + 1
    if day_of_week == 8:
        day_of_week = 1
    day_of_month = day_of_month + 1
    if day_of_month >= chosen_days_in_month[month - 1] + 1:
        day_of_month = 1
        month = month + 1
    if month == 13:
        month = 1
    day_of_year = day_of_year + 1
    if not leap_year and day_of_year == 366:
        day_of_year = 1
        year = year + 1
    elif leap_year and day_of_year == 367:
        day_of_year = 1
        year = year + 1
print(first_sunday_count)
