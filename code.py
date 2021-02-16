def consecutives(list):
    count = 1
    empty = []
    final = []
    for i in range(len(list) - 1):
        Item = list[i]
        if Item == list[i + 1]:
            count = count +1
        else:
            empty.append(count)
            count = 1
    for i in empty:
        if i > 1:
            final.append(i)
    return final
    
#example

I =  [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]

def consecutives(list):
    count = 1
    empty = []
    final = []
    for i in range(len(list) - 1):
        Item = list[i]
        if Item == list[i + 1]:
            count = count +1
        else:
            empty.append(count)
            count = 1
    for i in empty:
        if i > 1:
            final.append(i)
    return final
    
consecutives(I)

#returns: [3, 2, 2]

### Maximum Consecutives

def max_cons(list):
    count = 1
    empty = []
    for i in range(len(list) - 1):
        Item = list[i]
        if Item == list[i + 1]:
            count = count +1
        else:
            empty.append(count)
            count = 1
    return max(empty)

#Example
I =  [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]

def max_cons(list):
    count = 1
    empty = []
    for i in range(len(list) - 1):
        Item = list[i]
        if Item == list[i + 1]:
            count = count +1
        else:
            empty.append(count)
            count = 1
    return max(empty)
max_cons(I)

#returns: 3

