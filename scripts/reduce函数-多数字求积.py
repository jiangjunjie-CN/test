from functools import reduce

num_list=[2,5,7,9,10]
prod=reduce(lambda x,y:x*y,num_list)
print(prod)