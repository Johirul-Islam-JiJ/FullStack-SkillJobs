t=(1,2,3,44,55,66,77,88,99,56,11,67,435,535,76,8)

print(type(t))
print(t[10])
for i in t :
    print(i)

print(t[0:5])
print(t[2:6])
print(t[:])
print(t[:-2])
print(t[::-1])  # reversing
print(t[:] * 2)

print(t.count(2))
print(t.index(44))

# for i in t:
#     if i == 2:
#         continue
#         indx = t.index(i)
#         print(indx)