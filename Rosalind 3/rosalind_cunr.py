from math import prod

with open (r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_cunr.txt', 'r') as file:
    n = int(file.readline())
    modulo = 1000000

print(prod(range((2*n - 5), 0, -2)) % modulo)
