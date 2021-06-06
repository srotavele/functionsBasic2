#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
def thisLthatV(size, value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList


x = thisLthatV(5, 7)
print(x)
