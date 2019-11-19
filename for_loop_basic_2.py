#1. Biggie Size
def biggie_size(list):
    for idx in range(len(list)):
        if list[idx] > 0:
            list[idx] = "big"
    return list
# print(biggie_size([-1, 3, 5, -5]))

#2. Count Positives
def count_positives(list):
    pos_count = 0
    for idx in range(len(list)):
        if list[idx] > 0:
            pos_count += 1
    list.pop(len(list) - 1)
    list.append(pos_count)
    return list
# print(count_positives([-1,1,1,1]))

#3.Sum Total
def sum_total(list):
    sum = 0
    for idx in range(len(list)):
        sum = sum + list[idx]
    return sum
# print(sum_total([1,2,3,4,5]))

#4.Average
def average(list):
    sum = 0
    for idx in range(len(list)):
        sum = sum + list[idx]
    avg = sum / len(list)
    return avg
# print(average([1,2,3,4]))

#5. Length
def length(list):
    return len(list)
# print(length([1,2,3,4,5]))

#6. Minimum
def minimum(list):
    if len(list) == 0:
        return false
    min = list[0]
    for val in range(len(list)):
        if list[val] < min:
            min = list[val]
    return min
# print(minimum([1,-4,2,-5,1,0]))

#7. Maximum
def maximum(list):
    if len(list) == 0:
        return false
    max = list[0]
    for val in range(len(list)):
        if list[val] > max:
            max = list[val]
    return max
# print(maximum([1,-4,2,-5,1,0]))

#8. Ultimate Analysis
def ultimate_analysis(lst):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

# print(ultimate_analysis([37, 2, 1, -9]))
# print(ultimate_analysis([]))

#9. Reverse List
def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst
# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9, 5]))
# print(reverse_list([]))
# print(reverse_list([1]))
# print(reverse_list([1, 2]))