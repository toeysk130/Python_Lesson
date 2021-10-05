# Exercise 1: Reverse each word of a string

str = 'My Name is Jessa'
def solution(str):
    output = ""
    split_str = str.split()
    for i in range(len(split_str)):
        output += split_str[i][::-1]
        if i != len(str.split())-1:
            output += " "
    return output
    
# print(solution(str))

# Exercise 3: Renove items from a list while iterating
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def solution(list):
    i = 0
    n = len(list)
    
    while i < n:
        if list[i] > 50:
            del list[i]
            n = n - 1
        else:
            i = i + 1
    return list
            
# print(solution(number_list))

# Excercise 7: Print the foloowing number pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

def solution():
    value = 1
    size = 5
    for i in range(0,5):
        result_str = ""
        for j in range(0,size - value + 1):
            result_str = f"{result_str} {value}"
        value += 1
        print(result_str)
        
solution()