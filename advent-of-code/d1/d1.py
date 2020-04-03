f_input = open('input.txt', 'r')
f_input_read = f_input.read()[:-1]

data = [ f_input_read[i] for i in range(len(f_input_read))]
# data = '12131415'
print data

cur_c = -len(data)/2 # starting at the end
next_c = 0

check = 0

while next_c < len(data):
    if data[cur_c] == data[next_c]:
        check += int(data[cur_c])

    cur_c += 1
    next_c += 1


print check
