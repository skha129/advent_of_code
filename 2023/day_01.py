# import required modules
import os
import re

# declare required variables
data_path = r'C:\Code\advent_of_code\2023\data'
day = '01'

p1_test_file = fr'{day}-0-1.txt'
p2_test_file = fr'{day}-0-2.txt'
part_1_file = fr'{day}-1.txt'
part_2_file = fr'{day}-2.txt'

# functions
def solve_part_one(data):
    nums_list = [int(extract_numbers_part_1(x,'one')+extract_numbers_part_1(x[::-1],'one')) for x in data]
    #print(nums_list)
    print(sum(nums_list))

    
def solve_part_two(data):
    nums_list = [extract_numbers_part_2(x,'all') for x in data]
    print(nums_list)
    nums_list = [int(x[0]+x[-1]) for x in nums_list]
    print(nums_list)
    print(sum(nums_list))
    #print(sum(nums_list))


def extract_numbers_part_1(text:str, mode:str='all', reversed:bool='False') -> str:
    ret_str = ''
    if reversed:
        text = text[::-1]
    for char in text:
        if char.isnumeric():
            if mode=='one':
                return char
            else:
                ret_str += char

    return ret_str


def extract_numbers_part_2(text:str, mode:str='all', reversed:bool=False) -> str:
    ret_str = ''
    text = translate_numbers_l_to_r(text, reversed)
    print(text)
    for char in text:
        if char.isnumeric():
            if mode=='one':
                return char
            else:
                ret_str += char

    return ret_str


def translate_numbers_l_to_r(text:str, reversed:bool=False) -> str:
    
    ret_str = ''
    if reversed:
        text = text[::-1]

    for c in text:
        ret_str += c
        ret_str = translate_numbers(ret_str)

    return ret_str



def translate_numbers(text:str) -> str:
    map_dict = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
    }
    for i in map_dict:
        text = text.replace(i,map_dict[i])

    return text
    


def import_file(file_name):
    file_to_import = os.path.join(data_path,file_name)

    with open(file_to_import,'r') as f:
        return f.readlines()












# main function
if __name__ == '__main__':
    
    #solve_part_one(import_file(part_1_file))
    solve_part_two(import_file(part_2_file))
    