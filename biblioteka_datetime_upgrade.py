from datetime import datetime as dt

today = dt.today()

timestamp1 = today.strftime('Moja zmiena to: %d/%m/%y/%Y.txt')
print(timestamp1)

timestamp2 = today.strftime('Moja zmiena to: %H--%M--%S.txt')
print(timestamp2)

print(today.hour)
print(today.minute)
print(f'Dzisiaj jest dzień {today.day} miesiąc {today.month} i godzina {today.hour}.{today.minute}')
