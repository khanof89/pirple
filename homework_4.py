myUniqueList = []
myLeftovers = []


def addToLeftovers(value):
    global myLeftovers
    myLeftovers.append(value)


def addToList(value):
    global myUniqueList
    if value not in myUniqueList:
        myUniqueList.append(value)
        return True
    else:
        addToLeftovers(value)
        return False


addToList(34)

print(myUniqueList)

addToList(55)

print(myUniqueList)

addToList(55)

addToList(55)

print(myUniqueList)

print(myLeftovers)
