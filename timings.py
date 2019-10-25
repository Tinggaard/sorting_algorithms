from time import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sorting import *

matplotlib.rcParams['text.usetex'] = True


def spent(algorithm, liste):
    start = time()
    algorithm(liste)
    return (time() - start) * 1000




def compare(samples, lower, upper, key='avg', *algorithms):
    """
    possible keys: avg, min, max
    """

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


    ###############################################
    ################# PLOTTING ####################
    ###############################################

    #Getting each of the labels for bottom of chart
    labels = [10**i for i in range(lower, upper+1)]


    #Putting the 'key'-time into a dict
    comp = {a: [result[a][s][key] for s in result[a]] for a in result}



    x = np.arange(len(labels)) #Number of labels
    no = len(algorithms) #Number of algorithms
    width = 0.35 #Width of each bar


    fig, ax = plt.subplots()
    bars = [ax.bar(x + en*width, c[1], width, label=c[0]) for en, c in enumerate(comp.items())]


    labels = [r'$10^{' + str(n) +  r'}$' for n in range(lower, upper+1)]

    ax.set_xlabel('Size of array')
    ax.set_ylabel('Time in milliseconds')
    ax.set_title('Comparison of sorting algorithms')
    ax.set_xticks(x + width/no)
    ax.set_xticklabels(labels)
    ax.legend()


    # Plotting the value of the bar on top of it
    for bar in bars:
        for rect in bar:
            height = int(rect.get_height())
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    fig.tight_layout()
    plt.show()




samples = 5
lower = 0
upper = 4


c = compare(samples, lower, upper, 'avg', merge_sort, tim_sort)
# show_comparison(c)
