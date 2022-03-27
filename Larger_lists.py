# Create a function that compares the length of two lists and returns the last element of the longer list
# else return the lst element of lst1

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))