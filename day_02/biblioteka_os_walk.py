import os
import re
from pathlib import Path

print('\n 1..................')
# Ustawienie ścieżki do pulpitu
desktop_path = Path.home() / 'Desktop' / 'wsb'

print(desktop_path)

for root, dirs, files in os.walk(desktop_path):
    for filenames in files:
        if 'day_01' in root:
            print(filenames)


#
# for a, b, c in os.walk(desktop_path / 'wsb'):
#     print(f'{a} = a -> to jest root') ## ścieżka
#     print(f'{b} = b -> to jest dirs') ## foldery, tzw directory
#     print(f'{c} = c -> to jest files') ## pliki -> files


