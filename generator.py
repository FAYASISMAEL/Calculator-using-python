# 1.create a generator to yeild even number from 1 to 50

# def generator(n):
#     value = 1
#     while value <= n:
#         yield value
#         value += 2
# for value in generator(50):
#         print(value)

# def generator():
#     for num in range(2, 51, 2):
#         yield num

# for even in generator():
#     print(even)

# 2.write a generator expression to generate squarers of numbers from 1 to 10

# sqrs = tuple(x**2 for x in range(1, 11))
# print(sqrs)

# 3.write a generator function that yields all the characters of a given string one by one 

# def char(text):
#     for char in text:
#         yield char

# for gen in char('Hello welcome'):
#     print(gen)

# 4.write a program to use a generator expression to filter out vowels from a given string

def vowels(text):
    vowels = 'aeiouAEIOU'
    return(char for char in text if char not in vowels)

value =  "Fayas Ismael"
filtered = vowels(value)

for char in filtered:
    print(char, end='')