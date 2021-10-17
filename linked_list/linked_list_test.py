from linked_list import LinkedList

lst = LinkedList()
lst.set_head('nh')
lst.set_head('d')
lst.set_tail('tail')
lst.set_head((1, 2, 3))

print(lst)
print('head -> ', lst.get_head())
print('tail -> ', lst.get_tail())

for x in lst:
    print(x)
