
import numpy as np

data = np.loadtxt('input.txt')

print np.sum(data.max(axis=1) - data.min(axis=1))

def get_nb(line):
    for a in line:
        for b in line:
            if a != b:
                if a % b == 0:
                    return a/b


print np.sum([get_nb(line) for line in data])

