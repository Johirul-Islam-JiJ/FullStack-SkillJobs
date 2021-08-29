l = [1, 2, 3, 4, 5, 2.5, 4.2, "my list", "mylist2" ]

# indexing
print(l)
print(l[8])
for i in l:
    print(i)


    # slicing

print(l[0:5])
print(l[2:6])
print(l[:])
print(l[:-2])
print(l[::-1])  #reversing
print(l[:]*2)

#append

l.append(15)
print(l)

# nested list

l2 =[[1,2,3],[35,6,9]]
print(l2[0][1])

l.append([10,20,30])
print(l)

l3 = [10,20,30]
for i in l3:
    l.append(i)
    print(l)

    for i in l2:
        for j in i:
           l.append(j)
        print(l)


### Pop


print(l.pop())
print(l)

print(l.pop(2))
print(l)
pop_val = l.pop(2)

## list comprehension

l4 = [i for i in range(1,100,10)]
print(l4)

print(l.count(2))
print('*'*40)

remove_val = l.remove(15)
print(remove_val)
print(l)
l.remove('my List')
l.remove('mylist2')
l.sort()
print(l)