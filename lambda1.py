remainder = lambda num: num % 2

print(type(remainder)) #type belongs to a class called 'function'
print(remainder(5))


product = lambda x,y : x * y

print(product(2,3))


def testfunc(num):
    return lambda x: x * num

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9)) #whenever you print it that makes the number into the x
#doing it this way ^ and doing it this way v are the same
result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))

#filter function vvv
numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda x: (x > 7), numbers_list)) #give it iterable list, will go thru every value and see if meets criteria

print(filtered_list) #produces filter object, so have to do list function ^ to see what numbers actually are


#map function vvv
def divide2(x):
    return x % 2

mapped_list = list(map(divide2, numbers_list))
print(mapped_list)

mapped_list = list(map(lambda x: x % 2, numbers_list)) #no longer need divide2, can just use lambda instead of function
print(mapped_list)