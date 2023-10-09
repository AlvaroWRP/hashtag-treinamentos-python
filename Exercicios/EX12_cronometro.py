import time

seconds, minutes, hours = 0, 0, 0

print('Começou!', '\n')

while True:
    print(
        f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    )

    time.sleep(1)
    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1
    
    if minutes == 60:
        minutes = 0
        hours += 1
