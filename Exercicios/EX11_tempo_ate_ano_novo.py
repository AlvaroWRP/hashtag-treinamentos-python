import time

current_date = time.localtime()

# tupla montada igual o struct_time
# tm_year, tm_mon, tm_day, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
new_year = (current_date.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

remaining_seconds = int(time.mktime(new_year) - time.mktime(current_date))

seconds_per_minute = 60
seconds_per_hour = 60 * 60
seconds_per_day = 24 * 60 * 60

# pega os dias restantes e joga o resto fora
days, remainder = divmod(remaining_seconds, seconds_per_day)
# print(days, remainder)

# pega as horas restantes e joga o resto fora
hours, remainder = divmod(remainder, seconds_per_hour)
# print(hours, remainder)

# pega os minutos e segundos
minutes, seconds = divmod(remainder, seconds_per_minute)
# print(minutes, seconds)

print(
    f'Time until New Year: ' \
    f'{days} days, {hours} hours, ' \
    f'{minutes} minutes and {seconds} seconds!'
)
