from time import time
import numpy as np
import matplotlib.pyplot as plt
from sorting import *


def spent(algorithm, liste):
    start = time()
    algorithm(liste)
    return time() - start




def compare(samples, lower, upper, *algorithms):

    tal = random_dict(samples, lower, upper)

    #create dict for results
    result = {a.__name__: {10**i: {} for i in range(lower, upper+1)} for a in algorithms}

    for a in algorithms:

        for k in tal.keys():
            result[a.__name__][k]['samples'] = [spent(a, l) for l in tal[k]]

            result[a.__name__][k]['min'] = min(result[a.__name__][k]['samples'])
            result[a.__name__][k]['max'] = max(result[a.__name__][k]['samples'])
            result[a.__name__][k]['avg'] = sum(result[a.__name__][k]['samples']) / samples



    return result





def show_comparison(result):

    for k in result.keys():
        plt.plot(result[k][1000]['samples'])
        plt.legend(k)

    plt.show()




c = compare(5, 3, 4, merge_sort, insertion_sort)
show_comparison(c)
