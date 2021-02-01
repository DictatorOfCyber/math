print("Odd Number")
print(" ")
print("Even Number")
print(" ")
choice = int(input(" Please select the category 1 or 2 : "))

if choice == 1:
	print(" ")
	from file import odd
	print(odd)
elif choice ==2:
	print(" ")
	from file import even
	print(even)
else:
	print (" ")
	print("Invalid number Input")
