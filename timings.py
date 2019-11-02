from time import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sorting import *
import argparse

# matplotlib.rcParams['text.usetex'] = True


def spent(algorithm, liste):
    start = time()
    algorithm(liste)
    return (time() - start) * 1000




def compare(samples, lower, upper, key='avg', plot=True, *algorithms):

    tal = random_dict(samples, lower, upper)

    #create dict for results
    result = {a.__name__: {10**i: {} for i in range(lower, upper+1)} for a in algorithms}

    #Iterating algorithms
    for a in algorithms:

        #Creating stats
        for k in tal.keys():
            result[a.__name__][k]['samples'] = [spent(a, l) for l in np.copy(tal[k])]
            #Have to np.copy, to ensure deep copy

            result[a.__name__][k]['min'] = min(result[a.__name__][k]['samples'])
            result[a.__name__][k]['max'] = max(result[a.__name__][k]['samples'])
            result[a.__name__][k]['avg'] = sum(result[a.__name__][k]['samples']) / samples

        print('Done with {alg}, {nr}/{of}'.format(alg=a.__name__, nr=algorithms.index(a)+1, of=len(algorithms)))

    if not plot:
        return result

    ###############################################
    ################# PLOTTING ####################
    ###############################################

    #Getting each of the labels for bottom of chart
    labels = [10**i for i in range(lower, upper+1)]


    #Putting the 'key'-time into a dict
    comp = {a: [result[a][s][key] for s in result[a]] for a in result}



    x = np.arange(len(labels)) #Number of labels
    no = len(algorithms) #Number of algorithms
    width = 0.7 / no #Width of each bar


    fig, ax = plt.subplots()
    bars = [ax.bar(x + en*width, c[1], width, label=c[0]) for en, c in enumerate(comp.items())]


    labels = [r'$10^{' + str(n) + r'}$' for n in range(lower, upper+1)]

    ax.set_xlabel('Size of array')
    ax.set_ylabel('Time in milliseconds')
    ax.set_title('Comparison of sorting algorithms with {} samples and key: \'{}\''.format(len(labels), key))
    ax.set_xticks(x + (width/2)*(no-1))
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





def main():
    functions = {'bubble_sort': bubble_sort,
    'insertion_sort': insertion_sort,
    'selection_sort': selection_sort,
    'merge_sort': merge_sort,
    'tim_sort': tim_sort}

    parser = argparse.ArgumentParser(description='Compare sorting algorithms')

    parser.add_argument('-s', '--samples', default=3, type=int, help='Number of samples')

    parser.add_argument('-l', '--lower', default=1, type=int, help='The minimum size of the array as a power of 10')

    parser.add_argument('-u', '--upper', default=4, type=int, help='The maximum size of the array as a power of 10')

    parser.add_argument('-k', '--key', default='avg', type=str, help='The key to use for the timings, \
    valid keys are: \'avg\', \'min\', \'max\'')

    parser.add_argument('-q', '--quiet', dest='plot', action='store_false', help='Weather to plot or not')
    parser.set_defaults(plot=True)

    parser.add_argument('-f', '--functions', default='merge_sort', nargs='+', type=str, help='The sorting algorithms to use')


    args = parser.parse_args()



    return compare(args.samples, args.lower, args.upper, args.key, args.plot, *[functions[k] for k in args.functions])


if __name__ == '__main__':
    main()
