# -*- coding: utf-8 -*-
"""
Spyder Editor
#sushma first project
This is a temporary script file.
"""
# -*- coding: utf-8 -*-
#data structures
#are structures which can hold some data together. used to store collection of related data
#types - list, tuple, dictionary, set

#%%
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)

#run next 2 lines together
for item in shoplist:
    print(item, end =' ')

#add item to list
shoplist.append('rice')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]
