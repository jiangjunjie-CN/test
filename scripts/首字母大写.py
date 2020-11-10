name_list=['adam', 'LISA', 'barT','jjj']
new_ls=list(map(lambda k:k[0].upper() + k[1:len(k)].lower(),name_list))
print(new_ls)