import os
import time
from pathlib import Path

print(os.getcwd())                          ## os.getcwd() -> aktualna ścieżka
os.chdir(r'C:\Users\Piotr\Desktop')         ## os.chdir(r'PATH') -> przejście na ścieżke PATH
print(os.getcwd())
time.sleep(2)
os.mkdir('Folder1')                         ## os.mkdir('Folder1') -> stworzenie nowego folderu w
                                            ## aktualnej ścieżce (os.getcwd())

time.sleep(2)

os.rename('Folder1', 'Folder2')             ## zmiana nazwy z Folder1 na Folder2 w aktualnym katalogu

time.sleep(2)

os.rmdir('Folder2')                         ## os.rmdir('Folder1') usuwa Folder1 z bieżącego katalogu
time.sleep(2)

print(os.environ)                           ## os.environ -> wyświetla wszystkie zmienne środowiskowe
                                            ## dla bieżącego procesu


os.chdir(Path.home())
print(os.getcwd())
# w command line1
# zobacz dane ipconfig /all -> wszystkie dane
# ipconfig /all > result.txt        -> w ten sposób wszystkie dane z ipconfig wrzuć do pliku result.txt
#
# C:\Users\Piotr>
# C:\Users\Piotr>cd C:\Users\Piotr\Desktop
#
# C:\Users\Piotr\Desktop>cd
# C:\Users\Piotr\Desktop
#
# C:\Users\Piotr\Desktop>ipconfig /all > result.txt
