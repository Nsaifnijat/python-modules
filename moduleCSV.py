
import csv

channels=['EPYTHON LAB', 'Telegram Signals Copier', 'Telegram To MT4 Copier', 'Telegram', 'Test', 'Telegram MT4 Copier Forum', 'Ok', 'TradeCenter', 'Python Discussion', 'crazyfxtrader', 'Zest']

with open("alljang.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(channels) 
  

with open('alljang.csv', "r") as f:
  reader = csv.reader(f, delimiter=",",lineterminator="\n")
  for row in reader:
      print(row)
      print(type(row))
