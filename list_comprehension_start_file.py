'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# --> new_list = [expression(i) for i in original_list if filter(i)]
#can do what you wanted in 5 lines of code into 1 line of code
#on final - *3 parts of list comprehension are [expression/transformation, iteration, condition/filter]*


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.

x = [i for i in range(10)]
print(x)

#add an expression

squares = [x**2 for x in range(1,11)]
print(squares)

list1 = [3,4,5]
result = [item*3 for item in list1] #can also do for item for list1 then go back and do item*3. item in front bc its the iterator, use same one
print(result)

listOfWords = ['this', 'is', 'a', 'list', 'of', 'words']
result = [word[0].upper() for word in listOfWords] #add upper or any methods onto the expression (first part)
print(result)

#adding in an IF condition:
# create a list of the square of even numbers from 1 to 10
even_squares = [i*i for i in range(1,11) if i % 2 == 0] #% sign means remainder after division. if you divide any number by 2 you either get 1 or 0 as remainer
print(even_squares)

string = 'Hello 12345 World'
numbers = [int(x) for x in string if x.isdigit()] #get x for each x in the list 'string' if it is a digit. don't need == True. when do for x in string it goes letter by letter
print(numbers) #change the expression into int, not anything else. changes numbers from strings to integers. use x.isalpha() to get just letters instead of numbers

#if did this ^^^ the hard way vvv
numbers = []
for x in string:
    if x.isdigit():
        y = int(x)
        numbers.append(y)

print(numbers)

#create a new list of all odd numbers multiplied by 100
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list2 = []
for x in list1:
    if x%2 == 1:
        y = x * 100
        list2.append(y)

print(list2)
#long way^^ easy wayvv
list2 = [x*100 for x in list1 if x%2==1]
print(list2)


infile = open('test.txt', 'r')

result = [i.rstrip('\n') for i in infile if 'line3' in i] #uses 'in'. rstrip used to remove the \n from result
print(result)


def double(x):
    return x*2

print(double(10))

result = [double(x) for x in range(10)]

print(result)


result = [x+y for x in [10,30,50] for y in [20,40,60]] #can iterate thru 2 lists at same time
print(result)

infile.close()



## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(number) for number in numbers if number >= 0]
print(newlist)


## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_length = [len(word) for word in words if word != 'the']
print(word_length)


## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
vehicles = [k.upper() for k in dict if dict[k] < 5000]
print(vehicles)


## Find all the numbers from 1 to 1000 that have a 4 in them
numbers = [num for num in range(1,1001) if '4' in str(num)]
print(numbers)


## count how many times the word 'the' appears in the text file - 'sometext.txt'
infile = open('sometext.txt', 'r')
word_count = [i for i in infile.read().split() if i == 'The' or i == 'the']
print(len(word_count))
infile.close()


## Extract the numbers from the following phrase ##
phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'
num_extract = [int(word) for word in phrase.split() if word.isdigit()]
print(num_extract)