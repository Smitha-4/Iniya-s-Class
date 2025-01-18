# newlist = [expression for item in iterable if condition== True]

"""fruits = ["apple", "banana", "cherry", "dragonfruit", "orange", "kiwi", "mango"]
newlist =[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

list2 = [x for x in fruits if "a" in x] # List Comprehension
print(list2)"""

# write a program to generate the squares of numbers from 1 to 20 using list comprehension
# write a program to generate Math table of any number from 1 to 10 using list comprehension

squares = []
for i in range(1,21):
    squares.append(i*i)
print(squares)

squ = [i*i for i in range(1,21)]
print(squ)