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

        #Creating stats
        for k in tal.keys():
            result[a.__name__][k]['samples'] = [spent(a, l) for l in tal[k]]

            result[a.__name__][k]['min'] = min(result[a.__name__][k]['samples'])
            result[a.__name__][k]['max'] = max(result[a.__name__][k]['samples'])
            result[a.__name__][k]['avg'] = sum(result[a.__name__][k]['samples']) / samples



    return result





def show_comparison(result, key='avg'):
    """
    possible keys: avg, min, max
    """


    #Getting each of the values
    values = list(result[str(list(result.keys())[0])].keys())


    #Putting the 'key'-time into a dict
    comp = {a: [result[a][s][key] for s in result[a]] for a in result}


    #Plotting the different algorithms
    for c in comp:
        plt.semilogx(values, comp[c], 'x')

    #Must all bast at once, for legend to work
    plt.legend([k for k in result])

    plt.xlabel('Size of array')
    plt.ylabel('Time')

    plt.show()



samples = 5
lower = 0
upper = 4


c = compare(samples, lower, upper, merge_sort, builtin_sort)
show_comparison(c)
