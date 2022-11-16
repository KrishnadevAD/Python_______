# the difference between the functio and lambda funcrtion
def cube(y):
	return y*y*y


def lambda_cube(y): return y*y*y


# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))
