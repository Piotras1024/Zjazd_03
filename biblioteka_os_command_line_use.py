import os
import time
from pathlib import Path
os.chdir(Path.home())
print(os.getcwd())

os.system('cmd /c "cd C:\\Users\\Piotr\\Desktop"')          ## w 2 liniach i tak stworzy results na HomePATH
os.system('cmd /c "ipconfig \all > results.txt"')


os.system('cmd /c "cd C:\\Users\\Piotr\\Desktop && ipconfig \all > results.txt"') ## w 1 lini stworzy na pulpicie

## > 1 strzałka nadpisuje !! ,>> 2 strzałki dopisują
