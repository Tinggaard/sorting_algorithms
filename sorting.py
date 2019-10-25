import random

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


#Check if sorted, used for random_sort
def check_sort(A):
    return all([A[i] <= A[i+1] for i in range(len(A) - 1)])



def random_sort(A):
    """
    This function shuffles the array in place and checs if it's been sorted,
    otherwise it repeats.
    """

    #While not sorted: shuffle
    while not check_sort(A):
        random.shuffle(A)
    return A


def insertion_sort(A, show_progress=False):
    """
    Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

    // Sort an arr[] of size n
    insertionSort(arr, n)
    Loop from i = 1 to n-1.
    ……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]
    """

    #Iterate over list from index 1
    for k in range(1, len(A)):
        if show_progress:
            print(A)

        #Initiate variable for index counting
        i = k

        #While the 2nd item is bigger than the first and the is is > -1
        while A[i] < A[i-1] and i != 0:
            #Swap indexes and decrement i
            A[i], A[i-1] = A[i-1], A[i]
            i-=1

    if show_progress:
        print(A)

    return A


def selection_sort(A, show_progress=False):
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

    #Iterate the array as many times as there are items-1
    for k in range(len(A)-1):
        if show_progress:
            print(A)

        #Reference value for comparison
        ref = k

        #Find the smallest item of the array and put it in the front
        for i in range(k+1, len(A)):
            if A[i] < A[ref]:
                ref = i

        A[ref], A[k] = A[k], A[ref]

    if show_progress:
        print(A)

    return A



def merge_sort(A, show_progress=False):
    """
    Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
    It divides input array in two halves, calls itself for the
    two halves and then merges the two sorted halves. The merge()
    function is used for merging two halves. The merge(arr, l, m, r)
    is key process that assumes that arr[l..m] and arr[m+1..r]
    are sorted and merges the two sorted sub-arrays into one.
    """

    #If only 1 element in array, return
    if len(A) < 2:
        return A
    #Devide array on the middle until all arrays of 1 element
    mid = int(len(A) / 2)
    l = merge_sort(A[:mid], show_progress)
    if show_progress:
        print(l)
    r = merge_sort(A[mid:], show_progress)
    if show_progress:
        print(r)

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


def bubble_sort(A, show_progress=False):
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    """

    for i in range(len(A) - 1):
        swapped = False

        for j in range(0, len(A) - i - 1):
            if A[j] > A[j+1]:

                if show_progress:
                    print(A)

                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        if not swapped:
            break

    if show_progress:
        print(A)

    return A


def tim_sort(A):
    """
    The default python sorting algorithm
    """
    return sorted(A)





# To do some testing
if __name__ == '__main__':

    A = random_liste(10)

    sorteret = merge_sort(A, True)
    print(sorteret)
