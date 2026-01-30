#Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 5, 10, 15, 20,]

print(fruits[0])
print(fruits[-1])

fruits.append("mango")
print(fruits)

fruits.remove("banana")
print(fruits)

for fruit in fruits:
	print(f"I like {fruit}")

print(f"Total fruits: {len(fruits)}")
