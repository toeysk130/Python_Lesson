# def solution(string):
# print(len(string.split()[-1]))
    
# solution("Just some exercise!")
    
# 20 Write a Python program to check a sequence of numbers is an arithmetic progression or not. 

# input = [2 ,4 ,6 ,8 ,10, 12]
# def solution(array):
#   for i in range(1,len(array)):
#     if i == 1:
#       diff = array[i] - array[i-1]
#     else:
#       if diff != array[i] - array[i-1]:
#         return False
#   return True
  
#21. Write a Python program to check a sequence of numbers is a geometric progression or not. Go to the editor

# input = [2, 6, 18, 54]

# def solution(array):
#   for i in range(1,len(array)):
#     if i == 1:
#       diff = array[i] / array[i-1]
#     else:
#       if diff != array[i] / array[i-1]:
#         return False
#   return True
# print(solution(input))

# 22. Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form. Go to the editor
# Input : 13, 14
# Output : 27

input1 = 13
input2 = 14
def solution(num1, num2):
  sum = int(str(num1)[::-1]) + int(str(num2)[::-1])
  return int(str(sum)[::-1])
  
# print(solution(input1, input2))
# 23. Write a Python program where you take any positive integer n, if n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1. Go to the editor
# Input : 12
# Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]

input = 12
def solution(num):
  result = [num]
  
  while num != 1:
    if num % 2 == 0:
      num = num / 2
      result.append(num)
    else:
      num = (3 * num) + 1
      result.append(num)
  return result
      
# print(solution(input))

# 24. Write a Python program to check whether a given number is an ugly number. Go to the editor
# Input : 12
# Output : True
input = 12
def solution(num):
  for i in [2 ,3 ,5]:
    if num % i == 0:
      return True
  return False
# print(solution(input))

# 26. Write a Python program to check if a given string is an anagram of another given string. Go to the editor
# Input : 'anagram','nagaram'
# Output : True 
input1 = "anagram"
input2 = "nagaram"
def solution(str1, str2):
  str2 = list(str2)
  print(str2)
  for w in str1:
    if w in str2:
      str2.remove(w)
      print(str2)
    else:
      return False
  return True
# print(solution(input1, input2))

# 27. Write a Python program to push all zeros to the end of a list. Go to the editor
# Input : [0,2,3,4,6,7,10]
# Output : [2, 3, 4, 6, 7, 10, 0]
input = [2,0,3,4,6,7,10]

def solution(array):
  i = 0
  end = len(array)
  while i < end:
    if array[i] == 0:
      array.remove(0)
      array.append(0)
      end = end - 1
    i = i + 1 
  return array
# print(solution(input))

# 29. Write a Python program to find majority element in a list. Go to the editor
# Input : [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
# Output : 5

input = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]

def solution(num):
  maxNumber = 0
  maxCount = 0
  for i in set(input):
    if maxCount < input.count(i):
      maxNumber = i
      maxCount = input.count(i)
  return maxNumber

# print(solution(input))

# 34. Write a Python program to compute the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed one million. Go to the editor
# Note: Fibonacci series is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# output = [1,2,3,5,8,13,21,34,55]
def solution():
    value = 1
    before = 0
    result = [1]
    while True:
        diff = value - before
        before = diff 
        value = value + diff
        if value > 1000000:
            break
        result.append(value)
    return result
# print(solution())

def format_number(num):
    i = len(str(num))
    result = ""
    while i > 0:
        result += str(num)[i-1]
        if i % 3 == 0:
            result += ","
        i -= 1
    return result[::-1]
    
print(format_number(12345678))
#OUTPUT = "12,345,678"