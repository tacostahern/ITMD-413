'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will test the efficiency of multiple sorting
algorithms across lists of multiple sizes which include 10000, 30000, 50000,
70000, and 90000 size arrays. The sorting algorithms that will be tested include
bubble sort, shell sort, and quick sort. The results will be recorded and
plotted in a graph to show the different times.
'''
import time
import random
import sys
#For use in charting, used from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    list10k = createList(10000)
    list30k = createList(30000)
    list50k = createList(50000)
    list70k = createList(70000)
    list90k = createList(90000)

    bubbleList = list()
    shellList = list()
    quickList = list()

    #Testing 10k list
    bubbleList.append(bubbleRun(list10k))
    shellList.append(shellRun(list10k))
    quickList.append(quickRun(list10k))

    
    #Testing 30k list
    bubbleList.append(bubbleRun(list30k))
    shellList.append(shellRun(list30k))
    quickList.append(quickRun(list30k))

    
    #Testing 50k list
    bubbleList.append(bubbleRun(list50k))
    shellList.append(shellRun(list50k))
    quickList.append(quickRun(list50k))

    #Testing 70k list
    bubbleList.append(bubbleRun(list70k))
    shellList.append(shellRun(list70k))
    quickList.append(quickRun(list70k))

    #Testing 90k list
    bubbleList.append(bubbleRun(list90k))
    shellList.append(shellRun(list90k))
    quickList.append(quickRun(list90k))

    labels = ['10k List', '30k List', '50k List', '70k List', '90k List']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/3, bubbleList, width, label='Bubble Sort')
    rects2 = ax.bar(x + width/3, shellList, width, label='Shell Sort')
    rects3 = ax.bar(x + width/3, quickList, width, label='Quick Sort')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time to Sort')
    ax.set_title('Times to Sort Lists of Various Sizes')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    fig.tight_layout()

    plt.show()


        
def createList(length): #creating a list of random values with a length of length
    myList = list()
    for i in range(0,length): 
        x = random.randint(1,length) #append a random range of numbers from 0 to length
        myList.append(x)
    return myList

def bubbleRun(myList):
    start_time = time.time() # start the clock
    bubbleSort(myList)
    stop_time = time.time() - start_time # stop the clock and calculate the time difference
    #print(stop_time)
    return stop_time

def shellRun(myList):
    length = len(myList)
    start_time = time.time() # start the clock
    shellSort(myList, length)
    stop_time = time.time() - start_time # stop the clock and calculate the time difference
    #print(stop_time)
    return stop_time
    

def quickRun(myList):
    start_time = time.time() # start the clock
    quickSort(myList)
    stop_time = time.time() - start_time # stop the clock and calculate the time difference
    #print(stop_time)
    return stop_time

#bubble sort code, used from https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

#shell sort code, used from https://www.programiz.com/dsa/shell-sort
def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

#quicksort code, used from https://www.reddit.com/r/AskProgramming/comments/csm1ag/python_exercise_quicksort_results_in/
def quickSort(A: list):
    if len(A) < 1: 
        return A

    pivot = int(len(A) / 2)

    A_l = [i for i in A if i < A[pivot]]

    A_r = [j for j in A if j > A[pivot]]

    A_l = quickSort(A_l)

    A_r = quickSort(A_r)

    result = A_l + [A[pivot]] + A_r

    return result

main()




     
