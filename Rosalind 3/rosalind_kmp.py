from Bio import SeqIO
s =''
with open (r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_kmp.txt', 'r') as file:
 for record in SeqIO.parse(file,'fasta'):
        s = str(record.seq)
        n = len(s)
        failure_array = [0] * n 

j = 0  
for k in range(1, n):
    while j > 0 and s[k] != s[j]:
            j = failure_array[j - 1]

    if s[k] == s[j]:
        j += 1
        
    failure_array[k] = j
    
print(failure_array)   


with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_kmpoutput.txt', 'w') as outfile:
        for i in failure_array:
            outfile.write(str(i)+ ' ')