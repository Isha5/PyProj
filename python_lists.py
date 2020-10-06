#creating lists using Range function with a diff val of 3 

list1 = list(range(2, 20, 3))
print(type(list1))
print(list1)

#output
[2, 5, 8, 11, 14, 17]

#calculate length
list1_len = len(list1)

print(list1_len)





# try except
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]

print(len(employees))

try:
  print(employees[8])
  print('No error')
except IndexError:
  print('Some error occured with Index')
except:
  print('some unknown err')
else:
  print('No err occured, demonstrating else')
finally:
  print('this block is used in database connections, but prints here also. ')


#Counting elements in a list

letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

num_i = letters.count('i')
print(num_i) # prints 4


