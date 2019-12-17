with(open('rosalind_tree.txt', 'r')) as f:
    nodes = int(f.readline())
    grap = [line.split() for line in f]
    
edges= nodes-len(grap)-1

print(edges)