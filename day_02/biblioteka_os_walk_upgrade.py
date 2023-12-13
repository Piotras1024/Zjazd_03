import os
import re
from pathlib import Path

# Stałe dla wzorców regex
IGNORE_PATTERNS = ['\.git', '\.idea', 'venv', '__pycache__']

# Ustawienie ścieżki do pulpit/wsb
desktop_path = Path.home() / 'Desktop' / 'wsb'
print(desktop_path)

print('\n 2..................')
for root, dirs, files in os.walk(desktop_path):
    # List comprehension do filtrowania plików
    files_to_print = [f for f in files if not f.startswith('.') and
                      not any(re.search(pattern, root) for pattern in IGNORE_PATTERNS)]

    for filename in files_to_print:
        print(root, filename)
