import random

list_of_words = ['hello', 'python', 'world', 'experts', 'fun']

result = []

for word in list_of_words:
    result.append(word[0])

print(word)  # still exists

print(result)

# comprehension
result2 = [word[0:2] for word in list_of_words if word != 'experts']

print(result2)


numbers = [4, 10, -5, 200] #we multiplay by 3, #ignorenegetive numbers


numbers_3 = [x*3 for x in numbers if x > 0]
print(numbers_3)
print('===========================')
matrix = [[1,2,6], [7,8,10],[100,5,2]]
#we create a list of first item(int) in each list

rows = [y[0] for y in matrix] #onerow

# all rows
# matrix = [[1,2,6], [7], [100, 5, 2]]
for i in range(len(matrix)):
    rows = [y[i] for y in matrix if i < len(y)]
    print(rows)
print('==================================================')
l1 = list(range(10))
print(l1)

numbers = [2, 6, 10, 200, -20, 3]
l2 = [x for x in range(0, 10, 2) if x % 2 == 0]
print(l2)

# create list of numbers sqr 1, 2, 4, 9, 16, 25, 36 ... 1-20
numSqr = [x ** 2 for x in range(1, 21)]

# create list of numbers between 1-100 which can divide by 3 or 5 or 7 without reminder
#    x % 3 == 0 or x % 5 == 0 or x % 7 == 0
num100 = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0]

# [5.9, 0.9, -9.2, 10.1] => [5, 0, -9, 10]
toInt = [int(number) for number in [5.9, 0.9, -9.2, 10.1]]

# create a list of 10 random numbers (random 1-100)
randoms = [random.randint(1, 100) for x in range(100)]
print(randoms)
print(len(randoms))

