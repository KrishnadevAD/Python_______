# list comprehension 
from operator import itemgetter

# list comprehension 
item= [1,2,3,4,5,6,7,9,10]
a={n for n in item if n % 2 == 0}# list comprehension
print(a)
a={n:n for n in item if n % 2 == 0} # dictionary comprehension
print(a)