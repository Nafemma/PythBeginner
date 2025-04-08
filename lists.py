fruits = ["apple", "banana", "apple", "cherry"]
print(fruits)

#extend list
#to add elements from another list to the current list, use the extend() method.
animals = ["cat", "dog"]
bird = ["parrot", "sparrow"]
animals.extend(bird)

courses = ['History', 'chemistry','Math']
#append list --- adding a single element to the end of the list
courses.append('English')
print(courses)
#insert list --- adding a single element to the specific index of the list
courses.insert(1, 'Biology')
print(courses)

#reverse list
courses.reverse()
print(courses)
