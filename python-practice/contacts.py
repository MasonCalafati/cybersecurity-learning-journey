contacts = [
	{"name": "John", "phone": "555-1234", "email": "john@email.com"},
	{"name": "Sarah", "phone": "555-5678", "email": "sarah@email.com"},
	{"name": "Mike", "phone": "555-9012", "email": "mike@email.com"}
]

print("=== All Contacts ===")
for contact in contacts:
	print(f"Name: {contact['name']}, Phone: {contact['phone']}")

new_contact = {
	"name": "Emma",
	"phone": "555-3456",
	"email": "emma@email.com"
}
contacts.append(new_contact)

search_name = "Sarah"
for contact in contacts:
	if contact["name"] == search_name:
		print(f"\nFound: {contact['name']} - {contact['phone']}")
