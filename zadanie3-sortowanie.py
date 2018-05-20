import numpy
import random
import time
class quickSort():
    def __init__(self):
        #self.unsortedData=data
        stop = len(data)
        start=0
        #sor=self.sort(data)
        # sorted(data)
       #

    def sort(self,unsortedData):
        if self.check(unsortedData):
            return unsortedData
        leftPointer = 0
        rightPointer = len(unsortedData)-1
        pivot = unsortedData[0]
        while not leftPointer>rightPointer:
            try:
                if unsortedData[leftPointer]>=pivot and unsortedData[rightPointer]<=pivot:
                    self.replace(unsortedData,leftPointer,rightPointer)
                    leftPointer+=1
                    rightPointer-=1
                elif unsortedData[leftPointer]<pivot:
                    leftPointer+=1
                elif unsortedData[rightPointer]>pivot:
                    rightPointer-=1
            except Exception as e:
                print(leftPointer,rightPointer,e,"Whats a problem?")
        left=self.sort(unsortedData[0:leftPointer])
        right=self.sort(unsortedData[leftPointer:len(unsortedData)])
        return left + right



    def replace(self,data,lpointer,rpointer):
        temporary = data[lpointer]
        data[lpointer]=data[rpointer]
        data[rpointer]=temporary

    def check(self,data):
        if len(data)<=1:
            return True

class BumbleSort():
    def __init__(self):
        #print(self.sort (data))
        pass

    def sort(self,data):
        sorting = True
        while sorting:
            sorting = False
            for i in range(1,len(data)):
                if (data[-i-1]>data[-i]):
                    self.replace(data,-i-1,-i)
                    sorting=True
                    break
        return data


    def replace(self,data,lpointer,rpointer):
        temporary = data[lpointer]
        data[lpointer]=data[rpointer]
        data[rpointer]=temporary


class selectionSort():
    def __init__(self):
        pass
        #print(self.sort (data))

    def sort(self,data):
        index=0
        for i in range(len(data)-1):
            try:
                min=data[i]
            except:
                pass
            for j in range(i,len(data)):
                try:
                    if data[j]<=min:
                        min=data[j]
                        index=j


                except:
                    pass
            self.replace(data,i,index)
        return data




    def replace(self,data,lpointer,rpointer):
        temporary = data[lpointer]
        data[lpointer]=data[rpointer]
        data[rpointer]=temporary



if __name__=="__main__":
    data=[random.randint(1, 10) for i in range(5000)]
    bombel = BumbleSort()
    selection = selectionSort()
    quick = quickSort()
    print(data,"Przed Sortowaniem")
    start = time.time()
    result = bombel.sort(data)
    end = time.time()
    print("algorytm bombelkowy czas - ",end - start,"ms")
    print("wynik",result)

    data = [random.randint(1, 10) for i in range(5000)]
    print(data, "Przed Sortowaniem")
    start = time.time()
    result = selection.sort(data)
    end = time.time()
    print("algorytm selection sort czas - ", end - start, "ms")
    print("wynik", result)

    data = [random.randint(1, 10) for i in range(5000)]
    print(data, "Przed Sortowaniem")
    start = time.time()
    result = quick.sort(data)
    end = time.time()
    print("algorytm quickSort czas - ", end - start, "ms")
    print("wynik", result)
    #data=np.random(20)
    # print(data)
    # s=selectionSort(data)
    # sor = BumbleSort(data)
    # # print(data)
    # sorting = quickSort(data)


