str ="Machine learning is fascinating"

splt = str.split()

li2 = []
for i in splt:
    
    li2.append(len(i))
   

print(f" so the longest Word and contine {max(li2)} cherecter")