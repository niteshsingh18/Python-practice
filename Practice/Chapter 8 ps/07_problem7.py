
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Harry", "Rohan", "Shubham", "an", 'anjali']

print(rem(l, "an"))