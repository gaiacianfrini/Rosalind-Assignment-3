from Bio import SeqIO

dna =''
with open (r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_revp.txt', 'r') as file:
    for record in SeqIO.parse(file,'fasta'):
        dna = str(record.seq)

c = ''
revp = ''
for n in dna:
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    c += complements[n]
    rev_comp = c[::-1]

def locate_sites(dna):
    r_dna = rev_comp

    for i in range(4, 13, 2):
        for length in range(len(dna)):
            s1 = dna[length:length+i]
            s2 = r_dna[len(r_dna)-length-i:len(r_dna)-length]
            if s1 == s2:
                yield length+1, i
            
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_revpoutput.txt', 'w') as outfile:
        for site in locate_sites(dna):
            outfile.write(' '.join(map(str, site)) + '\n')
