from datetime import date
import winsound

item = ''

events = {'dodo bhaiya': {'bday': (2017, 3, 1)}, 'alex': {'bday': (2017, 2, 28)}, 'raj': {'bday': (2017, 10, 17)},
          'ananya':{'bday': (2017, 3, 13)}, 'kunal':{'bday': (2017, 9, 22)}, 'punit': {'bday':(2017, 3, 28)},
          'avinash':{'bday': (2017, 6, 23)}, 'tej': {'bday': (2017, 8, 22)}, 'amul': {'bday': (2017, 8, 28)},
          'sweety':{'bday': (2017, 4, 25)}, 'soumya': {'bday':(2017, 10, 11)}, 'prashant':{'bday':(2017, 9, 17)},
          'karan':{'bday':(2017, 4, 19)}, 'raghuveer': {'bday':(2017, 12, 10)}, 'nishy':{'bday':(2017, 8, 2)},
          'anshu':{'bday':(2017, 11, 25)}, 'sps':{'bday':(2017, 5, 29)}, 'pratik':{'bday':(2017,11,9)},
          'ashwini':{'bday':(2017,6, 20)}, 'Aishwarya Srivastava':{'bday':(2017,4,22)}}

dt = date.today()

for k, v in events.items():
    if dt == date(*v['bday']):
        item = item + ' ' + k


if item != 0:
    print(item,' have Birthday Today!!!!!!')
    winsound.Beep(128,2000)

