# Question1
print("hello world"[8])

# Question 2
print("tinker"[1:4])


# Question 3
print(set('Mississippi'))


# Question 4
list_ex = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
for i in range(len(list_ex)):
    list_ex[i] = list(list_ex[i])
    list_ex[i][-1] = 100
    list_ex[i] = tuple(list_ex[i])

print(list_ex)


# Question 5
dict = {
    '1': ['a', 'b'],
    '2': ['c', 'd']
}

values = list(dict.values())

for i in values[0]:
    for j in values[1]:
        print(i, j)
