from functools import reduce

nums = [34, 56, 33, 78, 89, 10, 1]

filtered = filter(lambda x: x%2 == 0, nums)    
for i in filtered:
    print(i)             

print('---------------------------')

mapped = map(lambda x: x+1, nums)
for i in mapped:
    print(i)      

print('---------------------------')

reduced = reduce(lambda a,b : a + b, nums)
print(reduced)