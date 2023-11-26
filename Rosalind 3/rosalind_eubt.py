
import math

with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_eubt.txt', 'r') as file:
    taxa = file.read().split()
    trees = [['(', '(', taxa[1], ',', taxa[2], ')', ')', taxa[0], ';']]

new_items = taxa[3:]

def generate_unrootedtrees(list, new_taxa):
    new_tree = []
    for i in range(1,len(list)-2):
        j = -1
        if not list[i] in '(),;':
            j = i
        if list[i]=='(':
            m=1
            for j in range(i+1, len(list)):
                if list[j]=='(':
                    m +=1
                elif list[j]==')':
                    m -=1
                if m == 0:
                    break
        if j!=-1:
            t =  list[:i] + ['('] + list[i:j+1] + [','] + [new_taxa] + [')'] + list[j+1:]
            new_tree.append(t)
    return new_tree

for new_taxa in new_items:
    t = []
    for tree in trees:

        t2 = generate_unrootedtrees(tree, new_taxa)
        t = t + t2
    trees = t[:]

for tree in trees:
    print (''.join(tree))



    
    
