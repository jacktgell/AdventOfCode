
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def Get_txt(path):
    with open(path) as f:
        lines = f.readlines()
    return [line.replace('\n', '') for line in lines]

def Get_txt_as_int(path):
    data_list = Get_txt(path)
    return [int(sample) for sample in data_list]

def Display_solution(func, problem):
    print(f'solution for {problem}: {func()}')

def Find_Ratings_Criteria_Most_Or_Least_Common(common, zeros, ones):

    if common == "most":
        if len(zeros) > len(ones):
            return zeros
        else:
            return ones
    else:
        if len(ones) >= len(zeros):
            return zeros
        else:
            return ones


def Find_Ratings_Criteria(ratings, common):

    for i in range(12):
        ones = []
        zeros = []
        for rating in ratings:
            if (rating << i) & 0x000800 == 0:
                zeros.append(rating)
            else:
                ones.append(rating)

        ratings = Find_Ratings_Criteria_Most_Or_Least_Common(common, zeros, ones)
        if len(ratings) == 1:
            break
    return ratings
