import csv
n = input("Enter the number of students: ")

with open('coders.csv','wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  
  #heading 4 rows
	writer.writerow(['Sl. No','Name','Department','Phone','Rating'])

	for i in range(n):
		print("\nStudent #{}".format(i+1))

		student = {}
		student['no'] = i+1
		student['name'] = raw_input("Name: ")
		student['dept'] = raw_input("Department: ")
		student['phone'] = raw_input("Phone: ")
		student['rating'] = raw_input("Rating: ")
		writer.writerow([student['no'],student['name'],student['dept'],student['phone'],student['rating']])

	print("Successfully created coders.csv")
