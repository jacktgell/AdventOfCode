
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