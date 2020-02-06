#John DiNofrio
#ENPM661
#Project Zero

#Problem 1
list = []
for i in range(1,11):
  a = i**2
  list.append(a)

list.reverse()
list.pop(-2)
list.pop(-2)
print(list)


#Problem 2

## Write code to copy "original" dictionary and print the newly copied dictionary
original = {1:'geeks', 2:'for'}
copy = original
print(copy)

# write the code to clear the content of the dictionary and then print the empty dictionary
text = {1: "geeks", 2: "for"}
text.clear()
print(text)

inventory = {'shirts': 25, 'paints': 220, 'tshirts': 217}
new = inventory.pop('shoes',[100])
print(new)
# write code to get the value for the key 'shoes'. If the key is not is the dictionary return 100

test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }
x = test_dict.popitem()
print(x)
# write the code using popitem() to return + remove arbitrary key value pair and print it

dic = {"A":1, "B":2}
y = dic.get("C","Not found")
print(y)
# write the code to get the value for key 'C'. Print "Not found" if the key is not present

dictionary = {"A": 2, "B": 3, "C": 4}
z = dictionary.values()
print(z)
# write the code to print the values in the dictionary

Dictionary1 = { 'A': 'Geeks', 'B': 'For', }
Dictionary2 = { 'B': 'Geeks' }
Dictionary1.update(Dictionary2)
print(Dictionary1)
# Write the code to update "Dictionary1" with "Dictionary2" and print




#for loop problem
numbers = [1, 3, 4, 6, 81, 80, 100, 95]
my_list = []
for item in numbers:
    if (item % 5) == 0:
        if (item % 2) == 0:
            my_list.append('five even')
        else:
            my_list.append('five odd')
    else:
        if (item % 2) == 0:
            my_list.append('even')
        else:
            my_list.append('odd')
print(my_list)
assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']
