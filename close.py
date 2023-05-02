##def fun(txt):
##    def outer():
##        print('hi',txt)
##    return outer
##k=fun('hello')
##k()

##l=[1,2,3,4,5,6,7]
##for i in l:
##    ite=iter(l)
##    print(next(ite))
##    print(next(ite))
##    print(next(ite))
##    print(next(ite))
##    print(next(ite))

##g = [0,5,2,3,4,0,7,8,0,7,0]
##
##non_zero = []
##
##for i in g:
##    if i != 0:
##        non_zero.append(i)
##
##
##num_zeros = g.count(0)
##non_zero += [0] * num_zeros
##
##print(non_zero)



##k=[1,2,3,4,5,6,7,8,9,10]
##reversed_k = k[::-1]
##print(reversed_k)

##
##k=[1,2,3,4,5,6,7,8,9,10]
##
##for i in range(len(k)-1,-1,-1):
##    print(k[i])

##l=[2,5,0]
##f=l[0]
##for i in l:
##    if i<f:
##        f=i
##print(f)
##        



##
##f='hello world'
##g=f.split()[::-1]
##print(g)




##f = "hello world"
##g = f.split()
##
##g.reverse()
##reversed_ = " ".join(g)
##
##print(reversed_)



##
##
##f = "hello world"
####g = f.split()
##
### Reverse the order of the words without using the reverse() method
##f = f[::-1]
####reversed_string = " ".join(f)
##
### Print the reversed string
##print(f)


####generator
##def fun(num):
##    for i in num:
##        yield (i*i)
##var=fun([1,2,3,4,5])
####print(var)
##
##for i in var:
##    print(i)





##def outer():
##    x=5
##    def fun():
##       print(x+2)
##    return fun()
##var=outer()
##print(var())



##
##def func(x):
##    return x+1
##res=func
##print(res(2)+func(2))
    

##a=[10,20,30]
##res = (x for x in a if a.count(x)>0 )
##a=[40,20,60]
##print(list(res))



##def add(x):
##    return x+1
##def sub(x):
##    return x-1
##def cul(fun,x):
##    val=fun(x)
##    return val
##print(cul(add,10))
##print(cul(sub)20)
    
    

##def decore1(fun):
##    def wrapper():
##        return fun() * 5
##    return wrapper
##
##def decore2(fun):
##    def wrapper():
##        return fun() * 2
##    return wrapper
##
##@decore1
##def num():
##    return 10
##
##@decore2
##def num2():
##    return 10
##
##print(num())  # prints 50
##print(num())  # prints 50
##print(num2())  # prints 20








##string = "hello world"
##count = 0
##
##for char in string:
##    count += 1
##
##print(count) # Output: 11



##n=1
##while True:
##    n+1
##    print(n)


##def genertor():
##    n=0
##    while True:
##        n+=1
##        yield n
##for i in genertor():
##    print(i)
##    
    
    
import sys
l=[i*2 for i in range(1000)]
print(sys.getsizeof(l))

g=(i*2 for i in range(1000))
print(sys.getsizeof(g))
