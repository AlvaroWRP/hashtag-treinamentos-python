import time
import locale
import datetime

locale.setlocale(locale.LC_TIME, 'pt-BR.UTF-8')

timer = 10

starting_epoch = time.time()

while timer > 0:
    phrase = f'Time remaining: {timer} seconds'

    if timer == 1:
        print(phrase[:-1])
    else:
        print(phrase)

    time.sleep(1)
    timer -= 1

print('Done!')

ending_epoch = time.time()

print()
print(starting_epoch)
print(ending_epoch, '\n')

#####################################################################

now = datetime.datetime.now()
full_date = now.strftime('%A, %d de %B de %Y, %H horas e %M minutos.')

print(full_date)
