import argparse

parser = argparse.ArgumentParser(description='Program checking text files')
parser.add_argument('filename', help='nazwa pliku do otwarcia, plik powinien być w aktualnej sciezce')
# parser.add_argument('mode')
parser.add_argument('-m', '--mode', help='tryb pliku do odczytu r, w, x', required=False)
parser.add_argument('-cl', '--conflevel', help='poziom poufnosci 0-3', type=int, default=3, required=False)
args = parser.parse_args()

print('Nazwa pliku to: ',args.filename)
print('Tryb pliku to: ',args.mode)
print('Conflevel to: ', args.conflevel)