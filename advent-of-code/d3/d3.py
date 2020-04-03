import math

def get_dist(i):
    s = int((math.sqrt(i - 0.1) - 1)/2)*2 + 1  # 0.1 is epsilon
    r = i - np.power(s,2)
    # print s, r
    return np.abs( (r % (s + 1))  - (s + 1)/2) + (s + 1)/2


for i in [368078]:
    print get_dist(i)

# i = 368078
# print np.abs( ( (i - np.power(int((math.sqrt(i - 0.1) - 1)/2)*2 + 1,2)) % (int((math.sqrt(i - 0.1) - 1)/2)*2 + 1 + 1))  - (int((math.sqrt(i - 0.1) - 1)/2)*2 + 1 + 1)/2) + (int((math.sqrt(i - 0.1) - 1)/2)*2 + 1 + 1)/2
