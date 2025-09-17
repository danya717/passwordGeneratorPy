# words = ["apple", "banana", "cherry", "mango"]
#
# lengths = list(map(len, words))
# print(lengths)
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# def square(x):
#     return x * x
# print(square(5))
#
#
# squares = list(map(lambda x: x * x, numbers))
# print(squares)
#
#
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# result = list(map(lambda x, y: x+y, a, b))
# print(result)


#1
nums = [1, 2, 3, 4]
result = list(map(lambda x: x+1, nums))
print(result)


#2
chars = ["A", "B", "C", "D", "E", "F"]
lowercase = list(map(str.lower, chars))
print(lowercase)

#3
words = ["cat", "dog", "apple"]
res = list(map(lambda x: x[0], words))
print(res)

#4
numbers = [1, 5, 7]
times = list(map(lambda x: x*10, numbers))
print(times)

#5
num_list = [-1, 0, 3, 5, 6, 7, -2, 0]
boolean = list(map(lambda x: True if x>-1 else False, num_list))
print(boolean)
