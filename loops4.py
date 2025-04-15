#exiting out of the loop
'''for num in range(2, 12):
    if num == 5:
        break # This will exit the loop when num is 5.
    print(num) # This will print the numbers from 2 to 4.
print("Loop ended on number:", num)''' # This will print the number when the loop ended.

#continue statement
for dig in range(1, 17, 3):
    if dig % 2 == 0:
        continue
    # This will skip the even numbers in the range.
    print(dig) # This will print the numbers from 3 to 21 in steps of 3.
print("the last number in the loop is:", dig) # This will print the last number in the loop.