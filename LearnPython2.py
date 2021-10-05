#!/usr/bin/env python3

# ======== Q1: Replace NONE by its previous NON None value

input = [None,1,2,3,None,4,None,None]
def solution_q1(input):
  non_none = None
  for i in range(len(input)):
    if input[i] is not None:
      non_none = input[i]
    else:
      input[i] = non_none
  return input 

# ======== Q2: Calculate average word length from a string

input = 'Hi I am Pawan. I am here only'
def solution_q2(input):
  word_cnt = 0
  for word in input.split():
    word_cnt += len(word)
  return word_cnt / len(input.split())
# print(solution_q2(input))

def solution_q2_2(input):
  return sum(len(word) for word in input.split()) / len(input.split())
# print(solution_q2_2(input))

# ======== Q3: Find un-common words from two strings
 
a = 'Hi I am Pawan here only'
b = 'here only'
 
def solution_q3(string1, string2):
  result = []
  for word in string1.split():
    if word not in string2.split():
      result.append(word)
      
  for word in string2.split():
    if word not in string1.split():
      result.append(word)
  return result

# print(solution_q3(a, b))

# ======== Q4: Find uniqe words from string
a = 'Hi i am pawan here only only here i'

# My solution
def solution_q4(string):
  uniq = []
  for word in string.split():
    if word not in uniq:
      uniq.append(word)
  return uniq
# print(solution_q4(a))

# ======== Q5: Find common words from two strings

a = 'Hi I am Pawan. I am here only'
b = 'here only'

def  solution_q5(string1, string2):
  common = []
  for word in string1.split():
    if word in string2.split():
      common.append(word)
  return common
# print(solution_q5(a, b))

# ======== Q6: How to convert a string to a list

# With Python function
a = "abcde"
def solution_q6(string):
  return list(string)

# Without Python function
a = 'abcde'
def solution_q6(string):
  result = []
  for w in string:
    result.append(w)
  return result    

# print(solution_q6(a))

# ======== Q7: How to convert a list to a string
a = ['a','b','c','d','e']

# Without Python function
def solution_q7(array):
  result = ""
  for w in array:
    result += w
  return result

# print(solution_q7(a))

# With Python function
def solution_q7(array):
  result =""
  return result.join(array)

# print(solution_q7(a))

# ======== Q8: How to find LCM of two numbers

a = 15
b = 20

# Without Python func.
def solution_q8(num1, num2):
  i=0
  while True:
    i+=1
    if i%a == 0 and i%b == 0:
      return i
# print(solution_q8(a, b))

# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

# ======== Q10: Find maximum value from a list
a = [ 1 ,2, 4,1,10,12,100 , 2, 6]

def solution_q10(array):
  max = 0
  for i in a:
    if i > max:
      max = i
  return max

def solution_q10(array):
  return max(array)

# print(solution_q10(a)) 

# ======== Q11: Find the number of times a substring present in a string
a = 'Philadelphia'
fn = 'i'

def solution_q11(sentence, w):
  count = 0
  for i in sentence:
    if i == w:
      count += 1
  return count
# print(solution_q11(a, fn))

# ======== Q13: How to sort an array in ascending order
a = [1,3,4,5,10,8,19]

def solution_q13(array):
  for i in range(1,len(array)):
    if array[i] < array[i-1]:
      temp = array[i-1]
      array[i-1] = array[i] 
      array[i] = temp
  return array
# print(solution_q13(a))

# ========  Print the most recurring element in a list
a = [1, 1, 1, 2, 2,3,3,3,3]
result = {}
def solution(array):
  for i in array:
    if i not in result:
      result[i] = 1
    else:
      result[i] += 1
  return max(result, key=result.get)
# print(solution(a))

# Python's style
# max(a, key=a.count)

### ======== Chcek whether a number is prime or not

a = 29
def solution(input):
  for i in range(2,input):
    if input%i == 0:
      print(f'input: {input} % i:{i} = {input%i}')
      return False
  return True
print(solution(a))