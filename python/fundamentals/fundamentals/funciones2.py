

def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))
#should return [5,4,3,2,1,0]



def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))
#should print 1 and return 2



def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))
#should return 6 (first value: 1 + length: 5)




def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#should print 3 and return [5,3,4]
#values_greater_than_second([3]) should return False



def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
#should return [7,7,7,7]
#should return [2,2,2,2,2,2]