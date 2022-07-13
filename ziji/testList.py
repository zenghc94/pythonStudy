#翻转。。。。。。。。。
a = "123456789"
c= a[1]
print(c)
print(len(a))
print(a[::-1])
d = a[::-1]
print(d) #这个可以翻转
b = a[len(a)-1:0:-1]#原来是这样翻转
# b = a[1:len(a)-1:-1]这个没有返回值啊
print(a)
print(b)