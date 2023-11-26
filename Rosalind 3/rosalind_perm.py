from itertools import permutations 

n = 5


all_permutations = list(permutations(range(1, n + 1)))
total_permutations = len(all_permutations)


with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_permoutput.txt', 'w') as output_file: 
        output_file.write(str(total_permutations)+'\n') 
        for element in all_permutations:  
            output_file.write(str(element).replace(',', '').replace(')', ' ').replace('(', '') +'\n')    

    
