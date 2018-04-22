from name_function import get_formatted_name
print("Enter q at any time to exit")
while True:
	first=input("Please input your first name")
	if first=='q':
		break
	last=input("Please input your last name")
	if last=='q':
		break

	formatted_name=get_formatted_name(first,last)
	print("\tNeatly formatted name："+formatted_name)


