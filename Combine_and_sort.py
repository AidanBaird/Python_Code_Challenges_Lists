# Create a function that combines and sorts the two lists lst1 and lst2 into one chronological list

def combine_sort(lst1, lst2):
  lst3 = lst1 + lst2
  lst4 = sorted(lst3)
  return lst4

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
print("")
print(combine_sort([56, 234, 1516, 1367], [-3256, 5467, 34, 133]))