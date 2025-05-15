import random
import time

class Sort:
    def __init__(self):
        self.name="noname"

    def Sort(self,L):
        return L, -1


class MaxSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Max"

    def Sort(self, list):
        start = time.time()
        sorted=[]
        while len(list)>0:
            mx=max(list)
            sorted.append(mx)
            list.remove(mx)
        end = time.time()
        return sorted, end-start


class BubbleSort(Sort):
    def __init__(self):
        self.name="Bubble Sort"

    def Sort(self,list ):
        start = time.time()
        for iter_num in range(len(list) - 1, 0, -1):
            for idx in range(iter_num):
                if list[idx] > list[idx + 1]:
                    temp = list[idx]
                    list[idx] = list[idx + 1]
                    list[idx + 1] = temp
        end = time.time()
        return list, end-start

class MergeSort(Sort):
    def __init__(self):
        self.name="Merge Sort"

    def __merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
        # Liste orta noktasını bul ve ikiye ayır
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.__merge_sort(left_list)
        right_list = self.__merge_sort(right_list)
        return list(self.__merge(left_list, right_list))

    # Sıralanmış alt grupları birleştir

    def __merge(self, left_half, right_half):

        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

    def Sort(self, unsorted_list):
        start = time.time()
        InputList=self.__merge_sort(unsorted_list)
        end = time.time()
        return InputList, end - start

class InsertionSort(Sort):
    def __init__(self):
        self.name="Insertion Sort"

    def Sort(self, InputList):
        start = time.time()

        for i in range(1, len(InputList)):
            j = i - 1
            nxt_element = InputList[i]
            # Liste elemanını bir sonraki ile kıyasla

            while (InputList[j] > nxt_element) and (j >= 0):
                InputList[j + 1] = InputList[j]
                j = j - 1
            InputList[j + 1] = nxt_element
        end = time.time()

        return InputList, end-start

class SelectionSort(Sort):
    def __init__(self):
        self.name="Selection Sort"

    def Sort(self,input_list):
        start = time.time()
        for idx in range(len(input_list)):

            min_idx = idx
            for j in range(idx + 1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
            # Swap the minimum value with the compared value

            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        end = time.time()
        return input_list,end-start

class ShellSort(Sort):
    def __init__(self):
        self.name="Shell Sort"

    def Sort(self,input_list):
        start = time.time()

        gap = len(input_list) // 2
        while gap > 0:

            for i in range(gap, len(input_list)):
                temp = input_list[i]
                j = i
                # Sort the sub list for this gap

                while j >= gap and input_list[j - gap] > temp:
                    input_list[j] = input_list[j - gap]
                    j = j - gap
                input_list[j] = temp

            # Reduce the gap for the next element

            gap = gap // 2
        end = time.time()
        return input_list, end-start

class Test:
    def __init__(self):
        self.algorithms=[]
        self.performance={}


    def CreateObjects(self):
        self.algorithms.append(Sort())
        self.algorithms.append(BubbleSort())
        self.algorithms.append(MergeSort())
        self.algorithms.append(ShellSort())
        self.algorithms.append(InsertionSort())
        self.algorithms.append(SelectionSort())
        self.algorithms.append(MaxSort())


    def GenerateInputSet(self,n):
        liste = []
        for i in range(n):
            liste.append(random.randint(0, 1000))
        return liste

    def Test(self):
        self.CreateObjects()
        for i in self.algorithms:
            l = self.GenerateInputSet(1000)
            l, d = i.Sort(l)
            self.performance[i.name]=d
            print("name: ", i.name, " duration :",d)

    def ShowPerformanceMatrix(self):
        perfM=[]
        baslik=["Performans"]
        for i in self.performance.keys():
            baslik.append(i)
        perfM.append(baslik)

        for i in self.performance.keys():
            satir=[i]
            for j in self.performance.keys():
                oran = self.performance[i]/self.performance[j]
                satir.append(oran)
            perfM.append(satir)

        for i in perfM:
            print(i)
        return perfM


#test0= Test()

#test0.Test()
#test0.ShowPerformanceMatrix()

t=MergeSort()
t.Sort([4,2,5,1])