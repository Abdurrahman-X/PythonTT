courses = ["Math", "Science", "History", "Art"]

nums = [1, 7, 2, 3, 5, 6, 10, 9, 4, 8]

courses_2 = ["Biology", "Chemistry"]

# print(len(courses))
# print(courses[2])

# To get the last item from the list
#print(courses[-1]) # Output: Art

# Range of indices
#print(courses[1:3])  # Output: ['Science', 'History']. Starting index is inclusive, ending index is exclusive.
#print(courses[:2])   # Output: ['Math', 'Science']
#print(courses[2:])   # Output: ['History', 'Art']

# List Methods

#1. Append
courses.append("Physical Education") # Add 'Physical Education' to the end of the list
#courses.append(courses_2)  # Add courses_2 as a single element at the end of the list ==> ['Math', 'Science', 'History', 'Art', 'Physical Education', ['Biology', 'Chemistry']]. A list inside a list.

#2. Insert
courses.insert(1, "English")  # Insert 'English' at index 1
#courses.insert(2, courses_2)  # Insert courses_2 at index 2 ==> ['Math', 'Science', ['Biology', 'Chemistry'], 'History', 'Art', 'Physical Education']. A list inside a list.

#3. Extend
courses.extend(courses_2)  # Extend the list by adding elements from courses_2 ==> ['Math', 'English', 'Science', 'History', 'Art', 'Physical Education', 'Biology', 'Chemistry']. No nested list.


#4. Remove
#courses.remove("History")  # Remove 'History' from the list

#5. Pop
#popped_course = courses.pop()  # Remove and return the last item from the list
#print(f"Popped Course: {popped_course}")


# Sorting Lists

#1. Reverse
#courses.reverse()  # Reverse the order of the list

#2. Sort (Ascending)
#courses.sort()  # Sort the list in ascending order
nums.sort()  # Sort the numbers in ascending order

#3. Sort (Descending)
#courses.sort(reverse=True)  # Sort the list in descending order
nums.sort(reverse=True)  # Sort the numbers in descending order

sorted_courses = sorted(courses)  # Returns a new sorted list in ascending order
#print(f"Sorted Courses: {sorted_courses}")

nums_sorted = sorted(nums)  # Returns a new sorted list of numbers in ascending order
#print(f"Sorted Numbers: {nums_sorted}")


# 4. Minimum, Maximum and Sum
#print(min(nums))  # Output: 1
#print(max(nums))  # Output: 10      
#print(sum(nums))  # Output: 55

#print(courses, nums)



# Finding Values
#print(courses.index("Science"))  # Output: 2

#for index, course in enumerate(courses): # Enumerate returns both index and value
#    print(index, course)


# Joining Lists
courses_str = ", ".join(courses)  # Join list elements into a single string separated by ", "
#print(courses_str)  

# Splitting Strings
new_list = courses_str.split(", ")  # Split the string back into a list
#print(new_list)



# Tuples. These are immutable (cannot be changed).

# Lists on the other hand are mutable (can be changed).


list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1  # Both list_1 and list_2 point to the same list in memory

print(list_1)
print(list_2)

list_1[2] = "Art"  # Changing list_1 also changes list_2 since they reference the same list
print(list_1)
print(list_2)


tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1  # Both tuple_1 and tuple_2 point to the same tuple in memory

#tuple_1[2] = "Art"  # This will raise an error since tuples are immutable.


# Sets. These are unordered collections of unique elements.
cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}
print(cs_courses)
print(art_courses)  
# Duplicates will be automatically removed
print("Math" in cs_courses)  # Check membership. Returns True

print(cs_courses.intersection(art_courses))  # Courses common to both sets
print(cs_courses.difference(art_courses))    # Courses in cs_courses but not in art_courses
print(cs_courses.union(art_courses))         # All unique courses from both sets


# Empty Lists, Tuples, and Sets
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # This creates an empty dictionary, not a set
empty_set = set()  # Note: {} creates an empty dictionary, not a set



