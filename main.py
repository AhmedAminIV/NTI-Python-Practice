"""
Exercise 1: Create a list of five favorite fruits. Add a new fruit to the list.
Remove one fruit. Sort the list alphabetically. Print the final list.
"""

favFruits = ["Apple", "Orange", "Strawberry", "Banana", "Peach"]
favFruits += ["Grapes"]
favFruits.remove("Orange")
favFruits.sort()
print("\nExercise 1: \n", favFruits)

"""
Exercise 2: Create a tuple representing the coordinates (x, y, z) of a point. 
Access and print the y-coordinate. Attempt to change the x-coordinate and observe the error.
"""

pointCord = (5, 7, 3)
print("\nExercise 2: \n", pointCord[1])
# pointCord[0] = 6
# line 17, in <module> pointCord[0] = 6
# TypeError: 'tuple' object does not support item assignment

"""
Exercise 3: Create a dictionary storing information about a book (title, author, publication year).
Add a new key-value pair for "genre". Update the publication year. Print all keys and then all values.
"""

bookDic = {
    "title": "Lightning degree",
    "author": "One",
    "publication year": 2017
}

bookDic["genre"] = ["Comedy", "Martial Arts"]
bookDic["publication year"] = 2018
print("\nExercise 3: \n", bookDic)

"""
Exercise 4: Create two sets of numbers. Find their union, intersection, and difference.
 Add a new element to one set. Remove an existing element from the other set.
"""

numbersSet1 = {1, 2, 3, 4, 5, 6, 7}
numbersSet2 = {11, 7, 6, 8, 10, 9}

union = numbersSet2 | numbersSet1
intersection = numbersSet2 & numbersSet1
difference = numbersSet1 - numbersSet2
print(f"\nExercise 4: ",
      f"set 1: {numbersSet1}",
      f"set 2: {numbersSet2}",
      f"union: {union}",
      f"intersection: {intersection}",
      f"difference: {difference}",
      sep="\n")

"""
Exercise 5: Write a Python program that:
• Asks the user to enter a student's name and three subject marks.
• Calculates the average grade.
• Determines the final result:
• Displays the result in a clear format.
90-100   A
80-89    B
70-79    C
60-69    D
Below 60 F
"""

stuName = input("Name: ")
subjectsGrade = list(map(int, input("Enter numbers separated by space: ").split()))

avgGrade = sum(subjectsGrade) / len(subjectsGrade)
fullScore = 300
finalResult = sum(subjectsGrade) / fullScore
finalResult *= 100

if 90 <= finalResult <= 100:
    grade = "A"
elif 80 <= finalResult < 90:
    grade = "B"
elif 70 <= finalResult < 80:
    grade = "C"
elif 60 <= finalResult < 70:
    grade = "D"
else:
    grade = "F"

print(f"\nExercise 5: ",
      f"Average grade : {avgGrade}",
      f"GPA: {grade}",
      sep="\n")

"""
Exercise 6: Using for loops design the shape below using for loop.
                                        * 
                                        * * 
                                        * * * 
                                        * * * * 
                                        * * * * * 
                                        * * * * 
                                        * * * 
                                        * * 
                                        * 
"""

width = eval(input("Enter the base width you want "))
for i in range(width * 2):
    stars = width - abs(width - i)
    print("* " * stars)

"""
Exercise 7.1: 

Sum of elements in a list
Input: [1, 2, 3, 4, 5]
Output: 15
"""

inputList = [1, 2, 3, 4, 5]
out = sum(inputList)
print("\nExercise 7.1")
print("the sum is: ", out)

"""
Exercise 7.2: 
Find the largest and smallest element in a list.
Input: [34, 78, 12, 89, 2]
Output Min=2, Max=89
"""

inputList = [34, 78, 12, 89, 2]
Min = min(inputList)
Max = max(inputList)
print("\nExercise 7.2")
print("Min: ", Min, "       Max: ", Max)

"""
Exercise 7.3: 
Remove duplicates from a list.
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
"""

inputList = [1, 2, 2, 3, 4, 4, 5]
out = list(set(inputList))
print("\nExercise 7.3")
print("Unique list: ", out)

"""
Exercise 7.4: 
List comprehension practice
Create a new list of squares from [1, 2, 3, 4, 5].
Output: [1, 4, 9, 16, 25]
"""

inputList = [1, 2, 3, 4, 5]
out = [x ** 2 for x in inputList]
print("\nExercise 7.4")
print("Squared list: ", out)

"""
Exercise 7.5: 
Rotate a list by n positions.
Input: [1, 2, 3, 4, 5], n=2
Output: [4, 5, 1 ,2 ,3] 
"""

n = 2
inputList = [1, 2, 3, 4, 5]
out = inputList[-n:] + inputList[:n]
print("\nExercise 7.5")
print("Rotated list: ", out)

"""
Exercise 7.6: 
Flatten a nested list using loops
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
Write a function "flatten_list" to flatten a nested list flattened = flatten_list(nested_list)
print("Flattened list", flattened)  
"""


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)

    return flat_list


nestedlist = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
print("\nExercise 7.6")
print("Flattened list:", flatten_list(nestedlist))

"""
Exercise 7.7:
Merge two Python dictionaries into one
dict1= {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2= {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
"""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

merged = {**dict1, **dict2}
print("\nExercise 7.7")
print("Merged dictionaries: ", merged)

"""
Exercise 7.8
Problem Statement:
Given an array of integers and a number k, find the maximum sum of any contiguous 
subarray of size k.
Input: arr = (2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray |5,1,3, has the maximum sum = 9
"""


def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print("\nExercise 7.8")
print("Max subarray sum: ", max_subarray_sum(arr, k))

"""
Exercise 8.1: 
Sort a tuple of tuples by 2nd item
Given:
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
Expected output:
(Sorted tuple by 2nd item: (('c', 11), ('a', 23), ('d', 29), ('b', 37)))
"""

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
sorted_tuple = sorted(tuple1, key=lambda x: x[1])
print("\nExercise 8.1")
print("Sorted tuple by 2nd element: ", sorted_tuple)

"""
Exercise 8.2: 
Write a program or function that takes any tuple and any value, 
and returns how many times that value appears in the tuple.
Given:
python
tuple1 = (50, 10, 60, 70, 50)
value1= 50
Expected output:
2
"""


def tuple_value_counter(t, value):
    return t.count(value)


tuple1 = (50, 10, 60, 70, 50)
value1 = 50
occurrence = tuple_value_counter(tuple1, value1)
print("\nExercise 8.2")
print(f"The value {value1} has appeared {occurrence} times.")

"""
Exercise 8.3: 
Open a file and read its content. 
Use finally to make sure the file closes, even an error occurs.
"""

print("\nExercise 8.3")
try:
    file = open("test.txt", "a")
    try:
        file.write("\nLine 5: Added using python.")
    except ValueError:
        print("Can't write to file.")
    finally:
        file.close()
except FileNotFoundError:
    print("Can't open file, make sure the file path is correct.")


"""
Exercise 8.4: 
Write a function that takes three parameters: name, age, and city 
(with a default value of "Unknown" for city).
- Call the function once using only positional arguments.
- Call it again using only keyword arguments.
- Call it a third time using a mix of positional and keyword arguments
"""


def person_info(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}", sep="\n")


print("\nExercise 8.4")
print("1-Using only positional arguments: ")
person_info("Ahmed", "24", "Cairo")
print("2-Using only keyword arguments: ")
person_info(name="Ahmed", city="Cairo", age=24)
print("3-Using mix of positional and keyword arguments: ")
person_info("Ahmed", age="24")

