import datetime
N = int(input())
year = int(input())
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}
weekday_work = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
year_weekday_count = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
start_date = datetime.date(year, 1, 1)
end_date = datetime.date(year, 12, 31)
all_days = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
for day in all_days:
    year_weekday_count[day.strftime('%A')] += 1
for _ in range(N):
    day = str(input())
    d = datetime.date(year, month_dict[day.split()[1]], int(day.split()[0]))
    year_weekday_count[d.strftime('%A')] -= 1
input()
print(list(year_weekday_count)[list(year_weekday_count.values()).index(max(list(year_weekday_count.values())))],\
      list(year_weekday_count)[list(year_weekday_count.values()).index(min(list(year_weekday_count.values())))])
