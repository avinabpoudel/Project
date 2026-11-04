student = ("Ram Sharma", 15, "Grade 10", "Pokhara Secondary School")

print("My School Subject Planner")
print("Name:", student[0])
print("Age:", student[1])
print("Class:", student[2])
print("School:", student[3])

monday = {"Math", "Science", "English", "Computer"}
tuesday = {"Math", "Social", "Nepali", "Art"}

print("Monday subjects:", monday)
print("Tuesday subjects:", tuesday)

monday.add("Health")
print("After adding Health to Monday:", monday)

monday.remove("Computer")
print("After removing Computer from Monday:", monday)

tuesday.add("Music")
print("After adding Music to Tuesday:", tuesday)

print("Common subjects:", monday.intersection(tuesday))
print("All subjects:", monday.union(tuesday))
print("Only on Monday:", monday.difference(tuesday))
print("Only on Tuesday:", tuesday.difference(monday))
