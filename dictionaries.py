# add_ten function :
def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# prints {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# prints {10:11, 100:12, 1000:13}


# sum_of_even_keys function here:
def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary:
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
# prints 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# prints 6


def sum_values(my_dictionary ):
  sum = 0
  for values in my_dictionary:
    sum += my_dictionary[values]
  return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
#  prints 10
print(sum_values({10:1, 100:2, 1000:3}))
# prints 6

#This function  returns a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  keys = my_dictionary.keys()
  vals = my_dictionary.values()
  common = []
  for k in keys:
    if k in vals:
      common.append(k)
  return common



#calculates the frequency of words 

def frequency_dictionary (words):
  dict={}
  for w in words:
    if w not in dict:
      dict[w] = 1
    else:
      dict[w] += 1
  return dict
  
print(frequency_dictionary(["apple", "apple", "cat", 1]))
#  prints {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# prints {0:5}
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# word_length_dictionary function here:
def word_length_dictionary(words):
  dict = {}
  for w in words:
    dict[w] = len(w)
  return dict
  
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
#************************************************************
#  max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
#
##########################################################
#  unique_values function
def unique_values(my_dictionary):
  unique_sum=[]
  for val in my_dictionary.values():
    if val not in unique_sum:
      unique_sum.append(val)
  return len(unique_sum)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
