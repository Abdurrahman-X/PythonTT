student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "Art"]
}

print(student)
#print(student[0])  # This will raise an error since dictionaries are accessed by keys, not indices.
print(student["name"])  # Correct way to access value by key


 # Try to access a non-existent key
#print(student["grade"])  # This will raise a KeyError since "grade" key does not exist.

#print(student.get("grade"))  # Using get() method returns None if key does not exist
#print(student.get("grade", "Not Found"))  # Returns "Not Found" if key does not exist

# Add New Entry to Dictionary
student["grade"] = "A"

# Update Existing Entry
student["age"] = 22 

# Update Multiple Entries
student.update({"name": "Bob", "age": 23, "Phone": "555-1234", "courses": ["History", "Math"]}) 

# Delete Entry
del student["Phone"]  # Remove the "Phone" entry

student_age = student.pop("age")  # Remove and return the value associated with "age"

print(student)
print(f"Student Age: {student_age}")

print(len(student))  # Output: 3
print(student.keys())    # Output: dict_keys(['name', 'courses', 'grade'])
print(student.values())  # Output: dict_values(['Bob', ['History', 'Math'], 'A'])
print(student.items())   # Output: dict_items([('name', 'Bob'), ('courses', ['History', 'Math']), ('grade', 'A')])

# Looping through Dictionary
for key, value in student.items():
    print(f"{key}: {value}")  # Print each key and its corresponding value