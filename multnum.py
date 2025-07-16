# Write a prog to print the multiplication table of a given number upto 10

num = int(input('Enter a Number: '))

for i in range(1, 11):
    # print(num*i)
    print(num, 'x', i, '=', num*i)