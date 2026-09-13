# Jaylene McNeary
# CIS261
# Student Grade Calculator
# Data structure: Option A, a list of dictionaries.

FILE_NAME = "student_grades.txt"


def get_score(test_number):
	while True:
		try:
			score = float(input("Enter Test " + str(test_number) + " score: "))
			if 0 <= score <= 100:
				return score
			print("Score must be between 0 and 100.")
		except ValueError:
			print("Please enter a number.")


def calculate_grade(average):
	if average >= 90:
		return "A"
	if average >= 80:
		return "B"
	if average >= 70:
		return "C"
	if average >= 60:
		return "D"
	return "F"


def add_student(students):
	print("\nAdd Student")
	name = input("Enter student name: ").strip()
	student_id = input("Enter student ID: ").strip()

	if name == "" or student_id == "":
		print("Name and ID are required.")
		return

	for student in students:
		if student["id"].lower() == student_id.lower():
			print("That student ID already exists.")
			return

	test1 = get_score(1)
	test2 = get_score(2)
	test3 = get_score(3)
	average = (test1 + test2 + test3) / 3

	students.append({
		"name": name,
		"id": student_id,
		"test1": test1,
		"test2": test2,
		"test3": test3,
		"average": average,
		"grade": calculate_grade(average),
	})
	print("Student added.")


def display_students(students):
	if len(students) == 0:
		print("No students found.")
		return

	print("\nName                  ID             Test 1   Test 2   Test 3   Average  Grade")
	print("-" * 82)
	for student in students:
		print(
			f"{student['name']:<21} {student['id']:<14} "
			f"{student['test1']:>7.2f}  {student['test2']:>7.2f}  "
			f"{student['test3']:>7.2f}  {student['average']:>7.2f}  "
			f"{student['grade']:>5}"
		)


def display_statistics(students):
	if len(students) == 0:
		print("No students found.")
		return

	highest = max(students, key=lambda student: student["average"])
	lowest = min(students, key=lambda student: student["average"])
	class_average = sum(student["average"] for student in students) / len(students)

	print("\nClass Statistics")
	print(f"Highest average: {highest['average']:.2f} ({highest['name']})")
	print(f"Lowest average:  {lowest['average']:.2f} ({lowest['name']})")
	print(f"Class average:   {class_average:.2f}")


def search_student(students):
	search_name = input("Enter name to search: ").lower()
	found = False
	for student in students:
		if search_name in student["name"].lower():
			print(
				f"{student['name']} | ID: {student['id']} | "
				f"Average: {student['average']:.2f} | Grade: {student['grade']}"
			)
			found = True
	if not found:
		print("Student not found.")


def save_students(students):
	print("Saving records...")
	try:
		with open(FILE_NAME, "w") as file:
			for student in students:
				file.write(
					f"{student['name']}|{student['id']}|"
					f"{student['test1']:.2f}|{student['test2']:.2f}|"
					f"{student['test3']:.2f}|{student['average']:.2f}|"
					f"{student['grade']}\n"
				)
		print(f"Saved {len(students)} student records to file.")
	except OSError as error:
		print("Could not save records:", error)


def load_students():
	students = []
	try:
		with open(FILE_NAME, "r") as file:
			for line in file:
				parts = line.strip().split("|")
				if len(parts) != 7:
					continue
				test1 = float(parts[2])
				test2 = float(parts[3])
				test3 = float(parts[4])
				average = (test1 + test2 + test3) / 3
				students.append({
					"name": parts[0],
					"id": parts[1],
					"test1": test1,
					"test2": test2,
					"test3": test3,
					"average": average,
					"grade": calculate_grade(average),
				})
	except FileNotFoundError:
		print("No saved file found. Starting with no students.")
	except (OSError, ValueError) as error:
		print("Could not load records:", error)
	return students


def main():
	students = load_students()
	print("Welcome to Student Grade Calculator")
	while True:
		print("\nStudent Grade Calculator")
		print("1. Add new student")
		print("2. Display all students")
		print("3. Search student by name")
		print("4. View class statistics")
		print("5. Save and exit (ESC)")
		try:
			choice = input("Select an option (1-5) or press ESC to exit: ")
		except KeyboardInterrupt:
			print("\nExiting program.")
			save_students(students)
			print("Thank you for using Student Grade Calculator")
			break

		if choice in ("\x1b", "ESC", "esc", "5"):
			save_students(students)
			print("Thank you for using Student Grade Calculator")
			break
		if choice == "1":
			add_student(students)
		elif choice == "2":
			display_students(students)
		elif choice == "3":
			search_student(students)
		elif choice == "4":
			display_statistics(students)
		else:
			print("Invalid choice.")


if __name__ == "__main__":
	main()