

def BubbleSort(L):

    for i in range(len(L)):
        for j in range(i,len(L)):
            if L[i]<L[j]:
                L[i],L[j]=L[j],L[i]

    return L

print(BubbleSort([4,2,3,1,8,90]))