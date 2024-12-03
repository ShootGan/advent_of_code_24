import re

def get_data(file_path:str) -> str:
    with open(file_path) as file:
        return file.read()

def get_operations_list(data_stream:str) -> list:
    pattern = r"mul\(([0-9]+,[0-9]+)\)"
    return re.findall(pattern, data_stream)

def multiply_and_sum(number_pairs:list) -> int:
    result = 0
    for pair in number_pairs:
        a, b = pair.split(',')
        result += int(a) * int(b)
    return result

def reomve_uncorrect_data(data_stream:str) -> str:
    pattern = r"don't\(\).*?(?:(?:do\(\))|$)"
    return re.sub(pattern, '', data_stream.replace('\n', ''))
    
if __name__ == '__main__':
    #Part 1
    input_str = get_data('day3/input.txt')
    pairs = get_operations_list(input_str)
    part_one_result = multiply_and_sum(pairs)
    print(f'Part one solution: {part_one_result}')

    #Part 2 
    cleared_data = reomve_uncorrect_data(input_str)
    pairs = get_operations_list(cleared_data)
    part_two_result = multiply_and_sum(pairs)
    print(f'Part two solution: {part_two_result}')
