#1. Countdown
def countdown(num):
    nums_list = []
    for val in range(num, -1, -1):
        nums_list.append(val)
    return nums_list
# print(countdown(5))

#2. Print and Return
def print_return(nums_list):
    print(nums_list[0])
    return(nums_list[1])
# print(print_return([2, 5]))

#3.First Plus Length
def first_plus_len(nums_list):
    sum = nums_list[0] + len(nums_list)
    return sum
# print(first_plus_len([1,2,3,4,5]))


#4. Values Greater than Second
def greater_than_second(nums_list):
    new_list = []
    second_val = nums_list[1]
    if len(nums_list) < 2:
        return false
    for idx in range(len(nums_list)):
        if nums_list[idx] > second_val:
            new_list.append(nums_list[idx])
    return new_list
# print(greater_than_second([1,2,3,4,5,6]))

#5. This Length, That Value
def length_value(size, value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list
print(length_value(6, 2))