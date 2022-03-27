# Create a function that compares the count of item to n and if the count of item in lst is greater than n
# return True, else return False

def more_than_n(lst, item, n):
  #if item is in lst more than n
  if lst.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
print("")
print(more_than_n([1, 4, 6, 1, 3, 2, 1, 2], 2, 3))