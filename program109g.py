# Python code to illustrate
# map() with lambda()
# to get double of a list.
list1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, list1))
print(final_list)