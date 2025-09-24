tags = ["bat", "tab", "cat", "act"]

groups ={}

for i in tags:
    key = "".join(sorted(i))
   
    if key not in groups:
        groups[key]=[]
    groups[key].append(i)
print(list(groups.values()))        