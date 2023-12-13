import os
import re
from pathlib import Path
"""

https://www.w3schools.com/python/python_regex.asp
link do opisu re

"""
# Ustawienie ścieżki do pulpit/wsb
desktop_path = Path.home() / 'Desktop' / 'wsb'
print(desktop_path)

print('\n 1..................')
for root, dirs, files in os.walk(desktop_path):
    for filenames in files:
        if 'day_01' in root:
            print(filenames)

print('\n 2..................')
for root, dirs, files in os.walk(desktop_path):
    for filenames in files:
        if not filenames.startswith('.'):
            x = re.search('\.git', root)
            y = re.search('\.idea', root)
            z = re.search('venv', root)
            q = re.search('__pycache__', root)
            if x is None and y is None and z is None and q is None:
                print(root, filenames)


# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x) ## zwraca <re.Match object; span=(0, 17), match='The rain in Spain'> gdy znajdzie i None gdy nie znajdzie

#
# for a, b, c in os.walk(desktop_path / 'wsb'):
#     print(f'{a} = a -> to jest root') ## ścieżka
#     print(f'{b} = b -> to jest dirs') ## foldery, tzw directory
#     print(f'{c} = c -> to jest files') ## pliki -> files


