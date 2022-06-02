
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

def Day2_21_P2():
    data = Get_txt(r'Data/D2Y21_dataP1.txt')
    data = [[sample.split()[0], int(sample.split()[1])] for sample in data]
    aim = 0
    position = 0
    depth = 0
    for sample in data:
        if sample[0] == 'forward':
            position += sample[1]
            depth += (aim * sample[1])
        elif sample[0] == 'down':
            aim += sample[1]
        elif sample[0] == 'up':
            aim -= sample[1]
    return position * depth

def Day3_21_P1():
    data = Get_txt(r'Data/D3Y21_dataP1.txt')
    gamma = 0
    for bit in range(len(data[0])):
        ones = 0
        zeros = 0
        for sample in data:
            if sample[bit] == '1':
                ones += 1
            elif sample[bit] == '0':
                zeros += 1
            else:
                print(f'unexpected val: {bit}')
        gamma = gamma << 1
        if ones > zeros:
            gamma += 1

    return gamma * (~gamma & 0xfff)

def Day3_21_P2():
    data = Get_txt(r'Data/D3Y21_dataP1.txt')
    oxygen_ratings = [int(sample, 2) for sample in data]
    CO2_ratings = oxygen_ratings
    oxygen_rating = Find_Ratings_Criteria(oxygen_ratings, "most")
    CO2_rating = Find_Ratings_Criteria(CO2_ratings, "least")
    return oxygen_rating[0]*CO2_rating[0]

def Day4_21_P1():
    data = Get_txt(r'Data/D4Y21_dataP1.txt')
    sequence = data.pop(0)
    sequence = [int(val) for val in sequence.split(',')]
    data.pop(0)
    cards = [[]]
    card = 0

    for line in data:
        if line == '':
            card += 1
            cards.append([])
        else:
            vals = [int(val) for val in line.split()]
            cards[card].append(vals)

    for i, table in enumerate(cards):
        for j in range(5):
            cards[i].append([table[0][j], table[1][j], table[2][j], table[3][j], table[4][j]])

    Flag = False
    for i in range(5, len(sequence)):
        for j, card in enumerate(cards):
            for combination in card:
                if all(elem in sequence[:i] for elem in combination):
                    winning_card = j
                    winning_stats = [winning_card, sequence[:i]]
                    Flag = True
                if Flag:
                    break
            if Flag:
                break
        if Flag:
            break

    sequence = winning_stats[1]
    winning_card = cards[winning_stats[0]][0:5]
    unselected = []
    for set in winning_card:
        for val in set:
            if val not in sequence:
                unselected.append(val)

    return sum(unselected)*sequence[-1]























