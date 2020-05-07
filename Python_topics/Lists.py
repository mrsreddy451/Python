'''
My_list = ['red','white','green']
print(My_list)

My_list.append('yellow')

print(My_list)

My_list.extend(['blue','pink'])
print(My_list)
'''
list1 = [1,2,3,4]

def nlist(lists):
    lists = list(lists) + [5,6]
    #print(lists)
    lists+=[5,6]
    return  lists
print(nlist(list1))

#print(list1)