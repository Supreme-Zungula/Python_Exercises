# List ends
import random
def list_ends(lst):
    listEnds = []
    listEnds.append(lst[0])
    listEnds.append(lst[len(lst)-1])
    return listEnds

def test():
    myList = random.sample(range(1, 20), 10)
    print("myList = ", myList)
    print("listEnds = ", list_ends(myList))

test()