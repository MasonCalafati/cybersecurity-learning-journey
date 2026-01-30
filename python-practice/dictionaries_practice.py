person = {
	"name": "Mason",
	"age": 22,
	"job": "Starbucks",
	"studying": "Cybersecurity"
}

print(person["name"])
print(person["age"])

person["location"] = "New York"
print(person)

person["job"] = "Security Analyst"
print(person)

for key, value in person.items():
	print(f"{key}: {value}")

if "age" in person:
	print(f"Age is {person['age']}")
