password = input("Enter a password: ")

if len(password) < 8:
	print("Password too short. Must be atleast 8 characters.")
elif password.isdigit():
	print("Password can't be only numbers.")
elif password.isalpha():
	print("Password needs numbers or special characters.")
else:
	print("Password is strong enough")

