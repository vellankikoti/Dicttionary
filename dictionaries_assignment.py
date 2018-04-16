# 1. Write a Python script to sort (ascending and descending) a dictionary by value

d = {'A':20,'B':10,'C':40,'D':30}
print("Ascending Order:",sorted(d.values()))
print("Descending Order:",sorted(d.values(),reverse = True))

# output:
# Ascending Order: [10, 20, 30, 40]
# Descending Order: [40, 30, 20, 10]

# 2.	Write a Python script to add a key to a dictionary
d = {
	"key1" : "val1",
	"key2" : "val2",
	"key3" : "val3"
}

print("Dictionary:",d)

d["newkey"] = "newval"
print("Dictionary after adding key:",d)

# output:
# Dictionary: {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
# Dictionary after adding key: {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'newkey': 'newval'}

'''3.	Write a Python script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

dic1={1:10,2:20} 
dic2={3:30,4:40} 
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# output:
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 4.	Write a Python script to print a dictionary where the keys are numbers between 
# 1 and 15 (both included) and the values are square of keys. 

d = {}
for value in range(1,16):
	d[value] = value**2
print(d)

# output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# 5.Write a Python script to generate and print a dictionary that contains
# a number (between 1 and n) in the form (x, x*x). 

d = {}
for x in range(1,11):
	d[x] = x*x
	print(x,x*x)
print(d)


#6.	Write a Python program to check a dictionary is empty or not. 
d= {}
if len((d.keys()))==0:
	print("Dictionary is Empty ")
else:
	print("Dictionary has some elements")