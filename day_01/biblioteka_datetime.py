# import datetime
# now = datetime.datetime.now()
# powyższe to to samo co poniższe

from datetime import datetime as dt

today = dt.today()
today = str(today)

print('Logi_' + today[11:13] + today[14:16] + '.txt')
