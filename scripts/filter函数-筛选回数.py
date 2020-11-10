#回数是指从左向右读和从右向左读都是一样的数
num_list=[909,1578,56265,321,888]
filt=list(filter(lambda x:str(x)[::-1] == str(x),num_list))
print(filt)