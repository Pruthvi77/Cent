########## assiignment 3 ############

lst = [1,2,3,4,5,6,]
def myreduce(values):
    sum = 0
    for i in values:
        sum = i + sum
    return sum
print("Sum of list of values using custom reduce 'function' -->",myreduce(lst))

def myfilter(list_values):
    empty_list = []
    for i in list_values:
        if i%2 ==0:
            empty_list.append(i)
    return  empty_list

print("getting even numbers just like 'filter' using custom function -->", myfilter(lst))


input_list = ['x','y','z']
list1 = [i*num for i in input_list for num in range(1,5) ]
print(list1)
  #['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

list2 = [i*num for num in range(1,5) for i in input_list ]
print(list2)
  #['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

input_list = [2,3,4]
list3 = [ [i+num] for i in input_list for num in range(0,3) ]
print(list3)
  #[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

input_list = [2,3,4,5]
list4 = [ [item+num for item in input_list] for num in range(0,4)  ]
print(list4)
  #[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
 
list_append = [list3,list4]
print("final list -> ",list_append)
  #final list ->  [[[2], [3], [4], [3], [4], [5], [4], [5], [6]], [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]]

list5 = [(num,i) for i in range(1,4) for num in range (1,4) ]
print(list5)
  #[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
