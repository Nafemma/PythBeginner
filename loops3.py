#looping through dictionary

profile = {
   'name': 'John Doe',
    'age': 12, 
    'city': 'Lilongwe',
}

'''for key, value in profile:
    print(key, ":", value)'''
# The above code will give an error because the dictionary is not iterable in that way.
# To iterate through the dictionary, we can use the items() method.

for key, value in profile.items():
    print(key, ":", value) # This will print the key-value pairs in the dictionary. 
