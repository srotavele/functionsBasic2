#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
def greaterThan(myList):
    newList = []
    for i in myList:
        if i > myList[1]:
            newList.append(i)
    print(len(newList))
    return newList


x = greaterThan([2, 3, 6, 5, 7, 9, 25, 34])
print(x)
