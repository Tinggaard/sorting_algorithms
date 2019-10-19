import random
import numpy as np


def random_liste(count):
    """
    Returning a list containing 'count' no. of elements
    with random values between 0 and 100 (both inclusive)
    """

    #Return a list of len 'count', with random numbers from 0..100
    return [random.randint(0, 100) for _ in range(count)]


#Dictionary of random lists
def random_dict(samples, lower_power, upper_power):
    """
    Used for testing operation speeds of different algorithms
    """

    return {10**i : [random_liste(10**i) for _ in range(samples)] for i in range(lower_power,upper_power+1)}



def random_sort(liste):
    """
    This function shuffles the list in place and checs if it's been sorted,
    otherwise it repeats.
    """

    #Check if sorted
    def check_sort(liste):
        return all([liste[i] <= liste[i+1] for i in range(len(liste) - 1)])

    count = 0
    #While not sorted: shuffle
    while not check_sort(liste):
        random.shuffle(liste)
        count +=1
    return liste, count


def insertion_sort(liste, show_progress=False):
    """
    Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

    // Sort an arr[] of size n
    insertionSort(arr, n)
    Loop from i = 1 to n-1.
    ……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]
    """

    comp = moves = 0
    #Iterate over list from index 1
    for k in range(1, len(liste)):
        if show_progress:
            print(liste)

        #Initiate variable for index counting
        i = k

        #While the 2nd item is bigger than the first and the is is > -1
        while liste[i] < liste[i-1] and i != 0:
            comp += 1
            moves += 1
            #Swap indexes and decrement i
            liste[i], liste[i-1] = liste[i-1], liste[i]
            i-=1
        comp += 1

    if show_progress:
        print(liste)

    return comp, moves


def selection_sort(liste, show_progress=False):
    """
    The selection sort algorithm sorts an array by repeatedly
    finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning.
    The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element
    (considering ascending order) from the unsorted subarray
    is picked and moved to the sorted subarray.
    """

    comp = moves = 0
    #Iterate the array as many times as there are items-1
    for k in range(len(liste)-1):
        if show_progress:
            print(liste)

        #Reference value for comparison
        ref = k

        #Find the smallest item of the array and put it in the front
        for i in range(k+1, len(liste)):
            comp += 1
            if liste[i] < liste[ref]:
                ref = i

        moves += 1
        liste[ref], liste[k] = liste[k], liste[ref]

    if show_progress:
        print(liste)

    return comp, moves



def merge_sort(liste):
    """
    Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
    It divides input array in two halves, calls itself for the
    two halves and then merges the two sorted halves. The merge()
    function is used for merging two halves. The merge(arr, l, m, r)
    is key process that assumes that arr[l..m] and arr[m+1..r]
    are sorted and merges the two sorted sub-arrays into one.
    """

    #If only 1 element in array, return
    if len(liste) < 2:
        return liste
    #Devide array on the middle until all arrays of 1 element
    mid = int(len(liste) / 2)
    l = merge_sort(liste[:mid])
    r = merge_sort(liste[mid:])

    # sort the 2 single elements
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            result.append(r[j])
            j += 1

        else:
            result.append(l[i])
            i += 1

    result += l[i:] + r[j:]

    return result


def bubble_sort(liste):
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    """
    comp = moves = 0

    for i in range(len(liste) - 1):
        swapped = False

        for j in range(0, len(liste) - i - 1):
            comp += 1
            if liste[j] > liste[j+1]:
                moves += 1
                liste[j], liste[j+1] = liste[j+1], liste[j]
                swapped = True

        if not swapped:
            break

    return comp, moves


def builtin_sort(liste):
    """
    The default python sorting algorithm
    """
    return sorted(liste)





# To do some testing
if __name__ == '__main__':

    liste = random_liste(50)

    sorteret = merge_sort(liste)
    print(sorteret)
