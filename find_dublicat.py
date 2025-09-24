li = ["ai", "ml", "python", "ml", "dl", "ai"]
seen = set()
dublicat = set()
for tag in li:
    if tag in seen:
        dublicat.add(tag)
    else:
        seen.add(tag)    

print(dublicat)            