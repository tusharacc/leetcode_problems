import random
from datetime import datetime
#import profile

@profile
def mergeTwoLists(l1,l2):
    return sorted(l1+l2)
    
@profile
def mergeTwoLists2(l1,l2):
    l1.extend(l2)
    return sorted(l1)

@profile
def mergeTwoLists3(l1,l2):
    return (l1+l2).sort()

if __name__ == '__main__':
    for i in range(1,100):
        len_l1 = random.randint(0,1000)
        len_l2 = random.randint(0,1000)
        l1 = []
        l2 = []
        for j in range(len_l1):
            l1.append(random.randint(0,1000))
        
        for j in range(len_l2):
            l2.append(random.randint(0,1000))

        #start = datetime.now()
        mergeTwoLists(l1,l2)
        mergeTwoLists2(l1,l2)
        mergeTwoLists3(l1,l2)
        #end = datetime.now()
        #print ("{}-{}-{}".format(len(l1),len(l2),end-start))
    #print (dis.dis(mergeTwoLists))
    #print (dis.dis(mergeTwoLists2))
    #print (dis.dis(mergeTwoLists3))