import re
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_ctbl.txt', 'r') as file:
   tree = file.read().strip()


def sort(labels):
    labels = re.findall(r'\w+', labels)
    return sorted(labels)

def character_table(tree):
    taxa_labels = sort(tree)
    list = []
    count, p, subtrees = 0, [], []

    for i, symbol in enumerate(tree):
        if symbol == '(':
            count+= 1
            p.append(i)
        elif symbol == ')':
            subtree = tree[p.pop() + 1:i]
            subtrees.extend([] for _ in range(len(subtrees), count))
            subtrees[count-1].append(subtree)
            count -= 1

    for i in range(1, len(subtrees)):
        for subtree in subtrees[i]:
            list.append([1 if label in sort(subtree) else 0 for label in taxa_labels])

    return list

with open(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 3\rosalind_ctbloutput.txt", 'w') as outfile:
    for row in character_table(tree):
        outfile.write(''.join(map(str, row))+ '\n')