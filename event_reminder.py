from datetime import date
import winsound

item = ''

events = {}

dt = date.today()

for k, v in events.items():
    if dt == date(*v['bday']):
        item = item + ' ' + k


if item != 0:
    print(item,' have Birthday Today!!!!!!')
    winsound.Beep(128,2000)

