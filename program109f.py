#lambda function with filter 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x % 2 != 0), li)) # it gives output on list 
print(final_list)
final_list = tuple(filter(lambda x: (x % 2 != 0), li)) # it gives output on  tuple 
print(final_list)