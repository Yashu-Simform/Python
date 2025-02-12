# # Strings
# s1 = '\'Yashu\''
# s2 = ''''Yashu's Home\''''

# print(s1,s2,sep=' - ')


# Ways to create a copy of list
d1 = {'name': "Yashu", "dept": "Python", "logs": ["Monday", "Tuesday", "Wednesday"]}

temp = d1['logs']       # Making an alias reference for df['logs]

print('d1', d1)
print('d1.logs', d1['logs'])
print('temp', temp)

lostele = temp.pop()
print('After updating temp, temp: ',temp)
print('After updating temp, d1.logs: ',d1['logs'])

#   1.  Create copy of a function using copy function of the list
tempdeepcopy = d1['logs'].copy()
tempdeepcopy.pop()
print('After updating tempdeepcopy, tempdeepcopy: ',tempdeepcopy)
print('After updating tempdeepcopy, d1.logs: ',d1['logs'])


#   2. Using slicing
listcopy_sliced = d1['logs'][:]




#   Dictonary

x = dict(k1="v1", k2="v2", k3="v3")  
type(x)

#Traversing
for (k,v) in x.items():
    print('Key: ', k, ' V: ',v,'.',sep='') 


