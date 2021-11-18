def count_down(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
count = count_down(5)
print(count)

def print_return(list):
    print(list[0])
    return list[1]
print_and_return = print_return([3,8])
print(print_and_return)

def first_plus_length(list):
    return list[0] + len(list)
list_sum = first_plus_length([10,2,3,4])
print(list_sum)

def greater_than_second(list):
    new_list = []
    for i in list:
        if len(list) > 1:
            if i > list[1]:
                new_list.append(i)
    if len(list) > 1:
        print(len(new_list))
        return new_list
    elif len(list) < 2:
        return False
print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))

def length_value(size, value):
    new_list = []
    for i in range(0, size):
        new_list.append(value)
    return new_list
print(length_value(4,7))
print(length_value(6,2))

