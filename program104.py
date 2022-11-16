# WAP That takes the value  0 to 9 and keep in the list of even numbers and 
# use filter and without filter 
# def is_even(n):
#     n=int(input(list[]))
#     return n%2==0
# a=list(filter(is_even,[1,2,3,4,5,6,7,8,9]))
# print(a)

#list comprehencion
def even_number(n):
    even_list = []
    for item in n:
        if item % 2 == 0:
            even_list.append(item)
    return even_list 
items = [1,2,3,4,5,6,7]
print(even_number(items))
a=[ n for n in  items if n % 2 ==0]
print(a)

