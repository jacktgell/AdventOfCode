
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


