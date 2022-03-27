# Create a function that adds the sum of the last two elements in the list to lst, redefining the and then
# doing it again to append another number to the end of the list

#def append_sum(lst):
 #   for num in lst:
  #      lst.append(lst[-1] + lst[-2])
   #     for num in lst:
    #        lst.append(lst[-1] + lst[-2])
     #       for num in lst:
      #          lst.append(lst[-1] + lst[-2])
       #         return lst


#print(append_sum([1, 1, 2]))

# Second attempt after realising that it wouldn't loop appropriately with the given code

def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))
print("")
print(append_sum([2, 4, 7]))
