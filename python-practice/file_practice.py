data = ["Python", "Linux", "Networking", "Security"]

with open("skills.txt", "w") as file:
	for skill in data:
		file.write(skill + "\n")

print("File written!")

with open("skills.txt", "r") as file:
	content = file.read()
	print("File contents:")
	print(content)

print("\nReading line by line:")
with open("skills.txt", "r") as file:
	for line in file:
		print(f"Skill: {line.strip()}")
