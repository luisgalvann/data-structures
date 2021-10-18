from linked_list import LinkedList

# lst = LinkedList()
# lst.set_head('nh')
# lst.set_head('d')
# lst.set_tail('tail')
# lst.set_head((1, 2, 3))

# print(lst)
# print('head -> ', lst.get_head())
# print('tail -> ', lst.get_tail())

# for x in lst:
#     print(x)

lst = LinkedList()
lst.set_head(7)
lst.set_head(6)
lst.set_head(5)
lst.set_head(4)
lst.set_head(3)
lst.set_head(2)
lst.set_head(1)
lst.set_head(0)
lst.pop_node(1)
print(lst)
