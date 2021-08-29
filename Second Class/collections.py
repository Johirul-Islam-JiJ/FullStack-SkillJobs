

# List, Tuple, Set, Dictionary

# list == mutable(cahnge kora jay)

l = [1,2,3,4.5,5.5,'7.5','8.5','9.5','name','age',True,False]
l[1] = 100

print(type(l))
print(l)

# for i in l:
#     print(i)
#     print(type(i))


    # tuple == immutable(change kora jay na)

t = (1,2,3,4.5,5.5,'7.5','8.5','9.5','name','age',True,False)

print(type(t))
print(t)

# for i in t:
#     print(i)
#     print(type(i))


# Set => immutable
s = {1,2,3,4,5}
print(s)


# Dictionary => key value pair

d = {'key1':'value2',"k2":"v2",'k3':'v3'}
d2 = {0:10,1:20,2:30}
print(d2[1])
print(d['k2'])