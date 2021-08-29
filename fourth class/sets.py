# immutable, no indexing



s = {1,2,3,3,3,3,3,4,5,6,7,8,9}
s2 = {10,20,30,40,50}
s3 = {1,2,3}
print(s)

s.add(10)
print(s)

print(s.union(s2))
print(s3.isdisjoint(s))
print(s.intersection(s2))
print(s.difference(s2))

