
from helper_methods import *

def Day1_21_P1():
    data = Get_txt_as_int(r'Data/D1Y21_dataP1.txt')
    counter = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            counter += 1
    return counter

def Day1_21_P2():
    data = Get_txt_as_int(r'Data/D1Y21_dataP2.txt')

    convolved_data = [data[i-1]+data[i]+data[i+1] for i in range(1, len(data)-1)]

    counter = 0
    for i in range(1, len(convolved_data)):
        if convolved_data[i] > convolved_data[i-1]:
            counter += 1
    return counter

def Day2_21_P1():
    data = Get_txt(r'Data/D2Y21_dataP1.txt')
    data = [[sample.split()[0], int(sample.split()[1])] for sample in data]
    x = 0
    y = 0
    for sample in data:
        if sample[0] == 'forward':
            y += sample[1]
        elif sample[0] == 'down':
            x += sample[1]
        elif sample[0] == 'up':
            x -= sample[1]
    return x * y

