def flatten(list1):
    result = []
    for item in list1:
        if(isinstance(item,list)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

data = [1, [2, 3], [4, [5]]]
print(flatten(data))            
