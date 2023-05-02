##def fun():
##    a=10
##    b=500
##    c=30
##    def fun1():
##        d=20
##        c=30
##    fun1()
##    def fun2():
##        d=20
##        print(d)
##    fun2()
##    def fun3():
##        print(b)
##    fun3()
##fun()
##        
    


##a=10
##b=20
##def fun ():
##    c=a+b
##    print(c)
##fun()    
##
##
##a=10
##b=20
##def fun ():    
##    fun()    
##c=a+b
##print(c)


##def fun():
##    global x,y
##    x=10
##    y=20
##fun()
##c=x+y
##print(c)



##my_dict = {('apple', 'red'): 1, ('banana', 'yellow'): 2}
##
### Access a value using a tuple key
##print(my_dict[('apple', 'red')])





##g='hello world'
##b=list(g)
##print(b[-1::-1])



##a = "hello world"
##b=list[a]
##
##b = a[::-1]
##
##print(b)


##a = "hello world"

# Initialize an empty string to store the reversed string
##b = ""
##
### Use a loop to iterate over the string in reverse order
####for i in range(len(a)-1, -1, -1):
##    # Concatenate each character to the reversed string
##    b += a[i]
##
### Print the reversed string
##print(b)


##my_string = "hello world"
##b=list(my_string)
##
### Use string slicing to create a reversed copy of the string
##reversed_string = b[::-1]
##
### Print the reversed string
##print(reversed_string)




##def fun(x ):
##    print(x)
##fun(10)
##fun(20)
##fun(30)





##def fun(a,b=30):  ##default
##    print(a,b)
##fun(40)    
##

##def fun(a=10,b): ##non default
##    print(a,b)
##fun(40)


##
####keyword arguement
##def fun(name,age):
##    print(name,age)
##fun(name='hello',age=10)    
##
##    

##def fun(name,age):
##    print(name,age)
##fun('hello',10)    





##g=[10,20,30,40,100,500,25,45,65,78]
##def fun():
##    k=g
##    k.append(50)
##    k.insert(1,80)
##    k.pop(4)
##    k.remove(100)
##    k.reverse()
##    k.sort()
##    print(g)
##fun()    

      
##def gowtham():
##    a=[20,4,54,68,40,2,100,457,500]
##    def b1():
##        a.append(888)
##        print(a)
##    b1()
##    def b2():
##        c=[1000,2000]
##        a.extend(c)
##        print(a)
##    b2()
##    def b3():
##        a.pop(5)
##        print(a)
##    b3()
##    def b4():
##        a.remove(888)
##        print(a)
##    b4()
##    def b5():
##        a.sort()
##        print(a)
##    b5()
##    def b6():
##        a.reverse()
##        print(a)
##    b6()
##gowtham()    
    



        
##def fun(name):
##    print(name)
##fun('hello','hi','hello')    

##
#### variable length arugement 
####def fun (**hello):
####     for arg in hello.items():
####         print(arg)
####
####fun(hi='hello',welcome='gotam')


####return function

##def my_fun(x):
##    return x**10
##
##def inner():
##    return my_fun
##k=inner()
##print('the value is:',k(10))

######

##def add(c):
##    return c
##a=10
##b=20
##c=a+b
##print(c)



##def add_numbers(a, b):
##    return a + b
##
##b = add_numbers(2, 3)
##print(b)

##def get_even_numbers(n):
##    even_numbers = []
##    for i in range(1, n+1):
##        if i % 2 == 0:
##            even_numbers.append(i)
##    return even_numbers
##
##result = get_even_numbers(10)
##print(result)

##def a(num):
##    if num % 2 == 0:
##        return True
##    else:
##        return False
##
##result1 = a(4)
##result2 = a(11)
##print(result1)  # Output: True
##print(result2)



##def fun(num1,num2):
##    sum1=num1+num2
##    print('sum is :', sum1)
##fun(5,6)    

##def fun(num):
##    b=num*num
##    return b
##c=fun(3)
##print('c is ', c)


##number=[2,3,4]
##def fun(num):
##    d=num*num
##    return d
##for i in number:
##    a=fun(i)
##    print('a value is ',i,'=',a)


##def fun(name,message):
##    print('hello',name)
##    print(message)
##
##fun('gowtham','whats going onn')
##fun(message='byeeeeeeeeeeeeeee',name='yoki')


##Python Keyword Argument
##In keyword arguments, arguments are assigned based on the name of arguments. For example,
##
##def display_info(first_name, last_name):
##    print('First Name:', first_name)
##    print('Last Name:', last_name)
##
##display_info(last_name = 'Cartman', first_name = 'Eric')









# program to find sum of multiple numbers 

##def find_sum(*numbers):
##    result = 0
##    
##    for num in numbers:
##        result = result + num
##    
##    print("Sum = ", result)
##
##
### function call with 3 arguments
##
##
##find_sum(1, 2, 3)
##
### function call with 2 arguments
##find_sum(4, 9)
##
##find_sum(1, 8, 5,40)



# program to find sum of multiple numbers 

### function to find the maximum number in a list
##def find_max(numbers):
##    max_num = numbers[0]
##    for num in numbers:
##        if num > max_num:
##            max_num = num
##    return max_num
##
### main function to find sum of numbers
##def find_sum(*numbers):
##    result = 0
##    for num in numbers:
##        result = result + num
##    print("Sum = ", result)
##
### function call with 3 arguments
##find_sum(1, 2, 3)
##
### function call with 2 arguments
##find_sum(4, 9)
##
### example function call to find the maximum number in a list
##numbers_list = [5, 2, 8, 1, 9]
##max_num = find_max(numbers_list)
##print("Maximum number in the list: ", max_num)




##def fun(name,**data):
##    print(name)
####    for i,k in data.items():
####        print(i,k)
##fun('gowtham',age=28,city='chennai',phone=7448545688)    


##
##
##def fun(name,course='bca'):
##    print(name)
##    print(course)
##fun(name='gowtham',course='bom')
##fun(name='yoki')


##a=lambda s:s + 10
##print(a(5))

##lambda argument

##l=[1,2,3,4,5]
##for i in l:
##    a=lambda l: i*2
##    print(i)


##
##def addition(n):
##    return n * n
##
##numbers = (1, 2, 3, 4)
##result = map(addition, numbers)
##print(list(result))




##def fun(n):
##    a=n*15
####    return a
##h=fun(10)
##print(h)



##def fun(n):
##    return lambda a: a*n
##b=fun(2)
##print(b(11))

##
##my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
### Get even numbers
##even_nums = tuple(filter(lambda x: x % 2 == 0, my_list))
 ##print(even_nums)  # Output: [2, 4, 6, 8, 10]
##
### Get odd numbers
 ##odd_nums = list(filter(lambda x: x % 2 != 0, my_list))
##print(odd_nums)  # Output: [1, 3, 5, 7, 9]



##def fun():
##    a=10
##    b=20
##    return a+b
##print(fun())


##add = (lambda a,b : a*b)(5,6)
##print(add)

##seq=[0,1,2,3,5,8,13]
##result=filter(lambda n:n%2 !=0,seq)
##print(list(result))

####reduce
##from functools import reduce
##def hello(a,b):
##
##    print(f"a={a},b={b},{a}+{b}={a+b}")
##    return a+b
##c=[75,65,80,95,90]
##d=reduce(hello,c)
##print(d)

##a=[1,2,3,4,5,6,7,8]
##b=[i for i in a if i%2==0]
##print(b)





####recursion
##
##def recursion(n):
##    if (n==0):
##        return 1
##    return n* recursion(n-1)
##print(recursion(5))
##




##def fun(a):
##    if a==1:
##        return a
##    else:
##        return a*fun(a-1)
##b=fun(5)
##print(b)
