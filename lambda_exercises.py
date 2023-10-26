''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens_filtered_list = list(filter(lambda x: (x % 2 == 0), integers))
odds_filtered_list = list(filter(lambda x: (x % 2 == 1), integers))

print(evens_filtered_list)
print(odds_filtered_list)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

six_letter_days = list(filter(lambda x: (len(x) == 6), weekdays))
print(six_letter_days)



''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_words = ['orange', 'black']

removed_words_list = list(filter(lambda x: x not in remove_words, original_list))
print(removed_words_list)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

removed_numbers = list(filter(lambda x: x not in list2, list1))
print(removed_numbers)



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
original_list = ['red', 'black', 'white', 'green', 'orange']

filtered_list = list(filter(lambda x: ('ack' in x), original_list))
print(filtered_list)

filtered_list = list(filter(lambda x: ('abc' in x), original_list))
print(filtered_list)




''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"
'''

str1 = ["Hello8world", "HELLO", "hello"]

valid_password = list(map(lambda x: (any(c.isupper() for c in x) and any(c.islower() for c in x) and any(c.isdigit() for c in x) and (len(x) >= 8)), str1))
print(valid_password)



''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_scores = sorted(original_scores, key=lambda x: x[1])
print(sorted_scores)