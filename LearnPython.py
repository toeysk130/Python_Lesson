# 1 Reverse Integer
# Given an interger, return the integer wiith reversed digits.
# Note: The integer could be either positive or negative.

## INPUT: 123 OUTPT: 321
## INPUT: -321 OUTPUT: -123

def _reverse_interger(input):
    string_result = str(input)
    if string_result[0] == "-":
        return int("-"+string_result[:0:-1])
    else:
        return int(string_result[::-1]) #Extended slice syntax= [begin:end:step]

# output=_revers_interger(12345678)
# print(output)

# output=_reverse_interger(-12345678)
# print(output)

# 2 Average Words Length
# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def average_words_length(sentence):
    for p in ",.!":
        sentence = sentence.replace(p,"")
    split_sentence = sentence.split(" ")
    
    # sum=0
    # for word in split_sentence:
    #     sum+=len(word)
    # return print(round(sum/len(split_sentence),2))
        
    ## Improving method
    return round(sum(len(word) for word in split_sentence)/len(split_sentence),2)
    
# print(average_words_length(sentence1))
# print(average_words_length(sentence2))

# 3 Add Strings
# Given two non-negative integers num1 and num2 reresented as string, return the sum of num1 and num2
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

# Solution 1
# The evan function lets a Python program run Python code within itself.

def sum_string(str1, str2):
    return (eval(str1) + eval(str2))

# print(sum_string(num1, num2))

# Solutuin 2
# Given a string of length one, the ord() function returns an integer representing the Unicode code point of the character
# When the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

def sum_string(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)
    print(f'm1: {m1} m2: {m2}')
    
    for i in num1:
        print(f'i={i} ord(i)={ord(i)} {ord(i) - ord("0")}')
        n1 += ((ord(i)) - ord("0")) * m1   
            
        print(f'n1={n1}')
        m1 = m1//10
        
        print(f'm1={m1}')
        
    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10
        
    return str(n1+n2)
        
# print(sum_string(num1, num2))

# 4 First Uniqe Character
# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. Note: all the input strings are already lowercase.

# My Solution
def solution(string):
    for i in range(len(string)):
        new_string = string.replace(string[i],'',1) # Remove only the first match character
        if string[i] not in new_string: # Check if still find another one
            return i
        
# Answer 1
# Create array of characters to sum up amount
# Loop through created array to find the first char that only have amount=1
def solution(s):
    frequency = {} 
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1

# Answer 2
# Using external Library
import collections

def solution(s):
    # built hash map : character and how often it appears
    count = collections.Counter(s) # <-- gives back a dictionary with words occurrence count
    print(f'count: {count}')
    #find the index
    for idx, ch in enumerate(s): #Return mapping array object
        # print(f'idx: {idx} ch: {ch}')
        
        if count[ch] == 1:
            return idx
    return -1   

# print(solution('alphabet'))
# print(solution('barbados'))
# print(solution('crunchy'))

# Problem 5: Valid Palindrome
# Given a non-empty sting s, you may delete at most one character. Judge whether you can make it a palindeome.
# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
# The string wilo only contain lowercase characters a-z

s ='raddar'

# My Program
def solution(s):
    middle = round(len(s)/2)

    if len(s) % 2 == 0:
        print(f'{s[:middle:]} | {s[:middle:]}')
        if s[:middle:] == s[:middle:]:
            return True
    else:
        print(f'{s[:middle-1:]} | {s[:middle-1:]}')
        if s[:middle-1:] == s[:middle-1:]: 
            return True
    return False
  
  
# def solution_nook(s):
#   middle = round(len(s)/2)
#   print(f'{s[:middle:]} | {s[:middle:]}')

# print(solution('radkdar'))
# print(solution('raddar'))

#Solution
def solition(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True
    return s == s[::-1]

# print(solition('radkdar'))

## 6. Monotonic Array
# Given an array of integers, determine whether the array is monotomic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

# 'all' function will return True/False if all of value in Array are True/False
def solution(arry):
    return (all(arry[i] >= arry[i+1] for i in range(len(arry) -  1)) or
            all(arry[i] <= arry[i+1] for i in range(len(arry) -  1)))
            
# print(solution(A))
# print(solution(B))
# print(solution(C))

#given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

#My Answer
def solution(arry):
    for i in arry:
        if 0 in arry:
            arry.remove(0)
            arry.append(0)
    return arry
        
# print(solution(array1))
# print(solution(array2))

# 8: Fill the blanks
# Given an array containing None values fill in the None values with most recent
# non None value in the array
array1 = [1,None,2,3,None,None,5,None]

#My Answer
def solution(arry):
    recent = None
    for i in range(len(arry)):
        if arry[i] is None:
            arry[i] = recent
        else:
            recent = arry[i]
    return arry

# Solution
def solution(nums):
    valid = 0
    res = []
    for i in nums:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res
# print(solution(array1))

## 9:Matched & Mismatched Words
#Given two sentence, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

# Toey Answer
def solution(sentence1, sentence2):
    mismatch = []
    match = []
    
    for word in sentence1.split(" "):
        if word in sentence2.split(" "):
            if word not in match:
                match.append(word)
        else:
            mismatch.append(word)
            
    for word in sentence2.split(" "):
        if word in sentence1.split(" "):
            if word not in match:
                match.append(word)
        else:
            mismatch.append(word)
    return [mismatch, match]

#Solution
#'Set' returns an empty set if no element is passed. Non-repeating element iterable modified as apssed as argument.
def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    print(f'set1: {set1}')
    print(f'set2: {set2}')
    # print(set1^set2) ## '^' called symmetric_difference() which '&' called intersection()
    return sorted(list(set1^set2)), sorted(list(set1&set2))

# print(solution(sentence1, sentence2))