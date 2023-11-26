from itertools import product

with open (r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_lexf.txt', 'r') as file:
    symbols = file.readline().strip().split(' ')
    n = int(file.readline())

all_strings = [''.join(i) for i in product(symbols, repeat=n)]

print('\n'.join(all_strings))

    