

your_name='Joy'


def myget():
    print("this is my custom get functions")
    print(your_name)


def greetings(name):
    print("Welcome",name)

def wish(name,age):
    print("happy Birthday",name,"you are on ",age)

def my_sum(num1,num2):
    return num1+num2

def get_num(num):
    print(num)

myget()
greetings("Johirul")
wish("joy",10)
print(my_sum(10,20)+100)
s = my_sum(20, 40)
print(s)


# print(get_num(10)+200) not work in print...have to use return function..

print('*'*30)


