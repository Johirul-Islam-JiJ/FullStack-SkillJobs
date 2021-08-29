
# Key value pairs

d = {"key":"value",'1':'100','2':'200'}
data = {"name":"Joy","age":25,"dept":"swe"}

print(d)

print(d["key"])
print(d['2'])
print('*'*30)

# for loop in dictionary

for i, j in data.items():
    print(i,":",j)

print('*'*30)

print(data.keys())
print(data.values())

print(d.get("key"))
v = d.get("key")
print(v)

print('*'*30)


stu_data1 = {
    "name": ["johirul","surove","joy",'joni'],
    "age" : [25,21,24,30]
}

print(stu_data1)

stu_data2 = {
    "17335257":{
        "name": "Johirul",
        "age" : 25,
        "dept": "swe"
    },
    "18235375": {
        "name" : "Surove",
        "age": 21,
        "dept": "swe"
      }
    }


print(stu_data2["17335257"])
print(stu_data2["18235375"])

print('*'*30)

data['name'] ="Johirul"
print(data)

stu_data2["18235375"]['name'] = "Sultana"
print(stu_data2["18235375"])
