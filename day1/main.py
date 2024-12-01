
def load_lists (filename:str ) -> list:
    with open(filename) as file:
        left, right = zip(*(line.strip().split('   ') for line in file))
    return left, right

def get_part_one_results (left_list:list, right_list:list) -> int:
    results:int = 0
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    for left, right in zip(left_sorted, right_sorted):
        results += abs(int(right) - int(left))
    return results


if __name__ == '__main__':
    #load 
    left_list, right_list = load_lists('day1/input.txt')
    #part one nice
    result_readble = get_part_one_results(list(left_list), list(right_list))
    print(f'Part one readable solution: {result_readble}')

     #part one one liner
    result_one_liner = sum(abs(int(right) - int(left)) for left, right in zip(sorted(left_list), sorted(right_list)))
    print(f'Part one one liner solution: {result_one_liner}')

    #part two
    result_part_two = sum((int(number) * right_list.count(number)) for number in left_list)
    print(f'Part two solution: {result_part_two}')

