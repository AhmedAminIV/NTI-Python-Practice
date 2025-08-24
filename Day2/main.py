"""
Exercise 1:
Create a Python script that performs the following actions:
1- In the same directory as your script, create a new folder.
2- Inside this new folder, create an empty text file.
3- Write a single line of text into this file.
4- Print the absolute path to the file you just created.
5- Check if the file exists and print a message confirming its presence.

"""
import os

print("\nExercise 1")
new_dir_name = "dir1"
curr_dir = os.path.dirname(os.path.abspath(__file__))
dir_path = os.path.join(curr_dir, new_dir_name)
os.makedirs(dir_path, exist_ok=True)

file_path = os.path.join(dir_path, "file.txt")
with open(file_path, "w") as f:
    f.write("A single line.")

print("the absolute path of the new file is: ", file_path)

if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File not found: {file_path}")

"""
Exercise 2: 
Write a script to handle an existing file and its directory.
1- Assume a file named document.temp exists within a directory called staging.
2- Your script must rename document.temp to final_document.txt.
3- After renaming, create a new directory named processed inside the staging folder.
4- Move the renamed file (final_document.txt) into the new processed directory.
5- Print the new full path of final_document.txt.
"""
from pathlib import Path

print("\nExercise 2")
dir_path = Path("staging")
dir_path.mkdir(exist_ok=True)
file_path = dir_path / "document.temp"
file_path.write_text("")
new_file_path = dir_path / "final_document.txt"

try:
    os.rename(file_path, new_file_path)
    print(f"File renamed to: {new_file_path.name}")
except FileExistsError:
    os.remove(new_file_path)  # delete the existing file
    os.rename(file_path, new_file_path)
    print(f"♻️ Existing file replaced with: {new_file_path.name}")

nested_dir_path = dir_path / "processed"
os.makedirs(nested_dir_path, exist_ok=True)
final_path = nested_dir_path / new_file_path.name
try:
    os.rename(new_file_path, final_path)
    print(f"File renamed to: {final_path.name}")
except FileExistsError:
    os.remove(final_path)  # delete the existing file
    os.rename(new_file_path, final_path)
    print(f"♻️ Existing file replaced with: {final_path.name}")
print("The full path is: ", os.path.abspath(final_path))

"""
Exercise 3: 
Complete the following tasks using the pathlib module.
1- Create a Path object representing a directory named data_collection.
2- Create this directory on your file system.
3- Use the appropriate pathlib operator to
4- create a new Path object for a file named log.csv inside the data_collection directory.
5- Write the text "timestamp,event\n2025-08-24,start" into log.csv.
6- Using pathlib attributes, print the name of the file, its parent directory,
   and its file extension separately.
"""
print("\nExercise 3")

data_dir = Path("data_collection")

data_dir.mkdir(exist_ok=True)

log_file = data_dir / "log.csv"

log_file.write_text("timestamp,event\n2025-08-24,start")

print("File name:", log_file.name)
print("Parent directory:", log_file.parent)
print("File extension:", log_file.suffix)

"""
Exercise 4: 
Create a script that analyzes a given directory and reports its contents.
1- Prompt the user to enter a path of a directory
2- Verify that the entered path corresponds to an existing directory.
   if not, inform the user and stop the script
3- List all items within the directory. For each item, identify if it's a file or a subdirectory.
4- print a formatted list that clearly labels each item. 
   For example: [FILE] my_script.py or [DIR] subdirectory.
"""
print("\nExercise 4")

user_input = input("Enter the path of a directory: ")
directory = Path(user_input)

if not directory.exists() or not directory.is_dir():
    print("The entered path is not a valid directory.")
else:
    print(f"\nContents of: {directory.resolve()}\n")

    for item in directory.iterdir():
        if item.is_file():
            print(f"[FILE] {item.name}")
        elif item.is_dir():
            print(f"[DIR]  {item.name}")
        else:
            print(f"[OTHER] {item.name}")

"""
Exercise 5: 
Your first task is to create a CSV file named inventory.csv to serve as your product database.
The file should have three columns: product_id, product_name, and stock_quantity. 
Add the following four rows of data to the file:
101, Laptop, 50
102, Mouse, 250
103, Keyboard, 100
104, Monitor, 75
"""
import csv

print("\nExercise 5")
csv_file_path = Path("inventory.csv")

header = ["product_id", "product_name", "stock_quantity"]
rows = [
    [101, "Laptop", 50],
    [102, "Mouse", 250],
    [103, "Keyboard", 100],
    [104, "Monitor", 75],
]

with csv_file_path.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"inventory.csv created at: {csv_file_path.resolve()}")

"""
Exercise 6: 
Write a Python script that will perform the following actions:
1. Read the data from inventory.csv.
2. Iterate through each row of the inventory.
3. Simulate a sale for two products:
    1. Decrease the stock_quantity for product_id 102 (Mouse) by 10.
    2. Decrease the stock_quantity for product_id 104 (Monitor) by 5.
    3. Write the updated inventory data back to a new CSV file named updated_inventory.csv. 
    This new file should contain all products, with the updated quantities for the two sold items.
"""
print("\nExercise 6")
input_file = Path("inventory.csv")
output_file = Path("updated_inventory.csv")

with input_file.open("r", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    if row["product_id"] == "102":  # Mouse
        row["stock_quantity"] = str(int(row["stock_quantity"]) - 10)
    elif row["product_id"] == "104":  # Monitor
        row["stock_quantity"] = str(int(row["stock_quantity"]) - 5)

with output_file.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["product_id", "product_name", "stock_quantity"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated inventory saved to: {output_file.resolve()}")

"""
Exercise 7: 
After writing the updated data, the script should print the following to the console:
1. The total number of products in the inventory.
2. The updated stock quantity for the Monitor and Mouse.
3. A message confirming that the updated_inventory.csv file has been created.
"""
print("\nExercise 7")

total_products = len(rows)
mouse_stock = next(row["stock_quantity"] for row in rows if row["product_id"] == "102")
monitor_stock = next(row["stock_quantity"] for row in rows if row["product_id"] == "104")

print("\nInventory Update Summary")
print("----------------------------")
print(f"Total number of products: {total_products}")
print(f"Updated Mouse stock: {mouse_stock}")
print(f"Updated Monitor stock: {monitor_stock}")
print(f"{output_file.name} has been created at: {output_file.resolve()}")

"""
Exercise 8: 
Create a Parent Class:
Define a parent class called Person
The init method of this class should accept name and age as parameters. 
These should be stored as instance attributes.
Include a method called get details() that 
returns a string containing the person's name and age (e.g.. "John Smith, 25 years old")

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(fr"('{self.name}, {self.age} years old')")


p1 = Person("ahmed", 25)
print("\nExercise 8")
p1.get_details()

"""
Exercise 9: 
Create a Student Subclass:
Define a child class called Student that inherits from Person.
The Student's init method should accept name, age, and student id.
Use super() to call the init method of the Person class to handle the name and age.
Store the student id as a new attribute in the student class.
Override the get details() method to return a string that includes the person's details
from the parent class and the student's ID (e.g., "Jane Doe, 20 years old. Student ID: 12345").
"""


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_details(self):
        print(fr"('{self.name}, {self.age} years old. Student ID: {self.student_id}')")


print("\nExercise 9")
s1 = Student("atef", 23, 12345)
s1.get_details()

"""
Exercise 10: 
Create a Professor Subclass:
Define another child class called Professor that also inherits from Person.
The Professor's init method should accept name, age, and department.
Again, use super() to call the parent's init method.
Store the department as a new attribute.
Override the get details() method to include the person's details 
from the parent class and their department 
(e.g"Dr. Alan Turing, 42 years old. Department: Computer Science").
"""


class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def get_details(self):
        print(fr"('{self.name}, {self.age} years old. Department: {self.department}')")


print("\nExercise 10")
r1 = Professor("Ali", 39, "Computer and Systems")
r1.get_details()

"""
Exercise 11: 
Write a Python program to create a Singleton class called DatabaseConnection 
that ensures only one instance of the class is ever created.
Demonstrate by creating two objects and show that both refer to the same instance.
"""


class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.connection = "connected to Database"


db1 = DatabaseConnection()
db2 = DatabaseConnection()
print("\nExercise 11")
print("Database 1 id: ", id(db1))
print("Database 2 id: ", id(db2))

"""
Exercise 12: 
File Manipulation Challenge
Write a Python script to perform a series of operations on a file named log.txt. 
Your program must handle the file in three distinct stages, 
demonstrating your understanding of different file modes and pointer manipulation.

Stage 1: Initial Setup
Your script must first create log.txt and write the following three lines to it, 
ensuring the file is clean before you begin the next stages
Start of log file.
This is a second line
End of file.

Stage 2: Read and Insert
Open log.txt with a single file operation that allows you to read and write. Read the entire content. 
Without closing the file, use a method to move the file pointer to the end of the second line and then 
write a new line of text: This is an inserted line.

Stage 3: Append and Read
Open log.txt with a single file operation that allows you to both append and read. 
Append a new line: This line was appended at the end. 
After appending, move the file pointer back to the beginning of the file and read the entire contents.
Print the content to the console

Stage 4: Overwrite and Verify
Open log.txt with a single file operation that allows you to overwrite and read.
Write two completely new lines to the file:

All old content is gone!
This is the new file.

After writing, read the file and print its contents to the console to 
verify that the original content was completely replaced.
"""
print("\nExercise 12")

# Stage 1: Initial Setup
with open("log.txt", "w") as f:
    f.writelines([
        "Start of log file.\n",
        "This is a second line\n",
        "End of file.\n"
    ])

# Stage 2: Read and Insert
with open("log.txt", "r+") as f:
    content = f.read()
    # Find end of second line
    second_line_end = content.find("\n", content.find("\n") + 1) + 2
    f.seek(second_line_end)  # Move pointer after second line
    f.write("This is an inserted line.\n")

# Stage 3: Append and Read
with open("log.txt", "a+") as f:
    f.write("This line was appended at the end.\n")
    f.seek(0)  # Move pointer back to start
    content = f.read()
    print("\n--- Stage 3 Content ---")
    print(content)

# Stage 4: Overwrite and Verify
with open("log.txt", "w+") as f:
    f.write("All old content is gone!\n")
    f.write("This is the new file.\n")
    f.seek(0)
    content = f.read()
    print("\n--- Stage 4 Content ---")
    print(content)
